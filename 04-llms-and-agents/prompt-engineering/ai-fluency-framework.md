---
tags:
  - status/seed
  - llms
  - prompt-engineering
related:
  - "[[iterative-prompt-refinement]]"
  - "[[prompt-engineering-fundamentals]]"
  - "[[claude-work-modes]]"
  - "[[claude-academy-claude-101]]"
domain: llms
sources:
  - "https://academy.claude.com/courses/claude-101/getting-better-results"
---

> **TL;DR** — AI fluency is the judgment to collaborate well with an AI, and the 4D framework names four competencies for it: Delegation, Description, Discernment, and Diligence.

---

## Intuition

Knowing which buttons to press makes you a user. Knowing what to hand off, how to ask, how to check the answer, and how to stand behind the result makes you fluent. Think of a new analyst on a team. Technical skill matters, but so does knowing which tasks to give them, how to brief them, how to review their work, and when to take responsibility for it yourself.

The framework was developed by Rick Dakan (Ringling College of Art and Design) and Joseph Feller (University College Cork). Its value is that it separates four skills that people tend to blur together.

## Mechanics

The 4D framework is a taxonomy, not a formula, so there is nothing to derive. Each competency answers one question you should ask during a collaboration.

| Competency | Question it answers | Example |
|------------|--------------------|---------|
| Delegation | Who should do this: me, Claude, or both? | Claude drafts the summary; you make the final call |
| Description | How do I specify the result and the process? | Stage, task, and rules in one prompt ([[prompt-engineering-fundamentals]]) |
| Discernment | Is the output correct, accurate, and fit for purpose? | Checking a figure against a source you trust |
| Diligence | Am I using the output responsibly and transparently? | Verifying results and disclosing AI's role |

The lesson links Description to the prompt structure from Lesson 2, and it links the troubleshooting techniques to Discernment and Diligence.

```python
# Conceptual checklist: run through the four competencies per task
checklist = {
    "delegation":  "Should a human, Claude, or both do this?",
    "description": "Did I say what the result and the process should look like?",
    "discernment": "Did I check quality and accuracy against what I know?",
    "diligence":   "Can I stand behind this, and did I disclose AI's role?",
}
```

## In ML

**Description and prompt structure** — Specifying the output and the process is the prompt-design side of the job. Most weak outputs trace back to a missing piece of description, which is why [[iterative-prompt-refinement]] treats a bad answer as a diagnosis problem.

**Discernment and evaluation** — Checking outputs against cases where you already know the answer is a holdout-style evaluation. The lesson's Rio example runs this loop on past quarters, the same logic as testing a model on data it did not see during tuning.

**Delegation and capability boundaries** — The lesson's conclusion is that a task that fails your validation is a task you should not delegate. Delegation is a decision you revisit, not a setting you choose once. Connects to [[claude-work-modes]], where delegated work runs without you approving each step.

## Exercises

**Basic** — Label each action with one competency: (a) you write the final decision yourself after Claude drafts options, (b) you add the audience and length to a prompt, (c) you check a cited statistic against its original source, (d) you state in a report that AI helped with the analysis.

**Intermediate** — In the lesson's Rio example, the first answer missed the program-type detail. Which competency did Rio exercise to catch it, and which did he exercise when he added the program type to the next prompt? Why does the loop only work if he compares against known results?

**Advanced** — Delegation and Diligence overlap. Suppose Claude passes your validation on a task that involves personal data. Why might the task still be one you should not delegate, and what does Diligence require even if the output is correct?

## Gaps: notes still to create

- An evaluation note on testing Claude against past cases with known answers (the lesson's "simple evaluation approach"), derived from the Rio example.
- A note on the delegation validation cycle, separate from this framework note.
