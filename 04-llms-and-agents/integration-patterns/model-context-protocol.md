**Related**: [[anthropic-claude-api]], [[claude-code]], [[claude-agent-sdk]], [[Agent Patterns]]
**Tags**: #status/seed

## Core Idea

MCP (Model Context Protocol) is an **open standard** for connecting AI to
external data sources and tools. It solves the "last mile" problem: LLMs are
powerful reasoners, but they're trapped inside their training data. MCP gives
them a universal way to reach out and interact with the real world — databases,
APIs, files, services.

**Analogy**: Think of USB. Before USB, every device had its own proprietary
connector. USB created one standard that works for everything. MCP is USB for
AI-to-tool connections. Instead of writing custom integrations for every tool,
you implement one MCP server and any AI client can use it.

## Details

### The Problem MCP Solves

Without MCP, connecting Claude to your tools looks like this:

```
BEFORE MCP (custom everything):

Claude ──custom code──→ PostgreSQL
Claude ──custom code──→ Slack
Claude ──custom code──→ GitHub
Claude ──custom code──→ Your API

Every tool needs its own integration. N tools = N integrations.
```

With MCP:

```
AFTER MCP (one standard):

Claude ←→ MCP ←→ PostgreSQL server
Claude ←→ MCP ←→ Slack server
Claude ←→ MCP ←→ GitHub server
Claude ←→ MCP ←→ Your custom server

One protocol. Each tool exposes itself as an MCP server.
Any MCP-compatible client can connect to any server.
```

### Architecture

```
┌──────────┐     MCP Protocol     ┌──────────────┐
│          │ ←──────────────────→  │  MCP Server   │
│  Claude  │                      │  (your tool)  │
│ (client) │     JSON-RPC         │              │
│          │ ←──────────────────→  │  Exposes:     │
└──────────┘                      │  - Tools      │
                                  │  - Resources  │
                                  │  - Prompts    │
                                  └──────────────┘
```

An MCP server exposes three types of capabilities:

| Type | What it is | Example |
|------|-----------|---------|
| **Tools** | Functions Claude can call | `search_database(query)`, `send_slack_message(channel, text)` |
| **Resources** | Data Claude can read | Database schemas, file contents, API docs |
| **Prompts** | Pre-built prompt templates | "Summarize this PR", "Analyze this query" |

### How MCP Servers Run

Three modes:

```
1. LOCAL PROCESS (stdio)
   Server runs on your machine, communicates via stdin/stdout.
   Best for: local tools, file access, development.

2. HTTP (SSE / Streamable HTTP)
   Server runs remotely, communicates over HTTP.
   Best for: shared services, team tools, cloud resources.

3. IN-PROCESS
   Server runs inside your Python/TypeScript application.
   Best for: custom tools in the Claude Agent SDK.
```

### Available MCP Servers (Community)

| Server | What it connects to |
|--------|-------------------|
| **postgres** | PostgreSQL databases (query, schema) |
| **slack** | Slack workspaces (read/send messages, channels) |
| **github** | Repos, PRs, issues, code search |
| **filesystem** | Local file read/write |
| **google-drive** | Google Docs, Sheets, files |
| **brave-search** | Web search |
| **puppeteer** | Browser automation |
| **sqlite** | SQLite databases |

Plus hundreds of community-built servers for almost any tool.

### MCP Apps

An extension to MCP that enables servers to supply interactive user interfaces.
MCP servers can render UI that accepts user interactions directly inside Claude
products — not just text responses.

### Configuration

In [[claude-code]], MCP servers are configured in your project's
`.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://..."
      }
    }
  }
}
```

## Code Example

```python
# Creating a custom MCP server in Python
from mcp.server import Server
from mcp.types import Tool

server = Server("my-custom-tools")

@server.tool("search_notes")
async def search_notes(query: str) -> str:
    """Search the Obsidian vault for notes matching a query."""
    # Your search logic here
    results = find_matching_notes(query)
    return f"Found {len(results)} notes: {', '.join(results)}"

@server.tool("get_note_content")
async def get_note_content(path: str) -> str:
    """Read the content of a specific note."""
    with open(path) as f:
        return f.read()
```

## Connections

- Used by [[claude-code]] to connect to external tools
- [[claude-agent-sdk]] supports MCP servers natively (local, HTTP, in-process)
- Built on the [[anthropic-claude-api]] — tool use is the underlying mechanism
- Enables building [[RAG]] systems by connecting to vector databases
- Connects to [[Agent Patterns]] — agents need tools, MCP provides them
- The open standard philosophy aligns with [[Open-Source vs Closed-Source Tradeoffs]]

## Sources

- [Model Context Protocol announcement](https://www.anthropic.com/news/model-context-protocol)
- [MCP Documentation](https://modelcontextprotocol.io)
- [MCP GitHub — servers and SDKs](https://github.com/modelcontextprotocol)
- [Claude expands tool connections using MCP](https://www.helpnetsecurity.com/2026/01/27/anthropic-claude-mcp-integration/)
