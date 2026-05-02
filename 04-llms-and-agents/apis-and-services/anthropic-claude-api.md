---
tags:
  - status/seed
  - llms
related:
  - "[[openai-api]]"
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[model-context-protocol]]"
domain: llms
sources:
  - "https://platform.claude.com/docs"
  - "https://github.com/anthropics/anthropic-sdk-python"
  - "https://github.com/anthropics/anthropic-cookbook"
  - "https://claude.com/pricing"
---

> **TL;DR** — The Anthropic API is stateless: you send the full conversation history every time. Managing that history is your job. Tool use + prompt caching + streaming are the three features to master first.

---

## Intuition

The API is how you embed Claude in your applications — chatbots, RAG pipelines, data extractors, agents. Every request is self-contained: Claude has no memory between calls. You control exactly what it "knows" by controlling the messages you send.

The broader Anthropic ecosystem: [[claude-code]] (agentic CLI), [[claude-agent-sdk]] (build agents), [[model-context-protocol]] (connect to external tools). This note covers the API itself.

## Mechanics

**Request structure:** model + system + messages + max_tokens

**Response:** content (text/tool calls) + stop_reason ("end_turn" / "tool_use" / "max_tokens") + usage

**Models (as of May 2026):**

| Model | Context | Best for |
|-------|---------|---------|
| Haiku 4.5 | 200K | Classification, extraction, high-volume |
| Sonnet 4.6 | 200K (1M beta) | Most tasks: coding, analysis, chat |
| Opus 4.6 | 200K | Complex reasoning, hard problems |

**Rule of thumb:** Start Sonnet. Drop to Haiku for cost/speed. Upgrade to Opus when Sonnet fails.

**Temperature guide:** 0.0 = deterministic (extraction, code), 0.3–0.5 = general, 0.7–1.0 = creative.

```python
import anthropic

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from env

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a helpful math tutor.",
    messages=[{"role": "user", "content": "What is a dot product?"}]
)
print(response.content[0].text)
print(f"Tokens: {response.usage.input_tokens} in / {response.usage.output_tokens} out")
```

> Runnable: [[code/llms/anthropic_api.py]]

## In ML

**Tool use (function calling).** Give Claude tool definitions. When it needs one, stop_reason = "tool_use". Your code executes the function and returns the result. Claude formulates the final answer. This is the foundation of [[claude-agent-sdk]] agents.

**Prompt caching.** Cache repeated prefixes (system prompts, long documents) — up to 90% cost reduction on subsequent calls. Prefix must be ≥ 1024 tokens and identical across requests. Critical for any production application with a long system prompt.

**Advanced features worth knowing:** Batch API (50% cheaper, async), Extended thinking (visible chain-of-thought), Vision (images + PDFs), Streaming (tokens as generated), Citations (source attribution in RAG).

## Exercises

**Basic** — Write a script that sends a multi-turn conversation (3 exchanges) to Claude and prints each response. Manually manage the messages array.

**Intermediate** — Implement a tool-use loop: define a get_weather tool, handle the tool_use stop_reason, return results, and get the final answer.

**Advanced** — Implement prompt caching for a long system prompt. Measure the token cost difference between cached and uncached calls using response.usage.
