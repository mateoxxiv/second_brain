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
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.5"
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

**Definition (Anton §4.5):** S = {v₁, v₂, ..., vᵣ} is a **basis** for V iff:
1. S is **linearly independent** — no redundancy
2. S **spans** V — every vector in V is a linear combination of S

Both conditions are required. Independent but not spanning = incomplete. Spanning but dependent = wasteful.

**Standard bases:**

| Space | Standard basis | Dimension |
|---|---|---|
| Rⁿ | {e₁, e₂, ..., eₙ} — unit vectors | n |
| P₂ | {1, x, x²} | 3 |
| P₃ | {1, x, x², x³} | 4 |
| M₂₂ (2×2 matrices) | {E₁₁, E₁₂, E₂₁, E₂₂} — one 1 in each entry, rest 0 | 4 |
| Mₘₙ (m×n matrices) | analogous entry-matrices, one per position | m·n |
| A line through origin | any one non-zero vector on it | 1 |
| A plane through origin | any two independent vectors on it | 2 |

**Why matrix spaces are easy to count**: a matrix is literally a grid of independent numbers — changing one entry doesn't affect any other — so the dimension is just the entry count (rows × columns). Don't confuse this with the *shape* of an individual matrix: "M₂₂" means each element is a 2×2 grid, but the *space itself* has dimension 4, not 2 — same trap as "P₂" describing max degree 2 while the space has dimension 3.

**Why {1, x, x²} is a basis for P₂:** every polynomial a + bx + cx² is uniquely determined by three numbers (a, b, c) — the coefficients. These are exactly the coordinates in this basis. The dimension of P₂ is 3, not because it has 3 terms, but because you need exactly 3 independent functions to span it.

**Dimension** = number of vectors in any basis of V. All bases of the same space have the same size — dimension is an intrinsic property of V, not of any particular basis. The zero vector space has dimension 0.

**Theorem 8 (Anton §4.5):** Any two bases for a finite-dimensional vector space have the same number of vectors. This is why dimension is well-defined — it doesn't matter which basis you pick, the count is always the same.

**General rule:** Rⁿ has dimension n. Pₙ has dimension **n+1** (the standard basis {1, x, ..., xⁿ} has n+1 vectors, not n).

**Theorem 9 — the shortcut:** If dim(V) = n and S has exactly n vectors, you only need to check ONE condition:
- (a) S independent → S is automatically a basis (spanning follows for free)
- (b) S spans V → S is automatically a basis (independence follows for free)
- (c) S independent with r < n vectors → S can always be extended to a full basis

**Example (Theorem 9a):** v₁=(-3,7), v₂=(5,5) in R². Neither is a scalar multiple of the other → independent. R² has dim 2 and S has 2 vectors → S is a basis. Done — no need to verify spanning.

**Basis for null space (Example 35):** The solution space of a homogeneous system Ax=0 has a basis formed by the free-variable vectors from Gaussian elimination. Dimension = number of free variables.

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


## In ML

**PCA is a change of basis.** Your data starts in the feature space (age, income, height). PCA rotates to a new basis where coordinates are uncorrelated (principal components), ordered by variance. Dropping low-variance components = dimensionality reduction.

**Intrinsic dimension** — 784-pixel images don't use all 784 dimensions equally. They live on a lower-dimensional surface. PCA estimates the intrinsic dimension by counting how many components capture most variance.

**[[eigenvalues-and-eigenvectors|Eigenvectors]]** define the "natural" basis of a linear transformation — the directions along which the matrix only stretches, never rotates.

## Exercises

**Basic** — Verify that $\{[1,1], [1,-1]\}$ is a basis for $\mathbb{R}^2$. Express $[4, 2]$ in this basis.

**Intermediate** — What is the dimension of the subspace $\{(x,y,z) : x + 2y - z = 0\}$? Find a basis for it.

**Advanced** — Why does PCA produce orthogonal principal components? Connect this to the spectral theorem and [[eigenvalues-and-eigenvectors]].
