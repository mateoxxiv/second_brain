---
tags:
  - status/seed
  - probability
related:
  - "[[random-variable]]"
  - "[[discrete-probability-distribution]]"
  - "[[uniform-distribution]]"
  - "[[standard-normal-distribution]]"
  - "[[normal-distribution]]"
  - "[[cdf-and-quantiles]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-1 (Repaso y preámbulo) and §6-2 (Distribuciones uniformes, función de densidad)"
---

> **TL;DR** — For a continuous random variable, probability is **area under the density curve**, never the curve's height — so the total area must be 1, and any single exact value has probability 0.

---

## Intuition

A [[discrete-probability-distribution|discrete distribution]] puts a chunk of probability on each countable value, and a probability histogram's bar *areas* already added to 1. Push that to a [[random-variable|continuous variable]]: there are infinitely many values, so no single value can get a positive chunk (infinitely many chunks would sum to ∞). The bars shrink to zero width and melt into a smooth curve, and what survives is the idea that **area = probability**.

Think of the curve as a *density* in the physical sense: mass per unit length. A density tells you how crowded probability is near $x$; you only get actual probability by multiplying by a width, meaning by taking an area.

## Mechanics

A **density function** $f(x)$ is the graph of a continuous probability distribution. It must satisfy two requirements (Triola):

| Requirement | Formula | Why it matters |
|---|---|---|
| Total area is 1 | $\int_{-\infty}^{\infty} f(x)\,dx = 1$ | something must happen; this is what makes area = probability |
| Never below the x-axis | $f(x) \ge 0$ for all $x$ | negative area would give negative probability |

Probabilities come from integrating over an interval:

$$P(a \le X \le b) = \int_a^b f(x)\,dx$$

**Single points have probability 0.** $P(X=a)=\int_a^a f(x)\,dx = 0$: a vertical line has no area. Consequences:
- $P(a \le X \le b) = P(a < X < b)$, so ≤ vs. < does not matter (unlike the binomial, where it matters a lot).
- "At most $b$" and "less than $b$" give the same probability. Still translate phrases like *at least* and *no more than* carefully.
- Example: P(a person is *exactly* 68.12345678 in tall) = 0.

**Height is not probability.** $f(x)$ can exceed 1. Uniform on $[0, 0.5]$ has height 2 so that $0.5 \times 2 = 1$.

```python
from scipy import stats
from scipy.integrate import quad

f = stats.norm(0, 1).pdf
print(quad(f, -float("inf"), float("inf"))[0])  # 1.0  → requirement 1
print(quad(f, -1, 1)[0])                         # 0.6827 = P(-1 ≤ Z ≤ 1), an area
print(stats.uniform(0, 0.5).pdf(0.2))            # 2.0 → density > 1 is fine
```

## In ML

**Likelihood of continuous data uses densities.** When you fit a Gaussian model or a regression with Gaussian noise, the "likelihood" is a product of *density values*, not probabilities. That is why a continuous negative log-likelihood can be **negative**: densities can be > 1, so their logs can be positive.

**Generative models must stay normalized.** Normalizing flows and VAEs are built so that the learned $f(x)$ still integrates to 1 (requirement 1). Flows track this with the change-of-variables Jacobian, and energy-based models struggle precisely because the normalizing constant is intractable.

## Exercises

**Basic** — A density is $f(x)=c$ on $[2, 6]$ and 0 elsewhere. Find $c$, then $P(3 < X \le 5)$.

**Intermediate** — Is $f(x) = 2x$ on $[0,1]$ a valid density? Compute $P(X \le 0.5)$ and explain why it is not 0.5 even though 0.5 is the midpoint.

**Advanced** — A model reports a log-density of $+3.2$ for a data point. Explain why this is not a bug, and why comparing such log-likelihoods across datasets measured in different units (cm vs. m) is meaningless.
