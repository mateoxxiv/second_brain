**Related**: [[anthropic-claude-api]], [[claude-agent-sdk]], [[model-context-protocol]], [[Agent Patterns]]
**Tags**: #status/seed

## Core Idea

Claude Code is an agentic command-line tool that gives Claude the ability to
**act on your computer** — read files, write code, run commands, search
codebases, and manage entire projects from the terminal. It's not a chatbot
that suggests code — it's an autonomous agent that plans, executes, and
iterates until the task is done.

What makes Claude Code powerful isn't just the individual features — it's how
they compose: subagents running in parallel worktrees, coordinating via agent
teams, triggered by hooks, connected to external services via MCP, with
persistent memory across sessions.

## Details

### How It Works

```
You: "Add error handling to the API endpoint in server.py"

Claude Code (agent loop):
  1. Think   → "I need to read the file first"
  2. Read    → reads server.py, understands the code
  3. Think   → "The endpoint needs try/except"
  4. Edit    → adds error handling
  5. Bash    → runs pytest to verify
  6. Think   → "All tests pass"
  7. Done    → shows you the diff
```

The agent loop repeats (think → act → observe) until the task is complete or
you intervene.

### Built-in Tools

| Tool | What it does |
|------|-------------|
| **Read** | Read any file in the working directory |
| **Write** | Create new files |
| **Edit** | Precise find-and-replace edits to existing files |
| **Bash** | Run terminal commands (git, pip, tests, scripts) |
| **Glob** | Find files by pattern (e.g., `**/*.py`) |
| **Grep** | Search file contents with regex |
| **Agent** | Spawn subagents for parallel tasks |
| **WebFetch** | Fetch content from URLs |
| **WebSearch** | Search the web |

### Built-in Slash Commands

| Command | What it does |
|---------|-------------|
| **/init** | Generate a CLAUDE.md for your project (conventions, build commands, patterns) |
| **/compact** | Compress conversation context — summarizes history while keeping key decisions |
| **/review** | Code review of recent git changes (correctness, security, performance, style) |
| **/cost** | Show token usage and cost for current session |
| **/memory** | Open the memory file editor |
| **/doctor** | Diagnose environment and configuration issues |
| **/model** | Switch between Claude models mid-session |
| **/clear** | Clear conversation history |
| **/help** | Show available commands |
| **/config** | View/edit configuration |
| **/login** | Authenticate |
| **/rewind** | Undo the last action |

### Permission Modes

Control how autonomous the agent is:

```
--permission-mode ask        → Asks before every action (safest)
--permission-mode auto-edit  → Read + Edit without asking, Bash still asks
--permission-mode full-auto  → Everything without asking (careful!)
```

You can also set per-tool permissions in settings — e.g., allow Read always
but ask for Bash.

### Custom Slash Commands (Skills)

Drop `.md` files in `.claude/commands/` and they become slash commands:

```
.claude/commands/
├── note.md       → /project:note
├── quiz.md       → /project:quiz
├── review.md     → /project:review
└── session.md    → /project:session
```

Claude auto-detects and invokes them when relevant. No code needed — just
plain markdown instructions. This vault uses custom commands for note creation,
quizzes, reviews, and study sessions.

**User commands** go in `~/.claude/commands/` and are available in all projects.

### Memory System

Three layers of persistent context:

```
1. CLAUDE.md (project root)
   Manual instructions: conventions, build commands, architecture.
   Loaded at the start of every conversation.

2. Auto-memory (~/.claude/projects/<project>/memory/)
   Claude auto-saves patterns across sessions:
   debug patterns, preferences, gotchas.
   Editable .md files, persists across conversations.

3. Conversation context
   Current session only. Use /compact to compress when it gets long.
```

CLAUDE.md is explicit instructions you write. Auto-memory is what Claude
learns from working with you over time. Both persist across sessions.

### Hooks System

Hooks execute **deterministic** actions at specific points in Claude's loop.
Unlike prompting (which is probabilistic), hooks **guarantee** execution.

**Hook Events** (14 lifecycle events):

| Event | When it fires | Use for |
|-------|--------------|---------|
| **PreToolUse** | Before a tool executes | Block dangerous commands, validate inputs |
| **PostToolUse** | After a tool completes | Auto-format code, run linters, log actions |
| **Notification** | When Claude needs your input | Desktop alerts, Slack notifications |
| **Stop** | When Claude finishes responding | Final checks, generate reports |
| **SubagentStop** | When a subagent finishes | Aggregate results, cleanup |
| **WorktreeCreate** | When a worktree is created | Custom VCS setup |
| **WorktreeRemove** | When a worktree is removed | Cleanup, teardown |

**Handler types**:
- **command**: Run a shell command
- **prompt/agent**: Run an LLM prompt
- **async**: Non-blocking execution

**Example**: Auto-format Python files after every edit:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "command": "black $FILE_PATH"
      }
    ]
  }
}
```

**PreToolUse** can return decisions via JSON output:
- `approve`: Allow the tool call
- `deny`: Block it (with reason)
- `modify`: Change the tool input

This enables guardrails — e.g., block `rm -rf` commands, prevent writing to
certain directories, enforce coding standards.

### Subagents

Spawn independent Claude instances for parallel work:

```
Main agent: "Refactor the authentication module"
  ├── Subagent 1: "Update the login endpoint"    (own context window)
  ├── Subagent 2: "Update the signup endpoint"   (own context window)
  └── Subagent 3: "Update the tests"             (own context window)
```

**Key properties**:
- Each subagent gets its own context window (doesn't pollute main)
- Can run in parallel
- Has restricted tools (you define which tools each subagent can use)
- Loads project context (CLAUDE.md, MCP servers, skills)
- Continues working after permission denials (tries alternatives)

**Custom subagents**: Define in `.claude/agents/` with frontmatter:

```markdown
---
name: researcher
tools: [Read, Glob, Grep, WebSearch]
isolation: worktree
---

