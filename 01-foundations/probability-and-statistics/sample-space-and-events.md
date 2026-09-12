---
tags:
  - status/seed
  - probability
related:
  - "[[three-methods-of-assigning-probability]]"
  - "[[probability-fundamentals]]"
  - "[[complementary-events]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-2 (Ejemplo 1)."
---

> **TL;DR** — A **procedure** produces **outcomes**; an **event** is any set of outcomes, a **simple event** is one that can't be broken down further, and the **sample space** is the set of *all* simple events.

---

## Intuition

Before you can compute a probability you must answer one question: *what can possibly happen?* That complete inventory of indivisible results is the **sample space**. Everything else — every event you'll ever ask about — is just some subset of it. Get the sample space wrong and every probability built on it is wrong, so this is the real first step of any probability problem.

The subtle trap is **granularity**. With three births, is "2 girls and 1 boy" a single result? No — it hides three distinct orderings (ffm, fmf, mff), so it's *compound*, not simple. But the ordered result `ffm` itself *is* simple: you cannot decompose it into "f, f, m" because those aren't the outcomes of *three* births. A simple event is defined by the procedure's finest resolution, not by whatever loose description you started with.

## Mechanics

| Term | Definition |
|------|------------|
| **Procedure** | An action producing results (roll a die, record 3 births, answer a question) |
| **Outcome / event** | Any collection of results of a procedure |
| **Simple event** | An outcome that cannot be broken into simpler components |
| **Sample space (S)** | The set of *all* simple events |

**Worked — three births** (`f`=girl, `m`=boy). The sample space has exactly 8 simple events:

```
S = {fff, ffm, fmf, fmm, mff, mfm, mmf, mmm}
```

"2 girls and 1 boy" = {ffm, fmf, mff} — a *compound* event, three simple events. Each of the 8 strings, e.g. `ffm`, is simple: no finer breakdown exists for the procedure "observe 3 births."

**Notation:** $P$ = a probability; $A, B, C$ = specific events; $P(A)$ = the probability event $A$ occurs.

## In ML

**The sample space is the support of a distribution.** When you write a random variable's distribution, its set of possible values *is* the sample space. A classifier's label set {spam, ham}, a die's {1..6}, a language model's vocabulary — each is a sample space, and the model just assigns probability mass across it.

**Correct enumeration underlies combinatorics.** Counting the simple events in $S$ is exactly what the [[three-methods-of-assigning-probability|classical method]] needs ($s/n$). Miscounting $S$ — the single most common beginner error — silently corrupts binomial coefficients, permutation counts, and any "how many ways?" reasoning downstream.

## Exercises

**Basic** — Write the full sample space for tossing a coin twice. How many simple events? Which simple events make up the event "exactly one head"?

**Intermediate** — For rolling two distinguishable dice, how many simple events are in $S$? Is "the sum is 7" a simple event? List the simple events it contains.

**Advanced** — A drawer has 3 socks: red, green, blue. You draw two *without* replacement. Argue why order does or doesn't matter, and give the sample space under each convention. How does the choice change the count $n$ used in the classical method?
