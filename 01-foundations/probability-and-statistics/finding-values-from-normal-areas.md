---
tags:
  - status/seed
  - probability
related:
  - "[[normal-probabilities-via-standardization]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[cdf-and-quantiles]]"
  - "[[percentiles]]"
  - "[[z-score]]"
  - "[[standard-normal-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-3 (Cálculo de valores de áreas conocidas, Ejemplos 3–4, Figura 6-16)"
---

> **TL;DR** — To find the **x** that cuts off a given area of $N(\mu,\sigma)$, find the z for that **left-cumulative** area, then undo the standardization: $x=\mu+z\sigma$. A z left of the mean must be negative.

---

## Intuition

The direction is reversed. Before, you were given a door height and asked what fraction of people fit. Now you are given a design goal ("fit 95% of men") and asked what door height achieves it. This is a **quantile** question: you walk along the $x$ axis until the area behind you reaches the target, and the place you stop is the answer.

## Mechanics

Solve Formula 6-2 for $x$: $\ z=\frac{x-\mu}{\sigma}\ \Rightarrow\ x=\mu+z\sigma$. So $x$ is the mean plus $z$ standard deviations, which is the quantile function $x=\mu+\sigma\,\Phi^{-1}(p)$ ([[cdf-and-quantiles]]).

**Procedure (area → x):**
1. Sketch the bell, write the given area in the correct region, and mark the unknown $x$.
2. Turn the area into a **left-cumulative** one ("top 1%" means left area 0.99), then find the closest area in the **body** of Table A-2 and read its z ([[critical-values-and-z-alpha]]).
3. Compute $x=\mu+z\sigma$.
4. Sanity-check against the sketch: is $x$ on the correct side of $\mu$?

**Triola's four warnings:** (1) z-scores are *distances* on the axis, areas are *regions* in the table body, so don't mix them up. (2) Pick the correct side: the top 10% lies on the right and the bottom 10% on the left. (3) A z in the left half is **negative**. (4) Areas are never negative.

| Triola example | Left area → z | $x=\mu+z\sigma$ |
|---|---|---|
| Door for 95% of men, $N(69.0,\,2.8)$ | $0.95\to1.645$ | $69.0+1.645(2.8)=73.6$ in |
| Bottom 3% of birth weights, $N(3420,\,495)$ | $0.03\to-1.88$ | $3420-1.88(495)=2489.4$ g |
| Top 1% of birth weights | $0.99\to2.33$ | $3420+2.33(495)=4573.35$ g |

With technology, the exact z values give 2489.0 g and 4571.5 g. The gap is caused only by rounding z to two decimals.

**Which direction? (Figure 6-16).** First ask: *is x known, or is the probability known?* If x is known, standardize and then look up the area ([[normal-probabilities-via-standardization]]). If the area is known, look up z and then compute $x=\mu+z\sigma$.

```python
from scipy.stats import norm
print(norm.ppf(0.95, loc=69.0, scale=2.8))   # 73.61 in
print(norm.ppf([0.03, 0.99], 3420, 495))     # [2489.0, 4571.5] g
```

## In ML

**Decision thresholds from a target rate.** "Flag the top 1% as anomalies" means threshold $=\mu+z_{0.01}\sigma$. You choose the false-alarm rate first and derive the cutoff, which is exactly the hospital committee's approach.

**Sampling and prediction intervals.** Inverse-transform sampling draws $p\sim U(0,1)$ and returns $\mu+\sigma\Phi^{-1}(p)$. A Gaussian regression head's 90% prediction interval is $\hat\mu\pm1.645\,\hat\sigma$, the same formula with a predicted $\mu$ and $\sigma$.

## Exercises

**Basic** — Men's heights $N(69.0,\,2.8)$: find $P_{10}$ and the height separating the tallest 2%.

**Intermediate** — Find the birth weights that bound the **middle 90%** of babies. Why are the two z-scores $\pm$ the same number, and why are the two weights equally far from 3420 g but not from 0?

**Advanced** — A designer needs a doorway that fits 99% of men **and** 99% of women, $N(63.7,\,2.9)$. Which constraint binds? Then: if heights keep rising by 0.1 in per decade, how many decades until the 80 in door fits only 99.9% of men?
