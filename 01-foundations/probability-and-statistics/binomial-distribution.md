---
tags:
  - status/growing
  - probability
related:
  - "[[probability-distributions]]"
  - "[[bernoulli-distribution]]"
  - "[[normal-distribution]]"
  - "[[poisson-distribution]]"
domain: probability
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.packtpub.com/"
  - "https://www.khanacademy.org/math/statistics-probability"
---

> **TL;DR** — Counts successes in n independent Bernoulli trials. PMF = C(n,k)·p^k·(1−p)^(n−k). Converges to Normal for large n via CLT.

---

## Intuition

Binomial is the answer to: "I flip a coin n times, each with probability p of heads. How likely am I to get exactly k heads?" It's n independent Bernoulli trials bundled into one distribution.

The PMF has two parts: the probability of one specific sequence with k successes, times the number of such sequences (combinations). Multiplied together they give the probability of getting *any* sequence with k successes.

## Mechanics

**PMF derivation:**
- One sequence with k successes: p^k · (1−p)^(n−k)
- Number of such sequences: C(n,k) = n! / (k!(n−k)!)

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**Expectation and variance** (from linearity — Binomial = sum of n Bernoullis):
$$E[X] = np \qquad \text{Var}(X) = np(1-p)$$

**CLT approximation** — for large n: Binomial(n,p) ≈ N(np, np(1−p))
Rule of thumb: approximation valid when np ≥ 5 and n(1−p) ≥ 5.

```python
import numpy as np
from math import comb

def binomial_pmf(k, n, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

# P(exactly 3 successes in 10 trials, p=0.3)
print(f"P(X=3) = {binomial_pmf(3, 10, 0.3):.4f}")  # ~0.2668

# Verify probabilities sum to 1
n, p = 10, 0.3
total = sum(binomial_pmf(k, n, p) for k in range(n+1))
print(f"Sum of all probs: {total:.6f}")  # must be 1.0

# Verify E[X] and Var(X) by simulation
samples = np.random.binomial(n=n, p=p, size=100000)
print(f"E[X]   = {samples.mean():.4f}  (expected {n*p})")
print(f"Var(X) = {samples.var():.4f}  (expected {n*p*(1-p):.4f})")
```

> Runnable: [[code/foundations/binomial_distribution.py]]

## In ML

**Classifier accuracy follows Binomial.** If a model has true accuracy p and you test it on n examples, the number of correct predictions is Binomial(n, p). This is the basis for exact Binomial confidence intervals on accuracy.

**A/B testing.** Conversions in each group follow Binomial(n, p). Testing whether two groups have the same p is the classic two-sample proportion test, derived from the Binomial likelihood.

**Relationship to Bernoulli and Poisson.** Bernoulli(p) = Binomial(1, p) — one trial only. As n → ∞ and p → 0 with np = λ fixed, Binomial converges to Poisson(λ). Both special cases clarify when to use each model.

## Exercises

**Basic** — Compute P(X=3) for Binomial(10, 0.3) step by step. Identify the two multiplicative parts.

**Intermediate** — Verify numerically that Bernoulli(p) = Binomial(1, p) for p = 0.4. Check that E and Var match.

**Advanced** — At what n does the Normal approximation become good for p=0.3? Check numerically by comparing exact PMF with Normal PDF at several points.
