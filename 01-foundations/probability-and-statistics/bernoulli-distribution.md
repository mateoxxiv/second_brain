---
tags:
  - status/growing
  - probability
related:
  - "[[probability-distributions]]"
  - "[[probability-fundamentals]]"
  - "[[binomial-distribution]]"
  - "[[normal-distribution]]"
domain: probability
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.packtpub.com/"
  - "https://www.khanacademy.org/math/statistics-probability"
---

> **TL;DR** — One binary trial. P(X=1)=p, P(X=0)=1−p. Binary cross-entropy loss IS the Bernoulli MLE loss — not a design choice, a consequence.

---

## Intuition

The Bernoulli distribution is the simplest possible random variable: one flip, two outcomes. Parameter p is the probability of success (1). Everything about binary classification in ML reduces to Bernoulli — logistic regression outputs p, and the training loss is derived from the Bernoulli likelihood.

## Mechanics

**PMF** (compact form encoding both outcomes):
$$P(X = k) = p^k (1-p)^{1-k}, \quad k \in \{0, 1\}$$

- k=1: p¹(1−p)⁰ = p
- k=0: p⁰(1−p)¹ = 1−p

**Expectation:** E[X] = p
**Variance:** Var(X) = p(1−p), maximized at p = 0.5 (maximum uncertainty)

**MLE → Binary cross-entropy:**
Log-likelihood of one label y ∈ {0,1}: y·ln(p̂) + (1−y)·ln(1−p̂)

Negate and average over n samples:
$$\mathcal{L} = -\frac{1}{n}\sum_{i=1}^n \left[ y_i \ln\hat{p}_i + (1-y_i)\ln(1-\hat{p}_i) \right]$$

This is **binary cross-entropy** — derived from first principles, not chosen arbitrarily.

```python
import numpy as np

def bernoulli_pmf(k: int, p: float) -> float:
    return p**k * (1 - p)**(1 - k)

p = 0.3
print(bernoulli_pmf(1, p))  # 0.3
print(bernoulli_pmf(0, p))  # 0.7

def binary_cross_entropy(y_true, y_pred, eps=1e-9):
    return -np.mean(y_true * np.log(y_pred + eps) +
                    (1 - y_true) * np.log(1 - y_pred + eps))

y_true = np.array([1, 0, 1, 1, 0])
y_pred = np.array([0.9, 0.1, 0.8, 0.7, 0.3])
print(f"Loss: {binary_cross_entropy(y_true, y_pred):.4f}")
```

> Runnable: [[code/foundations/bernoulli_distribution.py]]

## In ML

**Logistic regression outputs a Bernoulli parameter.** The sigmoid function squashes any real value into [0,1], producing p. Training minimizes binary cross-entropy, which is exactly the negative log-likelihood under the Bernoulli assumption.

**Binary cross-entropy IS MLE.** Maximizing the Bernoulli log-likelihood is identical to minimizing binary cross-entropy. When you pick this loss function, you are implicitly assuming labels are Bernoulli-distributed — if they aren't, the loss is suboptimal.

**Naive Bayes with binary features.** Each feature (word present/absent) is modeled as Bernoulli(p | class). The product of individual feature likelihoods (independence assumption) gives the joint likelihood used for classification.

## Exercises

**Basic** — Compute PMF for p=0.7 at k=0 and k=1. Verify they sum to 1.

**Intermediate** — Derive that binary cross-entropy is the negative log-likelihood of Bernoulli. Start from P(y|p̂) = p̂^y(1−p̂)^(1−y) and take the log.

**Advanced** — Explain why variance is maximized at p = 0.5 without using formulas. Why does the "most uncertain" coin have the largest variance?
