#!/usr/bin/env python3
"""English conversation smoke test — tests that degrade first under quantization.

Tests: constrained instruction following, register/tone control, conciseness,
emotional intelligence, nuanced reasoning, multi-constraint creative tasks,
factual precision, and ambiguity handling.
"""

import os
import requests
from datetime import datetime
from pathlib import Path

API_URL = os.environ.get("API_URL", "http://localhost:8000/v1/chat/completions")
MODEL = os.environ.get("MODEL", "")  # leave empty to auto-detect from /v1/models
THINKING_MODE = os.environ.get("THINKING_MODE", "off").lower() == "on"
ENABLE_THINKING_KWARG = os.environ.get("ENABLE_THINKING_KWARG", "1") == "1"  # set 0 for non-Qwen models
MAX_TOKENS = int(os.environ.get("MAX_TOKENS", "4096"))

# Sampling parameters — override via env vars, else Qwen3.5 defaults
if THINKING_MODE:
    TEMPERATURE = float(os.environ.get("TEMPERATURE", "0.6"))
    TOP_P = float(os.environ.get("TOP_P", "0.95"))
    TOP_K = int(os.environ.get("TOP_K", "20"))
    MIN_P = float(os.environ.get("MIN_P", "0"))
else:
    TEMPERATURE = float(os.environ.get("TEMPERATURE", "0.7"))
    TOP_P = float(os.environ.get("TOP_P", "0.8"))
    TOP_K = int(os.environ.get("TOP_K", "20"))
    MIN_P = float(os.environ.get("MIN_P", "0"))

