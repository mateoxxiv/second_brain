---
tags:
  - status/seed
  - probability
related:
  - "[[confidence-interval]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[point-estimate]]"
  - "[[sampling-error-vs-nonsampling-error]]"
  - "[[standard-normal-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-2 (Margen de error, Fórmula 7-1; Ejemplos 3–4)"
---

> **TL;DR** — The margin of error E is the largest difference you'd probably see between the sample proportion and the true p: E = z_{α/2} · √(p̂q̂/n), and the confidence interval is p̂ ± E.

---

## Intuition

A poll reports 70%, and the news says "with a margin of error of 2 points." That number is E: how far the sample result could plausibly be from the truth, at the stated confidence. It is the half-width of the confidence interval, so the interval is the estimate with E added and subtracted. A bigger E means a wider net, and the margin shrinks as the sample grows.

## Mechanics

**Formula 7-1:**

E = z_{α/2} · √(p̂q̂ / n)

Each part has a job:

| Part | Role |
|------|------|
| z_{α/2} | sets the confidence level; 1.96 for 95% ([[critical-values-and-z-alpha]]) |
| √(p̂q̂/n) | the standard error of p̂ ([[point-estimate]]) |
| E | the product of the two: the half-width of the interval |

**Triola's Ejemplo 3.** With n = 1501, p̂ = 0.70, and z = 1.96:

E = 1.96 · √(0.70 · 0.30 / 1501) ≈ 0.0232

The margin is about 2.3 percentage points. This is the 2 points quoted in the news, which rounds it down.

**Recovering E from a published interval.** If you know the limits, the midpoint is p̂, and E is half the width:

E = (upper − lower) / 2

**Relationships.** E is proportional to 1/√n. Halving E requires four times the sample. E is largest when p̂ = 0.5, because p̂q̂ is largest there.

```python
import math
from scipy.stats import norm
p_hat, n = 0.70, 1501
E = norm.ppf(0.975) * math.sqrt(p_hat * (1 - p_hat) / n)   # ≈ 0.0232
print(round(100 * E, 1), "percentage points")               # 2.3
```

**What E does not cover.** E accounts for random sampling error only. Biased samples, bad questions, and recording errors are nonsampling errors, and E can't measure them ([[sampling-error-vs-nonsampling-error]]).

## In ML

**Reporting an uncertainty on a metric.** A test accuracy of 0.92 with E ≈ 0.01 is a claim that the test set's noise is about one point. Smaller test sets make E large, so differences of a point or two between models may be meaningless.

**Choosing the test set size.** E tells you the size you need: to pin accuracy to ±1 point at 95%, use the sample-size formula with E = 0.01 ([[sample-size-for-proportion]] is planned).

**Ignoring the bias term.** A model evaluated on a skewed test set gets an E that looks tight, but the error can be far larger than E. The margin only covers the random part.

## Exercises

**Basic** — A sample of n = 400 gives p̂ = 0.30. Compute E at 95% and report it in percentage points.

**Intermediate** — Starting from n = 400, how many people do you need to halve E? Explain using the 1/√n relationship.

**Advanced** — For fixed n, why is E the largest when p̂ = 0.5? Compute E at p̂ = 0.5 and p̂ = 0.9 for n = 400 and explain why a conservative estimate uses p̂ = 0.5.
