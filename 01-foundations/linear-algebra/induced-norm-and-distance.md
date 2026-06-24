---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[inner-product-spaces]]"
  - "[[vector-norms]]"
  - "[[cauchy-schwarz-inequality]]"
  - "[[euclidean-n-space]]"
  - "[[angles-and-orthogonality]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 6 — Theorem 16 (Longitud y Distancia)."
---

> **TL;DR** — Every inner product automatically generates a norm and a distance: ||u|| = sqrt(<u,u>) and d(u,v) = ||u-v||; these satisfy the same eight geometric properties as Euclidean length and distance.

---

## Intuition

In R^n, length and distance come for free from the dot product. But once you define an inner product on *any* vector space — polynomials, matrices, functions — you get length and distance in that space automatically, with no extra work.

The inner product is the engine; length and distance are consequences. This is why Euclidean geometry works in spaces that look nothing like arrows.

## Mechanics

**Induced norm** (length): given an [[inner-product-spaces|inner product space]] V,

$$\|\mathbf{u}\| = \langle \mathbf{u}, \mathbf{u} \rangle^{1/2}$$

**Induced distance**: $d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\| = \langle \mathbf{u}-\mathbf{v},\, \mathbf{u}-\mathbf{v} \rangle^{1/2}$

**Theorem 16 (Anton)** — these definitions satisfy all standard geometric properties:

| # | Length property | # | Distance property |
|---|---|---|---|
| L1 | $\|\mathbf{u}\| \geq 0$ | D1 | $d(\mathbf{u},\mathbf{v}) \geq 0$ |
| L2 | $\|\mathbf{u}\| = 0$ iff $\mathbf{u}=\mathbf{0}$ | D2 | $d(\mathbf{u},\mathbf{v}) = 0$ iff $\mathbf{u}=\mathbf{v}$ |
| L3 | $\|k\mathbf{u}\| = \|k\|\,\|\mathbf{u}\|$ | D3 | $d(\mathbf{u},\mathbf{v}) = d(\mathbf{v},\mathbf{u})$ |
| L4 | $\|\mathbf{u}+\mathbf{v}\| \leq \|\mathbf{u}\|+\|\mathbf{v}\|$ | D4 | $d(\mathbf{u},\mathbf{v}) \leq d(\mathbf{u},\mathbf{w})+d(\mathbf{w},\mathbf{v})$ |

**Proof of L4 (triangle inequality)** — uses [[cauchy-schwarz-inequality]]:

$$\|\mathbf{u}+\mathbf{v}\|^2 = \langle\mathbf{u}+\mathbf{v},\mathbf{u}+\mathbf{v}\rangle = \|\mathbf{u}\|^2 + 2\langle\mathbf{u},\mathbf{v}\rangle + \|\mathbf{v}\|^2$$
$$\leq \|\mathbf{u}\|^2 + 2\|\mathbf{u}\|\|\mathbf{v}\| + \|\mathbf{v}\|^2 = \bigl(\|\mathbf{u}\|+\|\mathbf{v}\|\bigr)^2$$

Take the square root: $\|\mathbf{u}+\mathbf{v}\| \leq \|\mathbf{u}\|+\|\mathbf{v}\|$. $\blacksquare$

```python
import numpy as np
from scipy import integrate

# R^n: standard inner product
u, v = np.array([1., -1.]), np.array([1., 1.])
norm_u = np.sqrt(np.dot(u, u))                         # sqrt(2)
dist   = np.sqrt(np.dot(u - v, u - v))                 # 2.0
print(norm_u, dist, norm_u + np.sqrt(np.dot(v,v)) >= np.sqrt(np.dot(u+v,u+v)))

# Function space: ||p|| = sqrt(integral p^2) on [-1,1]
p = lambda x: x          # polynomial p = x
norm_p = np.sqrt(integrate.quad(lambda x: p(x)**2, -1, 1)[0])  # sqrt(2/3)
```


## In ML

**Metric spaces underlie clustering** — k-means, DBSCAN, and hierarchical clustering all require a distance function. Properties D1–D4 guarantee the distance is well-behaved. Choosing which inner product you use (standard vs. weighted vs. kernel) changes the geometry and which points cluster together.

**Weight norms in regularization** — L2 regularization penalizes $\|\mathbf{w}\|^2 = \langle\mathbf{w},\mathbf{w}\rangle$ using the standard inner product. Weighted norms (feature-scaled inner products) appear in Mahalanobis distance, which adjusts for feature correlations.

**Convergence in function spaces** — training neural networks on function approximation tasks implicitly uses a norm on function spaces. L4 (triangle inequality) is the property that makes "nearby functions produce nearby outputs" a coherent concept.

## Exercises

**Basic** — For the weighted inner product $\langle\mathbf{u},\mathbf{v}\rangle = 2u_1v_1 + u_2v_2$ on R^2, compute the induced norm of $\mathbf{u}=[3,4]$ and the induced distance $d(\mathbf{u},\mathbf{v})$ where $\mathbf{v}=[1,1]$.

**Intermediate** — Prove property L3: $\|k\mathbf{u}\| = |k|\,\|\mathbf{u}\|$ directly from the inner product axioms (homogeneity + positivity).

**Advanced** — Show that D4 (triangle inequality for distance) follows from L4. Then show the norm and distance defined via a weighted inner product $\langle\mathbf{u},\mathbf{v}\rangle_W = \mathbf{u}^T W \mathbf{v}$ (W positive definite) satisfy all 8 properties.
