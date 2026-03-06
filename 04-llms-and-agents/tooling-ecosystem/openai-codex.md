**Related**: [[openai-api]], [[openai-agents-sdk]], [[claude-code]], [[Agent Patterns]]
**Tags**: #status/seed

## Core Idea

Codex is OpenAI's agentic coding tool — the equivalent of [[claude-code]] but
with a different architecture. While Claude Code runs locally in your terminal,
Codex runs tasks in **cloud sandboxes** — isolated containers preloaded with your
repo where agents work in parallel, with no internet access during execution.

Codex also has a **local CLI** mode for interactive, approval-controlled
workflows (similar to Claude Code). But its signature feature is cloud-based
parallel execution: you can launch multiple agents on different tasks
simultaneously, each in its own sandbox.

**Latest model**: GPT-5.3-Codex — purpose-built for agentic coding, 25% faster
than GPT-5.2, best-in-class code generation and reasoning.

## Details

### Codex vs Claude Code

| Feature | OpenAI Codex | Claude Code |
|---------|-------------|-------------|
| Execution | Cloud sandboxes (primary) + local CLI | Local terminal only |
| Parallelism | Multiple cloud agents simultaneously | Subagents + Agent Teams |
| Network during execution | Disabled (security) | Full access |
| Multi-agent | Built-in parallel task management | Agent Teams (experimental) |
| Worktrees | Cloud sandboxes per task | Git worktrees |
| Model | GPT-5.3-Codex | Opus 4.6 |
| Output | Proposes PRs for review | Direct file edits |
| Platform | Web app + CLI (Windows, Mac, Linux) | CLI only |
| Hooks/Skills | No equivalent | Hooks, custom commands |
| MCP | Via Agents SDK | Native MCP support |

### Architecture

```
┌────────────────────────────────────────┐
│           Codex Interface              │
│     (Web app or CLI)                   │
├────────────┬───────────────────────────┤
│            │                           │
│  ┌─────────┴──────┐  ┌──────────────┐ │
│  │  Cloud Mode    │  │  Local CLI   │ │
│  │                │  │              │ │
│  │  ┌──────────┐  │  │  Interactive │ │
│  │  │Sandbox 1 │  │  │  approval-  │ │
│  │  │(no net)  │  │  │  controlled │ │
│  │  ├──────────┤  │  │  workflow    │ │
│  │  │Sandbox 2 │  │  │              │ │
│  │  │(no net)  │  │  │  Like Claude │ │
│  │  ├──────────┤  │  │  Code's      │ │
│  │  │Sandbox N │  │  │  local mode  │ │
│  │  └──────────┘  │  └──────────────┘ │
│  └────────────────┘                   │
├────────────────────────────────────────┤
│        GitHub Integration              │
│  (reads repos, proposes PRs)          │
└────────────────────────────────────────┘
```

### Two Execution Modes

**1. Cloud Sandboxes (parallel, async)**
- Each task runs in an isolated container preloaded with your repo
- Internet disabled during execution (security: agent can only access code you give it)
- Multiple tasks run simultaneously
- Results are proposed as PRs for you to review
- Best for: background work, parallel features, bulk refactoring

**2. Local CLI (interactive)**
- Runs on your machine, like Claude Code
- Approval-controlled: you approve/reject actions
- Full access to your local environment
- Best for: interactive coding, exploration, quick tasks

### What Codex Can Do

- Write features from natural language descriptions
- Answer questions about your codebase
- Fix bugs (point it at an issue, it proposes a fix)
- Propose pull requests for review
- Run tests and iterate until they pass
- Refactor code across multiple files

### Key Differences from Claude Code

1. **Security model**: Codex sandboxes have NO internet — can't exfiltrate code.
   Claude Code has full network access.

2. **PR-first workflow**: Codex proposes PRs you review. Claude Code edits
   files directly (you review via git diff).

3. **No hooks or skills**: Codex doesn't have Claude Code's extensibility
   (custom commands, hooks, MCP integration). The [[openai-agents-sdk]] fills
   this gap for programmatic use.

4. **Parallel by default**: Launch 5 tasks at once, each in its own sandbox.
   Claude Code requires Agent Teams (experimental) for peer parallelism.

## Code Example

```bash
# Install Codex CLI
npm install -g @openai/codex

# Interactive local mode
cd my-project
codex

# Single command
codex "add error handling to the payment endpoint"

# Cloud mode (from web app or CLI)
codex --cloud "refactor auth module and open a PR"
```

```python
# Using Codex programmatically via Agents SDK
from openai_agents import Agent, CodexTool

agent = Agent(
    model="gpt-5.3-codex",
    tools=[CodexTool(repo="my-org/my-repo")]
)

result = agent.run("Fix all failing tests and open a PR")
```

## Connections

- Codex is OpenAI's answer to [[claude-code]]
- Built on the [[openai-api]] — uses GPT-5.3-Codex model
- Integrates with [[openai-agents-sdk]] for programmatic use
- Follows [[Agent Patterns]] (ReAct loop) internally
- Compare architecture with [[claude-code-agent-teams]] (peer agents)
- Cloud sandboxes relate to [[Multi-Agent Systems]] concepts

## Sources

- [Introducing Codex](https://openai.com/index/introducing-codex/)
- [Codex Product Page](https://openai.com/codex/)
- [Codex on GitHub (CLI)](https://github.com/openai/codex)
- [GPT-5.3-Codex Announcement](https://openai.com/index/introducing-gpt-5-3-codex/)
- [Use Codex with the Agents SDK](https://developers.openai.com/codex/guides/agents-sdk/)
- [Codex Changelog](https://developers.openai.com/codex/changelog/)
