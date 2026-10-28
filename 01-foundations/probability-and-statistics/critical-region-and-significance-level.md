---
tags:
  - status/seed
  - probability
related:
  - "[[critical-values-and-z-alpha]]"
  - "[[test-statistic]]"
  - "[[one-tailed-vs-two-tailed-tests]]"
  - "[[type-i-and-type-ii-errors]]"
  - "[[p-value]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Herramientas para evaluar el estadístico de prueba; Ejemplos 5–6; Figura 8-3, 8-4)"
---

> **TL;DR** — The critical region is the set of test-statistic values that lead you to reject H0; the significance level α is the probability of landing in that region when H0 is true.

---

## Intuition

Before you see the data, decide the cutoff: "reject only if a result this extreme would occur less than 5% of the time under H0." α is the false-alarm rate you accept in advance. The critical value is the boundary between the rejection region and the rest of the distribution.

## Mechanics

- **Region position** depends on H1 (see [[one-tailed-vs-two-tailed-tests]]). A right-tailed H1 puts the whole α on the right.
- **Common α**: 0.05 (the most common), 0.01, 0.10. Triola's rule: choose α from the cost of a type I error (see [[type-i-and-type-ii-errors]]), and lower it when wrongly rejecting H0 is serious.
- **Critical values** from the normal table ([[critical-values-and-z-alpha]]):

| H1 | Region | Critical value at α = 0.05 |
|---|---|---|
| $p > 0.5$ | right tail, area 0.05 | $z = 1.645$ |
| $p < 0.5$ | left tail, area 0.05 | $z = -1.645$ |
| $p \ne 0.5$ | two tails, area 0.025 each | $z = \pm 1.96$ |

- **Decision**: if the test statistic falls in the region, reject H0. Otherwise, do not reject.

```python
from scipy.stats import norm

alpha = 0.05
print(round(norm.ppf(1 - alpha), 3))       # right-tail critical value: 1.645
print(round(norm.ppf(1 - alpha / 2), 2))   # two-tailed critical value: 1.96
```

For XSORT ($z = 3.21$), $3.21 > 1.645$, so the statistic lies in the right-tail region and H0 is rejected.

## In ML

**Alert thresholds** — a monitoring rule that fires when a metric leaves a band is a critical region. Its width sets the false-alarm rate, exactly like α. Connects to the $|z| > 2$ outlier rule in [[identifying-unusual-results]].

**Choosing α by cost** — a false positive in fraud blocking costs something different from a false positive in a medical screen. The same reasoning sets α.

## Exercises

**Basic** — Right-tailed test at α = 0.01. Find the critical value of $z$.

**Intermediate** — Two-tailed test at α = 0.10. Find both critical values. What is the probability of rejecting a true H0?

**Advanced** — For a fixed sample size, explain why lowering α widens the non-rejection region, and what that does to β.
