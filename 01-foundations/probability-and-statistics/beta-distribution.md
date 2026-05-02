---
tags:
  - status/growing
  - probability
related:
  - "[[probability-distributions]]"
  - "[[bernoulli-distribution]]"
  - "[[binomial-distribution]]"
  - "[[dirichlet-distribution]]"
domain: probability
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.packtpub.com/"
  - "https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers"
  - "https://www.countbayesie.com/blog/2015/4/25/bayesian-ab-testing"
---

> **TL;DR** — Models uncertainty about a probability p ∈ [0,1]. Conjugate prior for Bernoulli/Binomial: just add counts to update. Foundation of Bayesian A/B testing.

---

## Intuition

Bernoulli models a binary trial with a known p. But what if you're uncertain about p itself? Beta models your belief about what p might be. Parameters α and β are interpreted as pseudo-counts of successes and failures — the more data you have, the tighter the Beta distribution peaks around the true p.

The conjugate prior property is the killer feature: observe h heads and t tails, and your posterior is simply Beta(α+h, β+t). No integration, no complex math — just add counts.

## Mechanics

**PDF:**
$$f(x; \alpha, \beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}, \quad x \in [0,1]$$

$$E[X] = \frac{\alpha}{\alpha + \beta} \qquad \text{Var}(X) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$$

**Special cases:** Beta(1,1) = Uniform(0,1) — complete ignorance. α=β → symmetric peak at 0.5. α>>β → peaks near 1.

**Conjugate update rule:** Prior Beta(α, β) + observe h successes, t failures → Posterior Beta(α+h, β+t)

```python
import numpy as np

# Conjugate update
alpha_prior, beta_prior = 1, 1   # uninformative prior
h, t = 5, 2                      # observe 5 heads, 2 tails
alpha_post = alpha_prior + h     # 6
beta_post  = beta_prior + t      # 3
print(f"Posterior mean: {alpha_post/(alpha_post+beta_post):.4f}")  # 0.667

# Bayesian A/B test
def ab_test(ca, va, cb, vb, n=100000):
    """P(B > A) via Beta posterior sampling."""
    sa = np.random.beta(1 + ca, 1 + va - ca, n)
    sb = np.random.beta(1 + cb, 1 + vb - cb, n)
    print(f"P(B better than A) = {np.mean(sb > sa):.4f}")

ab_test(ca=40, va=200, cb=50, vb=200)  # ~0.82
```

> Runnable: [[code/foundations/beta_distribution.py]]

## In ML

**Bayesian A/B testing.** Sample from Beta posteriors for variant A and B. Compute P(B > A) by counting Monte Carlo samples. No p-values, no normality assumption, easy to interpret: "there is an 82% probability that B is better."

**Thompson sampling.** Multi-armed bandit algorithm: maintain a Beta(α, β) for each arm's success rate, sample one value from each, pull the arm with the highest sample. As evidence accumulates, the distributions tighten and the best arm dominates.

**Conjugacy and computational efficiency.** The conjugate prior property means Bayesian updates for Bernoulli/Binomial models never require numerical integration — just add counts. This makes Beta-Binomial models tractable even in production systems.

## Exercises

**Basic** — Compute E[X] for Beta(3, 7). What does this tell you about the estimated probability?

**Intermediate** — Interpret Beta(1, 1). What prior knowledge does it encode? What happens to the posterior after seeing 10 heads and 5 tails?

**Advanced** — Explain why the conjugate prior property is computationally valuable. What would you have to do to update beliefs without it?
