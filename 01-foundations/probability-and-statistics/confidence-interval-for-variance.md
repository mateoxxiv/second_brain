---
tags:
  - status/seed
  - probability
related:
  - "[[chi-squared-distribution]]"
  - "[[confidence-interval]]"
  - "[[confidence-interval-for-mean]]"
  - "[[measures-of-variation]]"
  - "[[unbiased-and-biased-estimators]]"
  - "[[estimating-sigma-for-sample-size]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-5 (Intervalo de confianza para σ² y σ; ejemplo 2, voltajes domésticos)"
---

> **TL;DR** — A confidence interval for a population variance is $\frac{(n-1)s^2}{\chi^2_R} < \sigma^2 < \frac{(n-1)s^2}{\chi^2_L}$, and it is only valid if the population is normal, because the chi-squared law depends on normality.

---

## Intuition

Because $(n-1)s^2/\sigma^2$ has a known chi-squared distribution, we can put bounds on it that capture $\sigma^2$ with the chosen probability. Then we rearrange the inequality to isolate $\sigma^2$. The result is not "$s^2 \pm$ something", because the chi-squared law is skewed: the interval stretches further upward than downward.

## Mechanics

Pick two critical values from $\chi^2_{n-1}$ so that $\alpha/2$ lies in each tail:

- $\chi^2_L$: the value with area $\alpha/2$ to its left, i.e. $\chi^2_{1-\alpha/2}$ on the right-tail scale
- $\chi^2_R$: the value with area $\alpha/2$ to its right

Starting from $P(\chi^2_L \le \frac{(n-1)s^2}{\sigma^2} \le \chi^2_R) = 1-\alpha$, multiply through by $\sigma^2$ and divide by the critical values:

$$\frac{(n-1)s^2}{\chi^2_R} \;<\; \sigma^2 \;<\; \frac{(n-1)s^2}{\chi^2_L}$$

For $\sigma$, take square roots of both bounds. The interval is not symmetric around $s^2$, so it cannot be written as $s^2 \pm E$.

| Step | Action | Pitfall |
|------|--------|---------|
| 1 | Check the population is normal (histogram, normal quantile plot) | Mild skew breaks coverage for small n |
| 2 | Use $df = n-1$ | Do not reuse $n-1$ for other problems |
| 3 | Get $\chi^2_L$ and $\chi^2_R$ for the $\alpha/2$ tails | Tables A-4 are right-tail: left value uses $1-\alpha/2$ |
| 4 | Plug into the bounds | Keep extra decimals until the end |
| 5 | Take square roots for $\sigma$ | Round only at the end |

**Worked example (Triola §7-5, Ej. 2).** $n = 10$, $s = 0.15$, 95% confidence, $df = 9$, $\chi^2_R = 19.023$, $\chi^2_L = 2.700$:

$$\frac{9(0.15)^2}{19.023} = 0.010645 < \sigma^2 < 0.075000 = \frac{9(0.15)^2}{2.700}$$

Square roots give $0.10 < \sigma < 0.27$ volts.

```python
import numpy as np
from scipy import stats

s, n, alpha = 0.15, 10, 0.05
chi_r = stats.chi2.ppf(1 - alpha / 2, n - 1)   # 19.023
chi_l = stats.chi2.ppf(alpha / 2, n - 1)       # 2.700
lo, hi = (n - 1) * s**2 / chi_r, (n - 1) * s**2 / chi_l
print(np.sqrt([lo, hi]))                       # ~[0.103, 0.274]
```

## In ML

**Noise-scale uncertainty** — When a model's residual variance is estimated from n points, this interval states how far the true noise variance could plausibly be. It makes the estimate's uncertainty explicit.

**Comparing spread across conditions** — Two intervals for $\sigma$ can be compared informally to see whether one process is noisier. Triola warns that overlapping intervals do not prove equal variances, so this is a heuristic, not a test.

**Normality is the fragile assumption** — Unlike the mean interval, this one depends strongly on normality. ML data (heavy tails, outliers) often violates it, which makes the variance interval unreliable without checking first.

## Exercises

**Basic** — With $n = 25$, $s = 4$, and 90% confidence, find the 5% and 95% chi-squared points for $df = 24$ and compute the interval for $\sigma^2$.

**Intermediate** — Show that the interval for $\sigma^2$ is not symmetric around $s^2$ by computing its midpoint and comparing it with $s^2$ for the Triola example. Explain why the asymmetry comes from the skewed chi-squared distribution.

**Advanced** — Suppose the population is a $t$ distribution with 5 degrees of freedom instead of normal. Explain qualitatively what happens to the true coverage of this interval and why the sample-size rule of thumb cannot fix it.
