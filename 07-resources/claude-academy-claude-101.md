---
tags:
  - status/seed
  - literature
  - llms
type: course
domain: llms
sources:
  - "https://academy.claude.com/es/courses/claude-101"
author: "Anthropic — Claude Academy"
date_read: "2026-09-06 (in progress)"
---

## Summary

*Claude 101* (Claude Academy) is Anthropic's official **beginner, product-usage** course: 13 short lessons (~2.5 h) + a quiz/badge that teach how to actually *use* Claude for everyday work — from a first conversation and effective prompting, through the desktop app's three work modes, to organizing context with Projects, Artifacts, and Skills, and extending reach with Connectors, Enterprise Search, and Research.

> **Role in the vault — read before deriving notes.** This is a **product/how-to course, not a source of ML theory.** It teaches *the Claude product surface* (which app, which button, which feature), deliberately containing no model internals, math, or "how the LLM works." So it originates **no ML concept notes**. Its legitimate output is a thin layer of **product-reference notes** in `04-llms-and-agents/` (tooling-ecosystem, prompt-engineering, integration-patterns) — the practical "how to drive Claude" companion to the conceptual LLM/agent notes. For *why* LLMs behave as they do, stay with papers and the theory track; use this only to work the tools fluently.

---

## Chapter / Class Map

| Module | Lesson | Topic | Vault notes |
|--------|--------|-------|-------------|
| Meet Claude | 1 | What is Claude? | *(product overview)* |
| | 2 | Your first conversation with Claude | *(product)* |
| | 3 | Getting better results (prompting, AI Fluency) | [[prompt-engineering-fundamentals]], [[ai-fluency-framework]] |
| | 4 | How you'll work with Claude on desktop (Chat / Cowork / Code) | [[claude-work-modes]], [[claude-code]] |
| Organizing work & knowledge | 5 | Introduction to Projects | [[claude-projects]] |
| | 6 | Creating with Artifacts | [[claude-artifacts]] |
| | 7 | Working with Skills | [[claude-skills]] |
| Expanding Claude's reach | 8 | Connecting your tools (Connectors) | [[model-context-protocol]], [[claude-connectors]] |
| | 9 | Enterprise Search | [[claude-connectors]] |
| | 10 | Research for deep dives | [[claude-research-mode]] |
| Putting it together | 11 | Claude in action: use-cases by role | *(applications)* |
| | 12 | Other ways to work with Claude | [[anthropic-claude-api]], [[claude-agent-sdk]] |
| | 13 | What's next? | *(next steps)* |

---

## All Topics at a Glance

**Meet Claude (1–4)**
- Product intro — what Claude is; access via web, desktop, mobile
- [[prompt-engineering-fundamentals]] — *(gap)* the context → task → format/style prompt structure, and iterating when results miss
- [[ai-fluency-framework]] — *(gap)* Anthropic's framework for getting better outcomes from an AI collaborator
- [[claude-work-modes]] — *(gap)* the three shapes of work in the desktop app: **Chat** (turn-by-turn), **Cowork** (hand work off), **Code** (build software), and picking the right one
- [[claude-code]] — *(exists)* the Code mode / CLI agent

**Organizing work & knowledge (5–7)**
- [[claude-projects]] — *(gap)* reusable context containers for related conversations
- [[claude-artifacts]] — *(gap)* generated documents/apps rendered beside chat and iterated in place
- [[claude-skills]] — *(gap)* packaged reusable instructions/workflows Claude can invoke

**Expanding Claude's reach (8–10)**
- [[model-context-protocol]] — *(exists)* the open protocol underneath Connectors
- [[claude-connectors]] — *(gap)* connecting external tools + Enterprise Search over org data
- [[claude-research-mode]] — *(gap)* multi-step research/deep-dive capability

**Putting it together (11–13)**
- Role-based use cases; other interfaces ([[anthropic-claude-api]], [[claude-agent-sdk]]); next steps

---

## Key Takeaways

1. **It's a product-fluency course, not an ML course** — the value is knowing *which feature fits which task*, not how the model works.
2. **The three work modes are the mental model** — Chat / Cowork / Code map to turn-by-turn help, delegated work, and software building; picking the right mode is the core skill.
3. **Prompting = context + task + format** — set the stage with context, define the action, specify format/style rules; then iterate when the result misses.
4. **Projects / Artifacts / Skills are the "reusable context" trio** — they persist and package context so you don't re-explain yourself each conversation.
5. **Connectors (built on MCP) + Enterprise Search + Research extend reach** — from a closed chat to acting over your real tools and data.

## Quotes / Important Passages

> *(Course in progress — quotes/timestamps to be added as lessons are watched.)*

## My Thoughts

Directly useful because I'm building on the Claude platform, but I'll keep it in its lane: it's the **operator's manual**, not the engineering text. The highest-leverage extractions are the product-reference gaps that fill my empty `prompt-engineering/` folder — [[prompt-engineering-fundamentals]] and [[ai-fluency-framework]] — plus a [[claude-work-modes]] note that finally distinguishes Chat/Cowork/Code cleanly (I already have [[claude-code]] but nothing on the other two). Projects/Artifacts/Skills deserve one compact note each since I use them. For the conceptual "why," the pairing is: this course for the *how*, and the [[claude-agent-sdk]] / [[model-context-protocol]] notes + Anthropic's docs for the *mechanism*. Next best step after this: **Claude Code 101** and **Claude Platform 101** (sibling Academy courses) map far more directly onto my build track.

---

## Permanent Notes Created

- *(None yet — product-reference notes below to be written as lessons are worked through.)*

## Gaps — Notes Still to Create

- [[prompt-engineering-fundamentals]] — Lesson 3: the context/task/format prompt structure and iteration loop; fills the empty `prompt-engineering/` folder
- [[ai-fluency-framework]] — Lesson 3: Anthropic's AI-collaboration framework
- [[claude-work-modes]] — Lesson 4: Chat vs. Cowork vs. Code and when each applies
- [[claude-projects]] — Lesson 5: reusable context containers
- [[claude-artifacts]] — Lesson 6: generated, iterable documents/apps
- [[claude-skills]] — Lesson 7: packaged reusable workflows
- [[claude-connectors]] — Lessons 8–9: Connectors + Enterprise Search (relate to [[model-context-protocol]])
- [[claude-research-mode]] — Lesson 10: multi-step research capability
