---
tags:
  - status/seed
  - probability
related:
  - "[[sample-size-for-proportion]]"
  - "[[confidence-interval-for-mean]]"
  - "[[margin-of-error]]"
  - "[[estimating-sigma-for-sample-size]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[multiplication-rule]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-3 (Determinación del tamaño de la muestra; Fórmula 7-4; Ejemplo 2)"
---

> **TL;DR** — Solve E = z·σ/√n for n: n = (z·σ/E)², then round up to the next whole number.

---

## Intuition

Before collecting data, you choose the precision you need, and precision is expensive. The margin shrinks with the square root of n, so getting it twice as tight costs four times the sample. This is the mean version of [[sample-size-for-proportion]]: σ replaces √(pq), so the unknown is the population spread instead of p.

## Mechanics

Start from E = z·σ/√n, multiply both sides by √n, divide by E, and square:

n = (z_{α/2} · σ / E)²    (Formula 7-4)

**Rounding.** Always round n up. A smaller sample would leave the margin too large.

**Population size.** The formula does not involve N. If n is a large fraction of a small population sampled without replacement, a finite-population correction applies (Triola's exercise 38). The 5% guideline from [[multiplication-rule]] is a common check.

**Worked (Triola Ejemplo 2, IQ scores).** Estimate the mean IQ of statistics students to within E = 3 points, 95% confidence, with σ = 15:

n = (1.96 · 15 / 3)² = 9.8² = 96.04, so **97** students.

| Target E | n (95%, σ = 15) |
|----------|-----------------|
| 3 | 97 |
| 1.5 | 385 |
| 0.75 | 1537 |

Halving E from 3 to 1.5 raised n from 97 to 385, about four times. That is the square-root law in action.

```python
import math
from scipy.stats import norm
z, sigma = norm.ppf(0.975), 15
for E in (3, 1.5, 0.75):
    print(E, math.ceil((z * sigma / E) ** 2))   # 3 97 / 1.5 385 / 0.75 1537
```

**Trade-off.** A larger sample costs time and money, and a smaller one gives a weak estimate. The target E is the balance point, chosen before data collection.

## In ML

**Test-set sizing.** To estimate a mean per-example loss within ±0.01 at 95%, with a per-example standard deviation of σ = 0.5: n = (1.96 · 0.5 / 0.01)² = 9604 examples.

**Pilot first.** When σ is unknown, a small pilot run gives an estimate for planning. See [[estimating-sigma-for-sample-size]].

## Exercises

**Basic** — σ = 12, E = 2, 95% confidence. Compute n. (Expected: 139.)

**Intermediate** — You want E = 0.5 at 99% confidence (z = 2.575) for a quantity with σ = 4. Compute n and round up. (Expected: 425.)

**Advanced** — You plan with σ = 15 and E = 3, so n = 97. The true σ turns out to be 20. What margin do you actually get with n = 97? Explain why an underestimated σ is the dangerous error.
