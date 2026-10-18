---
tags:
  - status/seed
  - llms
related:
  - "[[claude-code]]"
  - "[[claude-code-cron-jobs]]"
  - "[[claude-code-chrome]]"
  - "[[claude-agent-sdk]]"
  - "[[claude-code-agent-teams]]"
  - "[[claude-context-layers]]"
domain: llms
sources:
  - "https://academy.claude.com/es/courses/claude-101"
---

> **TL;DR** — Work with Claude comes in three shapes: turn-by-turn conversation, delegated tasks that run to a finished result, and building software in a codebase. The skill is recognizing which shape a task needs before you start.

---

## Intuition

Think of three different relationships with a capable colleague:

- **Pair thinking.** You ask, they answer, you steer. Each reply changes your next question. Good for brainstorming, rewriting, and "what does this dashboard mean?"
- **Delegation.** You hand over the whole job ("pull these six sources into a report, save it in the project folder"). You review the plan and the result, not every intermediate step.
- **Pairing at the keyboard.** The colleague works directly in your repo: reads files, edits code, runs tests. Built for developers.

The mistake to avoid is treating a delegable task as a chat: asking one question at a time about a multi-step job, when you could describe the finished result once.

## Mechanics

| Mode | Core loop | Output | Desktop surface (per the lesson) |
|------|-----------|--------|----------------------------------|
| Turn-by-turn | Human ↔ model exchange | The conversation itself | Chat (quick access, screenshots, dictation) |
| Delegated | Plan → execute steps → return result | Finished files or artifacts | Cowork (folder access, scheduled tasks, subagents, plugins) |
| Software | Read code → edit → run → verify | Changes in a repo, git history | Code tab (Local or Cloud) |

**Decision rule:** if the answer changes what you ask next, use turn-by-turn. If the task has several steps you would normally do in sequence and ends in a file, use delegation. If it touches a codebase, use Code.

**Autonomy controls in Code:** approve each change manually, accept edits automatically, or plan before changing anything.

*Caveat:* the course notes that Cowork is being folded into plain "Claude", so the surface names may change. The three shapes are the durable part.

---

## In ML / AI systems

The three modes are product-level versions of patterns that matter in agent design. Delegation is the agent loop from [[claude-agent-sdk]] (plan, act, observe, return). The Code mode is [[claude-code]] itself. Turn-by-turn is plain prompting, where all state lives in the context window ([[claude-context-layers]]).

**Connection 1 — Scheduling and parallelism.** Scheduled tasks ([[claude-code-cron-jobs]]) and subagents ([[claude-code-agent-teams]]) are delegation taken further: work runs without a human in each step.

**Connection 2 — Permission boundaries.** Each mode has a different trust surface: chat reads what you paste, delegation can read and write folders, Code can run commands. Matching the mode to the task is also a least-privilege decision.

---

## Exercises

**Basic** — For each task, name the mode: (a) explain a chart in a screenshot, (b) produce a weekly status PDF from three tools, (c) fix a failing test in a repo. Why does each fit its mode?

**Intermediate** — You have a 50-document contract folder and need a memo of the recurring risks. Which mode, and what would you put in the initial brief so you can review the plan instead of supervising every step?

**Advanced** — Turn-by-turn gives you more control per step but costs your attention; delegation saves attention but risks a wrong plan running for a long time. Where is the break-even? What signals would tell you to stop a delegated task early?

*Hint if stuck:* ask yourself how many decisions you would need to make in the middle of the job. Many decisions mid-task means turn-by-turn.
