#!/bin/bash
# =============================================================================
# Qwen3.5-397B-A17B FP16 Baseline Smoke Test — Vast.ai Setup & Run
# =============================================================================
#
# Runs smoke tests TWICE: once with thinking ON (budget=4096), once with
# thinking OFF. Uses Qwen-recommended sampling parameters for each mode.
#
# Tested 2026-02-22 on vast.ai with 8x H200 (1128GB VRAM, no CPU offload).
# Also works on 8x RTX PRO 6000 Blackwell (768GB VRAM, needs CPU offload).
#
# Instance setup:
#   vastai search offers 'gpu_total_ram>=1000 cpu_ram>=256 disk_space>=900 inet_down>=500 reliability>0.95' -o 'dph' --storage 900
#   vastai create instance <OFFER_ID> \
#     --image pytorch/pytorch:2.6.0-cuda12.6-cudnn9-devel \
#     --disk 1200 --ssh --direct --lang-utf8 \
#     --env '-e HF_TOKEN=hf_xxx' \
#     --label "qwen35-fp16-smoke-test"
#
# Then SCP this folder and run:
#   scp -P $PORT -r tests/smoke_test_suite root@$HOST:/workspace/smoke_test/
#   ssh -p $PORT root@$HOST "bash /workspace/smoke_test/run_fp16_baseline.sh"
#
# Estimated runtime (8xH200): ~1-1.5 hours (15min download + 5min setup + 60min inference)
# Estimated runtime (8xBlackwell): ~3-4 hours (slower due to CPU offload)
# Estimated cost: ~$18-25
# =============================================================================

set -euo pipefail

# --- Configuration -----------------------------------------------------------
MODEL_ID="Qwen/Qwen3.5-397B-A17B"
MODEL_DIR="/workspace/models/Qwen3.5-397B-A17B"
RESULTS_DIR="/workspace/smoke_test/results"
VLLM_PORT=8000
TP_SIZE=8
MAX_MODEL_LEN=32768
MAX_NUM_SEQS=16

# Auto-detect GPU type and set memory config accordingly
detect_gpu_config() {
    local gpu_name
    gpu_name=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1 | xargs)
    local total_vram_mb
    total_vram_mb=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits | awk '{s+=$1} END {print s}')
    local total_vram_gb=$(( total_vram_mb / 1024 ))

    log "Detected GPU: $gpu_name (${total_vram_gb}GB total VRAM across $(nvidia-smi -L | wc -l) GPUs)"

    if [ "$total_vram_gb" -ge 1000 ]; then
        # H200, H100, etc — plenty of VRAM, no offload needed
        GPU_MEM_UTIL=0.92
        CPU_OFFLOAD_GB=0
        log "  -> High-VRAM config: gpu_mem_util=$GPU_MEM_UTIL, no CPU offload"
    else
        # RTX PRO 6000 Blackwell, etc — tight VRAM, need offload
        GPU_MEM_UTIL=0.85
        CPU_OFFLOAD_GB=25
        log "  -> Low-VRAM config: gpu_mem_util=$GPU_MEM_UTIL, cpu_offload=${CPU_OFFLOAD_GB}GB/GPU"
    fi
}

# --- Logging -----------------------------------------------------------------
log() { echo "[$(date '+%H:%M:%S')] $*"; }

# --- Step 1: Install vLLM nightly -------------------------------------------
log "=== Step 1: Installing vLLM (nightly) ==="

pip install -q --upgrade pip

# vLLM v0.16.0 stable (Feb 13) shipped before Qwen3.5 (Feb 16).
# Must use nightly for Qwen3.5 support.
pip install -U vllm --pre \
    --extra-index-url https://wheels.vllm.ai/nightly 2>&1 | tail -5

# Install test dependencies
pip install -q requests

log "vLLM installed:"
python -c "import vllm; print(f'  vLLM: {vllm.__version__}')"
python -c "import torch; print(f'  PyTorch: {torch.__version__}, CUDA: {torch.version.cuda}')"

