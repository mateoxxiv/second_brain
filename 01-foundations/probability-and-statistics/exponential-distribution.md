---
tags:
  - status/growing
  - probability
related:
  - "[[probability-distributions]]"
  - "[[poisson-distribution]]"
domain: probability
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.packtpub.com/"
  - "https://en.wikipedia.org/wiki/Exponential_distribution"
  - "https://brilliant.org/wiki/queuing-theory/"
---

> **TL;DR** — Time between Poisson events. PDF = λe^{−λx}. Memoryless property: having already waited s units tells you nothing about how much longer you'll wait.

---

## Intuition

If a Poisson process produces events at rate λ, the waiting time until the next event follows Exponential(λ). Same process, two views: Poisson counts events; Exponential times them.

The memoryless property makes it special: whether you just arrived or have been waiting an hour, your expected remaining wait is the same — 1/λ. This is why it is the foundation of queuing theory — the math stays tractable because you never need to track history.

## Mechanics

**Deriving the PDF from survival function:**
P(X > t) = e^{−λt} (probability of no event by time t)

PDF = negative derivative of survival function:
$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

$$E[X] = \frac{1}{\lambda} \qquad \text{Var}(X) = \frac{1}{\lambda^2}$$

**Memoryless property:** P(X > s+t | X > s) = P(X > t) — the only continuous memoryless distribution.

**Proof:** P(X > s+t | X > s) = P(X > s+t) / P(X > s) = e^{−λ(s+t)} / e^{−λs} = e^{−λt} = P(X > t) ✓

```python
import numpy as np

lam = 3.0  # 3 events/hour → expected wait = 20 min

# Verify E and Var
samples = np.random.exponential(scale=1/lam, size=100000)
print(f"E[X]   = {samples.mean():.4f}  (expected {1/lam:.4f})")
print(f"Var(X) = {samples.var():.4f}  (expected {1/lam**2:.4f})")

# Memoryless property: P(X>0.8|X>0.5) should equal P(X>0.3)
s = np.exp(-lam * 0.8) / np.exp(-lam * 0.5)
t = np.exp(-lam * 0.3)
print(f"P(X>0.8|X>0.5) = {s:.6f}")
print(f"P(X>0.3)       = {t:.6f}")
print(f"Equal: {abs(s - t) < 1e-9}")  # True
```

> Runnable: [[code/foundations/exponential_distribution.py]]

## In ML

**Queuing theory (M/M/1).** The standard queuing model assumes both inter-arrival times and service times follow Exponential distributions. The memoryless property makes the math tractable — the queue's state at any moment fully describes its future behavior.

**Survival analysis.** Exponential is the simplest survival model: constant hazard rate (probability of "failure" per unit time is always λ, regardless of age). Used as a baseline before fitting more complex models.

**Inverse transform sampling.** The Exponential has a clean closed-form inverse CDF: F^{-1}(p) = −ln(1−p)/λ. This makes it easy to generate synthetic Exponential samples from Uniform(0,1) — a building block for simulation.

## Exercises

**Basic** — If λ = 2 events/hour, what is E[wait time]? Verify with a simulation of 100,000 samples.

**Intermediate** — Prove the memoryless property algebraically using the survival function. Show P(X > s+t | X > s) = P(X > t).

**Advanced** — Explain why only the Exponential is memoryless among continuous distributions. What does the geometric distribution (discrete) have to do with this?
