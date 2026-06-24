---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[basis-and-dimension]]"
  - "[[linear-independence]]"
  - "[[orthonormal-bases]]"
  - "[[change-of-basis]]"
  - "[[inner-product-spaces]]"
  - "[[gram-schmidt]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introduccion al Algebra Lineal. S4.10 -- Theorem 24, 25, Examples 59-62."
---

> **TL;DR** — Given a basis S, every vector has exactly one set of scalars expressing it as a linear combination of the basis vectors; those scalars are its coordinates relative to S.

---

## Intuition

Every basis defines a coordinate system — a set of "rulers" pointing in the basis directions. The coordinates of a vector are the readings on those rulers: how far to go along each basis direction to reach the vector.

The standard Cartesian axes {i, j, k} are just one choice of rulers. Any basis works, and swapping rulers gives different numbers for the same geometric object. This generalization extends naturally to polynomial spaces, function spaces, and any finite-dimensional vector space.

## Mechanics

**Theorem 24 (Anton S4.10):** If $S = \{v_1, v_2, \ldots, v_n\}$ is a [[basis-and-dimension|basis]] for a vector space $V$, then every $v \in V$ can be expressed in the form $v = c_1 v_1 + c_2 v_2 + \cdots + c_n v_n$ in *exactly one way*.

*Why unique?* Suppose two representations exist. Subtracting gives $\mathbf{0} = \sum (c_i - k_i)v_i$. [[linear-independence|Linear independence]] forces every coefficient to be zero, so $c_i = k_i$.

**Coordinate vector and matrix** — the scalars $c_1, \ldots, c_n$ are the **coordinates** of $v$ relative to $S$:

$$(\mathbf{v})_S = (c_1, c_2, \ldots, c_n) \qquad [\mathbf{v}]_S = \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix}$$

**Finding coordinates** — solve $c_1 v_1 + \cdots + c_n v_n = v$ as a linear system.

| Space | Basis $S$ | Coordinate rule |
|---|---|---|
| $\mathbb{R}^3$ | $\{(1,2,1),(2,9,0),(3,3,4)\}$ | Solve $[v_1\|v_2\|v_3]\,c = v$ |
| $P_2$ | $\{1, x, x^2\}$ | $p = a_0+a_1x+a_2x^2 \Rightarrow (p)_S=(a_0,a_1,a_2)$ by inspection |
| $\mathbb{R}^n$ | Standard $\{e_1,\ldots,e_n\}$ | $(v)_S = v$ — components ARE coordinates |

**ONB shortcut — Theorem 25:** If $S$ is [[orthonormal-bases|orthonormal]], coordinates are just inner products: $c_i = \langle v, v_i \rangle$. No system to solve. The coordinate map also preserves all geometric structure:

$$\|u\| = \sqrt{\textstyle\sum u_i^2}, \quad d(u,v) = \sqrt{\textstyle\sum (u_i-v_i)^2}, \quad \langle u,v\rangle = \textstyle\sum u_i v_i$$

```python
import numpy as np

# General basis: solve a linear system
B = np.array([[1,2,3],[2,9,3],[1,0,4]], dtype=float).T  # columns = basis vectors
v = np.array([5., -1., 9.])
c = np.linalg.solve(B, v)
print(c)   # coordinate vector

# ONB shortcut: coordinates = inner products
Q, _ = np.linalg.qr(np.random.randn(4, 3))   # random ONB for 3D subspace
u = np.random.randn(4)
coords = Q.T @ u                              # c_i = <u, q_i>
print(np.allclose(Q @ coords, Q @ Q.T @ u))  # True
```

## In ML

**Feature vectors** — a feature vector $x \in \mathbb{R}^d$ is the coordinate vector of a data point relative to the standard basis. PCA switches to a more informative basis (eigenvectors of the covariance matrix); the PCA scores are the new coordinate vector. See [[change-of-basis]].

**Embedding spaces** — word or image embeddings are coordinate vectors in a learned basis. Cosine similarity computes $\langle u, v \rangle = \sum u_i v_i$ — the Theorem 25 formula — which holds because embeddings are treated as living in an orthonormal basis.

## Exercises

**Basic** — Given $S = \{(1,1),(1,-1)\}$ in $\mathbb{R}^2$, find the coordinate vector of $v = (3,1)$ relative to $S$. Reconstruct $v$ from those coordinates.

**Intermediate** — Using the ONB from [[gram-schmidt]] (Example 58), find $(u)_S$ for $u=(2,1,0)$ via Theorem 25. Verify by solving the linear system.

**Advanced** — Prove Theorem 25(c): if $S$ is orthonormal and $(u)_S=(u_1,\ldots,u_n)$, $(v)_S=(v_1,\ldots,v_n)$, then $\langle u, v \rangle = \sum u_i v_i$. (Expand both vectors in basis, apply bilinearity, use $\langle v_i, v_j \rangle = \delta_{ij}$.)
