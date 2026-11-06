---
tags:
  - status/seed
  - probability
related:
  - "[[sampling-distribution]]"
  - "[[standard-error-of-the-mean]]"
  - "[[probabilities-for-sample-means]]"
  - "[[normal-distribution]]"
  - "[[law-of-large-numbers]]"
  - "[[skewness]]"
  - "[[normal-approximation-to-binomial]]"
  - "[[confidence-interval-for-mean]]"
  - "[[one-mean-z-test]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-5 (El teorema del límite central)"
  - "Wasserman, All of Statistics, §5.4"
---

> **TL;DR** — Take samples of size n from **any** population with mean μ and finite SD σ: as n grows, the distribution of the sample mean x̄ approaches a normal curve with mean μ and SD σ/√n. The CLT fixes the shape of **x̄**, not of the data.

---

## Intuition

One die roll is flat (uniform). The average of two rolls already peaks at 3.5, because extreme averages need *every* roll to be extreme, while middle averages can be reached in many ways. Add more rolls and the lumps and skews average out. What remains is the bell curve. This is why every z or t interval and test in Ch. 7–8 can use normal tables even when the raw data are skewed. Those methods are about x̄, and x̄ is (approximately) normal.

The [[law-of-large-numbers]] says *where* x̄ goes (to μ). The CLT says *how it wobbles* on the way: a normal wobble whose width shrinks like 1/√n.

## Mechanics

**Statement.** If $X_1,\dots,X_n$ are independent draws from a population with mean μ and finite variance σ², then
$$\frac{\bar x - \mu}{\sigma/\sqrt n} \;\xrightarrow{\;d\;}\; N(0,1) \quad\text{as } n\to\infty.$$
The mean $\mu_{\bar x}=\mu$ and SD $\sigma_{\bar x}=\sigma/\sqrt n$ hold for **every** n ([[standard-error-of-the-mean]]). Only the *normal shape* is the asymptotic part.

**Triola's usage rule** (for treating x̄ as normal):

| Population | Sample size | Use the normal for x̄? |
|---|---|---|
| Normal | any n | yes, exactly |
| Not normal | n > 30 | yes, approximately |
| Not normal | n ≤ 30 | no, use other methods (e.g. nonparametric, bootstrap) |

**How fast? It depends on the skew.** For an exponential population (skewness 2), the skewness of x̄ is $2/\sqrt n$:

| n | 1 | 5 | 30 | 100 |
|---|---|---|---|---|
| SD of x̄ (σ = 1) | 1.00 | 0.45 | 0.18 | 0.10 |
| Skewness of x̄ | 2.0 | 0.89 | 0.35 | 0.20 |

So n > 30 is a rule of thumb, not a theorem. Symmetric populations converge by n ≈ 5–15, but heavy skew needs more.

```python
import numpy as np
from scipy import stats
rng = np.random.default_rng(0)
for n in [1, 5, 30, 100]:
    xbar = rng.exponential(1.0, size=(100_000, n)).mean(axis=1)  # 100k sample means
    print(n, xbar.std().round(3), stats.skew(xbar).round(2))     # SD -> 1/sqrt(n), skew -> 2/sqrt(n)
```

## In ML

**Error bars on every metric.** Mean loss or accuracy over a test set is a sample mean, so ±1.96·SE is a valid 95% interval when n is large. This is how benchmark leaderboards *should* report results.

**SGD noise is Gaussian-ish.** A mini-batch gradient averages B per-example gradients. By the CLT its noise is roughly normal with spread ∝ 1/√B. Many analyses of SGD as a noisy (Langevin-like) process start from this.

**Where it breaks.** Heavy-tailed data (financial returns, token-frequency counts, some reward signals) can have infinite or huge variance, and then sample means converge slowly or not at all.

## Exercises

**Basic** — A population has μ = 50 and σ = 12. For n = 36, give the mean, SD and approximate shape of the distribution of x̄.

**Intermediate** — Draw the sampling distribution of the mean of n = 2 die rolls by hand (36 outcomes). Is it still uniform? What shape is it, and why?

**Advanced** — The Cauchy distribution has no finite mean or variance. Simulate means of n = 1, 100 and 10,000 Cauchy draws. Does x̄ settle down? Which CLT hypothesis fails, and what does the mean of n Cauchy variables actually follow?
