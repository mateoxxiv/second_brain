---
tags:
  - status/seed
  - probability
related:
  - "[[sample-size-for-mean]]"
  - "[[measures-of-variation]]"
  - "[[confidence-interval-for-mean]]"
  - "[[sampling-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-3 (Cómo manejar σ desconocida al calcular el tamaño de la muestra; Ejemplo 2 y regla de error conservador)"
---

> **TL;DR** — Sample size needs σ before any data exist. Estimate it from the range, a pilot sample, or a prior study, and when in doubt, use the larger value.

---

## Intuition

The sample-size formula asks for the very quantity you are trying to measure: the population spread. You cannot know it before you sample, so you need a stand-in. Any stand-in is a guess, and the guess should err toward too much spread, because extra samples are a safe cost while too few samples are a silent failure.

## Mechanics

Triola gives three practical options:

1. **Range rule of thumb.** σ ≈ range / 4 ([[measures-of-variation]]). Triola cites Browne (2005): for a sample of 87 or more values from a normal population, range/4 is at least as large as s in at least 95% of cases. For small samples it can badly understate σ.
   *Example:* a pilot sample runs from 60 to 100, so range = 40 and σ ≈ 10.
2. **Pilot sample.** Start sampling, compute s from the first values, use it in the formula, and update as data arrive.
3. **Prior study.** Use σ from earlier research on a similar population. The men's-weight example used σ = 26 lb from outside sources.

**Borrowing from known scales.** IQ tests are designed with σ = 15, and statistics students are a more homogeneous group, so their true σ is probably smaller. Using 15 still works, but it overshoots n on purpose.

**The conservative rule.** Overestimating σ gives an n larger than needed, which wastes resources but still meets the target. Underestimating σ gives an n too small, so the margin falls short of E without any warning. Triola: "cualquier error siempre debe ser conservador."

```python
import numpy as np
pilot = np.array([20, 31, 25, 52, 38, 27, 44, 33])
sigma_range = (pilot.max() - pilot.min()) / 4     # 8.0, rough planning value
sigma_sample = pilot.std(ddof=1)                  # ≈ 10.5, from the pilot itself
```

## In ML

**Estimating a metric's noise before an eval.** Run a few hundred examples, measure the per-example standard deviation, and size the full evaluation from it. The final interval then uses the data you actually collected.

**Pilot = a rough prior.** Pilot-based planning is a sequential choice: once real data come in, recheck whether σ was right.

## Exercises

**Basic** — A pilot sample ranges from 20 to 52. Estimate σ with the range rule, then compute n for E = 2 at 95%. (Expected: σ ≈ 8, n = 62.)

**Intermediate** — Two prior studies report s = 6 and s = 9 for your population. Which do you use for planning, and why? Compute n for E = 1 at 95% with that value. (Expected: 312 using σ = 9.)

**Advanced** — The range rule can understate σ for small samples. Explain why, using a sample of n = 5 drawn from a normal population. Why does Triola require 87 or more values for the 95% statement?
