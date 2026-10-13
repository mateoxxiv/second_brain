---
tags:
  - status/seed
  - probability
related:
  - "[[confidence-interval]]"
  - "[[margin-of-error]]"
  - "[[point-estimate]]"
  - "[[adjusted-wald-and-wilson-intervals]]"
  - "[[confidence-interval-for-proportion]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-2 (Cálculo de la estimación puntual y de E a partir de un intervalo de confianza; ejemplo con Dale et al., JAMA)"
---

> **TL;DR** — Given a published interval with limits L and U, the point estimate is the midpoint p̂ = (L + U) / 2, and the margin of error is half the width E = (U − L) / 2.

---

## Intuition

Papers often report only the interval, not the raw counts. The interval already contains the answer: its center is the estimate, and its half-width is the margin. Recovering these two numbers lets you check a claim, compare studies, or reconstruct the sample size.

## Mechanics

Given limits L < p < U:

- Point estimate: p̂ = (L + U) / 2
- Margin of error: E = (U − L) / 2

These are exact for the textbook interval, because it is symmetric around p̂. Any published interval is only as precise as its rounding.

**Triola's example** (Dale et al., JAMA; paraphrased from Triola's Spanish text): 70% of 71 subjects abstained from smoking for 8 weeks (95% CI, 58% to 81%).

- p̂ = (0.81 + 0.58) / 2 = 0.695
- E = (0.81 − 0.58) / 2 = 0.115

The reported 70% is close to the midpoint 69.5%. The gap is rounding.

**Caution.** The midpoint rule assumes a symmetric interval around p̂. Intervals such as the Wilson score interval are not symmetric around p̂, so the midpoint is only approximate for them ([[adjusted-wald-and-wilson-intervals]]).

```python
L, U = 0.58, 0.81
p_hat = (U + L) / 2     # 0.695
E = (U - L) / 2         # 0.115
```

## In ML

**Comparing reported metrics.** Papers often report "accuracy 0.87 (95% CI 0.85–0.89)." Recovering p̂ and E tells you the half-width, which you can use to decide whether a competitor's reported gain is larger than the noise.

**Reverse-engineering the sample size.** Solve E = z·√(p̂q̂/n) for n, using the recovered p̂ and E. If the implied n is far from the stated sample size, the interval was probably built with a different method, such as a Wilson or exact interval.

**Meta-analysis.** Combining studies needs each study's point estimate and standard error. The interval gives both, provided you know the method.

## Exercises

**Basic** — A published interval reads 0.42 < p < 0.58. Find p̂ and E.

**Intermediate** — The JAMA example reports 58% to 81% from 71 subjects. Compute the sample size implied by the standard formula using p̂ = 0.695 and E = 0.115, and compare it with 71. What might explain the gap?

**Advanced** — Explain why the midpoint rule gives an exact p̂ for the Wald interval but only an approximate one for the Wilson interval. What property of the interval causes the difference?
