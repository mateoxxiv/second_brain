---
tags:
  - status/seed
  - probability
related:
  - "[[one-mean-z-test]]"
  - "[[student-t-distribution]]"
  - "[[test-statistic]]"
  - "[[hypothesis-test-decision-methods]]"
  - "[[p-value]]"
  - "[[confidence-interval-for-mean]]"
  - "[[standard-error-of-the-mean]]"
  - "[[chi-squared-distribution]]"
  - "[[assessing-normality]]"
  - "[[normal-quantile-plot]]"
  - "[[central-limit-theorem]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-5 (Prueba de una afirmación respecto de una media: σ desconocida; Ejemplos 1–5)"
---

> **TL;DR** — When σ is unknown (almost always), replace it with s: $t = (\bar x - \mu_0)/(s/\sqrt n)$ follows a Student t distribution with n − 1 degrees of freedom. This is the [[one-mean-z-test]] with heavier tails that pay for estimating σ.

---

## Intuition

The z-test divides by the *true* spread σ/√n. Here you only have an *estimate*, s/√n, and s itself wobbles from sample to sample. Sometimes s comes out too small, which inflates the statistic. The [[student-t-distribution]] builds in that extra risk: same bell shape, center 0, but fatter tails. So you need a bigger statistic to call a result unusual. With more data, s gets closer to σ and t gets closer to z.

## Mechanics

**Requirements**: (1) a simple random sample; (2) σ is unknown; (3) the population is normal **or** n > 30. For n ≤ 30, check the [[normal-quantile-plot]] and look for outliers ([[assessing-normality]]). The t-test is robust to mild non-normality, not to outliers or non-random samples.

**Why t, not z (the derivation)**: write the statistic as a ratio:
$$t=\frac{\bar x-\mu_0}{s/\sqrt n}=\frac{\overbrace{(\bar x-\mu_0)/(\sigma/\sqrt n)}^{Z\,\sim\,N(0,1)}}{\sqrt{\underbrace{(n-1)s^2/\sigma^2}_{V\,\sim\,\chi^2_{n-1}}\,/\,(n-1)}}$$
σ cancels, which is why you never need it. For **normal** data, Z and V are independent ([[chi-squared-distribution]]), and $Z/\sqrt{V/k}$ is by definition $t_k$. That independence is exactly what fails for skewed small samples.

| Property of $t_{n-1}$ | Value | Why it matters |
|---|---|---|
| Mean | 0 | same center as z |
| SD | $\sqrt{k/(k-2)} > 1$ (1.29 at df = 5, 1.03 at df = 39) | wider than z, so bigger critical values |
| As n → ∞ | → N(0, 1) | for large n, t ≈ z |

**Worked, boats** (n = 40, x̄ = 172.55, s = 26.33, H1: μ > 166.3, α = 0.05):
$t = 6.25/(26.33/\sqrt{40}) = 1.501$, df = 39.

| Method | Result | Decision |
|---|---|---|
| Traditional | $1.501 < t_{0.05,39} = 1.685$ | fail to reject H0 |
| P-value | software 0.0707. Table A-3: 1.501 falls between 1.304 and 1.685, so 0.05 < P < 0.10 | fail to reject H0 |
| 90% CI | $165.54 < \mu < 179.56$ contains 166.3 | can't support the claim |

As with the z-test for means, all three methods agree. Compare with §8-4, where the same data with σ = 26 gave P = 0.0643. Estimating σ costs a little evidence.

**Small sample, failed requirement (WTC lead)**: 5.40, 1.10, 0.42, 0.73, 0.48, 1.10 with H1: μ > 1.5. Mechanically t = 0.049 and P = 0.4814. But n = 6, the quantile plot isn't straight and 5.40 is an outlier (Shapiro–Wilk P ≈ 0.001). The **requirements fail**, so the conclusion is questionable. Use nonparametric or bootstrap methods instead (Ch. 13).

```python
import numpy as np
from scipy import stats
lead = np.array([5.40, 1.10, 0.42, 0.73, 0.48, 1.10])
print(stats.shapiro(lead).pvalue)                              # 0.0012 -> not normal: stop here
res = stats.ttest_1samp(lead, popmean=1.5, alternative="greater")
print(round(res.statistic, 3), round(res.pvalue, 4))           # 0.049 0.4814 (don't trust it)
```

## In ML

**Comparing models across seeds or folds**: with k = 5–10 runs, the mean improvement and its s give a t-statistic with df = k − 1. Using z here would overstate significance. Watch out: CV folds overlap, so their scores are correlated, which is why corrected resampled t-tests exist (Nadeau & Bengio).

**Regression coefficients**: every "t value" column in `statsmodels` output is this test, $\hat\beta/\widehat{SE}$, with df = n − p.

## Exercises

**Basic**: n = 16, x̄ = 52, s = 8, H1: μ ≠ 50, α = 0.05. Find t, df and the critical values, and decide.

**Intermediate**: Using Table A-3 only, bound the two-tailed P-value for t = 2.3 with df = 20. Then check it with `stats.t.sf`.

**Advanced**: Simulate 10,000 samples of n = 6 from an exponential population with μ = 1. Test H0: μ = 1 at α = 0.05 (two-tailed). What fraction rejects? Explain which step of the derivation breaks.
