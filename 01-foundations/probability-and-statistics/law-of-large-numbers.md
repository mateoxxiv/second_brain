---
tags:
  - status/seed
  - probability
related:
  - "[[three-methods-of-assigning-probability]]"
  - "[[measures-of-center]]"
  - "[[probability-fundamentals]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-2."
---

> **TL;DR** — The **Law of Large Numbers**: as a procedure is repeated more and more, the **relative-frequency** estimate of an event's probability converges toward the *true* probability.

---

## Intuition

Flip a fair coin 10 times and you might see 7 heads (0.70) — nowhere near 0.5. Flip it 10,000 times and you'll be hugging 0.500. That's the whole idea: a probability estimate built on a handful of trials can be wildly off, but pile up enough trials and the estimate is squeezed toward the truth. It's the common-sense justification for *why* the [[three-methods-of-assigning-probability|relative-frequency method]] works at all — and equally a warning that a *small* sample's estimate deserves no trust.

Note what it does **not** say: it makes no promise about any single next trial. After 10 heads in a row, the coin is not "due" for tails — that's the gambler's fallacy. Convergence is about the *long-run proportion*, not about the universe balancing short-run streaks.

## Mechanics

Let $\hat{p}_n = \dfrac{\#\text{ occurrences in } n \text{ trials}}{n}$ be the relative frequency after $n$ trials. As $n \to \infty$,

$$\hat{p}_n \longrightarrow P(A) \quad \text{(the true probability)}$$

The estimate isn't monotone — it wobbles — but the *amplitude* of the wobble shrinks with $n$. Concretely, the standard error of a proportion falls like $1/\sqrt{n}$: to halve your typical error you need **four times** the data. Diminishing returns are baked in.

```python
import numpy as np
rng = np.random.default_rng(0)
flips = rng.integers(0, 2, size=10_000)          # fair coin
running = np.cumsum(flips) / np.arange(1, 10_001)
print(running[9], running[99], running[9999])    # 0.40, 0.56, 0.503
```

## In ML

**It's why Monte Carlo works.** Approximating an expectation $\mathbb{E}[f(X)]$ by the sample mean $\frac1n\sum f(x_i)$ is justified *entirely* by the LLN — the average of many simulated draws converges to the true expected value. Same engine behind bootstrap estimates and MCMC.

**It underwrites SGD and mini-batches.** A mini-batch gradient is a relative-frequency-style estimate of the true (full-dataset) gradient; larger batches give lower-variance estimates by the same $1/\sqrt{n}$ law. It also explains why **test accuracy on a tiny test set is unreliable** — a 20-example test set's error estimate can be far from the true error.

## Exercises

**Basic** — You estimate a webpage's click-through rate from 5 visits (1 click → 0.20) vs. 5,000 visits (1,000 clicks → 0.20). Both give 0.20 — which do you trust, and why?

**Intermediate** — Using the $1/\sqrt{n}$ rule, if 100 trials give a typical error of 0.05 in an estimated probability, roughly how many trials to cut the typical error to 0.01?

**Advanced** — A gambler argues: "The LLN says the proportion of heads → 0.5, so after 8 straight heads, tails is more likely next." Identify the fallacy precisely, and explain how the proportion can still converge to 0.5 *without* any single trial being "corrected."
