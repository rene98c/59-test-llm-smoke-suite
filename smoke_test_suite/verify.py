#!/usr/bin/env python3
"""Verify smoke test results using Claude API.

Parses results markdown files, sends each test's prompt + response + eval
criteria to Claude for analysis, and produces a verification report.

Usage:
    python verify.py <results_dir> [output_dir]
    python verify.py ~/source/qwen_awq/tests/FP16/

Loads ANTHROPIC_API_KEY from ~/source/qwen_awq/.env or environment.
"""

import os
import re
import sys
import asyncio
from pathlib import Path
from datetime import datetime

import anthropic

# --- Configuration -----------------------------------------------------------
EVALUATOR_MODEL = "claude-opus-4-6"
MAX_CONCURRENT = 5
MAX_TOKENS = 1024

SYSTEM_PROMPT = """\
You are an expert evaluator for LLM smoke tests. You will be given:

1. A test prompt that was sent to a model
2. The model's response
3. Evaluation criteria describing what a correct/good response looks like

Your job is to carefully analyze the response against the criteria and score it.

Scoring:
- PASS: Response fully satisfies all evaluation criteria
- PARTIAL: Response is mostly correct but has specific issues or misses some criteria
- FAIL: Response has significant errors or misses key criteria

Rules:
- Be rigorous but fair
- For coding tests: verify logic, algorithms, edge cases, and correctness
- For Estonian language tests: check grammar, orthography (especially õ/ö/ü/ä), \
case forms, and cultural accuracy
- For English tests: check constraint satisfaction, tone, and quality
- If the response includes thinking/reasoning before the final answer, evaluate \
the FINAL answer, not the intermediate thinking process
- Be specific about what's wrong when scoring PARTIAL or FAIL

Respond in this exact format (3 lines):
SCORE: <PASS|PARTIAL|FAIL>
ISSUES: <comma-separated list of specific issues, or "None">
NOTES: <1-2 sentence summary of the response quality>"""


# --- Helpers -----------------------------------------------------------------

