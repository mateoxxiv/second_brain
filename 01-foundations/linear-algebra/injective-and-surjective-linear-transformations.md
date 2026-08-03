---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[kernel-and-range]]"
  - "[[rank-nullity-theorem]]"
  - "[[linear-transformations]]"
  - "[[matrix-similarity]]"
  - "[[general-vector-spaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.2"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — A linear transformation is injective exactly when its kernel is trivial, and surjective exactly when its range fills the whole codomain — two independent questions the Rank-Nullity Theorem quietly links together.

---

## Intuition

**Injective** asks: does $T$ ever merge two different inputs into the same output? **Surjective** asks: does $T$'s output reach every corner of the target space, or does it miss some? These are genuinely separate questions — $T$ can cover the whole target while still merging inputs (surjective, not injective), or preserve every input distinction while missing most of the target (injective, not surjective).

## Mechanics

**Injective (one-to-one)** — $T(\mathbf{v}_1) = T(\mathbf{v}_2) \implies \mathbf{v}_1 = \mathbf{v}_2$ for all $\mathbf{v}_1, \mathbf{v}_2 \in V$. Equivalently, using Theorem 1(c) from [[kernel-and-range]]: $T(\mathbf{v}_1) = T(\mathbf{v}_2) \implies T(\mathbf{v}_1 - \mathbf{v}_2) = \mathbf{0}$. If $\ker(T) = \{\mathbf{0}\}$, this forces $\mathbf{v}_1 - \mathbf{v}_2 = \mathbf{0}$, i.e. $\mathbf{v}_1 = \mathbf{v}_2$. So:

$$T \text{ is injective} \iff \ker(T) = \{\mathbf{0}\}$$

**Surjective (onto)** — every vector in the codomain is reached: $R(T) = W$.

**The Rank-Nullity bridge** — for $T: V \to W$ with $\dim(V) = n$, $\dim(W) = m$:

| Property | Kernel/range condition | Rank-Nullity condition |
|---|---|---|
| Injective | $\ker(T) = \{\mathbf{0}\}$ | $\text{nullity}(T) = 0$, so $\text{rank}(T) = n$ |
| Surjective | $R(T) = W$ | $\text{rank}(T) = m$ |
| Bijective (isomorphism) | both | $n = m = \text{rank}(T)$ |

**Two dimension corollaries, for free:**

- If $\dim(V) < \dim(W)$, $T$ can **never** be surjective — $\text{rank}(T) \le n < m$, so there aren't enough output dimensions to fill.
- If $\dim(V) > \dim(W)$, $T$ can **never** be injective — [[rank-nullity-theorem]] forces $\text{nullity}(T) = n - \text{rank}(T) \ge n - m > 0$, so a nontrivial kernel is unavoidable.

**Bijective = isomorphism** — when $T$ is both injective and surjective (which requires $\dim(V) = \dim(W)$), $T$ has an inverse $T^{-1}$, and $V$, $W$ are structurally identical vector spaces — see [[matrix-similarity]] for what this identification enables.

```python
import numpy as np

def injective(A: np.ndarray) -> bool:
    return np.linalg.matrix_rank(A) == A.shape[1]   # rank == n (columns)

def surjective(A: np.ndarray) -> bool:
    return np.linalg.matrix_rank(A) == A.shape[0]   # rank == m (rows)

A = np.array([[1, 0], [0, 1], [1, 1]])   # R^2 -> R^3
print(injective(A), surjective(A))        # True False -- more outputs than inputs
```

## In ML

**Invertible layers / normalizing flows** — architectures like normalizing flows require each layer to be bijective (injective *and* surjective) so the transformation can be exactly inverted for density estimation; a non-bijective layer would make the inverse ill-defined.

**Dimensionality reduction is intentionally non-injective** — PCA and autoencoder bottlenecks map a high-dimensional space to a lower-dimensional one ($n > m$), so by the corollary above they can *never* be injective. Information loss here is mathematically guaranteed, not a training failure.

**Embeddings aim for injective, rarely need surjective** — a good embedding keeps distinct inputs distinguishable (avoiding collisions, i.e. approximately injective) without needing to cover every point of the embedding space (rarely truly surjective).

## Exercises

**Basic** — For $T(x,y) = (x+y,\ x+y)$ on $\mathbb{R}^2$ (the same map used in [[kernel-and-range]]'s basic exercise), is $T$ injective? Surjective? Justify using $\ker(T)$ and $R(T)$.

**Intermediate** — A linear transformation $T: \mathbb{R}^5 \to \mathbb{R}^3$. Can $T$ be injective? Prove your answer using the dimension corollary above.

**Advanced** — Construct a linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^3$ that is injective but not surjective, and one $T: \mathbb{R}^3 \to \mathbb{R}^2$ that is surjective but not injective. Verify each using [[rank-nullity-theorem]].
