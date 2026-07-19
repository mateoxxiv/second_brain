---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[determinant]]"
  - "[[cofactor]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[special-matrices]]"
domain: linear-algebra
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — For a block diagonal (or block triangular) matrix, the determinant is just the product of each diagonal block's own determinant — no need to expand the whole matrix at once.

---

## Intuition

A block diagonal matrix acts on two (or more) completely separate groups of coordinates independently — a top-left block only ever touches its own coordinates, a bottom-right block only touches its own, and the zero blocks guarantee they never mix. Since the two sub-transformations are independent, the *total* volume scaling ([[determinant|the determinant]]) is just the product of each piece's own scaling — the same way stretching 2× in one independent direction and 3× in a completely separate direction gives 2×3=6× the overall volume.

## Mechanics

**Theorem** — for a block diagonal matrix $M = \begin{bmatrix}A & 0\\0 & B\end{bmatrix}$ (A is m×m, B is n×n, the 0's are zero blocks of matching size):

$$\det(M) = \det(A)\cdot\det(B)$$

This extends to any number of diagonal blocks — with k blocks, the determinant is the product of all k blocks' determinants.

**It also works for block *triangular* matrices** — only one off-diagonal block needs to be zero (the other can have anything in it); the formula is unchanged.

**Why it's true** — from the [[determinant|Leibniz formula]]: det sums over every permutation of rows/columns, picking one entry per row without repeating a column. Any permutation that pairs an A-block row with a B-block column (or vice versa) is forced to land on a zero entry, contributing nothing. Only permutations that stay entirely within the A-block indices or entirely within the B-block indices survive — so the giant sum cleanly splits into `(sum over A's own permutations) × (sum over B's own permutations)`, which is exactly $\det(A)\cdot\det(B)$.

**Bonus — eigenvalues too**: the eigenvalues of a block diagonal matrix are just the combined eigenvalues of each block (union, with multiplicity). You never need to solve one big characteristic equation — solve each block's smaller one instead.

**Worked example** — for $A-\lambda I = \begin{bmatrix}10-\lambda & -9 & 0 & 0\\4 & -2-\lambda & 0 & 0\\0 & 0 & -2-\lambda & -7\\0 & 0 & 1 & 2-\lambda\end{bmatrix}$:

$$\det = \det\begin{bmatrix}10-\lambda & -9\\4 & -2-\lambda\end{bmatrix}\cdot\det\begin{bmatrix}-2-\lambda & -7\\1 & 2-\lambda\end{bmatrix} = (\lambda-4)^2(\lambda^2+3)$$

Two easy 2×2 determinants instead of one messy 4×4 cofactor expansion.

```python
import numpy as np
from scipy.linalg import block_diag

A = np.array([[10,-9],[4,-2]], dtype=float)
B = np.array([[-2,-7],[1,2]], dtype=float)
M = block_diag(A, B)

print(np.linalg.det(M))                       # full 4x4 determinant
print(np.linalg.det(A) * np.linalg.det(B))    # shortcut — matches exactly
```

## In ML

**Independent feature groups (covariance structure)** — a block-diagonal covariance matrix means groups of correlated features exist, but the groups are independent of each other. Its determinant (needed for the Gaussian normalization constant) factors into the product of each group's smaller determinant — far cheaper than inverting one giant covariance matrix.

**K-FAC and structured optimizers** — some second-order optimization methods (e.g. Kronecker-Factored Approximate Curvature) deliberately approximate a neural network's huge Fisher information / Hessian matrix as block diagonal (one block per layer), specifically to make otherwise-intractable determinant and inverse computations cheap — the exact shortcut from this note, applied at massive scale.

**[[eigenvalues-and-eigenvectors]] for structured matrices** — as seen in the worked example, block structure turns one hard eigenvalue problem into several easy ones — a recurring theme any time a matrix has independent substructure.

## Exercises

**Basic** — Compute $\det\begin{bmatrix}2&0&0\\0&3&1\\0&2&1\end{bmatrix}$ using the block shortcut (1×1 block + 2×2 block).

**Intermediate** — Verify the shortcut also holds for a block *triangular* (not fully diagonal) matrix: take $M=\begin{bmatrix}2&0&5\\0&3&7\\0&0&4\end{bmatrix}$ and confirm $\det(M)$ equals the product of the diagonal blocks despite the nonzero 5 and 7.

**Advanced** — Prove the theorem for 3 diagonal blocks by applying the 2-block case twice (treat the first block as one unit and "the rest" as a second block, then recurse).
