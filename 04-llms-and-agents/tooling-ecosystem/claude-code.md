**Related**: [[anthropic-claude-api]], [[claude-agent-sdk]], [[model-context-protocol]], [[Agent Patterns]]
**Tags**: #status/seed

## Core Idea

Claude Code is an agentic command-line tool that gives Claude the ability to
**act on your computer** — read files, write code, run commands, search
codebases, and manage entire projects from the terminal. It's not a chatbot
that suggests code — it's an agent that executes code.

Think of it as: "what if Claude could use your terminal the way you do?" You
describe a task, Claude plans the steps, uses tools to execute them, and
delivers the result.

## Details

### How It Works

```
You: "Add error handling to the API endpoint in server.py"

Claude Code:
  1. Read(server.py)           → understands the current code
  2. Grep("def endpoint")      → finds the specific function
  3. Edit(server.py, ...)      → adds try/except blocks
  4. Bash("python -m pytest")  → runs tests to verify
  5. Shows you the diff        → you approve or reject
```

Claude Code runs an **agent loop**: it thinks about the task, picks a tool,
executes it, observes the result, and repeats until done. You approve or deny
each action based on your permission settings.

### Built-in Tools

| Tool | What it does |
|------|-------------|
| **Read** | Read any file in the working directory |
| **Write** | Create new files |
| **Edit** | Make precise edits to existing files (find & replace) |
| **Bash** | Run terminal commands (git, pip, tests, scripts) |
| **Glob** | Find files by pattern (e.g., `**/*.py`) |
| **Grep** | Search file contents with regex |

These are the same tools you're interacting with right now in this conversation.

### Key Features

**Hooks**: Python functions that execute at specific points in Claude's loop.
Use them for:
- Auto-formatting code after edits
- Running linting before commits
- Blocking dangerous commands
- Adding custom validation

**MCP Servers**: Connect Claude Code to external tools via
[[model-context-protocol]]:
- Databases (query and modify)
- Slack (read/send messages)
- GitHub (create PRs, review code)
- Any custom API

**Memory System**:
- `CLAUDE.md` in project root — persistent instructions loaded every session
- Auto-memory in `~/.claude/projects/` — Claude saves patterns across sessions
- Project-level context that persists between conversations

**Background Tasks**: Run Claude Code via GitHub Actions — it codes
asynchronously. Push a task, get a PR back when it's done.

**Claude Code Security**: Reviews codebases for vulnerabilities. Goes beyond
static analysis — reasons about data flows, component interactions, and
attack surfaces like a human security researcher.

**Custom Slash Commands**: Create `.claude/commands/*.md` files to define
reusable workflows (like the /note, /quiz, /session commands in this vault).

### Permission Modes

```
Mode         What Claude can do without asking
-----------  -------------------------------------------
Ask          Nothing — asks for every action
Auto-edit    Read + Edit files without asking
Full auto    Everything including Bash commands (careful!)
```

### How It Differs from ChatGPT / Claude.ai Chat

| Feature | Claude.ai Chat | Claude Code |
|---------|---------------|-------------|
| Interface | Web browser | Terminal |
| Can read files | Only uploads | Reads your filesystem directly |
| Can edit files | No | Yes — modifies files in place |
| Can run code | No | Yes — executes Bash commands |
| Memory | Conversation only | CLAUDE.md + auto-memory across sessions |
| Context | Limited | Full codebase via Glob/Grep |
| Hooks | No | Yes — automate workflows |
| MCP | Limited | Full MCP server support |

### Cowork (Desktop Agent)

Cowork brings Claude Code's agentic capabilities to the Claude desktop app
for **non-coding** knowledge work. It runs in an isolated VM on your machine,
with access to local files and MCP integrations. Think of it as Claude Code
for everyone, not just developers.

### Requirements

- Anthropic Pro plan minimum ($20/mo)
- Node.js installed
- Install: `npm install -g @anthropic-ai/claude-code`

## Code Example

```bash
# Install
npm install -g @anthropic-ai/claude-code

# Start in a project directory
cd my-project
claude

# Or run a single command
claude "add type hints to all functions in utils.py"

# Run in non-interactive mode
claude --print "explain the architecture of this project"
```

```markdown
<!-- .claude/commands/test.md -->
Run the test suite and fix any failing tests.
Steps:
1. Run `pytest` and capture output
2. For each failure, read the test and the source code
3. Fix the issue
4. Re-run tests to verify
```

## Connections

- Built on the [[anthropic-claude-api]] — each tool call is an API request
- Uses [[model-context-protocol]] for external integrations
- [[claude-agent-sdk]] is the programmatic version of Claude Code's capabilities
- The agent loop pattern connects to [[Agent Patterns]] (ReAct)
- Custom commands enable workflows like [[Prompt Design Patterns]]
- This vault uses Claude Code for all note creation and management

## Sources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Claude Code on GitHub](https://github.com/anthropics/claude-code)
- [Claude Code Security announcement](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html)
