---
tags:
  - status/growing
  - probability
related:
  - "[[binomial-distribution-requirements]]"
  - "[[multiplication-rule]]"
  - "[[counting-and-combinatorics]]"
  - "[[hypergeometric-distribution]]"
  - "[[probability-distributions]]"
  - "[[bernoulli-distribution]]"
  - "[[normal-distribution]]"
  - "[[poisson-distribution]]"
  - "[[statistical-significance]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-3 (Fórmula 5-5)"
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.packtpub.com/"
  - "https://www.khanacademy.org/math/statistics-probability"
---

> **TL;DR** — Counts successes in n independent Bernoulli trials. PMF = C(n,k)·p^k·(1−p)^(n−k). Converges to Normal for large n via CLT.

---

## Intuition

Binomial is the answer to: "I flip a coin n times, each with probability p of heads. How likely am I to get exactly k heads?" It's n independent Bernoulli trials bundled into one distribution.

**The whole formula in one sentence: *probability of one way it can happen, times the number of ways it can happen.*** Those are the two factors, and here's why each exists.

*One way.* Take a specific sequence of 3 flips with 2 heads, say HHT. Independent trials → [[multiplication-rule|multiply]]: $P(\text{HHT}) = p\cdot p\cdot q = p^2q$. The key realization: **order doesn't change this probability.** HTH gives $p\cdot q\cdot p = p^2q$; THH gives $q\cdot p\cdot p = p^2q$ — identical, because multiplication is commutative. Any sequence with $k$ successes is just $k$ copies of $p$ and $n-k$ copies of $q$ multiplied, so *every* such sequence has the same probability $p^k q^{n-k}$.

*Number of ways.* "Exactly 2 heads" happens through several mutually exclusive orders (HHT, HTH, THH), and mutually exclusive events **add**. Since each has the same value $p^2q$, adding them = counting them and multiplying. The count is a [[counting-and-combinatorics|combination]]: $C(3,2)=3$. So $P(2\text{ heads})=3p^2q$.

Put together: $P(k)=\underbrace{C(n,k)}_{\text{how many ways}}\cdot\underbrace{p^k q^{n-k}}_{\text{one way}}$. Drop the $C(n,k)$ and you undercount the arrangements (the classic mistake); drop $p^k q^{n-k}$ and you count paths without weighting how likely each is.

## Mechanics

**Prerequisite:** the procedure must first pass the four [[binomial-distribution-requirements|binomial requirements]] (fixed n, independent trials, two categories, constant p). Only then does the formula apply.

**PMF derivation** — the formula is *multiplication rule × counting rule* (Triola §5-3):
- One *specific* sequence with k successes: by the [[multiplication-rule]], $p^k(1-p)^{n-k}$. E.g. 3 green then 2 non-green pods: $0.75^3\cdot0.25^2 = 0.0264$.
- But "exactly k successes" ignores order, so multiply by the number of arrangements — the [[counting-and-combinatorics|combination]] $C(n,k)$. For 3 of 5: $\tfrac{5!}{2!\,3!}=10$ arrangements, each with prob 0.0264 → $10\times0.0264 = 0.264$.

$$P(X = k) = \underbrace{\binom{n}{k}}_{\text{# arrangements}} \underbrace{p^k (1-p)^{n-k}}_{\text{prob. of one such sequence}}$$

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
