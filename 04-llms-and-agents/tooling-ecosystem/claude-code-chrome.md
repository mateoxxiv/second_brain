---
tags:
  - status/seed
  - llms
related:
  - "[[claude-code]]"
  - "[[claude-code-cron-jobs]]"
domain: llms
sources:
  - "https://docs.anthropic.com/en/docs/claude-code"
---

> **TL;DR** — Claude in Chrome is a browser automation MCP that lets Claude interact with live web pages in your Chrome session — clicking, filling forms, reading console logs, capturing screenshots, and recording GIFs.

---

## Intuition

Claude in Chrome bridges Claude Code and your browser: instead of describing a page to Claude, Claude *sees and acts on it directly*. It connects via a Chrome extension that exposes a set of MCP tools to the agent.

Mental model: Claude has a mouse and keyboard pointed at your Chrome window.

## Mechanics

**Setup:** install the Claude in Chrome extension; grant site-level permissions for the domains you want Claude to access.

**Invoke:** always start a browser task with the `claude-in-chrome` skill — it loads the MCP tool schemas into the session before any `mcp__claude-in-chrome__*` calls.

**Core tools:**

| Tool | What it does |
|------|-------------|
| `tabs_context_mcp` | List current open tabs — **always call first** |
| `tabs_create_mcp` | Open a new tab |
| `navigate` | Go to a URL |
| `read_page` | Read the visible page content as text |
| `computer` | Screenshot / click / type |
| `form_input` | Fill form fields |
| `read_console_messages` | Read browser console output |
| `read_network_requests` | Inspect network traffic |
| `gif_creator` | Record a multi-step interaction as a GIF |
| `javascript_tool` | Execute JS in the page context |

**Workflow pattern:**
1. Call `tabs_context_mcp` to see what is open
2. Create a fresh tab with `tabs_create_mcp` (never reuse tab IDs from previous sessions)
3. Navigate → interact → read / screenshot
4. Never trigger `alert()`, `confirm()`, or `prompt()` — they block all further browser events

**Loading tools:** load all expected tools in a single ToolSearch call (one round-trip):
```
select:mcp__claude-in-chrome__tabs_context_mcp,
       mcp__claude-in-chrome__navigate,
       mcp__claude-in-chrome__computer,
       mcp__claude-in-chrome__read_page,
       mcp__claude-in-chrome__tabs_create_mcp
```
Add `gif_creator`, `form_input`, `read_console_messages` to the same call when the task needs them.

## Use Cases

**Research automation** — navigate to a paper or blog, extract structured content, save it as a literature note directly in the vault.

**UI testing** — verify a locally running app renders correctly; check console errors; take before/after screenshots of a change.

**Form automation** — fill repetitive web forms, log into dashboards, extract data from pages that require authentication.

**GIF demos** — record a full multi-step interaction as a GIF for documentation or sharing. Capture extra frames before and after each action for smooth playback.

## Exercises

**Basic** — Open a new tab, navigate to `https://example.com`, and take a screenshot with `computer`.

**Intermediate** — Read the console messages from a locally running dev server while triggering a specific user action. Filter by a pattern to isolate relevant logs.

**Advanced** — Record a full login flow as a GIF using `gif_creator`. Combine with `read_network_requests` to capture the auth token being sent. Save the GIF path and token to a project note.
