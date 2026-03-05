**Related**: [[OpenAI API]], [[Model Selection Framework]], [[Prompt Design Patterns]], [[claude-code]], [[claude-agent-sdk]], [[model-context-protocol]]
**Tags**: #status/seed

## Core Idea

The Anthropic API is the programmatic interface to Claude models. Instead of
chatting in a browser, you send structured requests and get structured responses.
This is how you build AI-powered applications — chatbots, RAG pipelines, agents,
data extractors, and everything in between.

The most important thing to understand: **the API is stateless.** Claude doesn't
remember previous calls. You manage the conversation by sending the full message
history every time. This gives you complete control over what Claude "knows."

Anthropic's ecosystem is broader than just the API — it includes [[claude-code]]
(agentic CLI), [[claude-agent-sdk]] (build your own agents), and
[[model-context-protocol|MCP]] (connect AI to any data source). This note
covers the API itself.

## Details

### Architecture

```
YOUR APP                          ANTHROPIC SERVERS
   |                                    |
   |  POST /v1/messages                 |
   |  {model, system, messages,         |
   |   max_tokens, temperature, tools}  |
   |  --------------------------------> |
   |                                    |  Claude processes
   |  <-------------------------------- |
   |  {content, stop_reason, usage}     |
   |                                    |
```

Every request includes:
- **model**: Which Claude to use
- **system**: Instructions shaping behavior (optional but recommended)
- **messages**: The conversation history (alternating user/assistant)
- **max_tokens**: Maximum response length (required)

Every response includes:
- **content**: Claude's response (text and/or tool calls)
- **stop_reason**: Why it stopped ("end_turn", "max_tokens", "tool_use")
- **usage**: Token counts for billing (input_tokens, output_tokens)

### Models (as of March 2026)

| Model | ID | Context | Speed | Quality | Best for |
|-------|----|---------|-------|---------|----------|
| Haiku 4.5 | claude-haiku-4-5-20251001 | 200K | Fastest | Good | Classification, extraction, high-volume |
| Sonnet 4.6 | claude-sonnet-4-6 | 200K (1M beta) | Fast | Great | Most tasks: coding, analysis, conversation |
| Opus 4.6 | claude-opus-4-6 | 200K | Slower | Best | Complex reasoning, research, hard problems |

**Rule of thumb**: Start with Sonnet. Drop to Haiku for speed/cost. Upgrade to
Opus when Sonnet isn't good enough.

### Messages: The Conversation Format

Messages alternate between "user" and "assistant" roles:

```python
messages = [
    {"role": "user", "content": "What is a vector?"},
    {"role": "assistant", "content": "A vector is an ordered list..."},
    {"role": "user", "content": "Give me an example in ML."},
]
```

For multi-turn conversations, accumulate the history and send it all each time.

**Rules**:
- Messages MUST alternate user → assistant → user → assistant
- First message must be "user"
- You can pre-fill an assistant message to steer the response format

### System Prompt

A separate instruction that shapes Claude's behavior. Not part of the messages:

```python
system = "You are a math tutor. Explain step by step. Use simple language."
```

Keep it focused — long system prompts cost tokens every call. System prompts
are cached more efficiently than messages.

### Key Parameters

| Parameter | Range | What it controls |
|-----------|-------|-----------------|
| **temperature** | 0.0 - 1.0 | 0 = deterministic, 1 = creative |
| **max_tokens** | integer | Maximum output length (REQUIRED) |
| **top_p** | 0.0 - 1.0 | Nucleus sampling — alternative to temperature |
| **stop_sequences** | list[str] | Custom strings that stop generation |

**Temperature guide**:
- 0.0: Classification, extraction, math, code (same answer every time)
- 0.3-0.5: General tasks, analysis (slight variation)
- 0.7-1.0: Creative writing, brainstorming (different each time)

### Tool Use (Function Calling)

Give Claude tools — functions it can call to interact with the world:

```
1. You send message + tool definitions
2. Claude decides to call a tool → stop_reason = "tool_use"
3. Your code executes the function
4. You send the result back
5. Claude formulates its final answer

User: "Weather in Bogotá?"
  → Claude: tool_use(get_weather, {city: "Bogotá"})
    → Your code: calls weather API → "22°C, cloudy"
      → Claude: "It's 22°C and cloudy in Bogotá."
```

### Advanced API Features

| Feature | What it does | When to use |
|---------|-------------|-------------|
| **Extended thinking** | Claude shows step-by-step reasoning before answering | Complex math, logic, coding |
| **Prompt caching** | Cache repeated prefixes (system prompts, docs) — up to 90% savings | Any repeated context |
| **Batch API** | Async processing, 50% cheaper | Bulk classification, evaluation, non-urgent |
| **Citations** | Claude cites specific passages from provided documents | RAG, document Q&A |
| **Vision** | Process images and PDFs alongside text | Document analysis, charts, screenshots |
| **Computer use** | Claude operates a computer via screenshots + mouse/keyboard | Legacy software automation |
| **Streaming** | Get tokens as generated, not all at once | Better UX, real-time output |

### Subscription Plans

| Plan | Price | Key features |
|------|-------|-------------|
| Free | $0 | ~30-100 msgs/day, basic access |
| Pro | $20/mo | All models, [[claude-code]] access, Projects |
| Max 5x | $100/mo | 5x Pro, full Opus, priority, memory |
| Max 20x | $200/mo | 20x Pro usage |
| Team | $25-150/user/mo | Admin controls, shared workspaces |
| Enterprise | Custom | SSO, audit logs, HIPAA, 500K context |

### Tokens and Pricing (API)

Tokens ≈ word pieces. ~1 token = 4 characters in English.

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|----------------------|
| Haiku 4.5 | $0.80 | $4.00 |
| Sonnet 4.6 | $3.00 | $15.00 |
| Opus 4.6 | $15.00 | $75.00 |

**Cost optimization**:
- Use Haiku for simple tasks (10-20x cheaper than Opus)
- Prompt caching for repeated prefixes (up to 90% savings)
- Batch API for non-urgent tasks (50% discount)
- Trim conversation history — don't send 100 turns if 10 suffice
- Route by complexity: Haiku for easy, Sonnet for medium, Opus for hard

### Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 400 | Invalid parameters | Check message format, model ID |
| 401 | Bad API key | Check ANTHROPIC_API_KEY |
| 429 | Rate limit | Retry with exponential backoff |
| 529 | Server overloaded | Retry after delay |

### Authentication

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

**Never** hardcode API keys in source code. Use environment variables or a
`.env` file (add `.env` to `.gitignore`).

## Code Example

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a helpful math tutor.",
    messages=[
        {"role": "user", "content": "What is a dot product?"}
    ]
)

print(response.content[0].text)
print(f"Tokens: {response.usage.input_tokens} in, {response.usage.output_tokens} out")
```

> For runnable implementation, see: [[code/llms/anthropic_api.py]]

## Connections

- Compare with [[OpenAI API]] — similar structure, different features and pricing
- System prompts connect to [[Prompt Design Patterns]]
- Tool use is the foundation of [[Agent Patterns]] and [[Function Calling]]
- [[claude-code]] is built on this API + agentic capabilities
- [[claude-agent-sdk]] lets you build your own agents on top of the API
- [[model-context-protocol|MCP]] connects Claude to external data sources
- Token counting matters for [[Pricing Models and Cost Optimization]]

## Sources

- [Anthropic API Documentation](https://platform.claude.com/docs)
- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Anthropic Pricing](https://claude.com/pricing)
