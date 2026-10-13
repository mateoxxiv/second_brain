---
tags:
  - status/seed
  - probability
related:
  - "[[margin-of-error]]"
  - "[[confidence-interval-for-proportion]]"
  - "[[point-estimate]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-2 (Cálculo del tamaño de la muestra; Fórmulas 7-2 y 7-3; Ejemplo 4)"
---

> **TL;DR** — Solve the margin-of-error formula for n: n = z²·p̂q̂ / E², or n = 0.25·z² / E² when p is unknown, then round up.

---

## Intuition

Before collecting data, you choose the precision you need. A tighter margin requires more people, and the margin shrinks with the square of the sample size. This is the planning side of the margin of error: you decide E first, then find the n that delivers it.

## Mechanics

Start from E = z · √(pq / n) and solve for n:

- **If p is roughly known** (from a pilot, past data, or expert judgment), use **Formula 7-2**:

  n = z² · p̂ · q̂ / E²

- **If p is unknown**, use **Formula 7-3**, with p = q = 0.5 in the worst case:

  n = 0.25 · z² / E²

  The product pq is largest at 0.5, where it equals 0.25. Using 0.25 guarantees the margin is no larger than E.

**Rounding rule.** Always round n up to the next whole number, because a smaller sample would miss the margin.

**Triola's Ejemplo 4** (E = 0.03, 95% confidence, z = 1.96):

- With p̂ = 0.73 from earlier data: n = 1.96² · 0.73 · 0.27 / 0.03² ≈ 841.3, so **842**.
- With no prior information: n = 1.96² · 0.25 / 0.03² ≈ 1067.1, so **1068**.

Without prior information you need more people, because the worst-case 0.25 is larger than a realistic pq.

**Common errors.** Use E = 0.03 for "three percentage points," not E = 3. Use z = 1.96 for 95%, not 0.95 or 0.05.

**Population size.** The formulas don't depend on the population size N, as long as the population is large relative to the sample. Triola notes that a large sample drawn without replacement from a small population needs a finite-population correction (exercise 49 of the section).

```python
import math
from scipy.stats import norm
z = norm.ppf(0.975)                              # 1.96
E = 0.03
n_known = math.ceil(z**2 * 0.73 * 0.27 / E**2)   # 842
n_unknown = math.ceil(z**2 * 0.25 / E**2)        # 1068
```

## In ML

**Test set size.** To estimate accuracy to within ±1 point at 95% with no prior guess, use E = 0.01 and p = 0.5: n = 0.25 · 1.96² / 0.01² ≈ 9604. A test set smaller than this can't resolve a one-point difference in accuracy.

**Labeling budgets.** Before hiring annotators to measure how often a model fails, decide the precision you need. The formula tells you how many labeled examples that precision costs.

**Rare events.** When the true rate is small, pq is small and fewer samples are needed for the same E. But the normal approximation may then fail, so check np ≥ 5 afterward.

## Exercises

**Basic** — You want E = 0.05 at 95% with no prior information. Compute n using Formula 7-3.

**Intermediate** — Use 99% confidence, E = 0.04, and a prior estimate p̂ = 0.20. Compute n with Formula 7-2. Round up.

**Advanced** — Explain why p = 0.5 is the worst case for pq, and why choosing it guarantees the margin is no larger than E. How does the answer change if the true p is 0.05?
