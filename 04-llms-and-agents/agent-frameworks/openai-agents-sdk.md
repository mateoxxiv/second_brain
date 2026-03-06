**Related**: [[openai-api]], [[openai-codex]], [[claude-agent-sdk]], [[Agent Patterns]]
**Tags**: #status/seed

## Core Idea

The OpenAI Agents SDK is a lightweight Python framework for building multi-agent
workflows. If [[openai-codex]] is OpenAI's agent for coding, the Agents SDK is
the toolkit for building agents that do **anything** — same idea as the
[[claude-agent-sdk]], but with a different design philosophy.

**Key difference**: The Claude Agent SDK wraps Claude Code's CLI and manages
the agent loop for you. The OpenAI Agents SDK is more of a **framework** —
it gives you primitives (agents, tools, handoffs, guardrails) and you compose
them using plain Python. It's lighter and more flexible, but you do more wiring.

## Details

### Core Primitives

The SDK is built around four concepts:

```
┌─────────────────────────────────────────────┐
│              Your Application               │
├─────────────────────────────────────────────┤
│           OpenAI Agents SDK                 │
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌───────────┐ │
│  │  Agents  │  │  Tools   │  │ Guardrails│ │
│  │          │  │          │  │           │ │
│  │ LLM +    │  │ Function │  │ Input &   │ │
│  │ instruct │  │ Hosted   │  │ output    │ │
│  │ + tools  │  │ Agent-as │  │ validation│ │
│  └────┬─────┘  └──────────┘  └───────────┘ │
│       │                                     │
│  ┌────┴─────┐  ┌──────────┐  ┌───────────┐ │
│  │ Handoffs │  │ Sessions │  │  Tracing  │ │
│  │          │  │          │  │           │ │
│  │ Delegate │  │ Persist  │  │ Debug &   │ │
│  │ to other │  │ memory   │  │ monitor   │ │
│  │ agents   │  │ context  │  │ workflows │ │
│  └──────────┘  └──────────┘  └───────────┘ │
├─────────────────────────────────────────────┤
│              OpenAI API                     │
└─────────────────────────────────────────────┘
```

### 1. Agents

An agent = LLM + instructions + tools + optional behavior:

```python
from openai_agents import Agent

agent = Agent(
    name="research_assistant",
    instructions="You are a research assistant. Search the web and summarize findings.",
    model="gpt-5-mini",
    tools=[web_search, file_reader],
)
```

### 2. Tools (Three Kinds)

| Kind | What it is | Example |
|------|-----------|---------|
| **Function tools** | Python functions with type hints, auto-converted to tool schemas | `def search_db(query: str) -> str` |
| **Hosted tools** | OpenAI's built-in tools (Responses API) | Web search, code interpreter, file search |
| **Agent-as-tool** | Use another agent as a tool | Research agent called by main agent |

```python
from openai_agents import function_tool

@function_tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return call_weather_api(city)
```

### 3. Handoffs

Transfer the **entire conversation** to another agent. Unlike agent-as-tool
(where the parent stays in control), a handoff gives full control to the
target agent:

```python
from openai_agents import Agent, handoff

billing_agent = Agent(name="billing", instructions="Handle billing questions.")
tech_agent = Agent(name="tech", instructions="Handle technical questions.")

triage_agent = Agent(
    name="triage",
    instructions="Route the user to the right agent.",
    handoffs=[handoff(billing_agent), handoff(tech_agent)],
)
```

**Use case**: Customer support — triage routes to billing, tech, or sales
agents. Each agent specializes in its domain.

### 4. Guardrails

Validation functions that run **in parallel** with agent execution. Fail fast
when checks don't pass:

```python
from openai_agents import input_guardrail, GuardrailResult

@input_guardrail
def block_profanity(input_text: str) -> GuardrailResult:
    if contains_profanity(input_text):
        return GuardrailResult(blocked=True, reason="Profanity detected")
    return GuardrailResult(blocked=False)
```

Two types:
- **Input guardrails**: Block or modify requests before they reach the model
- **Output guardrails**: Validate or reject agent responses after generation

### 5. Sessions (Memory)

Persistent working memory within an agent loop:

```python
session = Session(agent=my_agent)
response = session.run("Analyze the Q4 report")
# Later, in the same session:
response = session.run("Now compare with Q3")
# Agent remembers the Q4 context
```

### 6. Tracing

Built-in observability for debugging and monitoring:
- Visualize agent execution flow
- See which tools were called and when
- Track token usage and costs
- Export traces for evaluation and fine-tuning

### OpenAI Agents SDK vs Claude Agent SDK

| Feature | OpenAI Agents SDK | Claude Agent SDK |
|---------|------------------|-----------------|
| Philosophy | Framework (you compose primitives) | Wrapper (SDK manages the loop) |
| Language | Python-first | Python |
| Multi-agent | Handoffs + agent-as-tool | Subagents + teams |
| Guardrails | Built-in (input + output) | Hooks (pre/post tool use) |
| Memory | Sessions | CLAUDE.md + auto-memory |
| Tracing | Built-in | Hooks for logging |
| Built-in tools | Web search, code interpreter, file search | Read, Write, Edit, Bash, Glob, Grep |
| Hosted tools | Yes (Responses API) | Via MCP servers |
| Voice agents | Realtime API support | No |
| Complexity | Lightweight, more assembly | More batteries-included |

### When to Use What

| Scenario | Use |
|----------|-----|
| Single question → single answer | [[openai-api\|Chat Completions / Responses API]] |
| Multi-agent with handoffs | **Agents SDK** |
| Coding tasks in terminal | [[openai-codex]] |
| Custom agent for your product | **Agents SDK** |
| Voice agent | **Agents SDK** (Realtime API) |

## Code Example

```python
from openai_agents import Agent, Runner, function_tool, handoff

# Define tools
@function_tool
def search_database(query: str, limit: int = 10) -> str:
    """Search the product database."""
    results = db.search(query, limit=limit)
    return str(results)

# Define specialized agents
researcher = Agent(
    name="researcher",
    instructions="Search for information and summarize findings.",
    tools=[search_database],
    model="gpt-5-mini",
)

writer = Agent(
    name="writer",
    instructions="Write clear, concise reports based on research.",
    model="gpt-5-mini",
)

# Orchestrator with handoffs
orchestrator = Agent(
    name="orchestrator",
    instructions="Route tasks: research goes to researcher, writing goes to writer.",
    handoffs=[handoff(researcher), handoff(writer)],
)

# Run
result = Runner.run_sync(orchestrator, "Research our top 5 products and write a summary")
print(result.final_output)
```

## Connections

- Built on the [[openai-api]] — uses Chat Completions or Responses API
- Works with [[openai-codex]] for coding-specific agents
- Compare with [[claude-agent-sdk]] — different design philosophy, same goal
- Implements [[Agent Patterns]] (ReAct, handoff patterns)
- Guardrails relate to safety and [[Prompt Design Patterns]]
- Handoffs enable [[Multi-Agent Systems]] with clear delegation
- Tracing connects to [[Observability]] concepts

## Sources

- [OpenAI Agents SDK Documentation](https://openai.github.io/openai-agents-python/)
- [Agents SDK on GitHub](https://github.com/openai/openai-agents-python)
- [Agents SDK on PyPI](https://pypi.org/project/openai-agents/)
- [Guardrails Reference](https://openai.github.io/openai-agents-python/guardrails/)
- [Handoffs Reference](https://openai.github.io/openai-agents-python/handoffs/)
- [OpenAI Agents SDK Review (Agentlas)](https://agentlas.pro/frameworks/openai-agents-sdk/)
