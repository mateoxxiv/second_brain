---
tags:
  - status/seed
  - probability
related:
  - "[[standard-normal-distribution]]"
  - "[[cdf-and-quantiles]]"
  - "[[percentiles]]"
  - "[[identifying-unusual-results]]"
  - "[[statistical-significance]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-2 (Cálculo de puntuaciones z de áreas conocidas, Ejemplos 6–8; Valores críticos; notación z_α)"
---

> **TL;DR** — Going from **area → z** is the inverse of the table lookup. $z_\alpha$ is the z with area $\alpha$ **to its right**, so you look up $1-\alpha$ in the left-cumulative table: $z_{0.025}=1.96$, $z_{0.05}=1.645$.

---

## Intuition

The [[standard-normal-distribution|standard normal]] table normally answers "given z, what area?" Half of real statistics asks the reverse: "which z cuts off the top 5%?" or "where do the unlikely values start?" That boundary z is a **critical value**. It separates the *likely* z-scores from the *unlikely* ones, and it is the fence that hypothesis tests and confidence intervals are built on.

## Mechanics

**Procedure (area → z):**
1. Sketch the bell and shade the region for the given probability. If it isn't a left-cumulative region, restate it as one.
2. Find the *closest* area in the **body** of Table A-2, then read off its z. If the area falls exactly between two table values, take the larger z. z-scores left of center are always negative.

This is exactly the inverse CDF $\Phi^{-1}$ ([[cdf-and-quantiles]]).

**Notation.** $z_\alpha$ = the z-score with area $\alpha$ **to its right**. The table is left-cumulative, so look up $1-\alpha$:

$$z_\alpha = \Phi^{-1}(1-\alpha)$$

| Triola example | Area used in table | z |
|---|---|---|
| $P_{95}$ (95th [[percentiles\|percentile]]) | 0.95 | 1.645 |
| Bottom 2.5% / top 2.5% | 0.025 / 0.975 | −1.96 / 1.96 |
| $z_{0.025}$ | 1 − 0.025 = 0.975 | 1.96 |

**Special cases** (memorize them, since they come up constantly):

| z | Area from left |
|---|---|
| ±1.645 | 0.9500 / 0.0500 |
| ±1.96 | 0.9750 / 0.0250 |
| ±2.575 | 0.9950 / 0.0050 |

By symmetry, the left-tail critical value is $-z_\alpha$. Two tails with total area $\alpha$ use $\pm z_{\alpha/2}$, which is why 95% becomes ±1.96, not ±1.645.

```python
from scipy.stats import norm
alpha = 0.025
print(norm.ppf(1 - alpha))  # 1.96   z_alpha = Φ⁻¹(1-α)
print(norm.isf(alpha))      # 1.96   same thing: inverse *survival* (right-tail) fn
print(norm.ppf(0.95))       # 1.645  P95
```

## In ML

**Confidence intervals and A/B tests.** "Accuracy 0.87 ± 1.96·SE" uses $z_{0.025}$. Declaring a variant significant at 5% means the test statistic is beyond the critical value ([[statistical-significance]]). The two-tail vs. one-tail choice changes the fence from 1.96 to 1.645.

**Anomaly thresholds.** Alerting on $|z| > z_{0.005}=2.575$ fixes the false-alarm rate at about 1% by construction, which is a principled version of the $|z|>2$ rule in [[identifying-unusual-results]].

## Exercises

**Basic** — Find $z_{0.10}$, $z_{0.01}$, and the z separating the bottom 10%.

**Intermediate** — Find the two z-scores that bound the middle 99%. Explain why they are $\pm z_{0.005}$ and not $\pm z_{0.01}$.

**Advanced** — The trap: a student writes $z_{0.05} = \Phi^{-1}(0.05) = -1.645$. What went wrong, and in which scipy call is it easy to make this mistake? Why does Triola quote 2.575 even though 2.576 is closer?
