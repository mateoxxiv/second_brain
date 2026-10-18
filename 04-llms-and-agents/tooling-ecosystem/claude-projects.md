---
tags:
  - status/seed
  - llms
related:
  - "[[claude-context-layers]]"
  - "[[prompt-engineering-fundamentals]]"
  - "[[claude-work-modes]]"
  - "[[claude-skills]]"
  - "[[claude-artifacts]]"
  - "[[claude-academy-claude-101]]"
domain: llms
sources:
  - "https://academy.claude.com/es/courses/claude-101"
---

> **TL;DR** — A Claude Project is a persistent workspace that attaches the same instructions and reference files to every chat inside it, so you stop re-explaining the same context.

---

## Intuition

A project is a dedicated desk. The rules taped to the desk (instructions) and the binders on the shelf (knowledge files) are there every time you sit down. Without a project, every chat is a new temp who needs the full briefing again. A project lets you write the briefing once and reuse it across chats.

## Mechanics

Projects add a scope between a single chat and your global settings. A chat inside a project sees three things:

| Component | Scope | What it holds |
|-----------|-------|---------------|
| Project instructions | every chat in the project | Tone, process, required rules (e.g., "always end marketing copy with a call to action") |
| Knowledge files | every chat in the project | Reference documents: guides, reports, specs, examples |
| Chat history | that chat only | The conversation itself |

Global preferences still apply. The course says project instructions "work together with" user preferences but does not state which wins on a conflict.

**Knowledge scaling.** When the knowledge files approach the context window, Claude stops loading everything and searches the files for the passages relevant to your question (retrieval-augmented generation, or RAG). The course claims this extends capacity up to 10x. That is a product claim; verify it in Anthropic's docs before relying on the number.

```python
def project_context(project, global_prefs, query, count_tokens, retrieve, window):
    # Instructions are re-sent with every call, like any system prompt
    system = "\n\n".join([global_prefs, project["instructions"]])
    files = project["files"]
    if count_tokens(files) > window:            # too big to load whole
        files = retrieve(files, query, top_k=5) # send only the relevant passages
    return system, files + [query]              # conceptual, not the real API
```

## In ML

**Context container, not memory.** A project persists its files and instructions in storage, but the model is still stateless. Each call re-injects the project context, the same principle as in [[claude-context-layers]].

**Retrieval instead of stuffing.** Once knowledge exceeds the window, answer quality depends on which passages get retrieved. A question about a detail on page 300 fails if the retriever never surfaces that page. This is why descriptive file names matter: they help the retriever and the user target the right document.

**Shared context as a team contract.** Sharing a project shares its instructions and files as one unit. Whoever can edit the instructions changes behavior for everyone, which makes edit permissions a governance decision, not only an access setting.

## Exercises

**Basic** — Sort these into instructions or knowledge files: "Always answer in a formal tone", "Q3 sales report (PDF)", "Our brand guide", "End marketing copy with a call to action". Which two are rules, and which two are reference material?

**Intermediate** — Your project holds 400 pages of documents, and the team says answers miss details from late sections. Before changing the instructions, what do you check first? Think about file naming and what the retriever actually receives.

**Advanced** — Your instructions say "always cite the source file" and the knowledge base is 12 small files that fit in the window. Does retrieval run? What changes at 500 files, and why can an instruction like "use the Q3 numbers" fail silently when the chunk containing those numbers is never retrieved?
