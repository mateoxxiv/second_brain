---
tags:
  - status/seed
  - probability
related:
  - "[[confidence-interval-for-variance]]"
  - "[[unbiased-and-biased-estimators]]"
  - "[[measures-of-variation]]"
  - "[[student-t-distribution]]"
  - "[[sampling-distribution]]"
  - "[[normal-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-5 (Distribución chi cuadrada, Fórmula 7-5, Tabla A-4)"
---

> **TL;DR** — If you sample from a normal population, $(n-1)s^2/\sigma^2$ follows a chi-squared distribution with $n-1$ degrees of freedom, and that is the only tool that gives intervals for a variance or standard deviation.

---

## Intuition

Each squared standardized value $(x-\mu)^2/\sigma^2$ is a small, non-negative quantity, and adding several of them gives a total that can never be negative. The chi-squared distribution is the law of that total. It answers: "if I sum up n squared, unit-free deviations, how big is the sum likely to be?"

It matters for variance because $s^2$ is exactly such a sum (divided by $n-1$). Its distribution, unlike $\bar{x}$'s, is skewed and bounded at zero, so the usual "estimate ± margin" recipe with a symmetric critical value does not work.

## Mechanics

Let $Z_1, \dots, Z_k$ be independent standard normal variables. Then

$$Q = Z_1^2 + Z_2^2 + \dots + Z_k^2 \sim \chi^2_k$$

with $k$ degrees of freedom. For a normal sample, $s^2$ connects to this sum: with $Z_i = (x_i - \mu)/\sigma$,

$$\frac{(n-1)s^2}{\sigma^2} \sim \chi^2_{n-1}$$

The $n-1$ (not $n$) appears because $\bar{x}$ is estimated from the same data, which uses up one degree of freedom. The sum of squares around $\bar{x}$ is $\sum (x_i-\bar{x})^2 = \sum (x_i-\mu)^2 - n(\bar{x}-\mu)^2$, and the last term is a single squared standard normal.

| Property | Statement | Why it matters |
|----------|-----------|----------------|
| Support | $\chi^2 \ge 0$ | Variance intervals can never go negative |
| Shape | Right-skewed; approaches normal as $k$ grows | Two critical values, computed separately |
| Mean | $k$ | With $k=n-1$: $E[(n-1)s^2/\sigma^2]=n-1$, so $E[s^2]=\sigma^2$ (unbiased) |
| Variance | $2k$ | Spread grows with $k$, but the ratio to the mean shrinks |
| Table lookup | Tables give right-tail areas | Left-tail critical values need $1-\alpha/2$ |

```python
from scipy import stats

print(stats.chi2.ppf(0.025, df=9))  # 2.700  (left critical value)
print(stats.chi2.ppf(0.975, df=9))  # 19.023 (right critical value)
```

## In ML

**Variance of estimates** — Repeated training runs give a sample variance of a metric. Under normal noise, that variance has a chi-squared sampling distribution, which is how you would put an interval on the run-to-run spread.

**Likelihood-ratio tests** — Twice a log-likelihood difference is asymptotically chi-squared. This is the reason nested-model comparisons (for example, a regression with and without a feature) get a chi-squared p-value.

**Gaussian variance estimates** — Maximum-likelihood variance estimates for a Gaussian noise model are scaled chi-squared variables. Knowing this tells you how much a noise-scale estimate can wobble with small n.

## Exercises

**Basic** — For $df = 9$, look up the chi-squared values that leave 0.025 in each tail. Check both against the 2.700 and 19.023 values above.

**Intermediate** — Show that $E[\chi^2_k] = k$ by using $E[Z^2] = 1$ and linearity. Then explain why the mean of $(n-1)s^2/\sigma^2$ being $n-1$ implies $s^2$ is unbiased.

**Advanced** — Explain why the chi-squared distribution is not symmetric, and why it becomes approximately normal as $k$ grows. What does this imply for the interval in [[confidence-interval-for-variance]] when $n$ is small?
