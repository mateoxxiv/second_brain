---
tags:
  - status/seed
  - llms
  - prompt-engineering
related:
  - "[[claude-academy-claude-101]]"
  - "[[prompt-engineering-fundamentals]]"
  - "[[claude-skills]]"
  - "[[claude-projects]]"
  - "[[anthropic-claude-api]]"
  - "[[claude-code]]"
domain: llms
sources:
  - "https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude"
  - "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"
---

> **TL;DR** — The model is stateless: everything Claude "knows" about you is text injected into the context window, and each product feature is just a different *scope* (one message, one conversation, every conversation) for injecting it.

---

## Intuition

Imagine a brilliant consultant with total amnesia who meets you fresh every morning. The only way they know your job, your preferences, or yesterday's work is the briefing folder you hand them. A good first conversation with Claude is really about **filling that folder well** — and the product gives you several folders that persist for different lengths of time, so you don't rewrite the same briefing every day.

## Mechanics

An LLM computes a distribution over the next token conditioned *only* on the tokens in its window: $p(x_{t+1} \mid x_1, \dots, x_t)$. There is no hidden memory between calls; "remembering" means re-sending text. So the product's features are scopes over what gets prepended to $x_{1:t}$:

| Layer | Scope | Lesson feature | Why it matters |
|-------|-------|----------------|---------------|
| Prompt | one turn | context → task → rules | Highest-signal tokens; you control them directly |
| Attachments | one conversation | PDF, DOCX, CSV, TXT, images | Grounds answers in *your* data instead of priors |
| History + edits | one conversation | follow-ups, pencil-icon edit | Editing a message *rewrites* the context branch; a follow-up *appends* to it |
| Instructions / Memory | every conversation | Settings "Instructions for Claude", Memory | Stable facts (role, style) without repetition |
| Skills | on demand, any conversation | Reusable instruction packs | Loaded only when relevant → saves window space |

The first layer is where the stage → task → rules recipe lives; see [[prompt-engineering-fundamentals]].

```python
# Conceptually, every "chat" call is just this — the model sees one flat list.
def build_context(instructions, memory, skills, history, files, prompt):
    system = "\n\n".join([instructions, memory, *skills])  # cross-conversation layers
    messages = history + [{"role": "user", "content": files + [prompt]}]
    return system, messages  # nothing outside these two objects reaches the model

# Edit vs. follow-up: editing drops everything after the edited turn
def edit_turn(history, i, new_prompt):
    return history[:i] + [{"role": "user", "content": new_prompt}]
```

## In ML

**Stateless inference** — The same principle holds in the raw [[anthropic-claude-api]]: you must resend the whole `messages` list every call. The app's Memory and Instructions are simply managed versions of the `system` prompt.

**Context budget** — Every layer competes for a finite window and attention dilutes over long contexts. This is why Skills load lazily and why [[claude-code]] uses `CLAUDE.md` + on-demand files rather than dumping the whole repo.

**Conditioning, not learning** — Uploading a file or setting preferences does not update weights; it is in-context conditioning. Contrast with fine-tuning, which bakes behavior into parameters.

## Exercises

**Basic** — Rewrite "make me a pitch deck summary" into a three-part prompt (stage / task / rules) for an indie streaming startup seeking investors.

**Intermediate** — You state your job title in every chat. Which layer should hold it instead, and what is the token cost of *not* moving it over 200 conversations of ~40 tokens each?

**Advanced** — Claude gave a bad answer at turn 3 of 8. Argue why *editing* turn 3 usually beats a corrective follow-up at turn 9 (hint: what does the bad answer do to $p(x_{t+1} \mid x_{1:t})$ if it stays in the window?). When would the follow-up be better?
