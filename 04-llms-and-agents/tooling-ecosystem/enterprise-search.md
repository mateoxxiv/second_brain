---
tags:
  - status/seed
  - llms
related:
  - "[[model-context-protocol]]"
  - "[[claude-projects]]"
  - "[[claude-context-layers]]"
  - "[[claude-skills]]"
  - "[[claude-academy-claude-101]]"
domain: llms
sources:
  - "https://academy.claude.com/es/courses/claude-101"
---

> **TL;DR** — Enterprise Search answers questions across your organization's connected tools, and it only shows what each asking user could already open in those tools.

---

## Intuition

Your company's knowledge is spread across a shared drive, a chat tool, an inbox, and a document system. Searching each one by hand is slow, and you often miss what you cannot see. Enterprise Search is a single desk that asks every filing cabinet at once and returns one summary with sources. The important rule is that it opens only the drawers you already had a key to.

The question it answers is "what does our organization know about X?" It matters because the answer comes from across tools, not from one document you already chose.

## Mechanics

Enterprise Search is a preconfigured project, scoped to the whole organization and built on [[claude-projects]]-style shared context. Setup has two layers:

| Layer | Who sets it up | What happens |
|-------|----------------|--------------|
| Organization | Owner | Enables the project, picks a document connector (Google Drive or SharePoint) and a chat connector (Slack or Teams), optionally email, and names the project |
| Individual | Each user | Opens the project, signs in to each service with a personal account |
| Permissions | Source tool | Results include only what that user can already open there |

Every answer cites its sources, so you can check the original context. Connectors are the MCP-based links described in [[model-context-protocol]].

```python
# Conceptual only: the lesson does not describe the implementation
def enterprise_answer(question, sources, user):
    hits = [h for s in sources for h in s.search(question)]
    visible = [h for h in hits if user in h.readers]  # reader list from the source tool
    return synthesize(question, visible)              # each claim cites its hit
```

## In ML

**Retrieval across sources** — This is the retrieval pattern from [[claude-projects]], applied across several systems at once. The quality of the answer depends on which sources are connected, so the more connectors, the more complete the results.

**Permissions as a filter** — The lesson's key claim is that access control stays in the source tool. This is a security property, not a model property: the model should never see documents the user cannot open. Verify this for any sensitive dataset before you rely on it.

**Shared context as a team tool** — Like a shared project, Enterprise Search is one configuration for everyone. Its quality depends on the owner's setup choices, which is the same governance point made in [[claude-projects]].

## Exercises

**Basic** — Which is better suited to Enterprise Search, and which to a single document or project? (a) "What is our remote-work policy?", (b) "Summarize this week's discussion about the Q4 roadmap across Slack and Drive", (c) "How many words is my draft?"

**Intermediate** — A colleague without access to a private Slack channel asks about a decision made there. What should they get back, and where in the system is that enforced? Explain why the check belongs in the source tool and not only in the search layer.

**Advanced** — The lesson says connected data is not indexed or stored separately. What would you need to verify before trusting this for regulated data, and what question would you ask about a document that was just deleted from the source?

## Gaps: notes still to create

- A connectors note covering Lessons 8 and 9 together, since connectors are the shared mechanism.
- A note on the organization setup steps, if they change enough to need their own reference.
