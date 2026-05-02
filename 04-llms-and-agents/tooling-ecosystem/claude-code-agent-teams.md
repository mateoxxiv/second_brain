---
tags:
  - status/seed
  - llms
related:
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[model-context-protocol]]"
domain: llms
sources:
  - "https://code.claude.com/docs/en/agent-teams"
  - "https://claudefa.st/blog/guide/agents/agent-teams"
  - "https://alexop.dev/posts/from-tasks-to-swarms-agent-teams-in-claude-code/"
  - "https://claudefa.st/blog/guide/agents/agent-teams-use-cases"
---

> **TL;DR** — Agent Teams let multiple Claude Code instances work together as peers: shared task list with dependency tracking, peer-to-peer mailbox, and worktree isolation. Experimental, requires Opus 4.6.

---

## Intuition

Subagents report back to a single parent. Agent Teams are peers — they communicate directly with each other, share a task list, and coordinate dependencies automatically. Think of it as going from one developer to a coordinated team.

A "backend" teammate finishes an API endpoint → the "tests" teammate automatically unblocks and starts writing tests. No orchestrator polling required.

## Mechanics

**Subagents vs Agent Teams:**

| Feature | Subagents | Agent Teams |
|---------|-----------|-------------|
| Communication | Parent only | Peer-to-peer via mailbox |
| Coordination | Parent assigns | Shared task list with dependencies |
| Task claiming | Assigned | File locking prevents race conditions |
| Scope | Single task | Complex multi-step projects |

**Setup:** enable via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in `~/.claude/settings.json`. Then describe your team conversationally inside a Claude Code session — no config file needed.

**Infrastructure stored at** `~/.claude/tasks/{team-name}/`: task JSONs + mailbox directory.

**Team prompt template:**
```
Create an agent team with 3 teammates:
1. "backend" - refactor API endpoints in src/api/
2. "frontend" - update React components to match
3. "tests" - write integration tests for both

Use worktrees. Coordinate dependencies through the task list.
```

```bash
# 1. Enable in ~/.claude/settings.json:
# {"env":{"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS":"1"}}

# 2. Start Claude Code
claude

# 3. Inside the session — describe your team conversationally

# 4. Navigate teammates: Shift+Down to cycle (in-process mode)
# 5. Message a teammate directly: @backend: use async/await
```

> Runnable: [[code/llms/agent_teams_setup.sh]]

## In ML

**Parallel investigation.** Spawn 4 teammates to investigate different hypotheses about a bug simultaneously. Have them share findings and debate theories via mailbox. One teammate might prove another wrong — this is valuable signal.

**Large-scale refactoring.** Each teammate owns a module (src/api/, src/ui/, tests/). They work in parallel worktrees, no file conflicts. Dependencies ensure the right order: API changes before UI updates before tests.

**Plan approval for safety.** For risky changes, require teammates to write a plan and get lead approval before executing. This adds a human checkpoint without breaking the parallel workflow.

## Exercises

**Basic** — Describe the difference between agent-as-tool and handoff in agent systems. How does this relate to the subagent vs Agent Teams distinction?

**Intermediate** — Design an Agent Team for a code review workflow. What teammates would you spawn? What would each focus on? How would you use the mailbox?

**Advanced** — Analyze when Agent Teams add overhead vs. value. For what task sizes/complexities does a single agent + subagents outperform a full team? What is the token cost multiplier?
