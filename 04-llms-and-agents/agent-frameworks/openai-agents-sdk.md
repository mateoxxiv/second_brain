---
tags:
  - status/seed
  - llms
related:
  - "[[openai-api]]"
  - "[[claude-agent-sdk]]"
  - "[[openai-codex]]"
domain: llms
sources:
  - "https://openai.github.io/openai-agents-python/"
  - "https://github.com/openai/openai-agents-python"
  - "https://pypi.org/project/openai-agents/"
  - "https://openai.github.io/openai-agents-python/guardrails/"
  - "https://openai.github.io/openai-agents-python/handoffs/"
---

> **TL;DR** — Lightweight Python framework for multi-agent workflows. Six primitives: agents, tools, handoffs, guardrails, sessions, tracing. You compose them; the SDK stays out of the way.

---

## Intuition

Where [[claude-agent-sdk]] wraps the agent loop so you don't see it, the OpenAI Agents SDK exposes explicit primitives you compose in Python. More assembly required, but more control. Better for teams that want to see exactly what happens at each step.

The defining feature is handoffs — transferring the entire conversation to a specialized agent. This enables clean multi-agent routing without a complex orchestration layer.

## Mechanics

**Six primitives:**

| Primitive | What it is |
|-----------|-----------|
| Agent | LLM + instructions + tools + optional handoffs |
| Function tool | Python function with type hints, auto-converted to schema |
| Hosted tool | OpenAI built-ins (web search, code interpreter, file search) |
| Agent-as-tool | Use another agent as a callable tool (parent stays in control) |
| Handoff | Transfer full conversation to another agent (parent gives up control) |
| Guardrail | Input/output validation running in parallel with execution |

**Agent-as-tool vs Handoff:** agent-as-tool = parent calls child and gets a result; handoff = parent delegates the whole conversation and steps back.

```python
from openai_agents import Agent, Runner, function_tool, handoff

@function_tool
def search_database(query: str) -> str:
    return str(db.search(query))

researcher = Agent(
    name="researcher",
    instructions="Search for information and summarize.",
    tools=[search_database],
    model="gpt-5-mini",
)

triage = Agent(
    name="triage",
    instructions="Route tasks to the right agent.",
    handoffs=[handoff(researcher)],
)

result = Runner.run_sync(triage, "Research our top 5 products")
print(result.final_output)
```

> Runnable: [[code/llms/openai_agents_sdk.py]]

## In ML

**Handoffs for multi-agent routing.** Customer support systems route billing questions to a billing agent, tech questions to a tech agent. The triage agent reads the message, picks the right expert, and hands off — the expert agent then has full context without the triage agent staying involved.

**Guardrails run in parallel.** Input guardrails check requests before they reach the model (block profanity, validate format). Output guardrails validate responses before returning them (check for PII, ensure compliance). Running in parallel means no latency overhead.

**Tracing for production observability.** Built-in tracing captures every tool call, handoff, and model invocation. Visualize execution flow, debug unexpected behavior, and export traces for fine-tuning datasets.

## Exercises

**Basic** — Explain the difference between handoff and agent-as-tool. In a customer support scenario, when would you use each?

**Intermediate** — When would you use guardrails vs hooks (in the context of [[claude-agent-sdk]])? Compare their execution models.

**Advanced** — Design a 3-agent system for a customer support workflow: triage, billing specialist, and technical specialist. Include appropriate guardrails and describe what each should do.
