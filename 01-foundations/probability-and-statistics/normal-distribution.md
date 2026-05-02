---
tags:
  - status/growing
  - probability
related:
  - "[[probability-distributions]]"
  - "[[probability-fundamentals]]"
  - "[[optimization]]"
  - "[[gradient-descent]]"
  - "[[binomial-distribution]]"
domain: probability
sources:
  - "https://www.youtube.com/watch?v=zeJD6dqJ5lo"
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.packtpub.com/"
  - "https://www.khanacademy.org/math/statistics-probability"
---

> **TL;DR** — Bell-shaped, symmetric. Emerges everywhere via CLT. MSE loss is Normal MLE — not a design choice, a consequence of assuming Gaussian noise.

---

## Intuition

The Normal distribution is the natural shape when many independent random influences add together. Height, measurement error, natural variation — all follow it because they are sums of many small effects (Central Limit Theorem).

The bell shape comes from one principle: maximize entropy (spread probability as widely as possible) subject to having a fixed mean and variance. The Normal distribution is the unique solution.

## Mechanics

**PDF** (motivated by e^{−x²} → add center μ and scale σ → normalize):
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

$$E[X] = \mu \qquad \text{Var}(X) = \sigma^2$$

**Standardization:** Z = (X − μ) / σ → Z ~ N(0,1)

**68-95-99.7 rule:** 1σ covers 68%, 2σ covers 95%, 3σ covers 99.7%.

**CLT statement:** average of n i.i.d. variables with mean μ, variance σ² converges to N(μ, σ²/n).

**MSE from MLE:** assume y = w^T x + ε, ε ~ N(0,σ²). Maximizing log-likelihood over w minimizes Σ(yᵢ − ŷᵢ)² — this is MSE.

```python
import numpy as np

def normal_pdf(x, mu, sigma):
    coeff = 1.0 / (sigma * np.sqrt(2 * np.pi))
    return coeff * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Verify integrates to 1
x = np.linspace(-10, 10, 10000)
area = np.sum(normal_pdf(x, 0, 1)) * (x[1] - x[0])
print(f"Area: {area:.6f}")  # ~1.0

# 68-95-99.7 rule
samples = np.random.normal(0, 1, 100000)
for k in [1, 2, 3]:
    print(f"Within {k}σ: {np.mean(np.abs(samples) <= k):.4f}")
```

> Runnable: [[code/foundations/normal_distribution.py]]

## In ML

**MSE loss assumes Gaussian noise.** If you use MSE for regression, you implicitly assume the residuals are normally distributed. Heavy-tailed noise (outliers) makes this assumption wrong — use MAE or Huber loss instead.

**Weight initialization uses Normal.** Xavier/He initialization draws weights from N(0, σ²) to keep activation variance stable across layers. The choice of σ depends on layer width and activation function.

**VAEs and diffusion models use Normal latent space.** Variational autoencoders encode inputs as (μ, σ) of a Normal distribution. Diffusion models corrupt data by adding Gaussian noise at each step and learn to reverse this process.

## Exercises

**Basic** — Standardize the array [170, 175, 160, 180, 165] and interpret each z-score.

**Intermediate** — Derive why maximizing log-likelihood under Gaussian noise gives MSE. Start from the full log-likelihood expression and simplify.

**Advanced** — Explain why CLT justifies Normal approximations in statistics. What conditions on the original distribution are required for CLT to apply?
