---
tags:
  - status/seed
  - llms
related:
  - "[[anthropic-claude-api]]"
  - "[[claude-agent-sdk]]"
  - "[[model-context-protocol]]"
domain: llms
sources:
  - "https://code.claude.com/docs"
  - "https://github.com/anthropics/claude-code"
  - "https://code.claude.com/docs/en/hooks"
  - "https://code.claude.com/docs/en/sub-agents"
---

> **TL;DR** — Claude Code is an autonomous coding agent that lives in your terminal. It plans, reads files, writes code, runs tests, and iterates — not a chatbot that suggests code, an agent that executes.

---

## Intuition

Claude Code follows a think → act → observe loop. Give it a task like "add error handling to the API endpoint", and it reads the file, understands the code, makes the edit, runs tests to verify, and reports back — without you specifying each step.

What makes it powerful is composability: subagents for parallelism, worktrees for isolation, hooks for automation, MCP for external tools, custom slash commands for domain-specific workflows.

## Mechanics

**Built-in tools:** Read, Write, Edit, Bash, Glob, Grep, Agent (spawn subagents), WebFetch, WebSearch.

**Key slash commands:** /init (generate CLAUDE.md), /compact (compress context), /review (code review git changes), /cost (token usage), /rewind (undo last action).

**Permission modes:**
- `--permission-mode ask` — asks before every action (safest)
- `--permission-mode auto-edit` — read/edit without asking, Bash still asks
- `--permission-mode full-auto` — everything without asking

**Trusted directories** — by default Claude Code only operates in the current working directory. Add extra directories permanently in `~/.claude/settings.json`:
```json
{
  "permissions": {
    "additionalDirectories": ["C:\\Users\\mquiceno\\mateo\\second_brain"]
  }
}
```
Or per-session only with the `--add-dir /path/to/dir` CLI flag.

**Hooks system** — deterministic execution at 14 lifecycle events (PreToolUse, PostToolUse, Stop, SubagentStop, WorktreeCreate...):
```json
{
  "hooks": {
    "PostToolUse": [{"matcher": "Edit", "command": "black $FILE_PATH"}]
  }
}
```
PreToolUse can return `approve`, `deny`, or `modify` — enabling guardrails.

```bash
npm install -g @anthropic-ai/claude-code

claude "add type hints to all functions in utils.py"

# Headless mode for CI/scripts
claude -p "explain the architecture" --output-format json

# Start in a git worktree (isolated branch)
claude -w "implement feature X"
```

> Runnable: [[code/llms/claude_code_examples.sh]]

## In ML

**Subagents for parallel work.** Each subagent gets its own context window (no pollution to main), can run in parallel, and has restricted tools. Three subagents refactoring login/signup/tests simultaneously is faster than sequential execution.

**Hooks for guaranteed automation.** Unlike prompting (probabilistic), hooks guarantee execution. Use PostToolUse to auto-format code, run linters, log actions. Use PreToolUse to block dangerous commands or enforce standards.

**MCP integration for tool access.** 300+ MCP servers available. Connect Claude Code to your database, Slack, GitHub, or any custom service. The agent can query real data and take real actions.

## Exercises

**Basic** — Install Claude Code and run your first session. Use /init to generate a CLAUDE.md for a project, then ask it to explain the codebase architecture.

**Intermediate** — Create a custom slash command in `.claude/commands/` that automates a workflow (e.g., "run tests and create a PR summary"). Test it.

**Advanced** — Write a PreToolUse hook that blocks all Bash commands containing `rm -rf`. Verify it works by trying the command. Then extend it to log all Bash commands to a file.
