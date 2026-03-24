**Related**: [[probability-distributions]], [[normal-distribution]], [[exponential-distribution]], [[probability-fundamentals]]
**Tags**: #status/seed

## Core Idea

Every probability distribution has a **CDF** (Cumulative Distribution Function)
that answers "what is the probability of getting a value ≤ x?" and an
**Inverse CDF** (Quantile Function) that flips the question: "what value x
corresponds to probability p?" The inverse CDF is the foundation of confidence
intervals, percentiles, anomaly detection thresholds, and sampling from any
distribution.

## Details

### CDF — Cumulative Distribution Function

$$F(x) = P(X \leq x)$$

Input: a value $x$. Output: a probability in $[0, 1]$.

The CDF always:
- Starts at 0 (as $x \to -\infty$)
- Ends at 1 (as $x \to +\infty$)
- Is non-decreasing

For a **continuous** distribution, the CDF is the integral of the PDF:

$$F(x) = \int_{-\infty}^{x} f(t)\, dt$$

For a **discrete** distribution, it is the sum of probabilities up to $x$:

$$F(x) = \sum_{t \leq x} P(X = t)$$

### Inverse CDF — Quantile Function

$$F^{-1}(p) = \inf\{x : F(x) \geq p\}, \quad p \in [0, 1]$$

Input: a probability $p$. Output: the value $x$ such that $P(X \leq x) = p$.

Also called the **percent point function (ppf)** or **quantile function**.

**Worked example — Standard Normal:**

```
CDF:          P(Z <= 1.96) = 0.975
Inverse CDF:  F_inv(0.975) = 1.96
```

The 95% confidence interval $[-1.96, 1.96]$ comes directly from:

$$F^{-1}(0.025) = -1.96 \qquad F^{-1}(0.975) = 1.96$$

**Worked example — Exponential($\lambda$):**

CDF: $F(x) = 1 - e^{-\lambda x}$

Solving $p = 1 - e^{-\lambda x}$ for $x$:

$$x = F^{-1}(p) = -\frac{\ln(1-p)}{\lambda}$$

Clean closed form — used directly in inverse transform sampling.

### Key Applications

**Confidence intervals:**

```
lower = F_inv(alpha / 2)
upper = F_inv(1 - alpha / 2)
```

For 95% CI: $\alpha = 0.05$, so $F^{-1}(0.025)$ and $F^{-1}(0.975)$.

**Percentiles and quantiles:**

```
Median      = F_inv(0.50)
90th pctile = F_inv(0.90)
99th pctile = F_inv(0.99)
```

**Anomaly detection threshold:**

Flag $x$ as anomalous if $x > F^{-1}(0.99)$ — beyond the 99th percentile.

**Inverse transform sampling:**

To sample from any distribution with known inverse CDF:

$$u \sim \text{Uniform}(0, 1) \implies x = F^{-1}(u) \sim \text{target distribution}$$

This works because $F^{-1}$ maps uniform probability mass to the correct
density of the target. It is the foundation of most random number generators.

### Inverse CDF by Distribution

| Distribution | CDF $F(x)$ | Inverse CDF $F^{-1}(p)$ |
|---|---|---|
| Uniform$(a,b)$ | $(x-a)/(b-a)$ | $a + p(b-a)$ |
| Exponential$(\lambda)$ | $1 - e^{-\lambda x}$ | $-\ln(1-p)/\lambda$ |
| Normal$(\mu,\sigma)$ | $\Phi\!\left(\frac{x-\mu}{\sigma}\right)$ | $\mu + \sigma\,\Phi^{-1}(p)$ |
| Bernoulli$(p_0)$ | step function | $0$ if $p < 1-p_0$, else $1$ |

Note: Normal has no closed-form inverse — $\Phi^{-1}$ is computed numerically
(that's what `scipy.stats.norm.ppf` does internally).

## Code Example

```python
import numpy as np
from scipy import stats

# CDF: P(X <= x)
print(stats.norm.cdf(1.96))           # 0.9750  — standard Normal
print(stats.expon.cdf(0.5, scale=1))  # 0.3935  — Exponential(1)

# Inverse CDF: what x gives P(X <= x) = p?
print(stats.norm.ppf(0.975))          # 1.96   — ppf = inverse CDF
print(stats.norm.ppf(0.025))          # -1.96

# 95% confidence interval for N(0,1)
alpha = 0.05
lo = stats.norm.ppf(alpha / 2)
hi = stats.norm.ppf(1 - alpha / 2)
print(f"95% CI: [{lo:.4f}, {hi:.4f}]")  # [-1.96, 1.96]

# Inverse transform sampling from Exponential(lambda=2) using only Uniform
lam = 2.0
u = np.random.uniform(0, 1, size=100000)
x = -np.log(1 - u) / lam              # F_inv(u) for Exponential
print(f"Mean: {x.mean():.4f}  (expected {1/lam:.4f})")
print(f"Var:  {x.var():.4f}  (expected {1/lam**2:.4f})")
```

> For runnable implementation with exercises, see: [[code/foundations/cdf_and_quantiles.py]]

## Connections

- [[probability-distributions]] — CDF is defined for every distribution
- [[normal-distribution]] — 1.96 and 68-95-99.7 rule come from Normal CDF/inverse
- [[exponential-distribution]] — clean closed-form inverse CDF
- Forward link: confidence intervals — built directly on inverse CDF
- Forward link: hypothesis testing — p-values are CDF evaluations
- Forward link: sampling methods — inverse transform, rejection sampling

## Sources

- [Mathematics for Machine Learning — Chapter 6](https://mml-book.github.io/book/mml-book.pdf)
- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — Chapter 2
- [Khan Academy — Cumulative distribution functions](https://www.khanacademy.org/math/statistics-probability)
- [scipy.stats documentation — ppf methods](https://docs.scipy.org/doc/scipy/reference/stats.html)