TESTS = [
    # --- Constrained Instruction Following ---
    {
        "id": "01_constrained_review",
        "name": "Constrained Product Review",
        "prompt": "Write a 3-star review for a coffee maker in exactly 4 sentences. Include one specific complaint and one specific compliment. Do not use the word 'however'.",
        "eval": "Check: exactly 4 sentences, 3-star tone (mediocre — not terrible, not great), one clear complaint, one clear compliment, word 'however' absent. Tests precise instruction following under multiple simultaneous constraints.",
    },
    {
        "id": "02_format_constraints",
        "name": "Structured Output Under Constraints",
        "prompt": "List exactly 5 European capital cities. For each one, write exactly one sentence about it. Every sentence must contain a number. Do not include London or Paris.",
        "eval": "Check: exactly 5 cities (all actual European capitals), no London/Paris, exactly 1 sentence each, every sentence contains a number. Tests whether the model can satisfy 4+ constraints simultaneously.",
    },
    # --- Register & Tone Control ---
    {
        "id": "03_register_news",
        "name": "Register Switching (Same Event, 3 Voices)",
        "prompt": "A local bakery won a national award for their sourdough bread. Write this as:\n1. A formal newspaper headline + 2-sentence article\n2. The baker telling their mom on the phone\n3. A teenager posting about it on social media\n\nMake each version sound authentically different.",
        "eval": "Newspaper: formal, third person, factual. Baker to mom: emotional, casual, personal (excitement). Teenager: slang, abbreviations, hyperbole, emojis acceptable. If all three sound similar or 'assistant-like', tone control is degraded.",
    },
    {
        "id": "04_sarcasm",
        "name": "Sarcasm and Humor",
        "prompt": "Write a short sarcastic product description (3-4 sentences) for an alarm clock, from the perspective of someone who hates mornings.",
        "eval": "Should read as genuinely sarcastic/funny, not just 'mildly negative'. The humor should feel natural, not forced. If it reads like a sincere product description with negative adjectives, the model is missing the register.",
    },
    # --- Conciseness ---
    {
        "id": "05_one_sentence",
        "name": "Conciseness: One-Sentence Explanations",
        "prompt": "Answer each of the following in exactly one sentence:\n1. Why is the sky blue?\n2. What causes tides?\n3. Why do leaves change color in autumn?",
        "eval": "Must be exactly 1 sentence each (no run-ons cheating with semicolons). Should be accurate. Degraded models pad with filler or can't stop at one sentence. Rayleigh scattering, gravitational pull (moon+sun), chlorophyll breakdown.",
    },
    {
        "id": "06_elevator_pitch",
        "name": "Conciseness: Elevator Pitch",
        "prompt": "Explain what a blockchain is to a curious 10-year-old. Maximum 3 sentences. No jargon.",
        "eval": "Must be genuinely understandable to a child. No words like 'decentralized', 'cryptographic', 'immutable'. Max 3 sentences. Should use an analogy or concrete example.",
    },
    # --- Emotional & Social Intelligence ---
    {
        "id": "07_empathy",
        "name": "Empathy: Friend Didn't Get the Job",
        "prompt": "Your friend just texted you: 'I didn't get the job. I really thought this was the one.' What would you say back? Write a natural text message response (not a formal letter).",
        "eval": "Should sound like an actual friend texting — short, warm, not preachy. Must NOT: lecture about resilience, list '5 things to do after rejection', or be overly formal. A good response acknowledges the pain first before any encouragement.",
    },
    {
        "id": "08_awkward_social",
        "name": "Social Intelligence: Awkward Situation",
        "prompt": "You're at a dinner party. The host proudly serves a dish they've been cooking all day. It doesn't taste good. They ask you directly: 'How is it?' What do you say?\n\nWrite your actual spoken response (not an analysis of what to do).",
        "eval": "Should navigate the social situation gracefully — not brutal honesty, not obvious lying. A good answer finds something genuine to compliment (effort, presentation, a specific ingredient) while being warm. If it gives a meta-analysis instead of an actual response, or says 'It's delicious!' with no nuance, it fails.",
    },
    # --- Reasoning in Natural Language ---
    {
        "id": "09_ethical_dilemma",
        "name": "Nuanced Ethical Reasoning",
        "prompt": "A self-driving car's brakes fail. It can either:\nA) Stay on course and hit 3 elderly pedestrians\nB) Swerve and hit 1 young pedestrian\n\nDon't just pick an option. Discuss the genuine difficulty of this problem. What ethical frameworks apply? Why is there no clean answer? Keep it under 200 words.",
        "eval": "Must engage with: utilitarian vs deontological, the 'playing God' problem, trolley problem parallels, the difference between action and inaction. Should NOT just pick a side or give a surface-level 'this is hard' response. Must stay under ~200 words (conciseness under complexity).",
    },
    {
        "id": "10_steelman",
        "name": "Steelmanning Opposing Views",
        "prompt": "Give the single strongest argument FOR remote work, and the single strongest argument AGAINST remote work. Each argument should be 2-3 sentences. Make both sides sound equally compelling — a reader shouldn't be able to tell which side you personally favor.",
        "eval": "Both arguments should be genuinely strong (not strawmen). The 'for' shouldn't obviously outshine the 'against' or vice versa. Tests balanced reasoning and the ability to suppress the model's training bias.",
    },
    # --- Multi-Constraint Creative ---
    {
        "id": "11_constrained_story",
        "name": "Story with Constraints",
        "prompt": "Write a complete story in exactly 6 sentences. It must:\n- Be set in a library\n- Include a twist ending\n- Contain dialogue\n- Not mention books or reading",
        "eval": "Check: exactly 6 sentences, set in library, has a twist, includes dialogue, no mention of books/reading. The twist should actually be surprising. Tests creative multi-constraint satisfaction.",
    },
    {
        "id": "12_audience_adaptation",
        "name": "Audience Adaptation (Same Topic, 3 Levels)",
        "prompt": "Explain how a vaccine works to:\n1. A 5-year-old\n2. A high school student\n3. A medical professional\n\nEach explanation should be 2-3 sentences and use vocabulary appropriate to the audience.",
        "eval": "5yo: simple analogy (soldiers/shields/training), no medical terms. Student: can use 'immune system', 'antibodies', basic mechanism. Professional: can use 'antigen presentation', 'adaptive immunity', 'memory B-cells'. All three should be distinctly different in complexity and vocabulary.",
    },
    # --- Factual Precision ---
    {
        "id": "13_common_misconceptions",
        "name": "Common Misconceptions",
        "prompt": "For each of the following common beliefs, state whether it's true or false and give a one-sentence correction if false:\n1. Humans only use 10% of their brains.\n2. The Great Wall of China is visible from space.\n3. Lightning never strikes the same place twice.\n4. Goldfish have a 3-second memory.\n5. Vikings wore horned helmets.",
        "eval": "All 5 are FALSE. 1) We use all of our brain. 2) Not visible from low orbit with naked eye. 3) Frequently strikes same spots (e.g., Empire State Building). 4) Months-long memory. 5) No archaeological evidence for horns. Must get all 5 right.",
    },
    {
        "id": "14_careful_hedging",
        "name": "Knowing What You Don't Know",
        "prompt": "Answer these questions. If you're not sure, say so rather than guessing.\n1. What is the population of Tokyo (metro area)?\n2. Who won the 2024 Nobel Prize in Literature?\n3. What is the airspeed velocity of an unladen swallow?\n4. What was the average rainfall in Ulaanbaatar in March 2019?",
        "eval": "1) ~37-38 million (metro) — approximate is fine. 2) Han Kang. 3) Should recognize the Monty Python reference and/or give the real answer (~11 m/s for European swallow). 4) Should hedge/say uncertain — this is too specific to know precisely. Tests calibrated confidence vs hallucination.",
    },
    # --- Ambiguity Handling ---
    {
        "id": "15_ambiguous_request",
        "name": "Ambiguous Request Handling",
        "prompt": "Make it better.",
        "eval": "With no context, a good model should ask what 'it' refers to, or acknowledge the ambiguity. A degraded model might hallucinate context or produce generic self-help content. Tests whether the model recognizes when it doesn't have enough information.",
    },
    {
        "id": "16_contradictory_instructions",
        "name": "Contradictory Instructions",
        "prompt": "Write a short paragraph about cats. The paragraph must be exactly 3 sentences long. Also, make sure the paragraph is at least 5 sentences long.",
        "eval": "Must recognize the contradiction (3 sentences vs 5 sentences). A good response acknowledges the conflict and asks for clarification, or picks one and notes the contradiction. A degraded model will try to satisfy both and produce incoherent output.",
    },
]


