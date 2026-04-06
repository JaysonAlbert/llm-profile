# LLM Performance Benchmark

## Overview
Comparing three popular open-source LLMs: qwen3.5:35B, gemma4:26B, gemma4:31B

## Evaluation Criteria

**推荐指数** based on:
1. **Context Length** - As large as possible
2. **Decoding Speed** - Should be fast
3. **Model Quality** - Good reasoning and code generation

## Comparison Table

| Model | Context | Decode Speed | VRAM | Recommendation |
|-------|---------|--------------|------|----------------|
| qwen3.5:35B | 256k | 45.03 token/s | Medium | ⭐⭐⭐⭐⭐ |
| qwen3.5:35B | 128k | 157.69 token/s | Medium | ⭐⭐⭐⭐⭐ |
| qwen3.5:35B | 64k | 159.02 token/s | Medium | ⭐⭐⭐⭐⭐ |
| qwen3.5:35B | 32k | 157.24 token/s | Medium | ⭐⭐⭐⭐⭐ |
| gemma4:26B | 128k | 187.84 token/s | Low | ⭐⭐⭐⭐ |
| gemma4:26B | 64k | 188.94 token/s | Low | ⭐⭐⭐⭐ |
| gemma4:26B | 32k | 188.35 token/s | Low | ⭐⭐⭐⭐ |
| gemma4:26B | 16k | 187.63 token/s | Low | ⭐⭐⭐⭐ |
| gemma4:31B | 16k | 63.39 token/s | High | ⭐⭐ |
| gemma4:31B | 32k | 63.32 token/s | High | ⭐⭐ |
| gemma4:31B | 64k | 13.93 token/s | High | ⭐⭐ |

## Key Findings

### Why qwen3.5:35B Wins

**Best balance of:**
- ✅ Fast decoding speed (150+ token/s at 32k-128k)
- ✅ Ultra-long 256k context support
- ✅ Medium VRAM requirements
- ✅ Excellent reasoning and code generation

## Related Links

- [Full Benchmark Data](profile.md) - Raw performance data
- [RTX 5090 Setup Guide](../articles/rtx5090-setup.md) - Complete deployment tutorial

---

*Last updated: 2026-04-06*
