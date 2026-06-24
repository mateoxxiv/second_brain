---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[dot-product]]"
  - "[[vector-operations]]"
  - "[[vector-norms]]"
  - "[[determinant]]"
  - "[[projection]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — The cross product of two 3D vectors produces a third vector perpendicular to both; its magnitude equals the parallelogram area spanned by the two vectors, connecting the [[dot-product]]'s cosθ to sinθ via the Lagrange identity.

---

## Intuition

The [[dot-product]] tells you how much two vectors *agree* (cosθ). The cross product tells you how much they *differ* — how far apart they are in orientation (sinθ), and crucially, *which direction* they define together.

Grab a right hand: point fingers along **a**, curl toward **b** — your thumb points in the direction of **a × b**. Two parallel vectors span no area and produce the zero vector. Two perpendicular vectors span the maximum area.

## Mechanics

Only defined in 3D. For $\mathbf{a} = [a_1,a_2,a_3]$ and $\mathbf{b} = [b_1,b_2,b_3]$:

$$\mathbf{a}\times\mathbf{b} = \det\begin{bmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\a_1&a_2&a_3\\b_1&b_2&b_3\end{bmatrix} = \begin{bmatrix}a_2b_3-a_3b_2\\a_3b_1-a_1b_3\\a_1b_2-a_2b_1\end{bmatrix}$$

The [[determinant]] expansion with unit vectors $\mathbf{i},\mathbf{j},\mathbf{k}$ gives the components directly.

**Magnitude = parallelogram area:**

$$\|\mathbf{a}\times\mathbf{b}\| = \|\mathbf{a}\|\,\|\mathbf{b}\|\sin\theta$$

**Triangle area** = half the parallelogram:

$$\text{Area}_\triangle = \tfrac{1}{2}\|\mathbf{a}\times\mathbf{b}\|$$

**Lagrange identity** — connects cross product and [[dot-product]] via $\sin^2\theta + \cos^2\theta = 1$:

$$\|\mathbf{a}\times\mathbf{b}\|^2 + (\mathbf{a}\cdot\mathbf{b})^2 = \|\mathbf{a}\|^2\|\mathbf{b}\|^2$$

| Property | Rule |
|---|---|
| Anti-commutative | $\mathbf{a}\times\mathbf{b} = -(\mathbf{b}\times\mathbf{a})$ |
| Parallel vectors | $\mathbf{a}\times\mathbf{b} = \mathbf{0}$ when $\theta=0$ or $\pi$ |
| Perpendicular result | $(\mathbf{a}\times\mathbf{b})\perp\mathbf{a}$ and $\perp\mathbf{b}$ |
| Orthogonality (dot form) | $\mathbf{u}\cdot(\mathbf{u}\times\mathbf{v}) = 0$ and $\mathbf{v}\cdot(\mathbf{u}\times\mathbf{v}) = 0$ |
| Self cross product | $\mathbf{a}\times\mathbf{a} = \mathbf{0}$ |

```python
import numpy as np

a = np.array([1, 0, 0])
b = np.array([0, 1, 0])

c = np.cross(a, b)
print(c)                                       # [0 0 1] — points in z direction

a2 = np.array([2, 0, 0])
b2 = np.array([1, 3, 0])
area = np.linalg.norm(np.cross(a2, b2))
print(area)                                    # 6.0

lhs = np.linalg.norm(np.cross(a2, b2))**2 + np.dot(a2, b2)**2
rhs = np.linalg.norm(a2)**2 * np.linalg.norm(b2)**2
print(np.isclose(lhs, rhs))                    # True — Lagrange identity
```


## In ML

**Surface normals in 3D geometry** — cross product computes the normal vector to a surface face, used in 3D mesh processing, neural radiance fields (NeRF), and 3D point cloud models.

**Lagrange identity and Cauchy-Schwarz** — rearranging: $\|\mathbf{a}\times\mathbf{b}\|^2 = \|\mathbf{a}\|^2\|\mathbf{b}\|^2 - (\mathbf{a}\cdot\mathbf{b})^2 \geq 0$ immediately proves $|\mathbf{a}\cdot\mathbf{b}| \leq \|\mathbf{a}\|\|\mathbf{b}\|$ (Cauchy-Schwarz). This bound underlies the validity of [[cosine-similarity]] as a metric.

**Area-based losses** — in differentiable rendering and mesh generation, triangle area computed via cross product is used as a regularization term to prevent degenerate (zero-area) triangles.

## Exercises

**Basic** — Compute $[1,2,0]\times[3,4,0]$ by hand using the determinant formula. Verify the result is perpendicular to both input vectors using the [[dot-product]].

**Intermediate** — Three points: $P=(0,0,0)$, $Q=(2,0,0)$, $R=(0,3,0)$. Find the area of triangle PQR using the cross product. Verify geometrically (base × height / 2).

**Advanced** — Prove the Lagrange identity $\|\mathbf{a}\times\mathbf{b}\|^2 + (\mathbf{a}\cdot\mathbf{b})^2 = \|\mathbf{a}\|^2\|\mathbf{b}\|^2$ using only $\sin^2\theta + \cos^2\theta = 1$ and the magnitude definitions of dot and cross products.