# --- Step 2: Conditionally patch vLLM for cpu offload ----------------------
# Only needed when CPU offload is used (Blackwell/low-VRAM setups).
# Qwen3.5 has hybrid attention (GatedDeltaNet + full attention) which requires
# InputBatch re-initialization. vLLM blocks this when cpu_offload_gb > 0.
# This patch converts the assertion to a warning.
# See: https://github.com/vllm-project/vllm/pull/18298
log "=== Step 2: GPU detection & conditional patching ==="

detect_gpu_config

if [ "$CPU_OFFLOAD_GB" -gt 0 ]; then
    log "CPU offload enabled — applying vLLM patch..."
    python3 << 'PATCH'
import vllm, os

path = os.path.join(os.path.dirname(vllm.__file__), "v1", "worker", "gpu_model_runner.py")
with open(path, "r") as f:
    content = f.read()

old = '''            assert self.cache_config.cpu_offload_gb == 0, (
                "Cannot re-initialize the input batch when CPU weight "
                "offloading is enabled. See https://github.com/vllm-project/vllm/pull/18298 "  # noqa: E501
                "for more details."
            )'''

new = '''            if self.cache_config.cpu_offload_gb > 0:
                import logging
                logging.warning(
                    "Re-initializing input batch with CPU weight offloading "
                    "enabled. This was previously blocked by an assertion. "
                    "See https://github.com/vllm-project/vllm/pull/18298"
                )'''

if old in content:
    content = content.replace(old, new)
    with open(path, "w") as f:
        f.write(content)
    print("  Patch applied: cpu_offload assertion -> warning")
else:
    print("  Patch not needed (already applied or assertion changed)")
PATCH
else
    log "No CPU offload — skipping vLLM patch"
fi

# --- Step 3: Download model --------------------------------------------------
log "=== Step 3: Downloading model (753GB) ==="

# HF token should be set via HF_TOKEN env var (passed via --env on instance creation)
if [ -z "${HF_TOKEN:-}" ]; then
    log "WARNING: HF_TOKEN not set. If model is gated, set it with:"
    log "  export HF_TOKEN=hf_xxx"
fi

START_DL=$(date +%s)
huggingface-cli download "$MODEL_ID" \
    --local-dir "$MODEL_DIR" \
    --local-dir-use-symlinks False \
    --token "${HF_TOKEN:-}"
END_DL=$(date +%s)
log "Model downloaded in $(( (END_DL - START_DL) / 60 ))m $(( (END_DL - START_DL) % 60 ))s"

DU=$(du -sh "$MODEL_DIR" | cut -f1)
log "Model size on disk: $DU"

# Verify no corrupt shards (can happen if download is interrupted and resumed)
log "Verifying safetensors integrity..."
python3 << 'VERIFY'
from safetensors import safe_open
import glob, os, sys
files = sorted(glob.glob("/workspace/models/Qwen3.5-397B-A17B/model.safetensors-*"))
bad = []
for f in files:
    try:
        with safe_open(f, framework="pt") as sf:
            _ = sf.keys()
    except Exception as e:
        bad.append(os.path.basename(f))
if bad:
    print(f"ERROR: {len(bad)} corrupt shards: {bad}")
    print("Delete them and re-run the download step.")
    sys.exit(1)
else:
    print(f"  All {len(files)} shards OK")
VERIFY

# --- Step 4: Start vLLM server ----------------------------------------------
log "=== Step 4: Starting vLLM server ==="

mkdir -p "$RESULTS_DIR"

# Kill any existing vllm process
ps aux | grep vllm | grep -v grep | awk '{print $2}' | xargs -r kill -9 2>/dev/null || true
sleep 2

VLLM_ARGS=(
    --tensor-parallel-size "$TP_SIZE"
    --language-model-only
    --attention-backend FLASH_ATTN
    --gpu-memory-utilization "$GPU_MEM_UTIL"
    --max-model-len "$MAX_MODEL_LEN"
    --max-num-seqs "$MAX_NUM_SEQS"
    --trust-remote-code
    --port "$VLLM_PORT"
    --disable-log-requests
)

if [ "$CPU_OFFLOAD_GB" -gt 0 ]; then
    VLLM_ARGS+=(--cpu-offload-gb "$CPU_OFFLOAD_GB")
fi

CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve "$MODEL_DIR" \
    "${VLLM_ARGS[@]}" \
    > "$RESULTS_DIR/vllm_server.log" 2>&1 &