def load_api_key() -> str:
    """Load ANTHROPIC_API_KEY from environment or .env file."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key

    env_path = Path.home() / "source" / "qwen_awq" / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY="):
                return line.split("=", 1)[1].strip()

    print("ERROR: ANTHROPIC_API_KEY not found in environment or ~/.env")
    sys.exit(1)


def parse_results_file(filepath: Path) -> list[dict]:
    """Parse a results markdown file into individual test entries."""
    content = filepath.read_text(encoding="utf-8")

    # Test headers look like: ## 01_orthography: Name Here
    # or ## R1_01_palindrome: Name Here
    # ID must contain at least one underscore — filters out in-response headers
    # like "## Alternative: ..." or "## Example: ..."
    header_pattern = re.compile(r"^## ([A-Za-z0-9]+_[A-Za-z0-9_]+): (.+)$", re.MULTILINE)

    # Find all test header positions
    headers = list(header_pattern.finditer(content))
    tests = []

    for idx, match in enumerate(headers):
        start = match.start()
        end = headers[idx + 1].start() if idx + 1 < len(headers) else len(content)
        section = content[start:end]

        test_id = match.group(1)
        test_name = match.group(2).strip()

        # Extract prompt (between ``` markers after **Prompt:**)
        prompt_match = re.search(
            r"\*\*Prompt:\*\*\s*\n```\s*\n(.*?)```", section, re.DOTALL
        )
        prompt = prompt_match.group(1).strip() if prompt_match else ""

        # Extract system prompt if present
        system_match = re.search(r"\*\*System:\*\*\s*`(.+?)`", section)
        system = system_match.group(1) if system_match else None

        # Extract response (between **Response:** and **Evaluation criteria:**)
        response_match = re.search(
            r"\*\*Response:\*\*\s*\n(.*?)\*\*Evaluation criteria:\*\*",
            section,
            re.DOTALL,
        )
        response = response_match.group(1).strip() if response_match else ""

        # Extract eval criteria (everything after **Evaluation criteria:**)
        eval_match = re.search(
            r"\*\*Evaluation criteria:\*\*\s*\n(.+)", section, re.DOTALL
        )
        eval_criteria = eval_match.group(1).strip() if eval_match else ""

        if prompt and response:
            tests.append(
                {
                    "id": test_id,
                    "name": test_name,
                    "prompt": prompt,
                    "system": system,
                    "response": response,
                    "eval": eval_criteria,
                    "source_file": filepath.name,
                }
            )

    return tests


async def evaluate_test(
    client: anthropic.AsyncAnthropic,
    test: dict,
    semaphore: asyncio.Semaphore,
) -> dict:
    """Send a single test to Claude for evaluation."""
    async with semaphore:
        system_line = (
            f"\n**System prompt used:** {test['system']}" if test["system"] else ""
        )
        user_msg = (
            f"## Test: {test['name']}\n\n"
            f"**Prompt sent to model:**\n{test['prompt']}\n"
            f"{system_line}\n\n"
            f"**Model's response:**\n{test['response']}\n\n"
            f"**Evaluation criteria:**\n{test['eval']}"
        )

        try:
            message = await client.messages.create(
                model=EVALUATOR_MODEL,
                max_tokens=MAX_TOKENS,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_msg}],
            )

            reply = message.content[0].text

            # Parse structured response
            score_match = re.search(r"SCORE:\s*(PASS|PARTIAL|FAIL)", reply)
            issues_match = re.search(r"ISSUES:\s*(.+?)(?:\n|$)", reply)
            notes_match = re.search(r"NOTES:\s*(.+)", reply, re.DOTALL)

            score = score_match.group(1) if score_match else "UNKNOWN"
            issues = issues_match.group(1).strip() if issues_match else ""
            notes = notes_match.group(1).strip() if notes_match else reply

            return {
                **test,
                "score": score,
                "issues": issues,
                "notes": notes,
                "raw_reply": reply,
                "input_tokens": message.usage.input_tokens,
                "output_tokens": message.usage.output_tokens,
            }
        except Exception as e:
            return {
                **test,
                "score": "ERROR",
                "issues": str(e),
                "notes": f"API call failed: {e}",
                "raw_reply": "",
                "input_tokens": 0,
                "output_tokens": 0,
            }


# --- Main --------------------------------------------------------------------

async def main():
    if len(sys.argv) < 2:
        print("Usage: python verify.py <results_dir> [output_dir]")
        print("  results_dir: directory containing *_results_*.md files")
        print("  output_dir:  where to save report (default: results_dir)")
        sys.exit(1)

    results_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else results_dir

    if not results_dir.is_dir():
        print(f"ERROR: {results_dir} is not a directory")
        sys.exit(1)

    # Find results files
    result_files = sorted(results_dir.glob("*_results_*.md"))
    if not result_files:
        print(f"ERROR: No *_results_*.md files found in {results_dir}")
        sys.exit(1)

    print(f"Found {len(result_files)} results file(s):")
    for f in result_files:
        print(f"  {f.name}")

    # Parse all tests
    all_tests = []
    for f in result_files:
        tests = parse_results_file(f)
        print(f"  Parsed {len(tests)} tests from {f.name}")
        all_tests.extend(tests)

    print(f"\nTotal: {len(all_tests)} tests to verify")

    # Setup API client
    api_key = load_api_key()
    client = anthropic.AsyncAnthropic(api_key=api_key)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    # Run evaluations concurrently
    print(f"Evaluating with {EVALUATOR_MODEL} (max {MAX_CONCURRENT} concurrent)...\n")

    tasks = [evaluate_test(client, test, semaphore) for test in all_tests]
    results = []

    for i, coro in enumerate(asyncio.as_completed(tasks)):
        result = await coro
        results.append(result)
        icon = {
            "PASS": "\u2713", "PARTIAL": "~", "FAIL": "\u2717",
            "ERROR": "!", "UNKNOWN": "?",
        }.get(result["score"], "?")
        print(
            f"  [{i+1}/{len(all_tests)}] {icon} {result['id']}: "
            f"{result['name']} -> {result['score']}"
        )

    # Sort results back to original order
    order = {t["id"]: i for i, t in enumerate(all_tests)}
    results.sort(key=lambda r: order.get(r["id"], 999))

    # --- Generate report -----------------------------------------------------
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = output_dir / f"verification_{timestamp}.md"

    scores = {"PASS": 0, "PARTIAL": 0, "FAIL": 0, "ERROR": 0, "UNKNOWN": 0}
    for r in results:
        scores[r["score"]] = scores.get(r["score"], 0) + 1

    total_in = sum(r["input_tokens"] for r in results)
    total_out = sum(r["output_tokens"] for r in results)
    n = len(results)

    # Group by source file
    by_file: dict[str, list[dict]] = {}
    for r in results:
        by_file.setdefault(r["source_file"], []).append(r)

    lines = [
        "# Smoke Test Verification Report",
        f"**Evaluator:** `{EVALUATOR_MODEL}`",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Source:** {', '.join(f.name for f in result_files)}",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Total tests | {n} |",
        f"| PASS | {scores['PASS']} |",
        f"| PARTIAL | {scores['PARTIAL']} |",
        f"| FAIL | {scores['FAIL']} |",
        f"| ERROR | {scores.get('ERROR', 0) + scores.get('UNKNOWN', 0)} |",
        f"| **Pass rate** | **{scores['PASS']}/{n} "
        f"({100*scores['PASS']/n:.0f}%)** |",
        f"| **Pass+Partial** | **{scores['PASS']+scores['PARTIAL']}/{n} "
        f"({100*(scores['PASS']+scores['PARTIAL'])/n:.0f}%)** |",
        "",
        f"API usage: {total_in:,} input + {total_out:,} output tokens",
        "",
        "---",
        "",
        "## Results by Category",
        "",
    ]

    for source_file, file_results in by_file.items():
        fp = sum(1 for r in file_results if r["score"] == "PASS")
        pp = sum(1 for r in file_results if r["score"] == "PARTIAL")
        fl = sum(1 for r in file_results if r["score"] == "FAIL")

        category = source_file.split("_results_")[0].replace("_", " ").title()
        lines.append(
            f"### {category} "
            f"({fp} Pass / {pp} Partial / {fl} Fail "
            f"out of {len(file_results)})"
        )
        lines.append("")
        lines.append("| # | Test | Score | Issues |")
        lines.append("|---|------|-------|--------|")

        for r in file_results:
            icon = {
                "PASS": "PASS", "PARTIAL": "PARTIAL", "FAIL": "FAIL",
                "ERROR": "ERROR",
            }.get(r["score"], "???")
            issues_short = r["issues"]
            if len(issues_short) > 100:
                issues_short = issues_short[:100] + "..."
            lines.append(
                f"| {r['id']} | {r['name']} | {icon} | {issues_short} |"
            )

        lines.append("")

    # Detailed verdicts
    lines.append("---")
    lines.append("")
    lines.append("## Detailed Verdicts")
    lines.append("")

    for r in results:
        lines.append(f"### {r['id']}: {r['name']}")
        lines.append(f"**Score:** {r['score']}")
        if r["issues"] and r["issues"] != "None":
            lines.append(f"**Issues:** {r['issues']}")
        lines.append(f"**Notes:** {r['notes']}")
        lines.append("")

    report = "\n".join(lines)
    report_path.write_text(report, encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"Verification complete!")
    print(
        f"  PASS: {scores['PASS']}  "
        f"PARTIAL: {scores['PARTIAL']}  "
        f"FAIL: {scores['FAIL']}"
    )
    print(
        f"  Pass rate: {scores['PASS']}/{n} "
        f"({100*scores['PASS']/n:.0f}%)"
    )
    print(f"  Report: {report_path}")
    print(f"  API usage: {total_in:,} input + {total_out:,} output tokens")


if __name__ == "__main__":
    asyncio.run(main())
