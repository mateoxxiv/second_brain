---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[matrix-operations]]"
  - "[[vectors-and-vector-spaces]]"
  - "[[basis-and-dimension]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[inner-product-spaces]]"
  - "[[projection-onto-subspaces]]"
  - "[[coordinate-vector]]"
  - "[[gram-schmidt]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.1"
  - "https://www.youtube.com/watch?v=kYB8IZa5AuE"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — A linear transformation is a function between vector spaces that preserves addition and scaling; every matrix multiplication is one, and every linear transformation on finite-dimensional spaces is a matrix.

---

## Intuition

Two rules define linearity:

```
T(u + v) = T(u) + T(v)    ← structure preserved under addition
T(k·v)   = k·T(v)          ← structure preserved under scaling
```

**Linear:** $T(\mathbf{v}) = 2\mathbf{v}$. Double first or sum first — same result.

**NOT linear:** $f(\mathbf{v}) = \mathbf{v} + [1,0]$ (translation). The zero vector no longer maps to zero: $f(\mathbf{0}) = [1,0] \neq \mathbf{0}$.

The two axioms together imply the **superposition property** — the most general form:

$$F(k_1\mathbf{v}_1 + \cdots + k_n\mathbf{v}_n) = k_1F(\mathbf{v}_1) + \cdots + k_nF(\mathbf{v}_n)$$

## Mechanics

**Definition** — $F:V \to W$ is a linear transformation if for all $\mathbf{u}, \mathbf{v} \in V$ and scalar $k$:

$$F(\mathbf{u}+\mathbf{v}) = F(\mathbf{u})+F(\mathbf{v}), \qquad F(k\mathbf{u}) = kF(\mathbf{u})$$

**Catalog of named linear transformations (Anton §5.1):**

| Name | Rule | Notes |
|---|---|---|
| Matrix multiplication | $T(\mathbf{x}) = A\mathbf{x}$ | Every $m\times n$ matrix defines one |
| Zero transformation | $T(\mathbf{v}) = \mathbf{0}$ | Maps everything to zero |
| Identity | $T(\mathbf{v}) = \mathbf{v}$ | Operator on $V$; $I$ matrix |
| Dilation / contraction | $T(\mathbf{v}) = k\mathbf{v}$ | $k>1$ stretches; $0<k<1$ shrinks |
| Rotation by $\theta$ | $T(\mathbf{v}) = A_\theta\mathbf{v}$ | See derivation below |
| Orthogonal projection onto $W$ | $T(\mathbf{v}) = \sum_i \langle\mathbf{v},\mathbf{w}_i\rangle\mathbf{w}_i$ | $\{\mathbf{w}_i\}$ orthonormal basis of $W$ |
| Coordinate map | $T(\mathbf{v}) = (\mathbf{v})_S$ | $V \to \mathbb{R}^n$; see [[coordinate-vector]] |
| Inner product map | $T(\mathbf{v}) = \langle\mathbf{v},\mathbf{v}_0\rangle$ | $V \to \mathbb{R}$ |

**Rotation derivation** — Let $\mathbf{v} = [x,y]^T$ with $x = r\cos\phi$, $y = r\sin\phi$. After rotating by $\theta$ the new coordinates $x',y'$ satisfy:

$$x' = r\cos(\theta+\phi) = x\cos\theta - y\sin\theta$$
$$y' = r\sin(\theta+\phi) = x\sin\theta + y\cos\theta$$

(used the angle addition identities). So the rotation matrix is:

$$A_\theta = \begin{bmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{bmatrix}$$

**Alternative derivation — direct triangle construction (Anton, exercise 10 worked by hand):** instead of going through $r,\phi$, drop a perpendicular straight from the rotated point and read the two right triangles it creates directly. Let $B=(B_x,B_y)$ be the original point, rotated by $\theta$ to $A=(A_x,A_y)$. The perpendicular splits $A$'s position into a horizontal run and a vertical rise, each built from a $B_x$-piece and a $B_y$-piece at complementary angles $\theta$ and $90°-\theta$:

$$A_x = B_x\cos\theta - B_y\sin\theta, \qquad A_y = B_x\sin\theta + B_y\cos\theta$$

$$\begin{bmatrix}A_x\\A_y\end{bmatrix} = \begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}\begin{bmatrix}B_x\\B_y\end{bmatrix}$$

Identical result to the $r,\phi$ derivation above — $(B_x,B_y)$ and $(A_x,A_y)$ are just this note's $(x,y)$ and $(x',y')$ relabeled. Useful as a cross-check: two independent geometric routes, same matrix.

```python
import numpy as np

def rotation(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])

T = rotation(np.pi / 2)
v = np.array([1, 0])
print(T @ v)                         # [0, 1] — right becomes up

u, v = np.array([1, 2]), np.array([3, 1])
assert np.allclose(T @ (u + v), T @ u + T @ v)   # linearity check
```

## In ML

**Neural network layers** — each dense layer $\mathbf{z} = W\mathbf{x} + \mathbf{b}$ is a linear transformation plus a bias shift. Without nonlinear activations, any stack of layers collapses to one matrix — the network cannot learn curved boundaries.

**Orthogonal projection** — $T(\mathbf{v}) = \sum_i \langle\mathbf{v},\mathbf{w}_i\rangle\mathbf{w}_i$ onto a subspace is the core of PCA and attention: project data onto the directions of maximum variance, or map queries onto learned key subspaces. See [[projection-onto-subspaces]].

**Coordinate map as embedding** — $T(\mathbf{v}) = (\mathbf{v})_S$ maps a vector to its coordinates in basis $S$. This is exactly what learned embeddings do: represent an object (word, image patch) as a coordinate vector in a learned basis.

## Exercises

**Basic** — Is $T(\mathbf{v}) = \|\mathbf{v}\|\cdot\mathbf{v}$ linear? Check both axioms explicitly. What fails?

**Intermediate** — Compose a 45° rotation followed by a uniform scaling by 2. Write the result as a single $2\times 2$ matrix. Then verify: does it map $[1,0]$ and $[0,1]$ to the expected vectors?

**Advanced** — Prove that the orthogonal projection $T(\mathbf{v}) = \sum_{i=1}^r\langle\mathbf{v},\mathbf{w}_i\rangle\mathbf{w}_i$ (with $\{\mathbf{w}_i\}$ orthonormal) satisfies both linearity axioms using only inner product properties.
