---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[inner-product-spaces]]"
  - "[[dot-product]]"
  - "[[euclidean-n-space]]"
  - "[[vector-norms]]"
  - "[[cosine-similarity]]"
  - "[[projection-onto-subspaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 6 — Theorem 15 (Desigualdad de Cauchy-Schwarz)."
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
---

> **TL;DR** — The inner product of two vectors can never exceed the product of their norms; this single bound makes angles, correlation, and cosine similarity well-defined in any inner product space.

---

## Intuition

Think about the [[dot-product]] formula $\mathbf{u}\cdot\mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$. The cosine is bounded: $|\cos\theta| \leq 1$, so $|\mathbf{u}\cdot\mathbf{v}| \leq \|\mathbf{u}\|\|\mathbf{v}\|$. That's Cauchy-Schwarz in R^n.

The remarkable fact is it holds in *any* [[inner-product-spaces|inner product space]] — polynomials, functions, infinite-dimensional spaces — even when "angle" has no direct visual meaning. The inequality is what *allows* you to define angle from the inner product, not the other way around.

Equality holds exactly when u and v are parallel ($\mathbf{u} = \lambda\mathbf{v}$) — the two vectors point in the same direction, so no "angular penalty" reduces the product.

## Mechanics

**Euclidean form** (R^n, special case):

$$(\mathbf{u} \cdot \mathbf{v})^2 \leq (\mathbf{u} \cdot \mathbf{u})(\mathbf{v} \cdot \mathbf{v})$$

**General form** (Theorem 15, Anton Ch. 6) — for any [[inner-product-spaces|inner product space]] V:

$$\langle \mathbf{u}, \mathbf{v} \rangle^2 \leq \langle \mathbf{u}, \mathbf{u} \rangle \langle \mathbf{v}, \mathbf{v} \rangle \qquad \Longleftrightarrow \qquad |\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\|\,\|\mathbf{v}\|$$

**Proof (quadratic discriminant argument):**

If $\mathbf{u} = \mathbf{0}$, both sides are 0 and equality holds trivially. Assume $\mathbf{u} \neq \mathbf{0}$.

Let $a = \langle\mathbf{u},\mathbf{u}\rangle$, $b = 2\langle\mathbf{u},\mathbf{v}\rangle$, $c = \langle\mathbf{v},\mathbf{v}\rangle$. By the positivity axiom, for any real $t$:

$$0 \leq \langle t\mathbf{u}+\mathbf{v},\; t\mathbf{u}+\mathbf{v} \rangle = \langle\mathbf{u},\mathbf{u}\rangle t^2 + 2\langle\mathbf{u},\mathbf{v}\rangle t + \langle\mathbf{v},\mathbf{v}\rangle = at^2 + bt + c$$

This quadratic in $t$ is always $\geq 0$, so it has no real roots — its discriminant must be $\leq 0$:

$$b^2 - 4ac \leq 0 \implies 4\langle\mathbf{u},\mathbf{v}\rangle^2 - 4\langle\mathbf{u},\mathbf{u}\rangle\langle\mathbf{v},\mathbf{v}\rangle \leq 0 \implies \langle\mathbf{u},\mathbf{v}\rangle^2 \leq \langle\mathbf{u},\mathbf{u}\rangle\langle\mathbf{v},\mathbf{v}\rangle \quad \blacksquare$$

| Form | Statement | Equality when |
|---|---|---|
| Euclidean | $\|\mathbf{u}\cdot\mathbf{v}\| \leq \|\mathbf{u}\|\|\mathbf{v}\|$ | $\mathbf{u} \parallel \mathbf{v}$ |
| General IP | $\langle\mathbf{u},\mathbf{v}\rangle^2 \leq \langle\mathbf{u},\mathbf{u}\rangle\langle\mathbf{v},\mathbf{v}\rangle$ | $\mathbf{u} = \lambda\mathbf{v}$ for some scalar $\lambda$ |
| Normalized | $-1 \leq \cos\theta \leq 1$ | angle = 0 or π |

```python
import numpy as np

u, v = np.array([3., 4.]), np.array([1., 2.])
lhs = abs(np.dot(u, v))            # |<u,v>|
rhs = np.linalg.norm(u) * np.linalg.norm(v)

print(f"|<u,v>| = {lhs:.4f}")      # 11.0
print(f"||u||·||v|| = {rhs:.4f}")  # 5 · sqrt(5) ≈ 11.180
print(f"CS holds: {lhs <= rhs}")   # True
```


## In ML

**Cosine similarity is Cauchy-Schwarz normalized** — [[cosine-similarity]] computes $\frac{\langle\mathbf{u},\mathbf{v}\rangle}{\|\mathbf{u}\|\|\mathbf{v}\|}$, which is well-defined only because Cauchy-Schwarz guarantees the ratio lies in $[-1, 1]$. Every embedding similarity search (word2vec, BERT, FAISS) relies on this bound.

**Attention scores are bounded** — the scaled dot product $\mathbf{q}\cdot\mathbf{k}/\sqrt{d}$ in transformer attention is an inner product. Cauchy-Schwarz ensures that before softmax the logits stay controlled relative to query/key magnitudes. The $1/\sqrt{d}$ factor counteracts the variance growth that Cauchy-Schwarz allows as $d$ grows.

**Kernel validity** — a kernel function $K(\mathbf{x}, \mathbf{y})$ must satisfy Cauchy-Schwarz (as any valid inner product does). This is why Mercer's theorem requires positive semi-definiteness: it's the algebraic condition that guarantees the kernel behaves like a true inner product — including the Cauchy-Schwarz bound — in some feature space.

## Exercises

**Basic** — For $\mathbf{u}=[1,2,2]$ and $\mathbf{v}=[2,1,-2]$: compute $|\mathbf{u}\cdot\mathbf{v}|$ and $\|\mathbf{u}\|\|\mathbf{v}\|$ by hand. Verify Cauchy-Schwarz holds. What is the angle between them?

**Intermediate** — Prove the triangle inequality $\|\mathbf{u}+\mathbf{v}\| \leq \|\mathbf{u}\|+\|\mathbf{v}\|$ using Cauchy-Schwarz. Hint: expand $\|\mathbf{u}+\mathbf{v}\|^2 = \langle\mathbf{u}+\mathbf{v}, \mathbf{u}+\mathbf{v}\rangle$, apply CS to the cross term $2\langle\mathbf{u},\mathbf{v}\rangle \leq 2\|\mathbf{u}\|\|\mathbf{v}\|$, then take the square root.

**Advanced** — Characterize the equality condition completely. Prove that $\langle\mathbf{u},\mathbf{v}\rangle^2 = \langle\mathbf{u},\mathbf{u}\rangle\langle\mathbf{v},\mathbf{v}\rangle$ if and only if $\mathbf{u}$ and $\mathbf{v}$ are linearly dependent. (In the proof above, equality in the discriminant means the quadratic has exactly one real root $t^*$ — what does $t^*\mathbf{u}+\mathbf{v}=\mathbf{0}$ tell you?)
