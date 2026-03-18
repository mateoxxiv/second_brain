**Related**: [[probability-fundamentals]], [[gradient-descent]], [[linear-regression]]
**Tags**: #status/growing

## Core Idea

A probability distribution describes all possible outcomes of a random variable
and how likely each one is. In ML, distributions are everywhere: data is assumed
to follow a distribution, loss functions come from distributions, and weight
initialization uses distributions. The two numbers that summarize any distribution
are **expectation** (the center) and **variance** (the spread).

Distributions come in two flavors:
- **Parametric** — defined by a formula with parameters (Normal, Bernoulli, Poisson)
- **Empirical** — derived directly from data, no assumptions about shape. Iterative
  methods (bootstrap, permutation tests) let you compute confidence intervals and
  predictions without ever assuming a parametric form.

## Details

### Expectation — E[X]

The probability-weighted average of all outcomes:

$$E[X] = \sum_x x \cdot P(X = x)$$

If you ran the experiment infinitely many times, expectation is the long-run
average. For a fair die: $E[X] = (1+2+3+4+5+6)/6 = 3.5$.

### Variance — Var(X)

How spread out the distribution is around its mean $\mu = E[X]$:

$$\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

Standard deviation $\sigma = \sqrt{\text{Var}(X)}$ — same units as X.

**Computational form** (easier): $\text{Var}(X) = E[X^2] - \mu^2$

### Bernoulli Distribution

One trial, two outcomes: 1 (success) with probability $p$, 0 (failure) with $1-p$.

$$P(X = k) = p^k (1-p)^{1-k}, \quad k \in \{0, 1\}$$

$$E[X] = p \qquad \text{Var}(X) = p(1-p)$$

Variance peaks at $p = 0.5$ (maximum uncertainty) and is zero at $p = 0$ or $p = 1$.

**ML:** logistic regression outputs a Bernoulli parameter. Binary cross-entropy
loss is the negative log-likelihood of a Bernoulli.

See: [[bernoulli-distribution]]

### Normal (Gaussian) Distribution

The most important distribution. Bell-shaped, symmetric.

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

Written $X \sim \mathcal{N}(\mu, \sigma^2)$. Parameters: $\mu$ (center), $\sigma^2$ (spread).

$$E[X] = \mu \qquad \text{Var}(X) = \sigma^2$$

**Standard Normal** $Z \sim \mathcal{N}(0, 1)$: standardize with $Z = (X - \mu)/\sigma$.

**Why Normal is everywhere — Central Limit Theorem:**
The sum of many independent random variables converges to Normal, regardless
of their original distributions. Height, noise, measurement error — all Normal.

**68-95-99.7 rule:**

```
mu +- 1*sigma  ->  68% of data
mu +- 2*sigma  ->  95% of data
mu +- 3*sigma  ->  99.7% of data
```

**ML connections:**
- Weight initialization: $w \sim \mathcal{N}(0, \sigma^2)$
- MSE loss assumes Gaussian noise — comes from MLE under Gaussian assumption
- VAEs, diffusion models, Gaussian processes all rely on Normal distributions

See: [[normal-distribution]]

### Poisson Distribution

Number of rare, independent events in a fixed interval.

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$

$\lambda$ = average rate. **Key property: $E[X] = \text{Var}(X) = \lambda$.**

If variance >> mean in your data, it is NOT Poisson (overdispersed).

**Examples:** API requests per second, word counts in documents, anomalies per day.

See: [[poisson-distribution]]

### Empirical Distributions

When data doesn't fit a parametric form, you can use the data itself as the
distribution. No formula — just the observed frequencies.

**Iterative methods that work on empirical distributions:**
- **Bootstrap** — resample with replacement to build a confidence interval without
  assuming Normality
- **Permutation tests** — shuffle labels to test significance without a t-test
- **Monte Carlo** — simulate outcomes by sampling from empirical distributions

This is the approach taken in "Statistics for Machine Learning" (Dangeti) — iterative
and computational methods that avoid strong distributional assumptions.

See: [[empirical-distributions]]

### Summary Table

| Distribution | Parameters | $E[X]$ | $\text{Var}(X)$ | Use in ML |
|-------------|-----------|--------|-----------------|-----------|
| Bernoulli | $p$ | $p$ | $p(1-p)$ | Binary classification |
| Normal | $\mu, \sigma^2$ | $\mu$ | $\sigma^2$ | Noise, weight init, MSE |
| Poisson | $\lambda$ | $\lambda$ | $\lambda$ | Count prediction, NLP |
| Empirical | none | sample mean | sample variance | Bootstrap, permutation tests |

## Code Example

```python
import numpy as np

# Bernoulli
p = 0.3
samples = np.random.binomial(n=1, p=p, size=10000)
print(f"Bernoulli: E[X]={samples.mean():.3f} (expected {p})")
print(f"Bernoulli: Var(X)={samples.var():.3f} (expected {p*(1-p):.3f})")

# Normal
mu, sigma = 5, 2
samples = np.random.normal(mu, sigma, 10000)
print(f"Normal: E[X]={samples.mean():.3f}, Var(X)={samples.var():.3f}")

# Poisson
lam = 3
samples = np.random.poisson(lam, 10000)
print(f"Poisson: E[X]={samples.mean():.3f}, Var(X)={samples.var():.3f}")

# Empirical bootstrap confidence interval
data = np.array([2.1, 3.4, 2.8, 3.1, 4.0, 2.5, 3.7, 2.9])
bootstrap_means = [np.random.choice(data, len(data), replace=True).mean()
                   for _ in range(10000)]
ci_low, ci_high = np.percentile(bootstrap_means, [2.5, 97.5])
print(f"Bootstrap 95% CI for mean: [{ci_low:.3f}, {ci_high:.3f}]")
```

> For runnable implementation with exercises, see: [[code/foundations/probability_distributions.py]]

## Connections

- [[probability-fundamentals]] — distributions are built on top of basic probability rules
- [[bernoulli-distribution]] — binary outcomes, logistic regression
- [[normal-distribution]] — Gaussian, CLT, MSE loss derivation
- [[poisson-distribution]] — count data, NLP word frequencies
- [[empirical-distributions]] — bootstrap, permutation tests, no-assumption inference
- Forward link: MLE — fitting distribution parameters to data
- Forward link: Naive Bayes — Gaussian Naive Bayes assumes Normal features
- Forward link: VAEs — encoder outputs mu and sigma of a Normal distribution

## Sources

- [3Blue1Brown — But what is the Central Limit Theorem?](https://www.youtube.com/watch?v=zeJD6dqJ5lo)
- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — Chapter 2
- [Khan Academy — Random Variables and Probability Distributions](https://www.khanacademy.org/math/statistics-probability)
- [Mathematics for Machine Learning — Chapter 6.5](https://mml-book.github.io/book/mml-book.pdf)
