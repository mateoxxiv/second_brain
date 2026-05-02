---
tags:
  - status/seed
  - llms
related:
  - "[[anthropic-claude-api]]"
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
domain: llms
sources:
  - "https://www.anthropic.com/news/model-context-protocol"
  - "https://modelcontextprotocol.io"
  - "https://github.com/modelcontextprotocol"
  - "https://www.helpnetsecurity.com/2026/01/27/anthropic-claude-mcp-integration/"
---

> **TL;DR** — MCP is USB for AI-to-tool connections. One open standard lets any AI client connect to any tool server. Without it: N tools = N custom integrations.

---

## Intuition

LLMs are powerful reasoners but trapped inside their training data. MCP solves the "last mile": a universal standard for connecting AI to external data sources and tools.

Think of USB: before it, every device had its own connector. USB created one standard that works for everything. MCP does the same for AI integrations — implement one MCP server and any AI client can use it.

Without MCP: Claude → custom code → PostgreSQL, Claude → custom code → Slack, Claude → custom code → GitHub (N tools = N integrations). With MCP: Claude ↔ MCP ↔ any server.

## Mechanics

**An MCP server exposes three capability types:**

| Type | What it is | Example |
|------|-----------|---------|
| Tools | Functions AI can call | `search_database(query)` |
| Resources | Data AI can read | Database schemas, file contents |
| Prompts | Pre-built templates | "Summarize this PR" |

**Three transport modes:**
- **stdio (local):** server runs on your machine via stdin/stdout
- **HTTP (remote):** server runs remotely over HTTP/SSE
- **In-process:** server runs inside your Python app (Claude Agent SDK)

**Configuring in [[claude-code]]** (`.claude/settings.json`):
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": { "DATABASE_URL": "postgresql://..." }
    }
  }
}
```

```python
# Creating a custom MCP server in Python
from mcp.server import Server

server = Server("my-custom-tools")

@server.tool("search_notes")
async def search_notes(query: str) -> str:
    """Search the Obsidian vault for notes matching a query."""
    results = find_matching_notes(query)
    return f"Found {len(results)} notes: {', '.join(results)}"
```

> Runnable: [[code/llms/mcp_server.py]]

## In ML

**Tool use at scale.** MCP standardizes how agents access external tools — databases, APIs, file systems, services. Without a standard, every new tool requires custom integration code. MCP lets you add a new capability by deploying one server.

**RAG without the plumbing.** Connect Claude to a vector database via MCP and it can search, retrieve, and reason over your documents without you writing a retrieval pipeline. The MCP server handles the interface.

**[[claude-agent-sdk]] integration.** The Agent SDK supports MCP servers natively (local, HTTP, in-process). Custom agent tools are MCP tools under the hood — you get the MCP ecosystem for free.

## Exercises

**Basic** — Describe the difference between an MCP Tool and an MCP Resource. Give a concrete example of each for a code search use case.

**Intermediate** — Write a minimal MCP server in Python that exposes one tool: `get_file_content(path: str) -> str`. Test it by connecting to it from Claude Code.

**Advanced** — Design an MCP server architecture for a multi-source RAG system (Postgres + S3 + Notion). What tools and resources would you expose? How would you handle authentication?
