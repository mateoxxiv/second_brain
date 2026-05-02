---
tags:
  - status/seed
  - llms
related:
  - "[[anthropic-claude-api]]"
  - "[[claude-code]]"
  - "[[model-context-protocol]]"
domain: llms
sources:
  - "https://github.com/anthropics/claude-agent-sdk-python"
  - "https://pypi.org/project/claude-agent-sdk/"
  - "https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk"
  - "https://nader.substack.com/p/the-complete-guide-to-building-agents"
---

> **TL;DR** — The Claude Agent SDK manages the full agent loop (think → tool → observe → repeat) so you don't have to. Give it a task and custom tools; it handles everything in between.

---

## Intuition

The raw [[anthropic-claude-api]] handles one request → one response. If Claude decides to use a tool, you have to handle the loop yourself. The Agent SDK removes that burden: you describe a task, define your tools, and the SDK runs the complete think → pick tool → execute → observe → repeat cycle until done.

It was originally named "Claude Code SDK" but renamed because it goes far beyond coding.

## Mechanics

**Raw API vs Agent SDK:**
```
Raw API:   You send message → Claude responds → if tool needed, YOU manage the loop
Agent SDK: You describe task → SDK runs full loop until complete
```

**Custom tools — two approaches:**

1. In-process MCP (Python functions, no separate server)
2. External MCP servers (connect existing [[model-context-protocol]] servers)

**Hooks** fire at specific loop events:
- `before_tool_call` — log, validate, or block tool calls
- `after_response` — check cost, enforce constraints

```python
from claude_agent_sdk import ClaudeSDKClient

client = ClaudeSDKClient()

# Custom tool
@client.tool("get_weather")
def get_weather(city: str) -> str:
    return f'{{"city": "{city}", "temp": 22, "condition": "cloudy"}}'

# Hook for cost control
@client.hook("after_response")
def check_cost(response):
    if total_cost > budget:
        raise BudgetExceeded()

# Run — SDK handles the entire loop
response = client.send("What's the weather in Bogotá and Medellín?")
```

> Runnable: [[code/llms/claude_agent_sdk.py]]

## In ML

**Agent loop abstraction.** Building the tool-use loop from scratch with the raw API requires handling stop_reason == "tool_use", executing functions, returning results in the right format, and looping. The SDK makes this one method call, removing boilerplate that doesn't add value.

**MCP for external tool connections.** The SDK supports connecting to any MCP server — giving your agent access to databases, Slack, GitHub, or any custom service with a single configuration entry. No custom integration code needed.

**Hooks for observability and safety.** Hooks are the production-grade version of "add logging everywhere." A before_tool_call hook captures every tool call for debugging. An after_response hook enforces budget limits. These run deterministically, unlike prompting.

## Exercises

**Basic** — Describe the difference between agent-as-tool vs handoff in multi-agent systems. Which pattern does the Claude Agent SDK primarily support?

**Intermediate** — Write a custom tool that searches a Python list of dictionaries by key-value pair. Add a before_tool_call hook that logs the query to a file.

**Advanced** — Explain what hooks enable that raw API code cannot. Give three concrete production use cases where you would use hooks rather than prompting.
