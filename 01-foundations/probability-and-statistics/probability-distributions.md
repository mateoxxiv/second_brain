---
tags:
  - status/growing
  - probability
related:
  - "[[probability-fundamentals]]"
  - "[[bernoulli-distribution]]"
  - "[[binomial-distribution]]"
  - "[[normal-distribution]]"
  - "[[poisson-distribution]]"
  - "[[exponential-distribution]]"
  - "[[beta-distribution]]"
  - "[[dirichlet-distribution]]"
domain: probability
sources:
  - "https://www.youtube.com/watch?v=zeJD6dqJ5lo"
  - "https://www.packtpub.com/"
  - "https://www.khanacademy.org/math/statistics-probability"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — A distribution describes all outcomes and their likelihoods. Expectation = weighted average. Variance = spread. The right distribution depends on what you're modeling.

---

## Intuition

A distribution is the complete answer to "what values can X take and how likely is each?" Two numbers summarize any distribution: the **expectation** (where it's centered) and the **variance** (how spread out it is).

Distributions come in two flavors: **parametric** (defined by a formula — Normal, Bernoulli, Poisson) and **empirical** (derived from data, no shape assumption — bootstrap, permutation tests).

## Mechanics

**Expectation:**
$$E[X] = \sum_x x \cdot P(X = x) \quad \text{(discrete)}$$

**Variance:**
$$\text{Var}(X) = E[X^2] - (E[X])^2$$

**Quick reference table:**

| Distribution | Parameters | E[X] | Var(X) | Use in ML |
|-------------|-----------|------|--------|-----------|
| Bernoulli | p | p | p(1−p) | Binary classification |
| Binomial | n, p | np | np(1−p) | n trials, cross-entropy |
| Normal | μ, σ² | μ | σ² | Noise, weight init, MSE |
| Poisson | λ | λ | λ | Count prediction, NLP |
| Exponential | λ | 1/λ | 1/λ² | Inter-arrival times |
| Beta | α, β | α/(α+β) | complex | Bayesian A/B testing |
| Dirichlet | α vector | αᵢ/Σαⱼ | complex | Topic models (LDA) |

**Decision tree:**
```
Count (how many events)?  → mean ≈ var? Poisson. var < mean? Binomial.
Wait time?                → Exponential
Binary outcome?           → Bernoulli (single) or Binomial (n trials)
Continuous measurement?   → Normal
Uncertainty about p?      → Beta (2 categories) / Dirichlet (k categories)
```

```python
import numpy as np

data = np.array([2.1, 3.4, 2.8, 3.1, 4.0, 2.5, 3.7, 2.9])
bootstrap_means = [np.random.choice(data, len(data), replace=True).mean()
                   for _ in range(10000)]
lo, hi = np.percentile(bootstrap_means, [2.5, 97.5])
print(f"Bootstrap 95% CI: [{lo:.3f}, {hi:.3f}]")
```

> Runnable: [[code/foundations/probability_distributions.py]]

## In ML

**MSE assumes Gaussian noise.** Choosing MSE as a loss function is equivalent to assuming the residuals are normally distributed. If your target has heavy-tailed noise, MSE is the wrong loss — use MAE or Huber loss.

**Cross-entropy comes from Bernoulli MLE.** The binary cross-entropy loss is the exact negative log-likelihood of Bernoulli-distributed labels. Using the right distribution leads directly to the right loss function.

**Conjugate priors make Bayesian updates easy.** When the prior and posterior are the same family (Beta-Binomial, Dirichlet-Multinomial), Bayesian updating reduces to adding counts. This closed-form update is why these distributions dominate Bayesian ML.

## Exercises

**Basic** — Identify the right distribution for: (a) number of clicks per hour, (b) coin flip outcome, (c) height of people, (d) time until next server request.

**Intermediate** — Compute E[X] and Var(X) for Bernoulli(0.3) from the definition. Verify numerically by sampling.

**Advanced** — Explain what happens when you use MSE loss for a target with heavy-tailed (Laplace) noise. What loss function would be correct?
