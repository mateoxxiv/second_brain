---
tags:
  - status/seed
  - llms
related:
  - "[[claude-projects]]"
  - "[[claude-context-layers]]"
  - "[[claude-work-modes]]"
  - "[[claude-academy-claude-101]]"
domain: llms
sources:
  - "https://academy.claude.com/es/courses/claude-101"
---

> **TL;DR** — A skill is a packaged procedure (instructions, scripts, and resources) that Claude loads only when a request matches it, so the method is reusable without taking up context every time.

---

## Intuition

A project is a binder of reference material. A skill is a laminated checklist for one job, such as "write a quarterly review" or "format a board deck to brand rules". You do not read the checklist for every conversation, only when that job comes up. The question a skill answers is how Claude should do this task every time, in the same order, with the same standard.

## Mechanics

A skill is a folder: instructions for the procedure, optional scripts, and reference files. The lesson lists two kinds:

| Kind | Who maintains it | Examples | How it runs |
|------|------------------|----------|-------------|
| Anthropic skills | Anthropic | Excel, Word, PowerPoint, and PDF creation | Invoked automatically when relevant |
| Custom skills | You or your organization | Brand-voice review, meeting-note format, compliance checklist | Invoked automatically when relevant, after upload or creation |

Skills need code execution and file creation turned on, since they run inside Claude's isolated sandbox. On Team and Enterprise plans, an organization owner controls that switch. Custom skills are private to the account that creates them. Because skills can contain executable code, review a third-party skill's contents before you install it.

```python
# Conceptual only: the lesson does not describe the selection mechanism
def handle(request, skills, base_context):
    matched = [s for s in skills if s["matches"](request)]   # selection by relevance
    procedure = "\n\n".join(s["body"] for s in matched)      # load only what matched
    return base_context + procedure + request
```

## In ML

**Skills as lazy-loaded context** — The model still sees only its context window. A skill is a way to keep a long procedure out of the window until a request needs it, the scope described in [[claude-context-layers]].

**Skills vs. projects** — The lesson's split is clean: a project stores what Claude knows (the "what"), and a skill defines how Claude works (the "how"). A skill can read material from a project, such as a client-prep skill that uses a project's client profiles. This matches the context-budget tradeoff in [[claude-projects]].

**Procedures as code** — A custom skill that bundles scripts and checklists is a small, versioned program that the model follows and runs. It is closer to a deployable component than a prompt, which is why review and trust matter for it, as with any code you run.

## Exercises

**Basic** — Put each item in a project or a skill, and say why: (a) a client's brand guidelines PDF, (b) a step-by-step quarterly variance review, (c) the list of past board decisions, (d) a checklist that every contract must pass before sending.

**Intermediate** — You want every meeting summary to follow the same five-part format and pull attendee names from a project file. Design the split: what goes in the skill, what stays in the project, and what the skill must say to read from the project.

**Advanced** — A skill includes a script that a colleague shared. What checks would you run before enabling it, and why does executable content change the risk compared with a text-only instruction?

## Gaps: notes still to create

- Anthropic's document-creation skills (Excel, Word, PowerPoint, PDF) as their own note.
- The skill-creation workflow (conversation, save, upload), if the process grows enough to need its own note.
