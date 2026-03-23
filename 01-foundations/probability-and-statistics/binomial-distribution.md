**Related**: [[probability-distributions]], [[bernoulli-distribution]], [[normal-distribution]]
**Tags**: #status/growing

## Core Idea

The Binomial distribution counts the number of successes in $n$ independent
Bernoulli trials, each with success probability $p$. It is the natural generalization
of [[bernoulli-distribution]]: Bernoulli is one flip, Binomial is $n$ flips.
For large $n$, it converges to Normal via the Central Limit Theorem.

## Details

### Parameters

- $n$ — number of trials
- $p$ — probability of success on each trial
- $k$ — the outcome: number of successes (takes values $0, 1, \ldots, n$)

### PMF — Building it from scratch

The probability of exactly $k$ successes in $n$ trials comes from two parts:

**Part 1 — probability of one specific sequence with $k$ successes:**

Any sequence with $k$ successes and $n-k$ failures has probability:

$$p^k (1-p)^{n-k}$$

**Part 2 — how many such sequences exist:**

The binomial coefficient counts the number of ways to place $k$ successes
in $n$ positions:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

Multiply both:

$$\boxed{P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}}$$

### Expectation and Variance

Binomial is the sum of $n$ independent Bernoulli($p$) variables. Using linearity
of expectation and variance additivity for independent variables:

$$E[X] = np \qquad \text{Var}(X) = np(1-p)$$

Intuition: 100 trials with $p=0.3$ → expect 30 successes.

### Connection to Normal (CLT)

For large $n$, the Binomial converges to Normal:

$$\text{Binomial}(n, p) \approx \mathcal{N}(np,\; np(1-p))$$

Rule of thumb: approximation is good when $np \geq 5$ and $n(1-p) \geq 5$.

### Relationship to Bernoulli

$$\text{Bernoulli}(p) = \text{Binomial}(n=1, p)$$

Bernoulli is a special case — one trial only.

### ML Connections

| Use case | How Binomial appears |
|---|---|
| Classifier evaluation | Correct predictions ~ Binomial(n, accuracy) |
| A/B testing | Conversions per group ~ Binomial(n, p) |
| Naive Bayes | Word presence counted as Binomial trials |

## Code Example

```python
import numpy as np
from math import comb

def binomial_pmf(k: int, n: int, p: float) -> float:
    """P(X=k) for Binomial(n, p) from scratch.
    k: number of successes
    n: number of trials
    p: success probability per trial
    """
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

# P(exactly 3 successes in 10 trials, p=0.3)
print(f"P(X=3) = {binomial_pmf(3, 10, 0.3):.4f}")  # ~0.2668

# Full distribution
n, p = 10, 0.3
probs = [binomial_pmf(k, n, p) for k in range(n+1)]
print(f"Sum of all probs: {sum(probs):.6f}")  # must be 1.0

# Verify E[X] and Var(X)
samples = np.random.binomial(n=n, p=p, size=100000)
print(f"E[X]   = {samples.mean():.4f}  (expected {n*p})")
print(f"Var(X) = {samples.var():.4f}  (expected {n*p*(1-p):.4f})")

# CLT approximation
import scipy.stats as stats
k = 35
exact = binomial_pmf(k, 100, 0.3)
normal_approx = stats.norm.pdf(k, loc=100*0.3, scale=np.sqrt(100*0.3*0.7))
print(f"Exact P(X=35): {exact:.6f}")
print(f"Normal approx: {normal_approx:.6f}")
```

> For runnable implementation with exercises, see: [[code/foundations/binomial_distribution.py]]

## Connections

- [[bernoulli-distribution]] — Binomial is n repeated Bernoulli trials
- [[normal-distribution]] — Binomial converges to Normal for large n (CLT)
- [[poisson-distribution]] — Binomial with large n and small p converges to Poisson
- Forward link: logistic regression — predicts Bernoulli p, evaluated over Binomial
- Forward link: hypothesis testing — exact Binomial test for proportions

## Sources

- [Mathematics for Machine Learning — Chapter 6.2](https://mml-book.github.io/book/mml-book.pdf)
- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — Chapter 2
- [Khan Academy — Binomial distribution](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/binomial-random-variables/a/binomial-probability-article)
