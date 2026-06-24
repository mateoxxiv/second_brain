---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[determinant]]"
  - "[[adjugate-matrix]]"
  - "[[matrix-inverse]]"
  - "[[gaussian-elimination]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — A cofactor is the determinant of a submatrix (the minor) multiplied by a ± sign from a checkerboard pattern. Summing cofactors along any row or column gives the full determinant.

---

## Intuition

Computing the [[determinant]] of a big matrix feels overwhelming. Cofactor expansion solves this by breaking it down: pick any row or column, and express the determinant as a sum of smaller determinants — each from the submatrix left after removing one row and one column.

The ± sign comes from the position in a checkerboard pattern. Think of a chess board: each square is either + or −, alternating. The sign tells you whether a given submatrix contributes positively or negatively to the total area/volume.

## Mechanics

**Minor** $M_{ij}$ — determinant of the $(n-1)\times(n-1)$ submatrix formed by deleting row $i$ and column $j$.

**Cofactor** — minor with a position-based sign:

$$C_{ij} = (-1)^{i+j}\, M_{ij}$$

**Sign (checkerboard) pattern:**

$$\begin{bmatrix}+&-&+\\-&+&-\\+&-&+\end{bmatrix}$$

**Cofactor expansion** — expand along any row $i$ or column $j$:

$$\det(A) = \sum_{j=1}^n a_{ij}\, C_{ij} \qquad \text{(along row } i\text{)}$$

The choice of row or column never changes the result — pick the one with the most zeros.

**Worked example** — $A = \begin{bmatrix}1&2&3\\0&4&5\\1&0&6\end{bmatrix}$, expanding along row 1:

$$\det(A) = 1\cdot C_{11} + 2\cdot C_{12} + 3\cdot C_{13}$$
$$= 1\cdot\det\begin{bmatrix}4&5\\0&6\end{bmatrix} - 2\cdot\det\begin{bmatrix}0&5\\1&6\end{bmatrix} + 3\cdot\det\begin{bmatrix}0&4\\1&0\end{bmatrix}$$
$$= 1(24) - 2(-5) + 3(-4) = 24 + 10 - 12 = 22$$

```python
import numpy as np

def cofactor(A, i, j):
    minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
    return ((-1) ** (i + j)) * np.linalg.det(minor)

A = np.array([[1,2,3],[0,4,5],[1,0,6]], dtype=float)

# Cofactor expansion along row 0
det = sum(A[0, j] * cofactor(A, 0, j) for j in range(3))
print(det)                          # 22.0
print(np.linalg.det(A))             # 22.0 ✓
```


## In ML

**[[determinant]] computation** — cofactor expansion is the recursive definition behind every determinant algorithm. For small matrices (2×2, 3×3) it is practical; for large matrices, [[gaussian-elimination]] (product of pivots) is $O(n^3)$ vs $O(n!)$ for full expansion.

**Building the [[adjugate-matrix]]** — collect all $n^2$ cofactors into the cofactor matrix $C$; transposing it gives the adjugate, which leads directly to the closed-form inverse.

## Exercises

**Basic** — Compute $C_{23}$ for $A = \begin{bmatrix}2&1&0\\1&3&1\\0&1&2\end{bmatrix}$. (Delete row 2, column 3, compute the remaining 2×2 determinant, apply the sign.)

**Intermediate** — Expand $\det(A)$ from the same matrix along column 1. Then expand along row 3. Verify both give the same result.

**Advanced** — Why is expanding along a row with many zeros faster? Formalise the cost: if row $i$ has $k$ non-zero entries, how many $(n-1)\times(n-1)$ determinants do you actually need to compute?
