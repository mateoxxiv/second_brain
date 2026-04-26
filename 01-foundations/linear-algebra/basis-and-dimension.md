---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[linear-independence]]"
  - "[[linear-combination]]"
  - "[[vectors-and-vector-spaces]]"
  - "[[projection]]"
  - "[[eigenvalues-and-eigenvectors]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=P2LTAUO1TdA"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — A basis is the minimal coordinate system for a space: independent vectors that together reach every point. The dimension is how many basis vectors you need — an intrinsic property of the space.

---

## Intuition

A **basis** is like compass directions. N and E give you the full 2D plane — maximum coverage with zero redundancy. Adding NE wastes a direction. Having only N leaves you stuck on a line.

**Coordinates are coefficients.** When you write $\mathbf{v} = [3, 2]$, you're saying: 3 units of $\mathbf{e}_1$, 2 units of $\mathbf{e}_2$. Switch to a different basis → same point, different numbers.

**Change of basis** is like switching from GPS to street address. The location doesn't move — only the description changes.

## Mechanics

A set of vectors is a **basis** for space $V$ iff it:
1. **Spans** $V$ — you can reach every point
2. Is **linearly independent** — no redundancy

**Dimension** = number of vectors in any basis of $V$. All bases of the same space have the same size — the dimension is unique.

| Space | Dim | Meaning |
|---|---|---|
| A line through origin | 1 | One free direction |
| A plane through origin | 2 | Two free directions |
| $\mathbb{R}^{784}$ | 784 | 784 independent pixel dimensions |

To find coordinates in a new basis $B = [\mathbf{b}_1 \mid \mathbf{b}_2]$, solve $B\boldsymbol{\alpha} = \mathbf{v}$.

```python
import numpy as np

v = np.array([3.0, 1.0])
B = np.array([[1,1],[1,-1]])      # columns = new basis vectors

# Coordinates in B: solve B @ alpha = v
alpha = np.linalg.solve(B, v)    # [2., 1.]

# Verify: reconstruct v from new basis
v_check = alpha[0]*B[:,0] + alpha[1]*B[:,1]  # [3., 1.] ✓
```

> Runnable: [[code/foundations/vectors_and_spaces.py]]

## In ML

**PCA is a change of basis.** Your data starts in the feature space (age, income, height). PCA rotates to a new basis where coordinates are uncorrelated (principal components), ordered by variance. Dropping low-variance components = dimensionality reduction.

**Intrinsic dimension** — 784-pixel images don't use all 784 dimensions equally. They live on a lower-dimensional surface. PCA estimates the intrinsic dimension by counting how many components capture most variance.

**[[eigenvalues-and-eigenvectors|Eigenvectors]]** define the "natural" basis of a linear transformation — the directions along which the matrix only stretches, never rotates.

## Exercises

**Basic** — Verify that $\{[1,1], [1,-1]\}$ is a basis for $\mathbb{R}^2$. Express $[4, 2]$ in this basis.

**Intermediate** — What is the dimension of the subspace $\{(x,y,z) : x + 2y - z = 0\}$? Find a basis for it.

**Advanced** — Why does PCA produce orthogonal principal components? Connect this to the spectral theorem and [[eigenvalues-and-eigenvectors]].
