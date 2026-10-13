---
tags:
  - status/seed
  - probability
related:
  - "[[point-estimate]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[sampling-distribution]]"
  - "[[standard-normal-distribution]]"
  - "[[statistical-significance]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-2 (Intervalo de confianza; Ejemplo 3)"
---

> **TL;DR** — A confidence interval is a range built from the sample that contains the population parameter in a stated fraction (1 − α) of repeated samples.

---

## Intuition

A point estimate is an arrow: one value, no sense of accuracy. A confidence interval is a net thrown around that arrow. The population value is a fixed bullseye. The net moves with each sample, and a 95% net catches the bullseye in about 95 of every 100 throws. Each individual net either catches it or misses; the 95% describes the throwing method, not any one net.

## Mechanics

The general form is **estimate ± critical value × standard error**. For a proportion:

p̂ ± z_{α/2} · √(p̂q̂ / n)

| Piece | Role |
|-------|------|
| p̂ | the point estimate, the center of the interval |
| z_{α/2} | the critical value; sets the confidence level (1.96 for 95%) |
| √(p̂q̂/n) | the standard error of p̂ |
| z_{α/2} · SE | the margin of error E |

**Why it works.** When np and nq are at least 5, the sampling distribution of p̂ is approximately normal with mean p and SD √(pq/n). So

P(−z_{α/2} < (p̂ − p)/SE < z_{α/2}) = 1 − α.

Rearranging the inside gives p̂ − z·SE < p < p̂ + z·SE. The true SE uses the unknown p, so we substitute p̂. That substitution is the approximation behind the formula.

**Worked (Triola Ejemplo 3).** p̂ = 0.70, n = 1501, z = 1.96: E ≈ 0.0232, so 0.677 < p < 0.723.

```python
import math
from scipy.stats import norm
p_hat, n, conf = 0.70, 1501, 0.95
z = norm.ppf(1 - (1 - conf) / 2)              # 1.96
E = z * math.sqrt(p_hat * (1 - p_hat) / n)    # ≈ 0.0232
print(p_hat - E, p_hat + E)                   # 0.677, 0.723
```

| Change | Effect on width |
|--------|-----------------|
| Higher confidence (larger z) | wider |
| Larger n | narrower, by a factor of 1/√n |
| p̂ closer to 0.5 | wider, because pq is largest there |

## In ML

**Error bars on metrics.** Reporting test accuracy as 0.92 ± 0.02 says how much a difference between two models can be trusted. Without the interval, a 1% gain looks like progress even when it's noise.

**Comparing models.** Two intervals that overlap don't prove the models are equal, and two that don't overlap don't prove they differ. Compare the interval for the difference instead.

**Bootstrap intervals.** When no formula fits (AUC, F1, a custom metric), resample the test set and take percentiles of the results. The idea is the same: a range that captures the parameter at a chosen rate.

## Exercises

**Basic** — A sample of n = 400 finds p̂ = 0.30. Build the 95% interval.

**Intermediate** — For the same data, compare the 90% and 99% intervals. By what factor does the width change between them? Use z values 1.645 and 2.575.

**Advanced** — The interval is random; p is not. Explain what it means that a 95% interval "contains p" in a given case, and why the normal approximation is only trustworthy when np and nq are at least 5.
