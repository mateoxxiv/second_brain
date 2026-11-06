---
tags:
  - status/seed
  - probability
related:
  - "[[central-limit-theorem]]"
  - "[[sampling-distribution]]"
  - "[[probabilities-for-sample-means]]"
  - "[[measures-of-variation]]"
  - "[[mean-and-variance-of-a-probability-distribution]]"
  - "[[hypergeometric-distribution]]"
  - "[[margin-of-error]]"
  - "[[sample-size-for-mean]]"
  - "[[one-mean-z-test]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-5 (μ_x̄ = μ, σ_x̄ = σ/√n; corrección por población finita)"
---

> **TL;DR** — The SD of the sample mean is the **standard error** σ/√n. Averaging n independent values divides the variance by n, so precision grows only like √n: to halve the error you need 4× the data.

---

## Intuition

One person's weight can be far from the average. The average of 100 people almost never is, because high and low values cancel. The standard error measures *how far a sample mean typically lands from μ*. It is the σ of the [[sampling-distribution]] of x̄, not of the data. Two different questions: σ says how spread out *people* are, and σ/√n says how spread out *averages* are.

## Mechanics

**Derivation.** With independent $X_i$, each with mean μ and variance σ²:
$$E[\bar x] = \tfrac1n\sum E[X_i] = \mu, \qquad \mathrm{Var}(\bar x) = \tfrac{1}{n^2}\sum \mathrm{Var}(X_i) = \tfrac{n\sigma^2}{n^2} = \tfrac{\sigma^2}{n}$$
The middle step uses independence: variances of independent variables add, with no covariance terms. Taking the square root gives $\sigma_{\bar x} = \sigma/\sqrt n$.

| Property | Formula | Why it matters |
|---|---|---|
| Center | $\mu_{\bar x} = \mu$ | x̄ is unbiased |
| Standard error | $\sigma_{\bar x} = \sigma/\sqrt n$ | the denominator of every z for a mean |
| √n law | SE ÷ k needs n × k² | data gets expensive fast: 2× precision = 4× n |
| Estimated SE | $s/\sqrt n$ | used when σ is unknown, which leads to the t distribution |
| Finite population correction | $\frac{\sigma}{\sqrt n}\sqrt{\frac{N-n}{N-1}}$ | use when n > 5% of N (sampling without replacement) |

**Finite population correction (FPC).** Sampling without replacement from a small population makes the draws negatively dependent: taking a heavy item leaves fewer heavy ones. That shrinks the variance. Example: N = 500 and n = 50 (10% > 5%), so the factor is √(450/499) = 0.950, a 5% smaller SE. As N → ∞ the factor → 1. In the extreme case n = N (a census), it is 0: there is no sampling error.

```python
import numpy as np
rng = np.random.default_rng(1)
sigma = 15
for n in [4, 16, 64]:
    means = rng.normal(100, sigma, size=(50_000, n)).mean(axis=1)
    print(n, means.std().round(2), sigma / np.sqrt(n))   # 7.5, 3.75, 1.875: 4x n halves the SE
```

## In ML

**Test-set sizing.** The SE of accuracy is √(p(1−p)/n). At p ≈ 0.9, n = 1,000 gives SE ≈ 0.0095, so differences under about 2 points are noise. To detect a 0.5-point gain you need roughly 16× more data.

**Batch size vs. gradient noise.** Gradient noise scales like σ/√B. Going from B = 32 to B = 128 only halves the noise. This is part of why learning-rate scaling rules for large batches are not linear in B.

## Exercises

**Basic** — IQ has σ = 15. Find the SE of x̄ for n = 9, 36 and 225.

**Intermediate** — A survey has SE = 4 with n = 100. What n gives SE = 1? What does that cost compared with the original survey?

**Advanced** — Derive Var(x̄) when every pair of observations has correlation ρ. Show that it equals (σ²/n)(1 + (n−1)ρ), and explain why autocorrelated time-series data make naive σ/√n error bars far too small.
