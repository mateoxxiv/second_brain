---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[angles-and-orthogonality]]"
  - "[[inner-product-spaces]]"
  - "[[basis-and-dimension]]"
  - "[[gram-schmidt]]"
  - "[[projection-onto-subspaces]]"
  - "[[induced-norm-and-distance]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.9 — Bases Ortonormales."
---

> **TL;DR** — An orthonormal basis is a set of mutually perpendicular unit vectors that spans the space; coordinates in it reduce to plain dot products, and the matrix inverse becomes free (just transpose).

---

## Intuition

A general basis lets you reach every point in a space — but finding coordinates means solving a linear system. An orthonormal basis gives you the same coverage with a massive shortcut: to find how much of each basis vector is in v, just take the dot product. No system to solve.

Think of it as the ideal coordinate axes: perfectly perpendicular (no interference between directions), all the same length (no scaling confusion). The standard axes in R^2 and R^3 are the canonical example, but orthonormal bases exist in any [[inner-product-spaces|inner product space]] — including spaces of polynomials and functions.

## Mechanics

**Orthogonal set** — S = {v₁, v₂, ..., vₙ} where $\langle \mathbf{v}_i, \mathbf{v}_j \rangle = 0$ for all $i \neq j$ (every pair is [[angles-and-orthogonality|orthogonal]]).

**Normalization** — given any nonzero vector $\mathbf{v}$, by property L3 of the [[induced-norm-and-distance|induced norm]]:

$$\left\|\frac{1}{\|\mathbf{v}\|}\mathbf{v}\right\| = \frac{1}{\|\mathbf{v}\|}\|\mathbf{v}\| = 1$$

So $\mathbf{v}/\|\mathbf{v}\|$ always has norm 1 — it is the **unit vector** in the direction of $\mathbf{v}$. Dividing any nonzero vector by its norm is called *normalizing* it.

**Orthonormal set** — orthogonal + every vector has unit norm:

$$\langle \mathbf{v}_i, \mathbf{v}_j \rangle = \delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}$$

**Example (Anton §4.9, Ex. 53)** — orthonormal set in R^3 with Euclidean inner product:

$$\mathbf{v}_1 = (0,1,0), \quad \mathbf{v}_2 = \!\left(\tfrac{1}{\sqrt{2}},0,\tfrac{1}{\sqrt{2}}\right), \quad \mathbf{v}_3 = \!\left(\tfrac{1}{\sqrt{2}},0,-\tfrac{1}{\sqrt{2}}\right)$$

All pairwise inner products = 0, all norms = 1. ✓

**Theorem 19 (Anton §4.9) — orthogonal sets of nonzero vectors are [[linear-independence|linearly independent]].**

*Proof*: Suppose $k_1\mathbf{v}_1 + k_2\mathbf{v}_2 + \cdots + k_n\mathbf{v}_n = \mathbf{0}$. For each $\mathbf{v}_i \in S$, take the inner product of both sides with $\mathbf{v}_i$:

$$\langle k_1\mathbf{v}_1 + \cdots + k_n\mathbf{v}_n,\; \mathbf{v}_i \rangle = \langle \mathbf{0}, \mathbf{v}_i \rangle = 0$$

Expanding the left side by linearity:

$$k_1\langle\mathbf{v}_1,\mathbf{v}_i\rangle + k_2\langle\mathbf{v}_2,\mathbf{v}_i\rangle + \cdots + k_n\langle\mathbf{v}_n,\mathbf{v}_i\rangle = 0$$

By orthogonality of S: $\langle\mathbf{v}_j, \mathbf{v}_i\rangle = 0$ when $j \neq i$, so every term vanishes except the $i$-th:

$$k_i\langle\mathbf{v}_i,\mathbf{v}_i\rangle = 0$$

Since the vectors are nonzero, $\langle\mathbf{v}_i,\mathbf{v}_i\rangle \neq 0$ (axiom 4 — positivity). Therefore $k_i = 0$. Since $i$ is arbitrary, $k_1 = k_2 = \cdots = k_n = 0$, so S is linearly independent. $\blacksquare$

**Theorem 18 (Anton §4.9) — coordinate formula** — if $S = \{\mathbf{v}_1,\ldots,\mathbf{v}_n\}$ is an orthonormal [[basis-and-dimension|basis]] for V, then every $\mathbf{u} \in V$ is:

$$\mathbf{u} = \langle \mathbf{u}, \mathbf{v}_1 \rangle\mathbf{v}_1 + \langle \mathbf{u}, \mathbf{v}_2 \rangle\mathbf{v}_2 + \cdots + \langle \mathbf{u}, \mathbf{v}_n \rangle\mathbf{v}_n$$

*Proof*: Since S is a basis, write $\mathbf{u} = k_1\mathbf{v}_1 + \cdots + k_n\mathbf{v}_n$. Take the inner product of both sides with $\mathbf{v}_i$:

