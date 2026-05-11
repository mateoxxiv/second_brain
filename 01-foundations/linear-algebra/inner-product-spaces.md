---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[general-vector-spaces]]"
  - "[[dot-product]]"
  - "[[euclidean-n-space]]"
  - "[[vector-norms]]"
  - "[[gram-schmidt]]"
  - "[[projection-onto-subspaces]]"
  - "[[cosine-similarity]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 6 — Inner Product Spaces."
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
---

> **TL;DR** — An inner product is a dot-product-like operation you can define on any vector space; once you have one, all of Euclidean geometry — length, angle, orthogonality, projection — works in that space, even for polynomials or functions.

---

## Intuition

The [[dot-product]] gives R^n its geometry: lengths, angles, projections. But polynomial spaces and function spaces have no built-in dot product — so how do you measure alignment between two functions?

An inner product is the answer: a rule you *define* on any [[general-vector-spaces|vector space]] that behaves like the dot product. As long as four axioms hold, you immediately inherit the entire geometric toolkit — Cauchy-Schwarz, orthogonality, Gram-Schmidt — without changing what the objects are.

## Mechanics

**Definition (Anton Ch. 6)** — An inner product on a vector space V is a function $\langle\cdot,\cdot\rangle: V \times V \to \mathbb{R}$ satisfying for all u, v, w ∈ V and scalar k:

| # | Axiom | Rule |
|---|---|---|
| 1 | Symmetry | $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$ |
| 2 | Additivity | $\langle \mathbf{u}+\mathbf{v}, \mathbf{w} \rangle = \langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle$ |
| 3 | Homogeneity | $\langle k\mathbf{u}, \mathbf{v} \rangle = k\langle \mathbf{u}, \mathbf{v} \rangle$ |
| 4 | Positivity | $\langle \mathbf{u}, \mathbf{u} \rangle \geq 0$; $= 0$ iff $\mathbf{u} = \mathbf{0}$ |

**Three inner products:**

- **Standard** on R^n: $\langle \mathbf{u},\mathbf{v} \rangle = \sum_i u_i v_i$ — the ordinary [[dot-product]]
- **Weighted** on R^n: $\langle \mathbf{u},\mathbf{v} \rangle = \sum_i w_i u_i v_i$ with $w_i > 0$ (features on different scales)
- **Function** on C[a,b]: $\langle f, g \rangle = \int_a^b f(x)\,g(x)\,dx$ (signals, Fourier analysis)

**Derived geometry** — any inner product immediately induces:

$$\|\mathbf{u}\| = \sqrt{\langle \mathbf{u}, \mathbf{u} \rangle} \qquad \cos\theta = \frac{\langle \mathbf{u},\mathbf{v} \rangle}{\|\mathbf{u}\|\,\|\mathbf{v}\|} \qquad \mathbf{u} \perp \mathbf{v} \iff \langle \mathbf{u},\mathbf{v}\rangle = 0$$

**Cauchy-Schwarz** holds in every inner product space (same proof as [[euclidean-n-space]]):

$$|\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\|\,\|\mathbf{v}\|$$

```python
import numpy as np
from scipy import integrate

def standard_ip(u, v):            return float(np.dot(u, v))
def weighted_ip(u, v, w):         return float(np.dot(w * u, v))
def function_ip(f, g, a=0, b=1):  return integrate.quad(lambda x: f(x)*g(x), a, b)[0]

u, v = np.array([1., 2., 3.]), np.array([4., 5., 6.])
w    = np.array([1., 2., 1.])

print(standard_ip(u, v))                        # 32.0
print(weighted_ip(u, v, w))                     # 42.0
print(function_ip(np.sin, np.cos, 0, 2*np.pi)) # ≈ 0.0  (sin ⊥ cos)
```

> Runnable: [[code/foundations/inner_product_spaces.py]]

## In ML

**Kernel methods** — a kernel $K(\mathbf{x}, \mathbf{y})$ is an inner product in a (possibly infinite-dimensional) feature space. The kernel trick computes $\langle\phi(\mathbf{x}), \phi(\mathbf{y})\rangle$ without constructing $\phi$ explicitly — valid because the four axioms still hold, so all geometric tools (Cauchy-Schwarz, projections) apply in that hidden space.

**Attention mechanism** — the scaled dot product $\mathbf{q}\cdot\mathbf{k}/\sqrt{d}$ is the standard inner product on R^d measuring alignment between queries and keys. [[cosine-similarity]] is the normalized version of the same inner product. Every attention head is computing geometry in an inner product space.

**Gram-Schmidt generalizes** — [[gram-schmidt]] orthogonalization replaces every dot product with $\langle\cdot,\cdot\rangle$. This means you can build orthogonal bases in polynomial or function spaces — exactly how Fourier series work: sin and cos are orthogonal under the function inner product on [0, 2π].

## Exercises

**Basic** — Verify the weighted inner product $\langle \mathbf{u},\mathbf{v}\rangle = 2u_1v_1 + 3u_2v_2$ satisfies all 4 axioms for $\mathbf{u}=[1,2]$, $\mathbf{v}=[3,1]$. Compute the induced norm $\|\mathbf{u}\|$.

**Intermediate** — Show that $\sin(x)$ and $\cos(x)$ are orthogonal in $C[0, 2\pi]$ under $\langle f,g\rangle = \int_0^{2\pi} f(x)g(x)\,dx$. Compute the integral by hand using the product-to-sum identity.

**Advanced** — Prove Cauchy-Schwarz for a general inner product space. Use the fact that $\langle \mathbf{u} - t\mathbf{v},\, \mathbf{u} - t\mathbf{v}\rangle \geq 0$ for all real $t$, expand using axioms 1–3, minimize over $t$, and read off the inequality.
