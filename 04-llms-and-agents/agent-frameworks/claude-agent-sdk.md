**Related**: [[anthropic-claude-api]], [[claude-code]], [[model-context-protocol]], [[Agent Patterns]]
**Tags**: #status/seed

## Core Idea

The Claude Agent SDK lets you build your own AI agents powered by Claude. If
[[claude-code]] is Anthropic's agent for coding, the Agent SDK is the toolkit
for building agents that do **anything** — research, data analysis, workflow
automation, customer support, or your own custom use case.

It was originally called "Claude Code SDK" but renamed to "Claude Agent SDK"
to reflect that it goes far beyond coding tasks.

**Key difference from the raw API**: The [[anthropic-claude-api|Messages API]]
handles one request → one response. The Agent SDK manages the full **agent loop**
— reasoning, tool calls, multi-step execution, error recovery — so you don't
have to build that infrastructure yourself.

## Details

### What the SDK Provides

```
Raw API:
  You send a message → Claude responds → done.
  If Claude needs a tool, YOU manage the loop.

Agent SDK:
  You describe a task → SDK runs the full agent loop:
    Think → Pick tool → Execute → Observe → Repeat
  Until the task is complete. You define the tools and guardrails.
```

### Architecture

```
┌─────────────────────────────────────────────┐
│              Your Application               │
├─────────────────────────────────────────────┤
│              Claude Agent SDK               │
│  ┌─────────┐  ┌──────────┐  ┌───────────┐  │
│  │ Agent   │  │ Built-in │  │  Custom   │  │
│  │ Loop    │  │ Tools    │  │  Tools    │  │
│  │         │  │ (R/W/E/B)│  │ (via MCP) │  │
│  └─────────┘  └──────────┘  └───────────┘  │
├─────────────────────────────────────────────┤
│              Claude Code CLI                │
│         (bundled, no extra install)         │
├─────────────────────────────────────────────┤
│             Anthropic API                   │
└─────────────────────────────────────────────┘
```

### Built-in Tools

Same tools as [[claude-code]], available out of the box:

| Tool | What it does |
|------|-------------|
| Read | Read any file in the working directory |
| Write | Create new files |
| Edit | Precise edits to existing files |
| Bash | Run terminal commands |
| Glob | Find files by pattern |
| Grep | Search file contents |

### Custom Tools

Two ways to give your agent custom abilities:

**1. In-process MCP tools** — Python functions, no separate server:

```python
from claude_agent_sdk import ClaudeSDKClient

client = ClaudeSDKClient()

@client.tool("search_database")
def search_database(query: str, limit: int = 10) -> str:
    """Search the product database."""
    results = db.search(query, limit=limit)
    return json.dumps(results)
```

**2. External MCP servers** — connect to existing [[model-context-protocol]]
servers:

```python
client = ClaudeSDKClient(
    mcp_servers={
        "postgres": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-postgres"]
        }
    }
)
```

### Hooks

Python functions that fire at specific points in the agent loop:

```python
@client.hook("before_tool_call")
def log_tool_use(tool_name, tool_input):
    """Log every tool call for observability."""
    logger.info(f"Agent calling: {tool_name}({tool_input})")

@client.hook("after_response")
def check_cost(response):
    """Alert if spending too much."""
    if total_cost > budget:
        raise BudgetExceeded()
```

Use hooks for: logging, cost control, safety guardrails, custom validation.

### Conversations

The SDK supports interactive, multi-turn conversations:

```python
client = ClaudeSDKClient()

# Start a conversation
response = client.send("Analyze the sales data in data/sales.csv")

# Continue the conversation (history is managed for you)
response = client.send("Now create a chart of the top 10 products")

# The agent remembers the previous context
```

### When to Use What

| Scenario | Use |
|----------|-----|
| Single question → single answer | [[anthropic-claude-api\|Messages API]] |
| Multi-step task with tools | **Agent SDK** |
| Coding tasks in your terminal | [[claude-code]] |
| Custom agent for your product | **Agent SDK** |
| Quick prototyping | [[claude-code]] or Messages API |

## Code Example

```python
from claude_agent_sdk import ClaudeSDKClient
import json

# Create client (Claude Code CLI is bundled)
client = ClaudeSDKClient()

# Simple task — agent handles the loop
response = client.send(
    "Read all Python files in src/ and create a summary of each function"
)
print(response.text)

# With custom tools
@client.tool("get_weather")
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    # Your API call here
    return json.dumps({"city": city, "temp": 22, "condition": "cloudy"})

response = client.send("What's the weather in Bogotá and Medellín?")
# Agent will call get_weather twice, then summarize
```

## Connections

- Built on [[anthropic-claude-api]] — the SDK wraps the Messages API
- Shares tools with [[claude-code]] — same Read/Write/Edit/Bash/Glob/Grep
- Uses [[model-context-protocol]] for external tool connections
- Implements [[Agent Patterns]] (ReAct loop) internally
- Hooks enable [[Observability]] and cost control
- Can be used to build [[Multi-Agent Systems]]

## Sources

- [Claude Agent SDK on GitHub](https://github.com/anthropics/claude-agent-sdk-python)
- [Agent SDK on PyPI](https://pypi.org/project/claude-agent-sdk/)
- [Building Agents with Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [Complete Guide to Building Agents](https://nader.substack.com/p/the-complete-guide-to-building-agents)
- [DataCamp Agent SDK Tutorial](https://www.datacamp.com/tutorial/how-to-use-claude-agent-sdk)
