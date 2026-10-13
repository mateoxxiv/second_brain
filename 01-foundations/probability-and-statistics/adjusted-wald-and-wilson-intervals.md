---
tags:
  - status/seed
  - probability
related:
  - "[[confidence-interval-for-proportion]]"
  - "[[confidence-interval]]"
  - "[[normal-approximation-to-binomial]]"
  - "[[estimating-from-published-interval]]"
  - "[[margin-of-error]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-2 (Intervalos de confianza con mejor desempeño; ejemplo x = 10, n = 20)"
  - "Agresti & Coull, 'Approximation is Better than Exact for Interval Estimation of Binomial Proportions', American Statistician 52(2), 1998"
---

> **TL;DR** — The textbook interval can perform poorly for small n or extreme p; the adjusted Wald and Wilson intervals fix this, and their coverage is closer to the stated confidence level.

---

## Intuition

The textbook interval assumes the normal approximation is accurate, and that assumption fails when counts are small or p is near 0 or 1. Adjusted methods nudge the estimate toward 0.5 and change the interval's width so that its coverage is closer to the promised level. Think of it as adding a little humility to the estimate when the data are thin.

## Mechanics

**Textbook (Wald) interval.** p̂ ± z·√(p̂q̂/n). Its real coverage can fall well below the stated level when n is small or p̂ is near 0 or 1.

**Adjusted Wald interval.** Add 2 successes and 2 failures, so n increases by 4:

p̃ = (x + 2) / (n + 4), then p̃ ± z·√(p̃q̃/(n + 4))

**Wilson score interval.** Triola's formula:

(p̂ + z²/2n ± z·√(p̂q̂/n + z²/4n²)) / (1 + z²/n)

Its coverage is generally close to the nominal level, comparable to the adjusted Wald, but it is rarely taught in intro courses.

**Triola's example** (x = 10, n = 20, 95%):

| Method | Interval |
|---|---|
| Textbook (Wald) | 0.281 < p < 0.719 |
| Adjusted Wald | 0.300 < p < 0.700 |
| Wilson | 0.299 < p < 0.701 |

The adjusted and Wilson intervals are nearly identical here. The adjusted interval is also a bit narrower than the textbook one, because p̃ = 0.5 and the denominator is n + 4. The benefit is coverage, not width: width alone doesn't tell you whether an interval is reliable.

```python
import math
from scipy.stats import norm
x, n = 10, 20
z = norm.ppf(0.975)
# adjusted Wald: add 2 successes and 2 failures
p_t, n_t = (x + 2) / (n + 4), n + 4
E = z * math.sqrt(p_t * (1 - p_t) / n_t)
print(round(p_t - E, 3), round(p_t + E, 3))         # 0.300 0.700
# Wilson score
p_hat = x / n
center = (p_hat + z**2 / (2 * n)) / (1 + z**2 / n)
half = z * math.sqrt(p_hat * (1 - p_hat) / n + z**2 / (4 * n**2)) / (1 + z**2 / n)
print(round(center - half, 3), round(center + half, 3))   # 0.299 0.701
```

## In ML

**Small evaluation sets.** A model that gets 0 errors on 20 examples gets a textbook interval of exactly [0, 0], which claims perfect accuracy. The adjusted Wald interval gives a sensible upper bound instead.

**Rare events.** Conversion or failure rates near 0 need Wilson-type intervals to avoid negative lower bounds and overconfident claims.

**Reporting.** Name the interval method alongside the number. Two papers can report the same point estimate with different intervals.

## Exercises

**Basic** — Compute the adjusted Wald interval for x = 3, n = 10 at 95%.

**Intermediate** — For x = 0 and n = 20, the textbook interval is [0, 0]. Compute the adjusted Wald interval, then truncate its lower bound at 0. Explain why the textbook answer is misleading.

**Advanced** — Explain why adding 4 pseudo-observations pulls p̂ toward 0.5, and how that pull helps when p is near 0 or 1. Why does the Wilson formula approach the textbook one as n grows?
