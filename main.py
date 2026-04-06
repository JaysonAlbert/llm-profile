import json
import time
import requests
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Any

BASE = "http://localhost:11434/api/generate"
API_KILL = "http://localhost:11434/api/kill"


def kill_model(model: str) -> None:
    try:
        requests.post(API_KILL, json={"model": model}, timeout=10)
    except Exception as e:
        log(f"  Kill model failed: {e}")


MODELS = ["gemma4:26b", "gemma4:31b", "qwen3.5:35b"]

MODELS_CTX = {
    "qwen3.5:35b": [16384, 32768, 65536, 131072, 262144],
    "gemma4:26b": [16384, 32768, 65536, 131072],
    "gemma4:31b": [16384, 32768, 65536],
}

LONG_PROMPT = ("The following is benchmark filler text. " * 4000)[:320000]


def run(model, prompt, num_predict, num_ctx):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "keep_alive": -1,
        "options": {
            "num_ctx": num_ctx,
            "temperature": 0,
            "num_predict": num_predict,
            "seed": 42,
        },
    }
    r = requests.post(BASE, json=payload, timeout=600)
    r.raise_for_status()
    return r.json()


def tok_per_s(count, duration_ns):
    if not duration_ns:
        return 0.0
    return round(count / (duration_ns / 1e9), 2)


OUTPUT_FILE = "profile.md"


# Global output handler
output_lines = []


def log(msg):
    output_lines.append(msg)
    print(msg)


def format_result(model, ctx_size, short_out, long_out):
    short_eval = short_out.get("eval_count", 0) or 0
    short_eval_dur = short_out.get("eval_duration", 0) or 0
    long_eval = long_out.get("eval_count", 0) or 0
    long_eval_dur = long_out.get("eval_duration", 0) or 0
    long_prefill = long_out.get("prompt_eval_count", 0) or 0
    long_prefill_dur = long_out.get("prompt_eval_duration", 0) or 0

    return {
        "model": model,
        "context_length": ctx_size,
        "short_prompt": {
            "tokens_generated": short_eval,
            "decode_ms": round((short_eval_dur or 0) / 1e6, 2),
            "decode_tok_s": tok_per_s(short_eval, short_eval_dur),
        },
        "long_prompt": {
            "prompt_tokens": long_prefill,
            "prefill_ms": round((long_prefill_dur or 0) / 1e6, 2),
            "prefill_tok_s": tok_per_s(long_prefill, long_prefill_dur),
            "tokens_generated": long_eval,
            "decode_ms": round((long_eval_dur or 0) / 1e6, 2),
            "decode_tok_s": tok_per_s(long_eval, long_eval_dur),
            "total_ms": round((long_out.get("total_duration", 0) or 0) / 1e6, 2),
        },
    }


results_by_model = {}

prev_model = None

for model in MODELS:
    if prev_model and prev_model != model:
        kill_model(prev_model)
        time.sleep(2)
    prev_model = model

    print(f"\n=== {model} ===")
    ctx_sizes = MODELS_CTX[model]
    results_by_model[model] = {}

    for ctx_size in ctx_sizes:
        print(f"\n--- Context: {ctx_size // 1024}k ---")
        warmup_prompt = "hello"
        kill_model(model)
        time.sleep(1)
        try:
            _ = run(model, warmup_prompt, 8, ctx_size)
        except Exception as e:
            log(f"  Warmup failed: {e}")
            continue

        try:
            short_result = run(
                model,
                "Write exactly 500 short numbered facts about computing, one per line.",
                600,
                ctx_size,
            )
            short_result["success"] = True
        except Exception as e:
            print(f"  Short prompt test failed: {e}")
            short_result = {"success": False, "error": str(e)}

        try:
            long_prompt_payload = LONG_PROMPT[: min(200000, ctx_size)]
            long_result = run(
                model,
                long_prompt_payload
                + "\n\nSummarize the detailed text above in one sentence.",
                32,
                ctx_size,
            )
            long_result["success"] = True
        except Exception as e:
            print(f"  Long prompt test failed: {e}")
            long_result = {"success": False, "error": str(e)}

        result = format_result(model, ctx_size, short_result, long_result)
        results_by_model[model][ctx_size] = result

        if not short_result.get("success") or not long_result.get("success"):
            log(f"Skipped: context={ctx_size // 1024}k")
        else:
            log(json.dumps(result, indent=2))

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n# LLM Context Length Performance Benchmark\n\n")
    f.write("## Testing Notes\n")
    f.write("- Test tool: `uv run python main.py`\n")
    f.write("- Context lengths vary per model (see MODELS_CTX)\n")
    f.write("- Models automatically killed between tests\n\n")

    for model in results_by_model:
        f.write(f"\n## {model}\n\n")
        for ctx_size in sorted(results_by_model[model].keys()):
            f.write(f"\n### Context {ctx_size // 1024}k\n\n")
            f.write("```json\n")
            f.write(
                json.dumps(
                    results_by_model[model][ctx_size], indent=2, ensure_ascii=False
                )
            )
            f.write("\n```\n")

    f.write("\n# End of Benchmark\n")

print(f"\n=== Results written to {OUTPUT_FILE} ===")