You are a research agent. Search the codebase and web to answer questions.
Always cite your sources. Never modify files.
```

### Agent Teams

Agent Teams go beyond subagents — teammates communicate **directly with each
other**, not just back to the orchestrator:

```
┌─────────────────────────────────────────┐
│              Team Lead                   │
│         (orchestrator agent)             │
├──────┬──────────┬───────────────────────┤
│      │ Shared   │                       │
│  ┌───┴───┐  Task  ┌───────┐  ┌───────┐ │
│  │Team-  │  List + │Team-  │  │Team-  │ │
│  │mate 1 │ Mailbox │mate 2 │  │mate 3 │ │
│  └───┬───┘        └───┬───┘  └───┬───┘ │
│      │                │          │      │
│      └────────────────┴──────────┘      │
│        Direct peer communication        │
└─────────────────────────────────────────┘
```

**How they differ from subagents:**

| Feature | Subagents | Agent Teams |
|---------|-----------|-------------|
| Communication | Report to orchestrator only | Peer-to-peer via mailbox |
| Coordination | Independent tasks | Shared task list with dependencies |
| Task claiming | Assigned by parent | File locking prevents race conditions |
| Dependencies | None | Blocked tasks auto-unblock when deps complete |
| Scope | Single focused task | Complex multi-step projects |

**Shipped as experimental with Opus 4.6** (Feb 2026).

### Worktrees

Run parallel Claude sessions without file conflicts using git worktrees:

```bash
# Start Claude in a new worktree
claude --worktree

# Or use the -w flag
claude -w "implement the new API endpoint"
```

**What happens**:
1. Creates a git worktree (isolated copy of repo on a new branch)
2. Claude works in the worktree without touching your main files
3. When done, review and merge the changes
4. Worktree is cleaned up automatically

**Use cases**:
- Multiple features in parallel (one worktree each)
- Subagents each get their own worktree (`isolation: worktree`)
- Experiment without risk to main branch

### Headless / Remote Mode

```bash
# Headless: run from CLI with no interactive session
claude -p "refactor auth module" --output-format json

# Remote: start on desktop, access from phone/web
/remote-env
```

**Headless** is useful for CI/CD, scripts, and automation.
**Remote** lets you start a session on your machine and control it from anywhere.

### Background Tasks (GitHub Actions)

Run Claude Code as a GitHub Action — it codes while you sleep:

```yaml
# .github/workflows/claude.yml
- uses: anthropic/claude-code-action@v1
  with:
    prompt: "Fix all failing tests and open a PR"
```

### Claude Code Security

Reviews codebases for vulnerabilities. Goes beyond static analysis:
- Reasons about data flows across components
- Traces user input through the application
- Identifies vulnerabilities that rule-based tools miss
- Thinks like a human security researcher

### MCP Integration

Connect to external services via [[model-context-protocol]]:

```json
// .claude/settings.json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"]
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-slack"]
    }
  }
}
```

300+ MCP servers available for databases, APIs, services, and more.

### Cowork (Desktop Agent)

Cowork brings Claude Code's agentic capabilities to the Claude desktop app for
**non-coding** knowledge work. Runs in an isolated VM with access to local files
and MCP integrations. Claude Code for everyone, not just developers.

### Requirements

- Anthropic Pro plan minimum ($20/mo)
- Node.js installed
- Install: `npm install -g @anthropic-ai/claude-code`

## Code Example

```bash
# Install
npm install -g @anthropic-ai/claude-code

# Start interactive session
cd my-project
claude

# Single command (non-interactive)
claude "add type hints to all functions in utils.py"

# Headless mode (for scripts/CI)
claude -p "explain the architecture" --output-format json

# Start in a worktree
claude -w "implement feature X"

# Review recent changes
# (inside a session)
/review
```

```markdown
<!-- .claude/commands/deploy.md -->
Deploy the application:
1. Run the test suite
2. Build the Docker image
3. Push to registry
4. Update the deployment manifest
```

```markdown
<!-- .claude/agents/researcher.md -->
---
name: researcher
tools: [Read, Glob, Grep, WebSearch, WebFetch]
isolation: worktree
---

Research agent. Search codebase and web. Cite sources. Never modify files.
```

## Connections

- Built on the [[anthropic-claude-api]] — each tool call is an API request
- Uses [[model-context-protocol]] for external integrations (300+ servers)
- [[claude-agent-sdk]] is the programmatic equivalent for building your own agents
- Agent loop implements [[Agent Patterns]] (ReAct pattern)
- Hooks enable [[Observability]] and automated [[CI/CD]]
- Agent Teams connect to [[Multi-Agent Systems]] concepts
- Custom commands enable domain-specific [[Prompt Design Patterns]]
- This vault uses Claude Code for all note creation and management

## Sources

- [Claude Code Documentation](https://code.claude.com/docs)
- [Claude Code on GitHub](https://github.com/anthropics/claude-code)
- [Hooks Reference](https://code.claude.com/docs/en/hooks)
- [Custom Subagents](https://code.claude.com/docs/en/sub-agents)
- [Slash Commands Reference](https://code.claude.com/docs/en/slash-commands)
- [Agent Teams Guide](https://claudefa.st/blog/guide/agents/agent-teams)
- [Worktree Guide](https://claudefa.st/blog/guide/development/worktree-guide)
- [Claude Code Security](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html)
- [Claude Code to AI OS Blueprint](https://dev.to/jan_lucasandmann_bb9257c/claude-code-to-ai-os-blueprint-skills-hooks-agents-mcp-setup-in-2026-46gg)