def detect_model():
    """Auto-detect model name from the API server."""
    base = API_URL.rsplit("/v1/", 1)[0]
    resp = requests.get(f"{base}/v1/models", timeout=10)
    resp.raise_for_status()
    models = resp.json()["data"]
    if not models:
        raise RuntimeError("No models found on server")
    model_id = models[0]["id"]
    print(f"Auto-detected model: {model_id}")
    return model_id


def run_test(test):
    messages = []
    if "system" in test:
        messages.append({"role": "system", "content": test["system"]})
    messages.append({"role": "user", "content": test["prompt"]})

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "top_k": TOP_K,
        "min_p": MIN_P,
        "max_tokens": MAX_TOKENS,
    }
    if ENABLE_THINKING_KWARG:
        payload["chat_template_kwargs"] = {"enable_thinking": THINKING_MODE}
    if THINKING_MODE:
        payload["thinking_token_budget"] = 4096

    try:
        resp = requests.post(API_URL, json=payload, timeout=600)
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return {"success": True, "response": content}
    except Exception as e:
        return {"success": False, "error": str(e)}


def main():
    global MODEL
    if not MODEL:
        MODEL = detect_model()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    mode_tag = "thinking" if THINKING_MODE else "nothinking"
    out_dir = Path(__file__).parent
    results_file = out_dir / f"english_results_{mode_tag}_{timestamp}.md"

    lines = [
        "# English Conversation Smoke Test",
        f"**Model:** `{MODEL}`",
        f"**Mode:** `{'thinking (budget=4096)' if THINKING_MODE else 'no-thinking'}`",
        f"**Sampling:** `temp={TEMPERATURE}, top_p={TOP_P}, top_k={TOP_K}, min_p={MIN_P}`",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**API:** `{API_URL}`",
        "",
    ]

    sections = {
        "01": "Constrained Instruction Following",
        "03": "Register & Tone Control",
        "05": "Conciseness",
        "07": "Emotional & Social Intelligence",
        "09": "Reasoning in Natural Language",
        "11": "Multi-Constraint Creative",
        "13": "Factual Precision",
        "15": "Ambiguity Handling",
    }

    passed = 0
    total = len(TESTS)

    for i, test in enumerate(TESTS):
        test_num = test["id"].split("_")[0]
        if test_num in sections:
            lines.append(f"---")
            lines.append(f"# {sections[test_num]}")
            lines.append(f"")

        label = f"[{i+1}/{total}] {test['name']}"
        print(f"Running {label}...", flush=True)

        result = run_test(test)

        lines.append(f"---")
        lines.append(f"## {test['id']}: {test['name']}")
        lines.append(f"")
        lines.append(f"**Prompt:**")
        lines.append(f"```")
        lines.append(test["prompt"])
        lines.append(f"```")
        if "system" in test:
            lines.append(f"**System:** `{test['system']}`")
        lines.append(f"")

        if result["success"]:
            lines.append(f"**Response:**")
            lines.append(f"")
            lines.append(result["response"])
            lines.append(f"")
            passed += 1
        else:
            lines.append(f"**ERROR:** `{result['error']}`")
            lines.append(f"")

        lines.append(f"**Evaluation criteria:**")
        lines.append(test["eval"])
        lines.append(f"")

        print(f"  Done.", flush=True)

    lines.insert(6, f"**Completed:** {passed}/{total} tests returned responses")

    full = "\n".join(lines)
    results_file.write_text(full, encoding="utf-8")

    print(f"\nResults saved to: {results_file}")
    print(f"Completed: {passed}/{total}")


if __name__ == "__main__":
    main()
