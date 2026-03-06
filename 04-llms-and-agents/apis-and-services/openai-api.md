**Related**: [[anthropic-claude-api]], [[Model Selection Framework]], [[Prompt Design Patterns]], [[openai-codex]], [[openai-agents-sdk]]
**Tags**: #status/seed

## Core Idea

The OpenAI API is the programmatic interface to GPT models and the o-series
reasoning models. Like the [[anthropic-claude-api|Anthropic API]], it's
**stateless** — you send the full conversation each time and get a response back.
But OpenAI has evolved faster in API design: they now have **two APIs** for text
generation (Chat Completions and the newer Responses API), plus a growing
ecosystem of hosted tools and agentic products.

OpenAI's broader ecosystem includes ChatGPT (consumer product), [[openai-codex]]
(agentic coding), the [[openai-agents-sdk]] (build your own agents), and a
marketplace of GPTs. This note covers the API itself.

## Details

### Architecture

```
YOUR APP                          OPENAI SERVERS
   |                                    |
   |  POST /v1/chat/completions         |  (Legacy, still supported)
   |  POST /v1/responses                |  (New, recommended)
   |  {model, input/messages,           |
   |   max_tokens, temperature, tools}  |
   |  --------------------------------> |
   |                                    |  Model processes
   |  <-------------------------------- |
   |  {output/choices, usage}           |
   |                                    |
```

### Two APIs: Responses vs Chat Completions

OpenAI now has **two** text generation APIs. The Responses API is recommended
for all new projects:

| Feature | Chat Completions | Responses API |
|---------|-----------------|---------------|
| Data format | Messages array | Items array |
| State management | Manual (send full history) | `previous_response_id` chains responses |
| Built-in tools | None | Web search, file search, code interpreter, computer use |
| MCP support | No | Remote MCP servers |
| Reasoning models | Works, but less optimized | 3% better on benchmarks (SWE-bench) |
| Cache utilization | Standard | 40-80% better caching |
| Status | Supported indefinitely | Recommended for new projects |

**Rule of thumb**: Use Responses API for new projects. Chat Completions is fine
for existing code — no rush to migrate.

### Models (as of March 2026)

#### Flagship Models

| Model | ID | Context | Input (per 1M) | Output (per 1M) | Best for |
|-------|----|---------|----------------|-----------------|----------|
| GPT-5.2 | gpt-5.2 | 400K | $1.75 | $14.00 | Best quality: coding, reasoning, long context |
| GPT-5.2 Pro | gpt-5.2-pro | 400K | $21.00 | $168.00 | Maximum capability, complex research |
| GPT-5 | gpt-5 | 200K | $1.25 | $10.00 | Strong general purpose |
| GPT-5 Mini | gpt-5-mini | 200K | $0.25 | $2.00 | Fast, cost-efficient for most tasks |
| GPT-5 Nano | gpt-5-nano | 128K | $0.05 | $0.40 | Ultra-cheap, classification, extraction |

#### Reasoning Models (o-series)

| Model | ID | Input (per 1M) | Output (per 1M) | Best for |
|-------|----|----------------|-----------------|----------|
| o3 | o3 | $2.00 | $8.00 | Complex reasoning, math, science |
| o4-mini | o4-mini | $1.10 | $4.40 | Fast reasoning, cost-efficient |

**Reasoning tokens**: o-series models think internally using "reasoning tokens"
that are billed as output but NOT visible in the response. A 500-token visible
response can cost 2000+ tokens total. Budget accordingly.

#### Legacy (deprecated early 2026)

GPT-4.1, GPT-4o, GPT-4o Mini — still available but superseded by GPT-5 family.

**Rule of thumb**: Start with GPT-5 Mini. Drop to Nano for bulk/simple tasks.
Upgrade to GPT-5.2 for hard problems. Use o3/o4-mini for math and reasoning.

### Messages: The Conversation Format

