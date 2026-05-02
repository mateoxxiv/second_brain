---
tags:
  - status/seed
  - llms
related:
  - "[[anthropic-claude-api]]"
  - "[[openai-codex]]"
  - "[[openai-agents-sdk]]"
domain: llms
sources:
  - "https://developers.openai.com/api/docs"
  - "https://openai.com/api/pricing/"
  - "https://github.com/openai/openai-python"
  - "https://platform.openai.com/docs/guides/responses-vs-chat-completions"
---

> **TL;DR** — OpenAI has two APIs: Chat Completions (legacy, fine) and Responses API (new, recommended). Use Responses for new projects — it adds built-in tools, better caching, and stateful chaining via previous_response_id.

---

## Intuition

Like the Anthropic API, OpenAI's API is stateless — you send the full conversation each time. But OpenAI has evolved faster in API design: the new Responses API adds built-in web search, code interpreter, and file search without needing external integrations.

OpenAI's broader ecosystem: [[openai-codex]] (agentic coding), [[openai-agents-sdk]] (build custom agents).

## Mechanics

**Two APIs:**

| Feature | Chat Completions | Responses API |
|---------|-----------------|---------------|
| State | Manual | previous_response_id chains calls |
| Built-in tools | None | Web search, code interpreter, file search |
| Recommended for | Existing code | New projects |

**Models (as of May 2026):**

| Model | Input (per 1M) | Best for |
|-------|----------------|---------|
| GPT-5 Nano | $0.05 | Classification, extraction |
| GPT-5 Mini | $0.25 | Fast, cost-efficient |
| GPT-5 | $1.25 | Strong general purpose |
| GPT-5.2 | $1.75 | Best quality |
| o3 | $2.00 | Complex reasoning, math |

**Key OpenAI-specific features:** Structured Outputs (strict: true guarantees JSON schema compliance at token level), o-series reasoning tokens (billed but not visible in response).

```python
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from env

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor."},
        {"role": "user", "content": "What is a dot product?"}
    ]
)
print(response.choices[0].message.content)
print(f"Tokens: {response.usage.prompt_tokens} in / {response.usage.completion_tokens} out")
```

> Runnable: [[code/llms/openai_api.py]]

## In ML

**Structured Outputs.** Add strict: true to function definitions and OpenAI guarantees the output matches your JSON schema at the token generation level. More reliable than Anthropic's approach for applications requiring strict output format.

**o-series reasoning tokens.** Models o3 and o4-mini use internal reasoning tokens billed as output but not visible in the response. A 500-token visible response may cost 2000+ tokens. Always estimate real cost with a buffer for reasoning models.

**Responses API built-in tools.** Web search, code interpreter, and file search are hosted tools requiring no external setup — unlike Anthropic which requires [[model-context-protocol]] servers for equivalent functionality.

## Exercises

**Basic** — Write a script using Chat Completions that manages a 3-turn conversation manually. Then rewrite it using the Responses API with previous_response_id.

**Intermediate** — Implement a function-calling loop with strict: true. Define a schema, handle the tool call, return the result, and verify the output always matches your schema.

**Advanced** — Compare costs for an o3 call vs GPT-5 Mini call on a complex reasoning task. Account for reasoning tokens in your o3 cost estimate.
