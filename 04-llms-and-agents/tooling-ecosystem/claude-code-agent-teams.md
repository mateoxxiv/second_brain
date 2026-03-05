**Related**: [[claude-code]], [[claude-agent-sdk]], [[model-context-protocol]], [[Agent Patterns]], [[Multi-Agent Systems]]
**Tags**: #status/seed

## Core Idea

Agent Teams let you run **multiple Claude Code instances that work together**
on the same project — each teammate is an independent agent with its own context
window, but they communicate directly with each other, share a task list, and
coordinate dependencies automatically.

Unlike subagents (which report back to a single parent), teammates are **peers**
that can debate, share findings, and build on each other's work. Think of it as
going from a single developer to a coordinated team — each member owns a piece
of the problem, but they stay in sync.

**Status**: Experimental feature (as of March 2026). Requires Opus 4.6.

## Details

### Subagents vs Agent Teams

| Feature | Subagents | Agent Teams |
|---------|-----------|-------------|
| Communication | Report to parent only | Peer-to-peer via mailbox |
| Coordination | Parent assigns work | Shared task list with dependencies |
| Task claiming | Assigned by parent | File locking prevents race conditions |
| Dependencies | None | Blocked tasks auto-unblock when deps complete |
| Context | Own context, limited | Own context + shared CLAUDE.md |
| Scope | Single focused task | Complex multi-step projects |
| Mental model | "Do this subtask and report back" | "You're a team member, coordinate with others" |

### Architecture

```
┌─────────────────────────────────────────────────┐
│                   TEAM LEAD                      │
│            (your main Claude session)            │
│                                                  │
│  "Create a team to build the search feature..."  │
└──────────┬───────────────┬───────────────┬──────┘
           │               │               │
     ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐
     │ Teammate  │  │ Teammate  │  │ Teammate  │
     │ "api"     │  │ "indexer" │  │ "ui"      │
     │           │  │           │  │           │
     │ Own       │  │ Own       │  │ Own       │
     │ context   │  │ context   │  │ context   │
     │ window    │  │ window    │  │ window    │
     └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
           │               │               │
           └───────┬───────┴───────┬───────┘
                   │               │
          ┌────────┴──┐    ┌──────┴───────┐
          │ Shared    │    │   Mailbox    │
          │ Task List │    │  (peer-to-   │
          │           │    │   peer msgs) │
          └───────────┘    └──────────────┘

Files at: ~/.claude/tasks/{team-name}/
```

### Step-by-Step Setup

#### 1. Enable the Feature

Agent Teams is disabled by default. Enable it in settings:

```json
// ~/.claude/settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Or as an environment variable:

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

#### 2. Requirements

- **Opus 4.6 access**: Pro ($20/mo) or Max ($100-200/mo)
- **tmux** (optional): for split-pane view of all teammates simultaneously
- **Good CLAUDE.md**: all teammates read it — clear conventions save tokens

#### 3. Create a Team (Natural Language)

There's **no config file** for teams. You describe what you want conversationally
inside Claude Code:

```
Create an agent team with 3 teammates:
1. "backend" - refactor the API endpoints in src/api/
2. "frontend" - update the React components to match
3. "tests" - write integration tests for both changes

Have them coordinate through the shared task list.
Use worktrees so they don't conflict.
```

Claude Code spawns the teammates, creates the task list, and sets up communication.

#### 4. View Your Team

Two display modes:

```
In-process (default):
  All teammates in one terminal.
  Shift+Down → cycle between them.

Split panes (requires tmux or iTerm2):
  Each teammate gets its own pane.
  See everyone's output simultaneously.
