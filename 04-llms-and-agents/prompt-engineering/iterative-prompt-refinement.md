---
tags:
  - status/seed
  - llms
  - prompt-engineering
related:
  - "[[prompt-engineering-fundamentals]]"
  - "[[claude-context-layers]]"
  - "[[ai-fluency-framework]]"
  - "[[claude-academy-claude-101]]"
  - "[[binomial-distribution]]"
  - "[[complementary-events]]"
domain: llms
sources:
  - "https://academy.claude.com/courses/claude-101/getting-better-results"
  - "https://youtu.be/Zzn-g8lvLMA"
---

> **TL;DR** — Treat the first output as a draft: diagnose *which* part of the prompt failed, fix that part, and before trusting Claude on a recurring task, test it on past cases where you already know the right answer.

---

## Intuition

Prompting is closer to debugging than to asking an oracle. Code rarely runs right on the first try. You read the error, find the cause, fix it, and run it again. A weak answer is a symptom of a specific missing piece in your prompt. Saying "make it better" is like rerunning broken code without changing anything.

## Mechanics

**1. Diagnose the symptom, then fix its cause** (the lesson's troubleshooting table):

| Symptom | Root cause | Fix |
|---------|-----------|-----|
| Generic answer | Missing context | Add audience, role, constraints, relationship |
| Wrong length | Claude guessed the size | State it: "two paragraphs", "under 100 words" |
| Wrong format | Content understood, layout not | *Show, don't tell*: give a sample or an explicit structure |
| Inaccurate facts | Plausible but wrong output (niche facts) | Verify; ask for sources and confidence levels |
| Wrong tone | Professional default | Describe the tone in plain words plus an example |

**2. Steer or restart.** Give *specific* feedback ("cut the intro, keep the three numbers"), not just "shorter". If the conversation has gone off track, **start fresh with a clearer prompt** instead of piling corrections onto a context that still holds the bad answer (see [[claude-context-layers]]).

**3. Before delegating recurring work, run an eval.** This is the delegation–diligence loop from Rio's example in the video:

```text
gather 5–10 past cases with KNOWN correct results   # your baseline
loop:
    prompt Claude on them -> compare with the baseline
    gap found? -> refine the description (Rio: "consider program type")
                  or flag a limit (Rio: Claude guessed when data was missing)
until outputs match -> delegate, keep a human review where errors are costly
never matches -> this task should not be delegated
```

**How much does "it passed every test" prove? (derivation)** Suppose Claude fails each independent case with probability $p$. Passing all $n$ cases has probability $(1-p)^n$. For a 95% upper bound on $p$, find the $p$ where that event becomes unlikely:

$$(1-p)^n = 0.05 \;\Rightarrow\; n\ln(1-p) = \ln 0.05 \approx -3 \;\Rightarrow\; p \approx \frac{3}{n} \quad (\text{using } \ln(1-p)\approx -p)$$

This is the **rule of three**. Passing 10 out of 10 still allows an error rate of about **30%**. A small eval catches *systematic* gaps; it does not prove the model is reliable.

## In ML

**Evals are tests for LLM systems.** The lesson's 4-step loop is the small-scale version of production eval suites: a golden dataset, a scoring rubric, and regression runs after every prompt change.

**Human-in-the-loop.** "Keep human review where errors are costly" is the practical form of *Diligence* in the [[ai-fluency-framework]]. The eval tells you *where* to put that review.

**Statistics behind it.** Pass/fail over $n$ cases is a [[binomial-distribution]] experiment. The rule of three comes from the [[complementary-events]] logic of "no failures at all".

## Exercises

**Basic** — Claude wrote a 600-word update when you wanted a quick Slack message. Which row of the table applies? Rewrite the prompt.

**Intermediate** — Rio's first prompt missed the housing-assistance insight. Which prompt component from [[prompt-engineering-fundamentals]] was weak? Was "refine and re-run" the right move, or "start fresh"? Justify your choice.

**Advanced** — How many perfect test cases do you need to claim a 95% upper bound of 1% on the error rate? Why does the derivation fail if your test cases are near-duplicates (hint: independence)?