VLLM_PID=$!
log "vLLM server starting (PID: $VLLM_PID), waiting for it to be ready..."

# Wait for server to be ready (model loading takes ~2-5 min)
TIMEOUT=1200  # 20 minutes max
ELAPSED=0
while [ $ELAPSED -lt $TIMEOUT ]; do
    if curl -s "http://localhost:${VLLM_PORT}/v1/models" > /dev/null 2>&1; then
        log "vLLM server ready after ${ELAPSED}s"
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        log "ERROR: vLLM server died. Check $RESULTS_DIR/vllm_server.log"
        tail -30 "$RESULTS_DIR/vllm_server.log"
        exit 1
    fi
    sleep 10
    ELAPSED=$((ELAPSED + 10))
    if [ $((ELAPSED % 60)) -eq 0 ]; then
        log "  Still waiting... (${ELAPSED}s)"
    fi
done

if [ $ELAPSED -ge $TIMEOUT ]; then
    log "ERROR: vLLM server did not start within ${TIMEOUT}s"
    tail -30 "$RESULTS_DIR/vllm_server.log"
    exit 1
fi

# Verify model loaded
curl -s "http://localhost:${VLLM_PORT}/v1/models" | python -m json.tool

# --- Step 5: Run smoke tests (both modes) -----------------------------------
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
export API_URL="http://localhost:${VLLM_PORT}/v1/chat/completions"

run_suite() {
    local mode=$1  # "on" or "off"
    local mode_label=$2

    log "============================================================"
    log "=== RUNNING SUITE: $mode_label ==="
    log "============================================================"

    export THINKING_MODE="$mode"

    log "--- Running Estonian tests (16 tests) [$mode_label] ---"
    START_T=$(date +%s)
    python "$SCRIPT_DIR/estonian.py" 2>&1 | tee "$RESULTS_DIR/estonian_${mode}_run.log"
    END_T=$(date +%s)
    log "Estonian tests completed in $(( END_T - START_T ))s"

    log "--- Running Coding tests (27 tests) [$mode_label] ---"
    START_T=$(date +%s)
    python "$SCRIPT_DIR/coding.py" 2>&1 | tee "$RESULTS_DIR/coding_${mode}_run.log"
    END_T=$(date +%s)
    log "Coding tests completed in $(( END_T - START_T ))s"

    log "--- Running English tests (16 tests) [$mode_label] ---"
    START_T=$(date +%s)
    python "$SCRIPT_DIR/english.py" 2>&1 | tee "$RESULTS_DIR/english_${mode}_run.log"
    END_T=$(date +%s)
    log "English tests completed in $(( END_T - START_T ))s"
}

log "=== Step 5: Running smoke tests (2 passes) ==="

# Pass 1: Thinking ON (temp=0.6, top_p=0.95, budget=4096)
run_suite "on" "Thinking ON (budget=4096, temp=0.6, top_p=0.95)"

# Pass 2: Thinking OFF (temp=0.7, top_p=0.8)
run_suite "off" "Thinking OFF (temp=0.7, top_p=0.8)"

# --- Step 6: Collect results -------------------------------------------------
log "=== Step 6: Collecting results ==="

mv "$SCRIPT_DIR"/*_results_*.md "$RESULTS_DIR/" 2>/dev/null || true

log "Results saved to $RESULTS_DIR:"
ls -lh "$RESULTS_DIR"/*.md 2>/dev/null

# --- Done --------------------------------------------------------------------
log "=== All done! ==="
log ""
log "To download results to your local machine:"
log "  # Thinking mode results:"
log "  scp -P \$PORT root@\$HOST:$RESULTS_DIR/*_thinking_*.md ~/source/qwen_awq/tests/FP16_thinking/"
log "  # No-thinking mode results:"
log "  scp -P \$PORT root@\$HOST:$RESULTS_DIR/*_nothinking_*.md ~/source/qwen_awq/tests/FP16_nothinking/"
log "  # Or grab everything:"
log "  scp -P \$PORT root@\$HOST:$RESULTS_DIR/*.md ~/source/qwen_awq/tests/FP16_v2/"
log ""
log "To shut down vLLM:"
log "  kill $VLLM_PID"
log ""
log "Don't forget to destroy the vast.ai instance when done!"
