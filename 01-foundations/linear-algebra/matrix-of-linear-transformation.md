---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[linear-transformations]]"
  - "[[kernel-and-range]]"
  - "[[rank-nullity-theorem]]"
  - "[[matrix-operations]]"
  - "[[euclidean-n-space]]"
  - "[[geometry-of-planar-linear-transformations]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.3"
---

> **TL;DR** — Every linear transformation $T:\mathbb{R}^n \to \mathbb{R}^m$ is multiplication by one specific matrix — its **standard matrix** $A$, built by stacking $T(e_1), \dots, T(e_n)$ as columns.

---

## Intuition

Any $T$ looks arbitrary until you notice one thing: a linear $T$ is completely determined by what it does to a **basis**, because every other vector is just a linear combination of basis vectors, and $T$ preserves linear combinations ([[linear-transformations]]'s superposition property). So instead of describing $T$ by a formula, you can describe it by **n snapshots** — where does it send each standard basis vector $e_1, \dots, e_n$? Line those snapshots up as columns of a matrix, and multiplying by that matrix reproduces $T$ exactly, for every input, not just the basis vectors.

## Mechanics

**Theorem (Anton §5.3)** — If $T:\mathbb{R}^n \to \mathbb{R}^m$ is linear, there is a unique $m \times n$ matrix $A$, the **standard matrix for $T$**, such that $T(\mathbf{x}) = A\mathbf{x}$ for every $\mathbf{x} \in \mathbb{R}^n$:

$$A = \begin{bmatrix} T(e_1) & T(e_2) & \cdots & T(e_n) \end{bmatrix}$$

**Proof** — Write $\mathbf{x} = x_1e_1 + \cdots + x_ne_n$ (standard-basis decomposition). By linearity:
$$T(\mathbf{x}) = x_1T(e_1) + \cdots + x_nT(e_n) \quad (5.7)$$
Now compute $A\mathbf{x}$ directly, column by column, using the definition of matrix-vector multiplication:
$$A\mathbf{x} = x_1T(e_1) + \cdots + x_nT(e_n) \quad (5.8)$$
(5.7) and (5.8) are identical, so $T(\mathbf{x}) = A\mathbf{x}$ for every $\mathbf{x}$ — $T$ *is* multiplication by $A$. Since a matrix is determined by its columns and the columns are forced to be $T(e_i)$, $A$ is unique.

**Worked example** — $T(x_1,x_2) = (x_1+2x_2,\ x_1-x_2)$. Evaluate on the basis: $T(e_1) = (1,1)$, $T(e_2) = (2,-1)$. Stack as columns:
$$A = \begin{bmatrix}1 & 2\\ 1 & -1\end{bmatrix}$$

**Reading a matrix as a transformation (the reverse direction)** — this also means *any* $m\times n$ matrix $A$ already **is** the standard matrix for some $T:\mathbb{R}^n\to\mathbb{R}^m$, namely the one applying the standard basis of $\mathbb{R}^n$ onto $A$'s columns. E.g. $A=\begin{bmatrix}1&-2&1\\3&4&6\end{bmatrix}$ is standard matrix for the $T:\mathbb{R}^3\to\mathbb{R}^2$ sending $e_1,e_2,e_3 \mapsto (1,3), (-2,4), (1,6)$ respectively — no separate check needed, the matrix *is* the transformation.

```python
import numpy as np

def T(x):
    x1, x2 = x
    return np.array([x1 + 2 * x2, x1 - x2])

n = 2
A = np.column_stack([T(e) for e in np.eye(n)])   # evaluate T on each basis vector
print(A)                                          # [[1, 2], [1, -1]]

x = np.array([3, -1])
assert np.allclose(T(x), A @ x)                   # standard matrix reproduces T everywhere
```

## In ML

**Dense layer weights are literally standard matrices** — $\mathbf{z} = W\mathbf{x}$ means column $j$ of $W$ answers "if input feature $j$ were $1$ and everything else $0$, what does this layer output?" That's exactly $T(e_j)$. Reading a trained weight matrix column-by-column is reading off the network's response to each isolated input direction.

**Jacobians generalize this locally** — for a nonlinear map $f$, the Jacobian at a point is the standard matrix of $f$'s *best linear approximation* there; its columns are $\partial f/\partial x_i$, the image of each infinitesimal basis direction. Backprop is built on chaining these local standard matrices.

**Uniqueness enables weight inspection** — because the standard matrix is the *only* matrix representing $T$ in the standard basis, comparing two networks' weight matrices directly compares the linear maps they implement (per layer) — no ambiguity about "which matrix means what."

## Exercises

**Basic** — Find the standard matrix for $T(x,y,z) = (x-z,\ 2y+z)$. Verify by computing $T(1,2,3)$ both from the formula and from $A\mathbf{x}$.

**Intermediate** — You're told a linear $T:\mathbb{R}^2\to\mathbb{R}^2$ satisfies $T(1,1) = (2,0)$ and $T(1,-1) = (0,2)$ — note this is *not* the standard basis. Find the standard matrix for $T$. (Hint: first recover $T(e_1)$ and $T(e_2)$ from these two equations.)

**Advanced** — Prove the uniqueness claim directly: if $A$ and $B$ are both $m\times n$ matrices with $A\mathbf{x} = B\mathbf{x}$ for all $\mathbf{x}\in\mathbb{R}^n$, show $A=B$ by evaluating at $\mathbf{x}=e_i$ for each $i$.
