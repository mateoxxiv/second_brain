---
tags:
  - status/growing
  - probability
related:
  - "[[probability-distributions]]"
  - "[[beta-distribution]]"
domain: probability
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf"
  - "https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers"
  - "http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/"
---

> **TL;DR** — Generalization of Beta to k categories. Models uncertainty about a probability vector [p1,...,pk] summing to 1. Conjugate prior for Multinomial. Foundation of LDA.

---

## Intuition

Where Beta asks "what is the probability p of success in one binary trial?", Dirichlet asks "what is the probability vector [p1,...,pk] over k categories?" It lives on the probability simplex — all outputs are non-negative and sum to 1.

The concentration parameter α controls sparsity: small α produces vectors with one dominant category (documents dominated by one topic); large α produces nearly uniform vectors (topics mixed equally).

## Mechanics

**PDF:**
$$f(\mathbf{p}; \boldsymbol{\alpha}) = \frac{1}{B(\boldsymbol{\alpha})} \prod_{i=1}^k p_i^{\alpha_i - 1}$$

$$E[p_i] = \frac{\alpha_i}{\sum_j \alpha_j}$$

**Concentration effect:** if all αᵢ = α₀:
- α₀ < 1 → sparse (samples cluster at corners)
- α₀ = 1 → uniform over simplex
- α₀ >> 1 → dense (samples near center)

**Beta is the special case k=2.** All Beta intuitions carry over.

**Conjugate update:** Prior Dirichlet(α) + observe counts n → Posterior Dirichlet(α + n). Same closed-form update as Beta.

```python
import numpy as np

alpha = [2.0, 3.0, 5.0]
samples = np.random.dirichlet(alpha, size=100000)
expected = np.array(alpha) / sum(alpha)
print(f"E[p] expected: {expected}")
print(f"E[p] observed: {samples.mean(axis=0).round(4)}")

# Concentration effect
for a0 in [0.1, 1.0, 10.0]:
    s = np.random.dirichlet([a0, a0, a0], size=3)
    print(f"\nalpha={a0}: {s.round(3)}")
```

> Runnable: [[code/foundations/dirichlet_distribution.py]]

## In ML

**LDA topic models.** Latent Dirichlet Allocation uses two Dirichlet priors: θ_d ~ Dirichlet(α) for document-topic mixtures, φ_t ~ Dirichlet(β) for topic-word distributions. The α parameter controls how many topics each document uses — small α = focused on few topics.

**Bayesian inference over categories.** Whenever you need to estimate a probability vector (class probabilities, word probabilities) with uncertainty, Dirichlet is the natural prior. Combined with Multinomial likelihood, the posterior is Dirichlet with updated counts.

**Thompson sampling for multi-armed bandits.** When there are k arms and outcomes are categorical, maintain a Dirichlet posterior over reward probabilities. Sample one vector per arm, pull the arm with the highest relevant component.

## Exercises

**Basic** — For Dirichlet([2, 3, 5]), compute E[p]. What would you expect if you sampled from this distribution?

**Intermediate** — Simulate 5 samples from Dirichlet([0.1, 0.1, 0.1]) and from Dirichlet([10, 10, 10]). Describe the difference in words.

**Advanced** — Explain how Dirichlet differs from Beta in terms of what it models. Why can't you just use three independent Beta distributions to model a probability vector?
