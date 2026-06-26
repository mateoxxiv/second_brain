---
tags:
  - status/seed
  - llms
related:
  - "[[claude-code]]"
  - "[[claude-code-cron-jobs]]"
  - "[[claude-code-chrome]]"
domain: llms
sources:
  - "https://docs.anthropic.com/en/docs/claude-code/hooks"
---

> **TL;DR** — Hooks are shell commands (or LLM prompts/agents) that fire at deterministic lifecycle events in Claude Code; unlike instructions, they cannot be forgotten or skipped.

---

## Intuition

You can tell Claude "always run prettier after editing files" — and it might comply, or forget. A PostToolUse hook on `Write|Edit` runs the formatter *every single time*, unconditionally. That is the core value: **instructions are probabilistic; hooks are deterministic**.

Hooks live in `settings.json`, not in the conversation. Claude never decides whether to run them.

## Mechanics

**Configuration** — add a `hooks` block to `~/.claude/settings.json` (global) or `.claude/settings.json` (project):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "your-command", "timeout": 30 }]
      }
    ]
  }
}
```

**Key events:**

| Event | When | Can block? |
|-------|------|-----------|
| `PreToolUse` | Before tool runs | Yes — return `continue: false` |
| `PostToolUse` | After tool succeeds | No |
| `Stop` | When Claude finishes a turn | Yes |
| `SessionStart` | At session startup | No |
| `PreCompact` | Before context compression | No |
| `UserPromptSubmit` | When user submits | Yes |

**Hook types:** `command` (shell), `prompt` (LLM check), `agent` (full agent with tools).

**stdin protocol** — every hook receives JSON on stdin:
```json
{ "tool_name": "Write", "tool_input": { "file_path": "/path/file.md" } }
```
Extract with `jq -r '.tool_input.file_path'`.

**stdout protocol** — return JSON to influence behavior:
```json
{ "continue": false, "stopReason": "Blocked: reason", "systemMessage": "Shown to user" }
```

**Common patterns:**

```bash
# Auto-format after writes
jq -r '.tool_input.file_path' | { read -r f; prettier --write "$f"; } 2>/dev/null || true

# Log all Bash commands
jq -r '.tool_input.command' >> ~/.claude/bash-log.txt

# Block rm -rf
jq -r '.tool_input.command' | grep -q 'rm -rf' \
  && echo '{"continue":false,"stopReason":"Blocked rm -rf"}' || true
```

## Use Cases

**Vault automation** — PostToolUse on `Write|Edit`: auto-commit every note the moment Claude writes it. The hook reads the file path from stdin and runs `git add "$f" && git commit -m "auto: save $f"`.

**Guardrails** — PreToolUse on `Bash`: intercept dangerous shell patterns before they execute. Log every command to an audit file for review.

**Session logging** — Stop hook: append a summary line to `00-inbox/daily-log.md` whenever Claude finishes a turn, creating a passive record of every study session.

## Exercises

**Basic** — Add a PostToolUse hook on `Write|Edit` that appends `<timestamp> <file_path>` to `~/.claude/edit-log.txt`. Trigger it by editing any file and verify the log was updated.

**Intermediate** — Write a PreToolUse hook on `Bash` that blocks any command containing `git push --force` and returns a JSON `stopReason`. Test it safely by running the blocked command.

**Advanced** — Create a Stop hook that writes the session's last assistant message (extracted from the stdin JSON) to `00-inbox/last-session.md`. What happens if the JSON has no assistant message? Handle that edge case.