$$\langle \mathbf{u}, \mathbf{v}_i \rangle = k_1\langle\mathbf{v}_1,\mathbf{v}_i\rangle + \cdots + k_n\langle\mathbf{v}_n,\mathbf{v}_i\rangle$$

Since S is orthonormal: $\langle\mathbf{v}_j,\mathbf{v}_i\rangle = 0$ for $j \neq i$ and $\langle\mathbf{v}_i,\mathbf{v}_i\rangle = 1$. Every term vanishes except the $i$-th:

$$\langle \mathbf{u}, \mathbf{v}_i \rangle = k_i \cdot 1 = k_i \qquad \blacksquare$$

Each coefficient is a single inner product — no linear system to solve.

**Theorem 20 (Anton §4.9) — orthogonal projection onto a subspace** — let $\{\mathbf{v}_1,\ldots,\mathbf{v}_r\}$ be an orthonormal set in V and W = span{v₁,...,vᵣ}. Then every $\mathbf{u} \in V$ splits uniquely as:

$$\mathbf{u} = \mathbf{w}_1 + \mathbf{w}_2$$

where $\mathbf{w}_1 \in W$ and $\mathbf{w}_2 \perp W$, given by:

$$\mathbf{w}_1 = \langle\mathbf{u},\mathbf{v}_1\rangle\mathbf{v}_1 + \cdots + \langle\mathbf{u},\mathbf{v}_r\rangle\mathbf{v}_r \qquad \text{(proj}_W\mathbf{u)}$$

$$\mathbf{w}_2 = \mathbf{u} - \mathbf{w}_1 \qquad \text{(component of u orthogonal to W)}$$

$\mathbf{w}_1$ is the **orthogonal projection of u onto W**, written $\text{proj}_W\mathbf{u}$. Key distinction from Theorem 18: the set {v₁,...,vᵣ} does **not** need to be a full basis for V — it only needs to span the subspace W. The formula works for any orthonormal spanning set of W.

| Operation | General basis B | Orthonormal basis Q |
|---|---|---|
| Coordinates of v | Solve $B\mathbf{c} = \mathbf{v}$ | $c_k = \langle\mathbf{v},\mathbf{q}_k\rangle$ |
| Matrix inverse | $(B^TB)^{-1}B^T$ (expensive) | $Q^{-1} = Q^T$ (free) |
| Projection onto span | Full formula | $QQ^T\mathbf{v}$ |

```python
import numpy as np

# Build an orthonormal basis for R^3 and verify
Q = np.array([
    [0,  1,  0        ],
    [1/np.sqrt(2), 0,  1/np.sqrt(2)],
    [1/np.sqrt(2), 0, -1/np.sqrt(2)],
]).T  # columns = basis vectors

print(np.allclose(Q.T @ Q, np.eye(3)))   # True — orthonormal ✓

# Coordinates: just dot products
v = np.array([3., 1., 2.])
coords = Q.T @ v                          # c_k = <v, q_k>
v_reconstructed = Q @ coords
print(np.allclose(v, v_reconstructed))   # True ✓
```


## In ML

**PCA columns are orthonormal** — principal components are the eigenvectors of the covariance matrix, orthonormal under the standard inner product. Projecting data onto them reduces to dot products: `score = X @ components.T`. The orthonormality is why components capture independent variance with no redundancy.

**Q in QR and SVD** — every QR decomposition produces an orthonormal Q (built via [[gram-schmidt]]). The U and V matrices in SVD are orthonormal bases for column and row spaces. Orthonormal structure is why $Q^{-1} = Q^T$ — matrix inversion becomes a free transpose, which is computationally critical.

**Transformer attention with normalized queries/keys** — when Q and K are row-normalized to unit length, `QK^T` becomes a matrix of cosines — pure angle measurements. The orthonormality ideal is the geometric target: orthogonal heads would capture fully independent attention patterns with no redundancy.

## Exercises

**Basic** — Verify that $S = \{(1/\sqrt{2}, 1/\sqrt{2}),\, (-1/\sqrt{2}, 1/\sqrt{2})\}$ is orthonormal in R^2. Then express $\mathbf{v} = (3, 1)$ in this basis using the coordinate formula.

**Intermediate** — Prove the coordinate formula: if $\{\mathbf{q}_1,\ldots,\mathbf{q}_n\}$ is orthonormal and $\mathbf{v} = \sum c_k \mathbf{q}_k$, show that $c_k = \langle\mathbf{v}, \mathbf{q}_k\rangle$ by taking the inner product of both sides with $\mathbf{q}_k$.

**Advanced** — Show that an orthonormal matrix Q preserves norms and inner products: $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ and $\langle Q\mathbf{x}, Q\mathbf{y}\rangle = \langle\mathbf{x},\mathbf{y}\rangle$ for all x, y. What does this say about orthonormal transformations geometrically?
