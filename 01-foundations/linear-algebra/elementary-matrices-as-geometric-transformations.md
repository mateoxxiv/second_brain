---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[geometry-of-planar-linear-transformations]]"
  - "[[gaussian-elimination]]"
  - "[[determinant]]"
  - "[[special-matrices]]"
  - "[[matrix-of-linear-transformation]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.3"
---

> **TL;DR** — Every elementary matrix (one row operation applied to $I$) *is* one of the five geometric primitives — a shear, a reflection about $y=x$, or an axis-aligned scaling — so Gaussian elimination is literally a sequence of shape distortions applied to a matrix's columns.

---

## Intuition

[[gaussian-elimination]] reduces a matrix using three row operations: add a multiple of one row to another, swap two rows, scale a row. Each operation, applied once to $I$, produces an **elementary matrix** — and left-multiplying by it reproduces that operation. Since an elementary matrix is itself a standard matrix ([[matrix-of-linear-transformation]]), it must correspond to *some* geometric transformation. The surprise: it's always one of the primitives already catalogued in [[geometry-of-planar-linear-transformations]] — row reduction isn't an abstract bookkeeping trick, it's shearing, reflecting, and rescaling a shape step by step until it becomes the identity.

## Mechanics

**Theorem (Anton §5.3, Example 24)** — If $T:\mathbb{R}^2\to\mathbb{R}^2$ is multiplication by a $2\times2$ elementary matrix, $T$ is one of:

| Row operation on $I_2$ | Resulting matrix | Geometric identity |
|---|---|---|
| Add $k\times$ row to the other | $\begin{bmatrix}1&k\\0&1\end{bmatrix}$, $\begin{bmatrix}1&0\\k&1\end{bmatrix}$ | shear along an axis |
| Swap the two rows | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ | reflection about $y=x$ |
| Scale a row by $k$ | $\begin{bmatrix}k&0\\0&1\end{bmatrix}$, $\begin{bmatrix}1&0\\0&k\end{bmatrix}$ | expansion/compression along an axis |

**The scaling row splits further when $k<0$** — write $k=-k_1$ with $k_1>0$:
$$\begin{bmatrix}k&0\\0&1\end{bmatrix} = \begin{bmatrix}-1&0\\0&1\end{bmatrix}\begin{bmatrix}k_1&0\\0&1\end{bmatrix} \quad (5.13)$$
i.e. an $x$-scaling by $k_1$ followed by a reflection about the $y$-axis (analogous decomposition (5.14) holds for the $y$-row, reflecting about the $x$-axis). When $k=-1$ exactly, this collapses to a pure axis reflection — no scaling left over.

**Determinant check** — this matches [[determinant]]'s volume-scaling reading directly: shears have $\det=1$ (area preserved, no scaling — consistent with them being *pure* shape distortion), the swap/reflection has $\det=-1$ (area preserved but orientation flipped), and the scaling row has $\det=k$ (area literally multiplied by $k$).

```python
import numpy as np

shear = np.array([[1, 3], [0, 1]])
swap = np.array([[0, 1], [1, 0]])
scale = np.array([[-2, 0], [0, 1]])   # k = -2 -> reflection + expansion

for name, M in [("shear", shear), ("swap", swap), ("scale k=-2", scale)]:
    print(name, "det =", round(np.linalg.det(M), 4))
# shear det = 1.0 | swap det = -1.0 | scale k=-2 det = -2.0
```

**Theorem 5 (Anton §5.3)** — generalizes the table above from *one* elementary matrix to *any* invertible matrix: if $A$ is invertible, its geometric effect equals that of an appropriate sequence of shears, expansions/compressions, and reflections *only* — no other primitive (not even rotation, which itself decomposes into these) is needed. **Proof** — row-reduce $A$ to $I$ via elementary operations, i.e. $E_k\cdots E_2E_1A=I$; solving for $A$ gives
$$A = E_1^{-1}E_2^{-1}\cdots E_k^{-1} \quad (5.15)$$
Since the inverse of an elementary matrix is itself elementary, $A$ is a product of elementary matrices — each one geometrically identified by the table above, applied in the order given by reading (5.15) right to left.

**Worked example (Anton Example 27)** — $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ row-reduces to $I$ via: add $-3\times$row 1 to row 2, scale row 2 by $-\tfrac12$, add $-2\times$row 2 to row 1. Inverting and reordering per (5.15) shows multiplying by $A$ equals: shear $x$ by factor $2$ $\to$ expand $y$ by factor $2$ $\to$ reflect about the $x$-axis $\to$ shear $x$ by factor $3$ — four primitive steps, read off directly from the elimination record.

## In ML

**LU decomposition** — Gaussian elimination on $A$ produces $A = LU$, where $L$ is built from the shear-type elementary matrices recording each row operation. Seeing those steps as shears (area-preserving, cheap, reversible) explains why LU-based solves are computationally efficient — each elimination step is a minimal shape distortion, not a full re-derivation of $A$.

**Normalizing flows** — a flow builds a complex invertible map by composing simple layers, each with an easily-computed Jacobian determinant; elementary matrices are the linear-algebra prototype of this idea — decompose any invertible matrix into simple, individually-understood pieces and multiply their determinants for the total volume change.

**Why $\det(AB)=\det(A)\det(B)$ feels obvious geometrically** — since every invertible matrix factors into elementary matrices (row-reduce it to $I$ and invert the steps), and each elementary matrix has a known, simple determinant, the product rule for determinants is just "each shape distortion compounds the last."

## Exercises

**Basic** — Identify the geometric type (shear / reflection / scaling) of $\begin{bmatrix}1&0\\-4&1\end{bmatrix}$ and of $\begin{bmatrix}1&0\\0&-3\end{bmatrix}$.

**Intermediate** — Decompose $\begin{bmatrix}-5&0\\0&1\end{bmatrix}$ into a reflection composed with an expansion, following (5.13). Verify the product by hand.

**Advanced** — Every invertible $2\times2$ matrix can be row-reduced to $I$, hence written as a product of elementary matrices. Take $A=\begin{bmatrix}2&1\\1&1\end{bmatrix}$, row-reduce it to $I$ recording each elementary matrix, and reconstruct $A$ as that product — then classify each factor geometrically using the table above.
