---
tags:
  - status/seed
  - probability
related:
  - "[[statistical-significance]]"
  - "[[test-statistic]]"
  - "[[p-value]]"
  - "[[critical-region-and-significance-level]]"
  - "[[concluding-hypothesis-tests-in-plain-language]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Manejo de la afirmación; Figura 8-2)"
---

> **TL;DR** — The null hypothesis H0 is the "no effect" claim, always written with a fixed value and "="; the alternative H1 is what you want to show, written with ≠, < or >.

---

## Intuition

A hypothesis test works like a trial. H0 is the presumption of "nothing changed": you assume it is true and ask whether the data would be too strange to keep believing it. H1 is the accusation you are trying to support. You never prove H0; you only decide whether to reject it.

## Mechanics

Triola's three-step procedure (Figura 8-2):

1. Write the claim in symbols.
2. Write its negation: the form that must hold if the claim is false.
3. Of the two symbolic forms, the one **without** equality is H1. The other is H0, which contains "=".

Worked example from the text: the claim "the XSORT method raises the probability of a girl above 0.5" is $p > 0.5$. Its negation is $p \le 0.5$. The form without equality is $p > 0.5$, so H1: $p > 0.5$ and H0: $p = 0.5$.

| Claim | H0 | H1 | Tail |
|---|---|---|---|
| $p > 0.5$ | $p = 0.5$ | $p > 0.5$ | right |
| $p \ne 0.5$ | $p = 0.5$ | $p \ne 0.5$ | two |
| mean is at most 195 lb | $\mu = 195$ | $\mu > 195$ | right |

Rules the text states:
- H0 always uses a single fixed value. That lets you build one sampling distribution.
- Older texts write ≤ or ≥ in H0. Current practice (and this chapter) uses "=" only.
- The original claim can become H0, become H1, or match neither. In the 195 lb example the claim "at most 195" is neither; it is later restated as H0.
- To *support* a claim, put it in H1 and hope H0 is rejected. A claim that a parameter *equals* a value cannot be supported this way.

```python
# The claim goes in H1 only if it has no equality; H0 is the fixed-value form.
claim = "p > 0.5"
h1, h0 = claim, "p = 0.5"
print(f"H0: {h0}   H1: {h1}")
```

## In ML

**Baseline as the null** — "the new model beats the baseline" is H1: $\text{score}_{\text{new}} > \text{score}_{\text{base}}$. H0 is "no difference", the same logic used in [[statistical-significance]] when a result could be chance.

**You cannot prove two models equal** — a non-rejected H0 ("no difference") is not evidence of equivalence. Equivalence needs a different test design, which Triola does not cover.

## Exercises

**Basic** — Write H0 and H1 for the claim "the average commute is more than 30 minutes."

**Intermediate** — The claim is "fewer than 10% of emails are spam" ($p < 0.10$). Write H0 and H1. Which one would you have to reject to support the claim?

**Advanced** — Triola says you cannot support a claim that a parameter *equals* a specific value. Explain why, and say what you could test instead.