Same alternating pattern as Anthropic:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is a vector?"},
    {"role": "assistant", "content": "A vector is an ordered list..."},
    {"role": "user", "content": "Give me an example in ML."},
]
```

**Rules**:
- System message goes first (optional but recommended)
- Messages alternate user / assistant
- You can pre-fill assistant messages to steer output

### Key Parameters

| Parameter | Range | What it controls |
|-----------|-------|-----------------:|
| **temperature** | 0.0 - 2.0 | 0 = deterministic, 2 = very creative |
| **max_tokens** | integer | Maximum output length |
| **top_p** | 0.0 - 1.0 | Nucleus sampling (alternative to temperature) |
| **frequency_penalty** | -2.0 to 2.0 | Penalize repeated tokens |
| **presence_penalty** | -2.0 to 2.0 | Encourage talking about new topics |
| **stop** | list[str] | Custom stop sequences |

**Note**: OpenAI allows temperature up to 2.0 (Anthropic caps at 1.0).
`frequency_penalty` and `presence_penalty` are OpenAI-specific.

### Tool Use (Function Calling)

Same concept as Anthropic, slightly different schema:

```
1. You define tools with JSON Schema
2. Model decides to call a tool → stop_reason = "tool_calls"
3. Your code executes the function
4. You send the result back as a "tool" role message
5. Model formulates its final answer
```

**Structured Outputs**: Add `strict: true` to your function definition and
OpenAI guarantees the output matches your JSON schema exactly. This is more
reliable than Anthropic's approach — the model is constrained at the token
level.

### Advanced Features

| Feature | What it does | When to use |
|---------|-------------|-------------|
| **Structured Outputs** | Guaranteed JSON schema compliance | Any time you need reliable JSON |
| **Reasoning (o-series)** | Internal chain-of-thought before answering | Complex math, logic, coding |
| **Prompt caching** | Auto-caches repeated prefixes — up to 80% savings | Repeated system prompts, docs |
| **Batch API** | Async processing, 50% cheaper | Bulk classification, evaluation |
| **Vision** | Process images alongside text | Document analysis, charts, screenshots |
| **Computer use** | Operate a computer via screenshots + actions | UI automation, testing |
| **Web search** | Built-in web search (Responses API) | Real-time information |
| **Code interpreter** | Execute Python in sandbox (Responses API) | Data analysis, math |
| **File search** | Search uploaded files (Responses API) | RAG-like retrieval |
| **Streaming** | Get tokens as generated | Better UX, real-time output |
| **Realtime API** | WebSocket-based voice/text | Voice agents, live interaction |

### Subscription Plans

| Plan | Price | Key features |
|------|-------|-------------|
| Free | $0 | Basic GPT access, limited usage |
| Go | ~$10/mo | Expanded limits, faster responses |
| Plus | $20/mo | All models, higher limits, Codex access |
| Pro | $200/mo | Unlimited GPT-5.2, max reasoning, priority |
| Team | $25-30/user/mo | Shared workspaces, admin controls |
| Enterprise | Custom | SSO, audit logs, unlimited usage, data privacy |

### Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 400 | Invalid parameters | Check message format, model ID |
| 401 | Bad API key | Check OPENAI_API_KEY |
| 429 | Rate limit | Retry with exponential backoff |
| 500 | Server error | Retry after delay |

### Authentication

```bash
export OPENAI_API_KEY="sk-..."
```

**Never** hardcode API keys. Use environment variables or `.env` files.

### OpenAI vs Anthropic API Comparison

| Aspect | OpenAI | Anthropic |
|--------|--------|-----------|
| Text API | Chat Completions + Responses API | Messages API |
| State management | Manual or `previous_response_id` | Manual only |
| Built-in tools | Web search, file search, code interpreter | None (use MCP) |
| Structured output | `strict: true` — guaranteed schema | Less strict |
| Temperature range | 0.0 - 2.0 | 0.0 - 1.0 |
| Reasoning models | o3, o4-mini (reasoning tokens) | Extended thinking (Opus) |
| Coding agent | [[openai-codex\|Codex]] | [[claude-code]] |
| Agent SDK | [[openai-agents-sdk]] | [[claude-agent-sdk]] |
| Cheapest model | GPT-5 Nano ($0.05/$0.40) | Haiku 4.5 ($0.80/$4.00) |
| Best model | GPT-5.2 Pro ($21/$168) | Opus 4.6 ($15/$75) |

## Code Example

```python
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from env

# Basic message
response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor."},
        {"role": "user", "content": "What is a dot product?"}
    ]
)

print(response.choices[0].message.content)
print(f"Tokens: {response.usage.prompt_tokens} in, {response.usage.completion_tokens} out")
```

> For runnable implementation, see: [[code/llms/openai_api.py]]

## Connections

- Compare with [[anthropic-claude-api]] — similar structure, different features
- System prompts connect to [[Prompt Design Patterns]]
- Tool use is the foundation of [[Agent Patterns]] and [[Function Calling]]
- [[openai-codex]] is OpenAI's agentic coding tool (like [[claude-code]])
- [[openai-agents-sdk]] lets you build custom agents (like [[claude-agent-sdk]])
- Structured Outputs are key for reliable [[Function Calling]]
- Token counting matters for [[Pricing Models and Cost Optimization]]

## Sources

- [OpenAI API Documentation](https://developers.openai.com/api/docs)
- [OpenAI Pricing](https://openai.com/api/pricing/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Responses API vs Chat Completions](https://platform.openai.com/docs/guides/responses-vs-chat-completions)
- [OpenAI Models](https://developers.openai.com/api/docs/models)
- [Structured Outputs Guide](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
