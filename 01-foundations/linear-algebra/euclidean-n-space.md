---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[vectors-and-vector-spaces]]"
  - "[[vector-norms]]"
  - "[[dot-product]]"
  - "[[cosine-similarity]]"
  - "[[projection-onto-subspaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 3 — Euclidean Vector Spaces."
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
---

> **TL;DR** — R^n is the space of n-tuples of real numbers equipped with Euclidean distance; the Cauchy-Schwarz inequality is the single fact that makes angles, projections, and correlation all well-defined in any dimension.

---

## Intuition

R^2 and R^3 are the geometric spaces you already know — the plane and 3D space. R^n is the same idea with n coordinates. A point in R^784 is a grayscale image (28×28 = 784 pixels); a point in R^1536 is a word embedding. The geometry — distance, angle, projection — works exactly the same way, just with more coordinates.

The Euclidean norm is the Pythagorean theorem generalized to n terms. The distance between two points is the norm of their difference.

## Mechanics

**R^n** is the set of all ordered n-tuples $\mathbf{u} = (u_1, \ldots, u_n)$ with $u_i \in \mathbb{R}$.

**Euclidean norm** — length of a vector (special case of [[vector-norms]] L2):

$$\|\mathbf{u}\| = \sqrt{u_1^2 + \cdots + u_n^2} = \sqrt{\mathbf{u}\cdot\mathbf{u}}$$

**Euclidean distance** — length of the difference vector:

$$d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\| = \sqrt{\sum_{i=1}^n (u_i - v_i)^2}$$

**Cauchy-Schwarz inequality** — bounds the [[dot-product]] by the product of norms:

$$|\mathbf{u}\cdot\mathbf{v}| \leq \|\mathbf{u}\|\,\|\mathbf{v}\|$$

*Derivation*: for any real $t$, $\|\mathbf{u} - t\mathbf{v}\|^2 \geq 0$. Expanding: $\|\mathbf{u}\|^2 - 2t(\mathbf{u}\cdot\mathbf{v}) + t^2\|\mathbf{v}\|^2 \geq 0$. This is a quadratic in $t$ that is always non-negative, so its discriminant must be $\leq 0$: $4(\mathbf{u}\cdot\mathbf{v})^2 - 4\|\mathbf{u}\|^2\|\mathbf{v}\|^2 \leq 0$, which gives the inequality directly.

Consequence: dividing both sides by $\|\mathbf{u}\|\|\mathbf{v}\|$ gives $-1 \leq \cos\theta \leq 1$, so angles in R^n are always well-defined.

**Triangle inequality** — follows from Cauchy-Schwarz:

$$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$$

| Property | Formula |
|---|---|
| Norm | $\|\mathbf{u}\| = \sqrt{\mathbf{u}\cdot\mathbf{u}}$ |
| Distance | $d(\mathbf{u},\mathbf{v}) = \|\mathbf{u}-\mathbf{v}\|$ |
| Cauchy-Schwarz | $\vert\mathbf{u}\cdot\mathbf{v}\vert \leq \|\mathbf{u}\|\|\mathbf{v}\|$ |
| Angle | $\cos\theta = \mathbf{u}\cdot\mathbf{v} \;/\; (\|\mathbf{u}\|\|\mathbf{v}\|)$ |
| Triangle ineq. | $\|\mathbf{u}+\mathbf{v}\| \leq \|\mathbf{u}\|+\|\mathbf{v}\|$ |

```python
import numpy as np

u = np.array([1., 2., 3.])
v = np.array([4., 5., 6.])

dist   = np.linalg.norm(u - v)                   # sqrt(27) ≈ 5.196
cs_lhs = abs(np.dot(u, v))                       # 32
cs_rhs = np.linalg.norm(u) * np.linalg.norm(v)  # ≈ 32.83
print(cs_lhs <= cs_rhs)                          # True — Cauchy-Schwarz
print(np.linalg.norm(u + v) <= cs_rhs)           # True — triangle inequality
```


## In ML

**k-NN and clustering** — k-nearest neighbors and k-means both use Euclidean distance $d(\mathbf{u},\mathbf{v}) = \|\mathbf{u}-\mathbf{v}\|$ to find "close" points in feature space. Every distance-based algorithm in ML is this formula applied to R^n.

**Cosine similarity vs Euclidean distance** — in embedding spaces (word2vec, BERT), [[cosine-similarity]] is preferred over Euclidean distance because it normalizes for magnitude: two documents of different lengths compare by direction, not size. The Cauchy-Schwarz bound is exactly why cosine similarity always lands in [−1, 1].

**Curse of dimensionality** — in high-dimensional R^n, Euclidean distances concentrate: most random point pairs have nearly identical distances. This is why k-NN degrades in hundreds of dimensions and why [[projection-onto-subspaces]] (PCA, autoencoders) is critical before applying distance-based methods.

## Exercises

**Basic** — Compute the Euclidean distance between $\mathbf{u}=(1,0,0,1)$ and $\mathbf{v}=(0,1,1,0)$ in R^4 by hand. Then verify with NumPy.

**Intermediate** — For $\mathbf{u}=[3,4]$ and $\mathbf{v}=[1,2]$: verify Cauchy-Schwarz by computing both sides. Then compute the unit vector $\hat{\mathbf{u}}$ and show that $\hat{\mathbf{u}}\cdot\mathbf{v}$ equals the scalar projection of $\mathbf{v}$ onto $\mathbf{u}$.

**Advanced** — Prove the triangle inequality from Cauchy-Schwarz. Expand $\|\mathbf{u}+\mathbf{v}\|^2 = (\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}+\mathbf{v})$, apply Cauchy-Schwarz to the cross term $2\,\mathbf{u}\cdot\mathbf{v}$, and take the square root of both sides.
