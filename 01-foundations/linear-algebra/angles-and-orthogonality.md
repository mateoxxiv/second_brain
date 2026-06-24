---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[inner-product-spaces]]"
  - "[[induced-norm-and-distance]]"
  - "[[cauchy-schwarz-inequality]]"
  - "[[cosine-similarity]]"
  - "[[gram-schmidt]]"
  - "[[projection-onto-subspaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 6 — Angle, Orthogonality, Theorem 17."
---

> **TL;DR** — The Cauchy-Schwarz inequality guarantees that <u,v>/(||u||||v||) always lands in [-1,1], so you can define angle and orthogonality in any inner product space — even between polynomials or matrices.

---

## Intuition

In R^2 you draw two arrows and measure the angle with a protractor. In a space of polynomials there are no arrows and no protractor — so how do you define angle?

The key: [[cauchy-schwarz-inequality]] guarantees $|\langle\mathbf{u},\mathbf{v}\rangle| \leq \|\mathbf{u}\|\|\mathbf{v}\|$, which means the ratio $\langle\mathbf{u},\mathbf{v}\rangle / (\|\mathbf{u}\|\|\mathbf{v}\|)$ is always in $[-1, 1]$ — the exact range of cosine. So we *define* angle from this ratio, and it automatically behaves like a real angle.

Orthogonality is the special case: $\theta = 90°$, meaning $\langle\mathbf{u},\mathbf{v}\rangle = 0$. Two functions, matrices, or polynomials are "perpendicular" if their inner product is zero.

## Mechanics

**Angle** — for nonzero u, v in an [[inner-product-spaces|inner product space]] V (Theorem 16, Anton):

$$\cos\theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\|\,\|\mathbf{v}\|}, \qquad 0 \leq \theta \leq \pi$$

There is a unique such $\theta$ because cosine is one-to-one on $[0, \pi]$.

**Orthogonality** — u and v are *orthogonal* if $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ (equivalently $\theta = \pi/2$). A vector u is *orthogonal to a set W* if it is orthogonal to every vector in W.

**Theorem 17 — Generalized Pythagorean theorem**: if $\langle \mathbf{u}, \mathbf{v} \rangle = 0$, then:

$$\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$$

*Proof*: $\|\mathbf{u}+\mathbf{v}\|^2 = \langle\mathbf{u}+\mathbf{v},\mathbf{u}+\mathbf{v}\rangle = \|\mathbf{u}\|^2 + 2\langle\mathbf{u},\mathbf{v}\rangle + \|\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$ since $\langle\mathbf{u},\mathbf{v}\rangle=0$. $\blacksquare$

| Concept | Formula | Holds in |
|---|---|---|
| Angle | $\cos\theta = \langle\mathbf{u},\mathbf{v}\rangle / (\|\mathbf{u}\|\|\mathbf{v}\|)$ | Any IP space |
| Orthogonality | $\langle\mathbf{u},\mathbf{v}\rangle = 0$ | Any IP space |
| Pythagorean thm | $\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2+\|\mathbf{v}\|^2$ | When $\mathbf{u}\perp\mathbf{v}$ |

```python
import numpy as np
from scipy import integrate

# Angle in R^4 (Example 50, Anton)
u = np.array([4., 3., 1., -2.])
v = np.array([-2., 1., 2., 3.])
cos_t = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
print(f"cos θ = {cos_t:.4f}")           # -9 / sqrt(30*18) ≈ -0.3873
print(f"θ = {np.degrees(np.arccos(cos_t)):.2f}°")  # ≈ 112.8°

# Orthogonality in function space: p=x, q=x^2 on [-1,1]
ip = lambda f, g: integrate.quad(lambda x: f(x)*g(x), -1, 1)[0]
print(ip(lambda x: x, lambda x: x**2))  # 0.0  → orthogonal
```


## In ML

**Orthogonal features mean zero redundancy** — in PCA, eigenvectors are orthogonal under the standard inner product; each principal component captures variance the others do not. The Pythagorean theorem says their contributions to total variance add up exactly with no cross-terms.

**Attention is angle-based** — [[cosine-similarity]] is the normalized inner product, i.e., $\cos\theta$. Transformer attention computes this angle between query and key vectors to score relevance. High cosine → small angle → strong attention weight.

**Orthogonal weight initialization** — initializing neural network weight matrices to be orthogonal (columns satisfy $\langle\mathbf{w}_i,\mathbf{w}_j\rangle=0$) preserves gradient norms during backpropagation. The Pythagorean theorem is why: orthogonal transformations don't stretch or shrink the norm.

## Exercises

**Basic** — Find the angle between $\mathbf{u}=[4,3,1,-2]$ and $\mathbf{v}=[-2,1,2,3]$ in R^4 with the standard inner product. Compute $\langle\mathbf{u},\mathbf{v}\rangle$, $\|\mathbf{u}\|$, $\|\mathbf{v}\|$ by hand first.

**Intermediate** — In the polynomial space $P_2$ with inner product $\langle p,q\rangle = \int_{-1}^{1} p(x)q(x)\,dx$, show that $p(x)=x$ and $q(x)=x^2$ are orthogonal. Then compute $\|p\|$ and $\|q\|$.

**Advanced** — Prove the converse of the Pythagorean theorem: if $\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2+\|\mathbf{v}\|^2$ then $\langle\mathbf{u},\mathbf{v}\rangle=0$. (Expand the left side and conclude directly.)
