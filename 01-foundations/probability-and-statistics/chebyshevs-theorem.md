---
tags:
  - status/seed
  - probability
related:
  - "[[measures-of-variation]]"
  - "[[normal-distribution]]"
  - "[[measures-of-center]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 3, §3-3."
---

> **TL;DR** — Chebyshev's theorem guarantees that at least $1-\frac{1}{K^2}$ of *any* dataset lies within $K$ standard deviations of the mean — a universal but loose bound that works when the [[normal-distribution|Empirical Rule]] can't.

---

## Intuition

The [[normal-distribution|Empirical Rule (68–95–99.7)]] is precise but *only valid for bell-shaped data*. What if your data is skewed, bimodal, or unknown? Chebyshev's theorem is the safety net: it holds for **every** distribution, no shape assumption. The price for that universality is weakness — it only gives a *lower bound* ("**at least** this fraction"), so it's conservative and often far from the truth. Think of it as the guarantee you can always fall back on when you know nothing about the shape.

## Mechanics

For any dataset (or distribution) and any constant $K > 1$:
$$\text{fraction within } K \text{ std. deviations of the mean} \;\geq\; 1 - \frac{1}{K^2}$$

| $K$ | Bound $1-1/K^2$ | Reads as |
|-----|-----------------|----------|
| 2 | $1-\tfrac14 = \tfrac34$ | **≥ 75%** of values within $\bar{x} \pm 2s$ |
| 3 | $1-\tfrac19 = \tfrac89$ | **≥ 89%** of values within $\bar{x} \pm 3s$ |

**Worked (Triola):** IQ scores, mean 100, [[measures-of-variation|s]] = 15.
- $K=2$: at least 75% fall in $100 \pm 30$ → **between 70 and 130**.
- $K=3$: at least 89% fall in $100 \pm 45$ → **between 55 and 145**.

**Empirical Rule vs. Chebyshev — same interval, different claims:**

| Within 2 SD | Empirical Rule (normal only) | Chebyshev (any shape) |
|-------------|------------------------------|------------------------|
| Claim | ≈ 95% | ≥ 75% |
| Kind | approximate equality | guaranteed lower bound |

Chebyshev's 75% is *consistent* with (and weaker than) the normal case's 95% — it just refuses to assume the bell. Note $K$ need not be an integer, and for $K \le 1$ the bound is vacuous (≥ 0).

```python
import numpy as np
def chebyshev_min_fraction(K):
    return 1 - 1/K**2 if K > 1 else 0.0
chebyshev_min_fraction(2)  # 0.75
chebyshev_min_fraction(3)  # 0.888...
```

## In ML

**Distribution-free guarantees.** When you can't assume normality (heavy-tailed losses, unknown feature distributions), Chebyshev-style bounds give worst-case coverage — the same reasoning behind concentration inequalities (Markov, Chebyshev, Hoeffding) used to bound generalization error and estimator deviation.

**Outlier thresholds without a shape assumption.** "More than $K$ SDs from the mean" is a common anomaly rule; Chebyshev tells you the *most* data that rule can flag, so it bounds false-positive rates even for non-normal features — safer than blindly applying the 3σ (Empirical) rule.

## Exercises

**Basic** — Using Chebyshev, at least what fraction of *any* dataset lies within 4 standard deviations of the mean?

**Intermediate** — A right-[[skewness|skewed]] income dataset has mean \$50k, s = \$20k. What does Chebyshev guarantee about the interval [\$10k, \$90k]? Why can't you use the Empirical Rule here?

**Advanced** — Explain why Chebyshev's bound is *tight* (achievable) yet usually loose in practice. What kind of distribution makes the ≥75%-within-2-SD bound an equality, and why does that never happen for normal data?
