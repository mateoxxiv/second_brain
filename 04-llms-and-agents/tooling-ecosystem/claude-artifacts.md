---
tags:
  - status/seed
  - llms
related:
  - "[[claude-work-modes]]"
  - "[[claude-projects]]"
  - "[[claude-context-layers]]"
  - "[[claude-academy-claude-101]]"
domain: llms
sources:
  - "https://claude.com/features/artifacts"
---

> **TL;DR** — An artifact is a finished deliverable that lives outside the chat as an editable, shareable object, so you revise the thing itself instead of re-asking for it in new messages.

---

## Intuition

A chat reply is a spoken answer in a meeting: useful, but it scrolls away, and changing it means asking again. An artifact is the document you put on the table. It has a fixed place, you mark it up, and colleagues read the same copy. The question it answers is where work you will revise and reuse should live. It matters because it turns "generate, copy, paste into another app, fix there" into one loop inside Claude.

## Mechanics

An artifact is generated output that (1) persists beyond the message that created it, (2) can be edited in place, and (3) can be shared or exported. Claude creates one when the output stands on its own and you would edit, reuse, or share it. A one-time answer stays a chat reply.

| Property | Chat reply | Artifact | Why it matters |
|----------|-----------|----------|----------------|
| Lifetime | Scrolls away with the conversation | Stored in the Artifacts tab (paid plans) | You can come back to it |
| Editing | Ask for a rewrite in a new message | Edit directly, comment, or ask Claude | Small fixes skip a full regeneration |
| Sharing | Copy and paste the text | Link, with view, comment, or edit roles (design, slides, docs) | Collaborators see the same version |
| Export | Copy the text | .pptx, .pdf, .html, .docx, Google Docs | Work leaves Claude only when you choose |

On the Free plan, an artifact stays attached to the conversation that created it. Plan rules change, so check the current ones before relying on this.

```python
# Conceptual model only, not how Claude implements artifacts
reply = {"role": "assistant", "content": "...explanation..."}      # belongs to one message
artifact = {"title": "Q3 board memo", "type": "document", "content": "..."}  # outlives it
```

## In ML

**Artifacts and statelessness** — The model itself keeps no state between calls ([[claude-context-layers]]). The artifact gives you a durable object to iterate on, and each edit has to carry the relevant content back into the model. This is an inference from how stateless inference works. The lesson does not describe the mechanism.

**Live object vs. snapshot** — An artifact stays editable and linkable. An export is a frozen copy. Once a PDF is sent, it no longer reflects later edits to the source, the same trade-off as a live document versus an attachment in an email.

**Delegated outputs** — When delegated work ([[claude-work-modes]]) produces a document or app, the artifact is the container for that output, so you can keep working on it after the task finishes.

## Exercises

**Basic** — Decide chat reply or artifact for each request, and say why: (a) "explain what a p-value means", (b) "a one-page project brief my team will edit", (c) "a monthly expense tracker I will reuse", (d) "one sentence for a Slack update".

**Intermediate** — You need a board memo and a 10-slide deck from the same meeting notes. Which artifact types would you use, and in what order? Consider the lesson's "turn this document into a presentation" pattern and what changes between the two outputs.

**Advanced** — A client needs a deck, but your team keeps editing the source. Compare sending an exported .pptx with sharing the artifact link. What breaks if the source changes after export? When does the lesson's limit on charts, which do not update on their own, make a snapshot the wrong choice?
