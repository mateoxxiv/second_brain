---
tags:
  - status/seed
  - probability
related:
  - "[[critical-region-and-significance-level]]"
  - "[[p-value]]"
  - "[[hypothesis-test-decision-methods]]"
  - "[[multiple-testing-problem]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Tipos de pruebas de hipótesis; Figura 8-6; Figura 8-4)"
---

> **TL;DR** — The sign in H1 decides where the critical region sits: ≠ gives two tails, < gives the left tail, > gives the right tail.

---

## Intuition

The H1 sign points at the disagreement you care about. Only results in that direction count as evidence against H0. A result in the opposite direction, however extreme, does not support H1.

## Mechanics

| H1 sign | Test type | Where the region sits | Area in each region (α = 0.05) |
|---|---|---|---|
| ≠ | two-tailed | both tails | 0.025 each |
| < | left-tailed | left tail | 0.05 |
| > | right-tailed | right tail | 0.05 |

Same data, different tests. For $z = 1.80$:
- Right-tailed, $P = 0.036$: reject at α = 0.05.
- Two-tailed, $P = 0.072$: do not reject at α = 0.05.

Choose the direction **before** collecting data. Picking the direction after seeing the data so that $P$ falls below α is a form of p-hacking, and it inflates false positives (see [[multiple-testing-problem]]).

Confidence-interval link (Table 8-2): for the same α, a two-tailed test uses a $1-\alpha$ interval, while a one-tailed test uses a $1-2\alpha$ interval. For α = 0.05 that is 95% and 90%. See [[hypothesis-test-decision-methods]].

## In ML

**Two-sided A/B tests** — "variant B differs from A" is two-sided. "B is better" is one-sided. A change that hurts a metric matters too, so a two-sided test is the usual default when you ship on both outcomes.

**Chosen after the fact** — testing only the direction that produces significance inflates the false-positive rate.

## Exercises

**Basic** — For H1 with $p > 0.5$, $p < 0.5$, and $p \ne 0.5$, say where the critical region is.

**Intermediate** — With $z = 1.80$ and α = 0.05, decide with both a one-tailed and a two-tailed test. Compare the two P-values.

**Advanced** — Argue when a one-tailed test is justified. Consider: what would you do if the result came out in the opposite direction?
