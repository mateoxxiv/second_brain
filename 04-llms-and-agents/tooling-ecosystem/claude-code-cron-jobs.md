---
tags:
  - status/seed
  - llms
related:
  - "[[claude-code]]"
  - "[[claude-code-chrome]]"
domain: llms
sources:
  - "https://docs.anthropic.com/en/docs/claude-code"
---

> **TL;DR** — Claude Code cron jobs are scheduled cloud agents that run on a cron schedule automatically, even outside an active session; manage them with the `/schedule` skill or the CronCreate/CronList/CronDelete tools.

---

## Intuition

A cron job in Claude Code is a persistent scheduled routine: define a prompt and a schedule, and Claude runs it automatically at those times — even when you're not in a session. Think of it as a programmable assistant that wakes up on a timer.

Unlike hooks (which fire on tool events *within* a session), cron jobs are cloud-side and fully session-independent.

## Mechanics

**Managing cron jobs** — use the `/schedule` skill or the low-level tools directly:

| Action | Tool / Skill |
|--------|-------------|
| Create | `/schedule` skill or `CronCreate` tool |
| List all | `CronList` tool |
| Delete | `CronDelete` tool |

**Cron expression format** (standard 5-field):

```
*  *  *  *  *
│  │  │  │  └─ day of week (0-7, Sun=0 or 7)
│  │  │  └──── month (1-12)
│  │  └──────── day of month (1-31)
│  └──────────── hour (0-23)
└───────────────── minute (0-59)
```

**Common patterns:**

| Expression | Meaning |
|------------|---------|
| `0 9 * * 1-5` | 9 AM every weekday |
| `0 */6 * * *` | Every 6 hours |
| `30 23 * * *` | 11:30 PM daily |
| `0 0 * * 0` | Midnight every Sunday |

Each run starts a fresh agent session with the specified prompt and tools, then stops when the task completes.

## Use Cases

**Vault automation** — daily auto-commit of new notes, weekly summary of the Obsidian vault written to `00-inbox/`.

**Monitoring** — poll an API or scrape a page (combine with [[claude-code-chrome]]), alert on changes.

**Study routines** — schedule a daily quiz on a rotating topic, generate a spaced-repetition review card at 9 AM.

**News digest** — run `/news` every morning and append results to a literature note.

## Exercises

**Basic** — Create a cron job that fires every day at 9 AM with a simple "Good morning" prompt. Verify it appears in CronList.

**Intermediate** — Schedule a weekly agent (every Sunday at midnight) that runs `/status` on the vault and appends the output to `00-inbox/weekly-review.md`.

**Advanced** — Chain a cron job with a hook: the scheduled agent writes a file, and a PostToolUse hook in `settings.json` auto-commits the result to git.
