---
tags:
  - status/seed
  - probability
related:
  - "[[chi-squared-distribution]]"
  - "[[confidence-interval-for-variance]]"
  - "[[one-mean-t-test]]"
  - "[[one-mean-z-test]]"
  - "[[test-statistic]]"
  - "[[hypothesis-test-decision-methods]]"
  - "[[p-value]]"
  - "[[one-tailed-vs-two-tailed-tests]]"
  - "[[assessing-normality]]"
  - "[[measures-of-variation]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-6 (Prueba de una afirmación respecto de una desviación estándar o de una varianza; Ejemplos 1–3, Tabla A-4)"
---

> **TL;DR** — To test a claim about σ or σ², use $\chi^2 = (n-1)s^2/\sigma_0^2$ with df = n − 1. It works only if the population is truly normal: unlike the t-test, it is **not** robust.

---

## Intuition

Means tell you if a process is on target. Variation tells you if it is *consistent*. A coin press can average exactly 2.500 g and still make coins that jam vending machines because the weights are spread too widely. So quality control tests the spread too.

The question is: is the observed $s^2$ unusually far from the claimed $\sigma_0^2$? The ratio $s^2/\sigma_0^2$ should be about 1 if H0 is true. Scaling it by $n-1$ turns it into a quantity with a known law, the [[chi-squared-distribution]]. A value much smaller than $n-1$ means "less spread than claimed", and a value much larger means "more spread".

## Mechanics

**Requirements**: (1) a simple random sample; (2) a **normal** population. This is much stricter than for means. Large n does not save you, because there is no CLT for $s^2$ that removes the dependence on the population's shape.

**Statistic**: under H0, $\chi^2 = (n-1)s^2/\sigma_0^2 \sim \chi^2_{n-1}$. This is the same pivot as in [[confidence-interval-for-variance]], with $\sigma$ replaced by the claimed $\sigma_0$. A claim about σ and a claim about σ² are the same test, since squaring is monotone for positive values.

| Tail (α = 0.05) | Table A-4 column (area to the **right**) | Note |
|---|---|---|
| Right, H1: σ > σ0 | 0.05 | one critical value |
| Left, H1: σ < σ0 | 0.95 | not 0.05: the table is right-tailed |
| Two, H1: σ ≠ σ0 | 0.975 and 0.025 | two **different positive** values, not ±c |

**Two-tailed P-value**: double the smaller tail, $P = \min\{1,\ 2\min[P(\chi^2_{n-1} \le x),\ P(\chi^2_{n-1} \ge x)]\}$, i.e. `2 * min(cdf, sf)`. The smaller tail is the side where the statistic falls: left if $s^2 < \sigma_0^2$, right if $s^2 > \sigma_0^2$. Triola leaves this implicit; it is the §8-2 doubling rule from [[p-value]]. Using `sf` alone halves P and overstates the evidence (tar exercise: 0.1249 instead of 0.2498).

**Worked, pennies** (n = 37, s = 0.01648 g, H1: σ < 0.0230 g, α = 0.05; normality checked with a histogram and a [[normal-quantile-plot]]):
$\chi^2 = 36(0.01648)^2/0.0230^2 = 18.483$, df = 36.

| Method | Result | Decision |
|---|---|---|
| Traditional | $18.483 < \chi^2_L = 23.269$ (left region) | reject H0 |
| P-value | left-tail area 0.0069 < 0.05 | reject H0 |
| 90% CI (1 − 2α, left-tailed) | $0.01385 < \sigma < 0.02050$, all below 0.0230 | support the claim |

Conclusion: there is enough evidence that σ < 0.0230 g, so the process meets the spec.

```python
from scipy import stats
n, s, s0 = 37, 0.01648, 0.0230
chi2 = (n - 1) * s**2 / s0**2
print(round(chi2, 3), round(stats.chi2.ppf(0.05, n - 1), 3))  # 18.483 23.269
print(round(stats.chi2.cdf(chi2, n - 1), 4))                  # 0.0069 (left tail)
# two-tailed H1 (sigma != sigma0): double the smaller tail
p_two = min(1, 2 * min(stats.chi2.cdf(chi2, n - 1), stats.chi2.sf(chi2, n - 1)))
# Non-robustness: exponential data (true sigma = 1), n = 20, two-tailed alpha = 0.05
import numpy as np
v = 19 * np.random.default_rng(0).exponential(1, (20000, 20)).var(axis=1, ddof=1)
print(((v < stats.chi2.ppf(.025, 19)) | (v > stats.chi2.ppf(.975, 19))).mean())  # ~0.27, not 0.05
```

## In ML

**Noise checks**: the fit of a regression with assumed noise σ0 can be checked by testing whether the residual variance matches it. The same idea, summing squared standardized residuals, gives the chi-squared goodness-of-fit statistic in physics and Kalman-filter consistency tests (NIS/NEES).

**Model stability**: "the new training pipeline has run-to-run SD below 0.5 points" is a left-tailed σ claim. But metric distributions across seeds are often skewed, so use a bootstrap or Levene-type test rather than trusting this χ² P-value.

## Exercises

**Basic**: n = 10, s = 2.8, H1: σ ≠ 2.0, α = 0.05. Compute χ², find both critical values from Table A-4 (df = 9), and decide.

**Intermediate**: Explain why the left-tailed critical value uses the 0.95 column. Then show that rejecting H0 in the pennies test is equivalent to $\sigma_0$ lying above the upper bound of the 90% CI.

**Advanced**: Using the formula $\mathrm{Var}(s^2) = \sigma^4\left(\tfrac{2}{n-1} + \tfrac{\kappa}{n}\right)$, with κ the excess kurtosis, explain why the simulation above rejects about 27% of the time, and why increasing n does not fix it.
