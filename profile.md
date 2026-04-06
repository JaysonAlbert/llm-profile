
# LLM Context Length Performance Benchmark

## Testing Notes
- Test tool: `uv run python main.py`
- Context lengths vary per model (see MODELS_CTX)
- Models automatically killed between tests


## gemma4:26b


### Context 16k

```json
{
  "model": "gemma4:26b",
  "context_length": 16384,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 3197.72,
    "decode_tok_s": 187.63
  },
  "long_prompt": {
    "prompt_tokens": 2894,
    "prefill_ms": 328.17,
    "prefill_tok_s": 8818.66,
    "tokens_generated": 32,
    "decode_ms": 173.12,
    "decode_tok_s": 184.84,
    "total_ms": 676.94
  }
}
```

### Context 32k

```json
{
  "model": "gemma4:26b",
  "context_length": 32768,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 3185.48,
    "decode_tok_s": 188.35
  },
  "long_prompt": {
    "prompt_tokens": 5761,
    "prefill_ms": 683.46,
    "prefill_tok_s": 8429.2,
    "tokens_generated": 32,
    "decode_ms": 174.02,
    "decode_tok_s": 183.89,
    "total_ms": 1049.63
  }
}
```

### Context 64k

```json
{
  "model": "gemma4:26b",
  "context_length": 65536,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 3175.6,
    "decode_tok_s": 188.94
  },
  "long_prompt": {
    "prompt_tokens": 11495,
    "prefill_ms": 1395.16,
    "prefill_tok_s": 8239.18,
    "tokens_generated": 32,
    "decode_ms": 176.12,
    "decode_tok_s": 181.69,
    "total_ms": 1808.36
  }
}
```

### Context 128k

```json
{
  "model": "gemma4:26b",
  "context_length": 131072,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 3194.23,
    "decode_tok_s": 187.84
  },
  "long_prompt": {
    "prompt_tokens": 22963,
    "prefill_ms": 3068.02,
    "prefill_tok_s": 7484.64,
    "tokens_generated": 32,
    "decode_ms": 201.99,
    "decode_tok_s": 158.42,
    "total_ms": 3614.8
  }
}
```

## gemma4:31b


### Context 16k

```json
{
  "model": "gemma4:31b",
  "context_length": 16384,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 9465.28,
    "decode_tok_s": 63.39
  },
  "long_prompt": {
    "prompt_tokens": 2894,
    "prefill_ms": 915.51,
    "prefill_tok_s": 3161.08,
    "tokens_generated": 32,
    "decode_ms": 509.31,
    "decode_tok_s": 62.83,
    "total_ms": 1591.11
  }
}
```

### Context 32k

```json
{
  "model": "gemma4:31b",
  "context_length": 32768,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 9474.96,
    "decode_tok_s": 63.32
  },
  "long_prompt": {
    "prompt_tokens": 5761,
    "prefill_ms": 1998.94,
    "prefill_tok_s": 2882.03,
    "tokens_generated": 32,
    "decode_ms": 522.13,
    "decode_tok_s": 61.29,
    "total_ms": 2714.55
  }
}
```

### Context 64k

```json
{
  "model": "gemma4:31b",
  "context_length": 65536,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 43081.31,
    "decode_tok_s": 13.93
  },
  "long_prompt": {
    "prompt_tokens": 11495,
    "prefill_ms": 8760.39,
    "prefill_tok_s": 1312.16,
    "tokens_generated": 32,
    "decode_ms": 2290.91,
    "decode_tok_s": 13.97,
    "total_ms": 11295.73
  }
}
```

## qwen3.5:35b


### Context 16k

```json
{
  "model": "qwen3.5:35b",
  "context_length": 16384,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 44727.11,
    "decode_tok_s": 13.41
  },
  "long_prompt": {
    "prompt_tokens": 2890,
    "prefill_ms": 17451.43,
    "prefill_tok_s": 165.6,
    "tokens_generated": 32,
    "decode_ms": 2426.81,
    "decode_tok_s": 13.19,
    "total_ms": 20021.02
  }
}
```

### Context 32k

```json
{
  "model": "qwen3.5:35b",
  "context_length": 32768,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 3815.84,
    "decode_tok_s": 157.24
  },
  "long_prompt": {
    "prompt_tokens": 5757,
    "prefill_ms": 1674.19,
    "prefill_tok_s": 3438.68,
    "tokens_generated": 32,
    "decode_ms": 206.07,
    "decode_tok_s": 155.28,
    "total_ms": 2017.63
  }
}
```

### Context 64k

```json
{
  "model": "qwen3.5:35b",
  "context_length": 65536,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 3773.14,
    "decode_tok_s": 159.02
  },
  "long_prompt": {
    "prompt_tokens": 11491,
    "prefill_ms": 3417.79,
    "prefill_tok_s": 3362.11,
    "tokens_generated": 32,
    "decode_ms": 219.36,
    "decode_tok_s": 145.88,
    "total_ms": 3781.81
  }
}
```

### Context 128k

```json
{
  "model": "qwen3.5:35b",
  "context_length": 131072,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 3805.04,
    "decode_tok_s": 157.69
  },
  "long_prompt": {
    "prompt_tokens": 22959,
    "prefill_ms": 6874.26,
    "prefill_tok_s": 3339.85,
    "tokens_generated": 32,
    "decode_ms": 220.65,
    "decode_tok_s": 145.02,
    "total_ms": 7260.93
  }
}
```

### Context 256k

```json
{
  "model": "qwen3.5:35b",
  "context_length": 262144,
  "short_prompt": {
    "tokens_generated": 600,
    "decode_ms": 13323.99,
    "decode_tok_s": 45.03
  },
  "long_prompt": {
    "prompt_tokens": 28022,
    "prefill_ms": 11041.14,
    "prefill_tok_s": 2537.96,
    "tokens_generated": 32,
    "decode_ms": 685.55,
    "decode_tok_s": 46.68,
    "total_ms": 11880.79
  }
}
```

# End of Benchmark
