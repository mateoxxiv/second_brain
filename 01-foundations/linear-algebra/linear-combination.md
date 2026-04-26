---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[vector-operations]]"
  - "[[basis-and-dimension]]"
  - "[[linear-independence]]"
  - "[[projection-onto-subspaces]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=k7RM-ot2NWY"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Scale some vectors, add them up. That's a linear combination — and it's the single operation behind every ML computation: neurons, gradient updates, PCA reconstructions, regression predictions.

---

## Intuition

Think of mixing paint. You have base colors (vectors) and you choose how much of each to use (coefficients). Different amounts of the same bases produce different results. The bases are fixed — the coefficients are your degrees of freedom.

The set of *all* reachable results is the **span** — everything you can mix from those bases. Adding a new color expands the span only if it's genuinely new (not a blend of what you already have).

**Coordinates ARE coefficients.** When you write $\mathbf{v} = [3, 2]$, you're saying: use 3 units of $\mathbf{e}_1$ and 2 units of $\mathbf{e}_2$. Change the basis → same point, different numbers.

## Mechanics

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$$

If vectors are [[linear-independence|independent]] (no redundancy), every point has **exactly one** recipe. If dependent, infinitely many recipes produce the same point.

```python
import numpy as np

# Standard basis: coordinates = coefficients
e1, e2 = np.array([1,0]), np.array([0,1])
point = 3*e1 + 2*e2          # [3,2]

# Non-standard basis: same point, different coefficients
b1, b2 = np.array([1,1]), np.array([1,-1])
point2 = 2.5*b1 + 0.5*b2     # also [3,2]

# A neuron IS a linear combination
w = np.array([0.5, -0.3, 0.8])
x = np.array([1.0, 2.0, 0.5])
z = np.dot(w, x)             # 0.3 — weighted sum of inputs
```

> Runnable: [[code/foundations/vectors_and_spaces.py]]

## In ML

**Every neuron** computes $z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b$ — a linear combination of inputs. The network learns the coefficients.

**Gradient descent** — $\mathbf{w}_\text{new} = 1\cdot\mathbf{w} + (-\alpha)\cdot\nabla L$ is a linear combination of the current weights and the gradient.

**PCA reconstruction** — $\hat{\mathbf{x}} = c_1\cdot\text{PC}_1 + c_2\cdot\text{PC}_2 + \cdots$ reconstructs the original data as a linear combination of principal components. The scores $c_i$ are the new coordinates.

## Exercises

**Basic** — Express $[5, 1]$ as a linear combination of $[1, 1]$ and $[1, -1]$. Show your work.

**Intermediate** — If $\mathbf{v}_2 = 2\mathbf{v}_1$, show that the point $[4, 2]$ has infinitely many representations as $c_1\mathbf{v}_1 + c_2\mathbf{v}_2$. Write three different ones.

**Advanced** — Why does having a dependent feature in a regression model cause the weight vector to be non-unique? Connect this directly to linear combinations and the concept of span.
