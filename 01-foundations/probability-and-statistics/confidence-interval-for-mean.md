---
tags:
  - status/seed
  - probability
related:
  - "[[confidence-interval]]"
  - "[[confidence-interval-for-proportion]]"
  - "[[margin-of-error]]"
  - "[[point-estimate]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[sampling-distribution]]"
  - "[[sample-size-for-mean]]"
  - "[[interpreting-confidence-intervals]]"
  - "[[central-limit-theorem]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-3 (Intervalo de confianza para estimar μ con σ conocida; Ejemplo 1)"
---

> **TL;DR** — When σ is known, the confidence interval for a mean is x̄ ± z·σ/√n: the sample mean plus or minus the critical value times the standard error of the mean.

---

## Intuition

The sample mean x̄ is the best single guess for the population mean μ. But one number says nothing about accuracy. The interval adds that: how much x̄ would bounce from sample to sample, which is the standard error σ/√n. It is the same net idea as [[confidence-interval]], except the spread is σ itself instead of √(p̂q̂).

## Mechanics

Standardize the sample mean. When the requirements hold, this is approximately standard normal:

z = (x̄ − μ) / (σ/√n)

Keep the middle 1 − α of the z distribution, −z_{α/2} < z < z_{α/2}, and solve for μ:

x̄ − z_{α/2}·σ/√n < μ < x̄ + z_{α/2}·σ/√n

So E = z_{α/2}·σ/√n, and the interval is x̄ ± E.

**Requirements** (Triola §7-3):
1. The sample is a simple random sample.
2. σ is known. This is rare in practice; §7-4 handles unknown σ with the t distribution.
3. The population is normal, or n > 30. For 15 ≤ n ≤ 30 it is acceptable if the data have no outliers and look roughly bell-shaped. The rule is a guideline, not a hard cutoff.

**Worked (Triola Ejemplo 1, men's weights).** n = 40, x̄ = 172.55 lb, σ = 26 lb (from outside research), 95% confidence:

- z = 1.96, SE = 26/√40 ≈ 4.1110
- E = 1.96 × 4.1110 ≈ 8.0575
- Interval: 164.49 < μ < 180.61

**Rounding.** With the raw data, round the limits to one more decimal place than the data use. With only a summary (n, x̄, s), round to the same decimals as x̄.

```python
import math
from scipy.stats import norm
x_bar, sigma, n = 172.55, 26, 40
E = norm.ppf(0.975) * sigma / math.sqrt(n)            # ≈ 8.0575
print(round(x_bar - E, 2), round(x_bar + E, 2))       # 164.49 180.61
```

**Reading the interval.** The 95% describes the procedure, as in [[interpreting-confidence-intervals]]. The interval is a set of plausible values for μ. In Triola's example, the old standard of 166.3 lb falls inside it, so it is not ruled out. But the point estimate 172.55 sits well above it, which is why the authors call for more data. Plausible is not the same as likely. A value outside the interval is one that a two-sided test at the same α would reject.

| Change | Effect on width |
|--------|-----------------|
| Higher confidence (larger z) | wider |
| Larger n | narrower, by a factor of 1/√n |
| Larger σ | wider; the population spread caps the precision |

## In ML

**Average of a per-example measurement.** Mean per-example loss on a test set, or mean latency over requests, is a sample mean. If σ is trusted from a large earlier run, x̄ ± z·σ/√n gives the uncertainty of the average. Real pipelines rarely know σ, so they use s and a t-interval instead.

**Comparing model means.** Overlapping intervals for two models' mean losses do not prove they are equal, the same warning as for proportions.

## Exercises

**Basic** — x̄ = 50, σ = 10, n = 25, 95% confidence. Compute E and the interval. (Expected: E = 3.92, interval 46.08 to 53.92.)

**Intermediate** — Keep σ = 10 and x̄ = 50. By what factor must n grow to halve the width? Check with the 1/√n rule.

**Advanced** — Triola's rule needs a normal population or n > 30. Suppose n = 12 and the histogram is strongly skewed. Which requirement fails, and what would you do before trusting the interval?
