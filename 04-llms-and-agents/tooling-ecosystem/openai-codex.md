---
tags:
  - status/seed
  - llms
related:
  - "[[openai-api]]"
  - "[[openai-agents-sdk]]"
  - "[[claude-code]]"
domain: llms
sources:
  - "https://openai.com/index/introducing-codex/"
  - "https://openai.com/codex/"
  - "https://github.com/openai/codex"
  - "https://openai.com/index/introducing-gpt-5-3-codex/"
---

> **TL;DR** — OpenAI's agentic coding tool. Cloud sandboxes (primary) run tasks in parallel isolated containers with no internet. Local CLI is interactive like Claude Code. Model: GPT-5.3-Codex.

---

## Intuition

Codex is [[claude-code]]'s counterpart in the OpenAI ecosystem. The key architectural difference: Codex runs tasks in cloud sandboxes — isolated containers preloaded with your repo where multiple agents work in parallel, with no internet during execution. Claude Code runs locally.

This tradeoff: Codex is safer (no network = can't exfiltrate code, can't make unexpected external calls) and inherently parallel. Claude Code has full local access and a richer extensibility system (hooks, custom commands, MCP).

## Mechanics

**Two execution modes:**

| Mode | Where it runs | Best for |
|------|--------------|---------|
| Cloud sandboxes | OpenAI servers, no internet | Parallel async tasks, PRs |
| Local CLI | Your machine, full access | Interactive, exploration |

**Cloud mode workflow:** launch task → isolated container loads your repo → agent works → proposes PR for review. You never touch the intermediate state.

**Model:** GPT-5.3-Codex — purpose-built for agentic coding, 25% faster than GPT-5.2.

**Codex vs Claude Code:**

| Feature | Codex | Claude Code |
|---------|-------|-------------|
| Execution | Cloud sandboxes | Local terminal |
| Network during task | Disabled | Full access |
| Multi-agent | Built-in parallel | Agent Teams (experimental) |
| Output style | Proposes PRs | Direct file edits |
| Extensibility | Via Agents SDK | Hooks, skills, MCP |

```bash
npm install -g @openai/codex

# Interactive local mode
codex

# Single command
codex "add error handling to the payment endpoint"

# Cloud mode: proposes a PR for review
codex --cloud "refactor auth module"
```

> Runnable: [[code/llms/codex_examples.sh]]

## In ML

**Security-first architecture.** No internet in cloud sandboxes means the agent cannot exfiltrate your source code, call external APIs, or introduce supply chain risks during execution. For security-sensitive codebases, this is a meaningful difference from Claude Code's full network access.

**PR-first review workflow.** Codex always proposes changes as PRs rather than editing files directly. This forces a human review step and creates a clear audit trail. Better for team workflows, slightly more friction for solo exploration.

**Programmatic use via Agents SDK.** Codex integrates with [[openai-agents-sdk]] for building coding agents in Python applications. You can create agents that use Codex as a tool within larger workflows.

## Exercises

**Basic** — Describe the cloud sandbox security model. What can Codex access during task execution? What can it not access?

**Intermediate** — Compare the PR-first workflow (Codex) vs direct file editing (Claude Code) for a team scenario. What are the tradeoffs in speed, safety, and auditability?

**Advanced** — Design a hybrid agent system using Codex for parallel background tasks and Claude Code for interactive exploration. How would they hand off work to each other?