```

#### 5. Interact During Execution

Message any teammate directly mid-task:

```
@backend: Use async/await instead of callbacks for the new endpoints
@tests: Focus on error cases, happy path is already covered
```

Messages are delivered automatically. The lead doesn't need to poll.

### How Coordination Works

#### Task List

Stored at `~/.claude/tasks/{team-name}/`:

```
tasks/
├── task-001.json    (status: done,    owner: "backend")
├── task-002.json    (status: active,  owner: "frontend", blocked_by: [001])
├── task-003.json    (status: blocked, owner: "tests",    blocked_by: [001, 002])
```

- **File locking** prevents two teammates from claiming the same task
- **Auto-unblocking**: when "backend" finishes task-001, task-002 unblocks
  automatically and "frontend" starts
- Dependencies are declared when creating the team

#### Mailbox

Peer-to-peer messaging at `~/.claude/tasks/{team-name}/mailbox/`:

```
mailbox/
├── backend.json     (messages for "backend")
├── frontend.json    (messages for "frontend")
└── tests.json       (messages for "tests")
```

Any teammate can message any other. Examples:
- "backend" → "frontend": "API schema changed, the endpoint now returns X"
- "tests" → "backend": "Your endpoint crashes on empty input"
- Lead → all: "Prioritize the authentication flow first"

#### Worktrees (Isolation)

Each teammate can work in its own git worktree to avoid file conflicts:

```
main branch:          your working copy (untouched)
backend-worktree:     teammate "backend" works here
frontend-worktree:    teammate "frontend" works here
tests-worktree:       teammate "tests" works here
```

Say "use worktrees" when creating the team. Worktrees are cleaned up
automatically when teammates finish.

### Plan Approval Mode

For risky changes, require teammates to get approval before executing:

```
Spawn an architect teammate to redesign the auth module.
Require plan approval before making any changes.
```

The teammate writes a plan → sends it to the lead → you approve or reject
with feedback → only then does the teammate execute.

### Practical Prompt Templates

#### Code Review Team

```
Create an agent team to review this PR. Spawn three reviewers:
- One focused on security vulnerabilities
- One checking performance impact
- One validating test coverage
Have them each review and share findings.
Synthesize a final report.
```

#### Debugging Team

```
Spawn 4 teammates to investigate why the API is slow:
- Teammate 1: profile database queries
- Teammate 2: check network latency and external API calls
- Teammate 3: analyze memory usage and GC patterns
- Teammate 4: review recent commits in git log
Have them share findings and debate hypotheses.
Update a shared findings doc.
```

#### Feature Build Team

```
Create a team to build the new search feature:
- "api" teammate: build the search endpoint in src/api/
- "indexer" teammate: set up Elasticsearch indexing in src/services/
- "ui" teammate: build the search UI component in src/components/
Use worktrees. Coordinate dependencies through the task list.
Require plan approval before major changes.
```

#### Research / Investigation Team

```
Spawn 5 teammates to investigate different hypotheses about the bug.
Have them talk to each other to disprove each other's theories,
like a scientific debate.
Update the findings doc with whatever consensus emerges.
```

### Best Practices

| Practice | Why |
|----------|-----|
| **Write a clear CLAUDE.md** | All teammates read it. Module boundaries, build commands, and conventions reduce exploration costs. 3 teammates reading clear docs is cheaper than 3 teammates exploring independently. |
| **Use worktrees** | Prevents file conflicts between teammates |
| **Define clear boundaries** | "You own src/api/, don't touch src/ui/" prevents collisions |
| **Use plan approval for risky changes** | Review before execution |
| **Start with 2-3 teammates** | Scale up when comfortable |
| **Name teammates by responsibility** | "api", "frontend", "tests" — not "agent1", "agent2" |
| **Set dependencies explicitly** | "tests depends on api and frontend finishing first" |

### Limitations

- **Experimental** — API and behavior may change
- **Token cost** — each teammate has its own context window (multiplied cost)
- **Opus 4.6 required** — doesn't work with Sonnet or Haiku
- **Communication overhead** — for simple tasks, a single agent + subagents is faster
- **No persistent teams** — teams are created per session, not saved for reuse

## Code Example

```bash
# 1. Enable agent teams
# Add to ~/.claude/settings.json:
# {"env":{"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS":"1"}}

# 2. Start Claude Code in your project
cd my-project
claude

# 3. Inside the session, create your team:
# "Create a team with 3 teammates to refactor the payment module..."

# 4. Navigate between teammates
# Shift+Down to cycle (in-process mode)

# 5. Message a specific teammate
# @backend: change the response format to JSON

# With tmux (split panes):
# tmux must be installed, Claude Code auto-detects it
```

## Connections

- Agent Teams is a feature of [[claude-code]]
- Built on the [[anthropic-claude-api]] — each teammate is an API session
- Uses [[model-context-protocol]] when teammates need external tools
- Implements [[Multi-Agent Systems]] patterns (peer-to-peer coordination)
- Related to [[Agent Patterns]] — each teammate follows a ReAct loop
- [[claude-agent-sdk]] supports agent teams programmatically
- Worktrees use git's worktree feature for isolation

## Sources

- [Official Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)
- [Agent Teams Complete Guide 2026](https://claudefa.st/blog/guide/agents/agent-teams)
- [From Tasks to Swarms: Agent Teams](https://alexop.dev/posts/from-tasks-to-swarms-agent-teams-in-claude-code/)
- [Claude Code Agent Teams — Cobus Greyling](https://cobusgreyling.medium.com/claude-code-agent-teams-ca3ec5f2d26a)
- [Swarm Orchestration Skill (GitHub Gist)](https://gist.github.com/kieranklaassen/4f2aba89594a4aea4ad64d753984b2ea)
- [Agent Teams Use Cases and Prompt Templates](https://claudefa.st/blog/guide/agents/agent-teams-use-cases)
