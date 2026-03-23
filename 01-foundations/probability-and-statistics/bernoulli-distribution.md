**Related**: [[probability-distributions]], [[normal-distribution]], [[probability-fundamentals]]
**Tags**: #status/growing

## Core Idea

The Bernoulli distribution models a single binary trial — success (1) or failure (0).
One parameter, $p$, fully determines it: $P(X=1) = p$ and $P(X=0) = 1-p$.
It is the atomic unit of binary classification: logistic regression outputs a
Bernoulli parameter, and binary cross-entropy loss is the MLE loss for Bernoulli
labels.

## Details

### PMF

$k$ is the **outcome** — the value the random variable takes, either 0 (failure)
or 1 (success). You plug in the observed outcome and the formula returns its probability:

$$P(X = k) = p^k (1-p)^{1-k}, \quad k \in \{0, 1\}$$

This is a compact way to write two rules in one line:

```
k = 1 (success):  p^1 * (1-p)^0  =  p
k = 0 (failure):  p^0 * (1-p)^1  =  1-p
```

### Expectation and Variance

$$E[X] = p$$

$$\text{Var}(X) = p(1-p)$$

**Derivation of variance:**

$$E[X^2] = 1^2 \cdot p + 0^2 \cdot (1-p) = p$$
$$\text{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)$$

Variance is maximized at $p = 0.5$ (maximum uncertainty) and zero at $p=0$ or
$p=1$ (certainty — no randomness left).

### Binary Cross-Entropy from MLE

Logistic regression outputs $\hat{p} = P(Y=1|\mathbf{x})$. The log-likelihood
of a single label $y \in \{0,1\}$:

$$\log P(y | \hat{p}) = y \log\hat{p} + (1-y)\log(1-\hat{p})$$

Negate and average over $n$ samples:

$$\mathcal{L} = -\frac{1}{n}\sum_{i=1}^n \left[ y_i \log\hat{p}_i + (1-y_i)\log(1-\hat{p}_i) \right]$$

This is **binary cross-entropy loss** — not a design choice, but the direct
consequence of assuming labels are Bernoulli-distributed and doing MLE.

### When to Use

- Any binary outcome: spam/not-spam, click/no-click, fraud/legitimate
- Single trial only — for $n$ repeated trials, use [[binomial-distribution]]

## Code Example

```python
import numpy as np

def bernoulli_pmf(k: int, p: float) -> float:
    """P(X=k) for Bernoulli(p). k is the outcome: 0 or 1."""
    return p**k * (1 - p)**(1 - k)

p = 0.3
print(f"P(X=1) = {bernoulli_pmf(1, p)}")  # 0.3
print(f"P(X=0) = {bernoulli_pmf(0, p)}")  # 0.7

# Verify E[X] and Var(X)
samples = np.random.binomial(n=1, p=p, size=100000)
print(f"E[X] = {samples.mean():.4f}  (expected {p})")
print(f"Var(X) = {samples.var():.4f}  (expected {p*(1-p):.4f})")

# Binary cross-entropy loss
def binary_cross_entropy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """MLE loss for Bernoulli-distributed labels."""
    eps = 1e-9  # avoid log(0)
    return -np.mean(y_true * np.log(y_pred + eps) +
                    (1 - y_true) * np.log(1 - y_pred + eps))

y_true = np.array([1, 0, 1, 1, 0])
y_pred = np.array([0.9, 0.1, 0.8, 0.7, 0.3])
print(f"Cross-entropy loss: {binary_cross_entropy(y_true, y_pred):.4f}")
```

> For runnable implementation with exercises, see: [[code/foundations/bernoulli_distribution.py]]

## Connections

- [[probability-distributions]] — overview of all distributions
- [[binomial-distribution]] — n independent Bernoulli trials
- [[normal-distribution]] — Bernoulli is discrete; Normal is its continuous cousin
- Forward link: logistic regression — outputs a Bernoulli parameter
- Forward link: cross-entropy loss — MLE under Bernoulli assumption
- Forward link: Naive Bayes — models each feature as Bernoulli for binary inputs

## Sources

- [Mathematics for Machine Learning — Chapter 6.2](https://mml-book.github.io/book/mml-book.pdf)
- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — Chapter 2
- [Khan Academy — Bernoulli distribution](https://www.khanacademy.org/math/statistics-probability)
