**Related**: [[probability-distributions]], [[binomial-distribution]], [[exponential-distribution]]
**Tags**: #status/growing

## Core Idea

The Poisson distribution models the number of rare, independent events in a fixed
interval of time or space, given a known average rate $\lambda$. It is derived from
the Binomial by taking many trials ($n \to \infty$) with vanishing probability
($p \to 0$) while keeping $\lambda = np$ fixed. Its defining property:
mean equals variance — both equal $\lambda$.

## Details

### Parameters

- $\lambda$ — average number of events per interval (rate). Must be > 0.
- $k$ — the outcome: number of events observed (takes values $0, 1, 2, \ldots$)

### Deriving the PMF from Binomial

Divide an interval into $n$ tiny sub-intervals. Each either has an event (prob $p$)
or not. Keep $\lambda = np$ fixed and let $n \to \infty$, $p \to 0$:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

After applying the limit (dropping terms that vanish as $n \to \infty$):

$$\boxed{P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}}$$

The $e^{-\lambda}$ term emerges from $\lim_{n\to\infty}(1 - \lambda/n)^n = e^{-\lambda}$.

### Expectation and Variance

$$E[X] = \lambda \qquad \text{Var}(X) = \lambda$$

Both equal $\lambda$ — this is the key diagnostic property. If your count data
has $\text{Var}(X) \gg E[X]$, it is **overdispersed** and Poisson is the wrong model
(use Negative Binomial instead).

### When to Use

Good fit when:
- Counting events over time or space
- Events are rare and independent
- $\text{Var}(X) \approx E[X]$ in your data

Examples: emails per hour, server requests per second, typos per page, word
occurrences in a document.

### ML Connections

| Use case | How Poisson appears |
|---|---|
| NLP word counts | Word frequency per document ~ Poisson |
| Anomaly detection | Flag when observed count >> expected lambda |
| Poisson regression | Target is a count — avoids negative predictions |
| Queuing systems | Arrivals per time unit ~ Poisson |

## Code Example

```python
import numpy as np
from math import factorial, exp

def poisson_pmf(k: int, lam: float) -> float:
    """P(X=k) for Poisson(lambda) from scratch.
    k: number of events observed
    lam: average rate (lambda)
    """
    return (lam**k * exp(-lam)) / factorial(k)

lam = 3.0
# Full distribution up to k=10
probs = [poisson_pmf(k, lam) for k in range(11)]
print(f"Sum of probs (k=0..10): {sum(probs):.6f}")  # ~1.0

# E[X] and Var(X) both equal lambda
samples = np.random.poisson(lam=lam, size=100000)
print(f"E[X]   = {samples.mean():.4f}  (expected {lam})")
print(f"Var(X) = {samples.var():.4f}  (expected {lam})")

# Overdispersion check
def is_poisson(data: np.ndarray, threshold: float = 1.5) -> bool:
    """Check if variance/mean ratio suggests Poisson (ratio ~1)."""
    ratio = data.var() / data.mean()
    print(f"Var/Mean ratio: {ratio:.3f} (Poisson expects ~1.0)")
    return ratio < threshold

# Simulate overdispersed data (not Poisson)
overdispersed = np.random.negative_binomial(n=2, p=0.4, size=100000)
is_poisson(samples)        # True  — ratio ~1
is_poisson(overdispersed)  # False — ratio >> 1
```

> For runnable implementation with exercises, see: [[code/foundations/poisson_distribution.py]]

## Connections

- [[binomial-distribution]] — Poisson is the limit of Binomial as n→∞, p→0
- [[exponential-distribution]] — time between Poisson events follows Exponential
- [[probability-distributions]] — overview of all distributions
- Forward link: Poisson regression — GLM for count targets
- Forward link: NLP — word count models use Poisson as baseline

## Sources

- [Mathematics for Machine Learning — Chapter 6.2](https://mml-book.github.io/book/mml-book.pdf)
- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — Chapter 2
- [Khan Academy — Poisson distribution](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/poisson-distribution/v/poisson-process-1)
