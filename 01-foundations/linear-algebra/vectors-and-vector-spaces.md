---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[vector-operations]]"
  - "[[vector-norms]]"
  - "[[basis-and-dimension]]"
  - "[[linear-independence]]"
  - "[[projection]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=fNk_zzaMoSs"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — A vector is an ordered list of numbers describing a thing with many attributes. A vector space is the set of rules that let you combine vectors freely without "breaking out" of the space.

---

## Intuition

Forget arrows. A vector is just a list of measurements about one thing:

```
Patient:          [35, 72, 120, 68]   → age, weight, bp, heart rate → R^4
Grayscale image:  [0.2, 0.8, ..., 0.5] → 784 pixel values → R^784
Word embedding:   [0.23, -0.87, 1.05]  → meaning in R^1536
```

A **vector space** is the playground where these vectors live. It guarantees two things: add two vectors → get another valid vector; scale a vector → stay in the space. These are called *closure* properties.

Why closure matters: gradient descent computes $\mathbf{w}_\text{new} = \mathbf{w} - \alpha\nabla L$. If subtraction could "escape" the space, the update would be meaningless.

A **subspace** is a smaller space living inside a bigger one. Must contain **0**, and be closed under addition and scaling. The xy-plane inside R³ is a subspace. A plane shifted away from the origin is not (missing **0**).

## Mechanics

A vector $\mathbf{v} \in \mathbb{R}^n$ is an ordered tuple of $n$ real numbers. The **8 axioms** (commutativity, associativity, zero element, inverses, distributivity) guarantee all the expected arithmetic works.

In practice, you only need to check closure — everything else is inherited from $\mathbb{R}^n$.

**Subspace test** (3 steps):
1. Does it contain **0**?
2. Closed under addition?
3. Closed under scalar multiplication?

```python
import numpy as np

patient = np.array([35.0, 72.0, 120.0, 68.0])
another = np.array([28.0, 65.0, 110.0, 72.0])
combined = patient + another   # still in R^4
scaled = 0.5 * patient         # still in R^4

# Subspace check: xy-plane in R^3
v1 = np.array([3.0, 4.0, 0.0])   # z = 0
v2 = np.array([1.0, -2.0, 0.0])  # z = 0
print((v1 + v2)[2] == 0)          # True — closure holds
```


## In ML

**PCA** finds the subspace where your data actually lives. 784-dimensional images don't use all 784 dimensions equally — they live on a lower-dimensional subspace. PCA finds it.

**Linear regression** — the prediction $\hat{\mathbf{y}}$ lives in the column space of $X$ (a subspace). The residual is always perpendicular to it.

**Null space** — vectors that a matrix maps to zero. Dead neurons in a network live here.

## Exercises

**Basic** — Is the set $\{(x, y, 1) : x, y \in \mathbb{R}\}$ a subspace of $\mathbb{R}^3$? Why or why not?

**Intermediate** — Prove that the set of all vectors in $\mathbb{R}^3$ with $x + y + z = 0$ is a subspace. What is its dimension?

**Advanced** — If your model has two perfectly correlated features ($x_2 = 2x_1$), what does that say about the column space of $X$? What happens when you try to solve the normal equations?
