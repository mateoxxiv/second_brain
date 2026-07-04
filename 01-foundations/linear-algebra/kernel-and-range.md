---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[linear-transformations]]"
  - "[[subspaces]]"
  - "[[general-vector-spaces]]"
  - "[[row-and-column-spaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.2"
---

> **TL;DR** — The kernel of a linear transformation $T$ is everything it crushes to zero; the range is everything it can actually reach in $W$ — together they measure how much information $T$ destroys and how much of the target space it covers.

---

## Intuition

Once you know what $T$ does to a **basis** of $V$, you know what it does to every vector in $V$ — because any vector is a linear combination of basis vectors, and $T$ preserves linear combinations (the superposition property from [[linear-transformations]]). This section asks two follow-up questions about that behavior:

- **What does $T$ destroy?** Some nonzero vectors might collapse to $\mathbf{0}$ — that "blind spot" is the **kernel**.
- **What can $T$ reach?** $T$ might not hit every vector in $W$ — the vectors it *does* reach form the **range**.

**Concrete example** — let $T(x,y) = (x, 0)$, flattening every vector onto the x-axis (a shadow cast straight down):

- *Kernel:* $T(x,y) = (0,0)$ forces $x=0$, but $y$ is free. So $\ker(T) = \{(0,y)\}$ — the entire **y-axis**. Anything standing straight up gets crushed to the origin; $T$ is blind to the $y$-component, and that information is gone for good.
- *Range:* the output is always $(x, 0)$ for some $x$ — you can never produce a point like $(3,5)$, since the second coordinate is always forced to $0$. So $R(T) = \{(x,0)\}$ — the **x-axis**, everywhere $T$'s outputs actually land. (*Recorrido* literally means "the route traveled" in Spanish — a good name for "everywhere this function's outputs go.")

So: kernel lives in the *input* space $V$ (what gets lost), range lives in the *output* space $W$ (what's actually hit). Think of $T$ as a lossy projector: the kernel is the shadow that disappears, the range is the wall the shadow lands on.

## Mechanics

**Theorem 1 (Anton §5.2)** — If $T: V \to W$ is a linear transformation, then:

$$\text{(a) } T(\mathbf{0}) = \mathbf{0} \qquad \text{(b) } T(-\mathbf{v}) = -T(\mathbf{v}) \qquad \text{(c) } T(\mathbf{v}-\mathbf{w}) = T(\mathbf{v}) - T(\mathbf{w})$$

**Proof** — All three follow from linearity alone, no new axioms needed:

(a) Since $0\mathbf{v} = \mathbf{0}$ for any $\mathbf{v}$: $T(\mathbf{0}) = T(0\mathbf{v}) = 0\,T(\mathbf{v}) = \mathbf{0}$.

(b) $T(-\mathbf{v}) = T((-1)\mathbf{v}) = (-1)T(\mathbf{v}) = -T(\mathbf{v})$.

(c) Rewrite the subtraction as addition: $\mathbf{v}-\mathbf{w} = \mathbf{v} + (-1)\mathbf{w}$, so
$$T(\mathbf{v}-\mathbf{w}) = T(\mathbf{v} + (-1)\mathbf{w}) = T(\mathbf{v}) + (-1)T(\mathbf{w}) = T(\mathbf{v}) - T(\mathbf{w})$$

**Definition (Anton §5.2)** — For a linear transformation $T: V \to W$:

| Term | Notation | Definition | Lives in |
|---|---|---|---|
| Kernel (núcleo) | $\ker(T)$ | $\{\mathbf{v} \in V : T(\mathbf{v}) = \mathbf{0}\}$ | $V$ |
| Range (recorrido) | $R(T)$ | $\{\mathbf{w} \in W : \mathbf{w} = T(\mathbf{v}) \text{ for some } \mathbf{v} \in V\}$ | $W$ |

Part (a) of Theorem 1 guarantees $\mathbf{0} \in \ker(T)$ always — the kernel is never empty.

```python
import numpy as np

A = np.array([[1, 2], [2, 4]])   # T(x) = Ax, rank-deficient (rows are dependent)

# Kernel: solve Ax = 0 -> null space, via SVD
u, s, vt = np.linalg.svd(A)
null_mask = np.isclose(s, 0)
kernel_basis = vt[len(s):][::-1] if not null_mask.any() else vt[-1]
print("kernel direction:", kernel_basis)          # e.g. [-0.89, 0.45] ~ span{[-2, 1]}
print("T(kernel vector) ~ 0:", A @ kernel_basis)  # ~ [0, 0]

# Range: column space of A
print("range = span of columns:", A[:, 0])        # [1, 2] -- everything reachable is a multiple of this
```

## In ML

**Weight matrix null space** — for a layer $\mathbf{z} = W\mathbf{x}$, $\ker(W)$ is the set of input directions the layer is completely blind to; anything in that direction is invisible downstream, no matter how it changes. A large kernel signals redundant or under-parameterized input directions.

**Range and achievable outputs** — in linear regression $\hat{\mathbf{y}} = X\boldsymbol\beta$, $R(T)$ is the column space of $X$: the only targets reachable exactly. If $\mathbf{y} \notin R(T)$, the best fit is the projection of $\mathbf{y}$ onto $R(T)$ — the residual is orthogonal to it (see [[projection-onto-subspaces]]).

**Autoencoders as kernel/range engineering** — the encoder's effective kernel determines what input variation gets discarded (compression), while the decoder's range determines what can be reconstructed. A well-trained autoencoder has a small, meaningful kernel (only noise is destroyed) and a range that covers the true data manifold.

## Exercises

**Basic** — For $T(x, y) = (x + y, x + y)$ on $\mathbb{R}^2$, find $\ker(T)$ and $R(T)$ explicitly. What geometric objects are they?

**Intermediate** — Using Theorem 1(c), show that if $T(\mathbf{v}_1) = T(\mathbf{v}_2)$ for $\mathbf{v}_1 \neq \mathbf{v}_2$, then $\ker(T)$ contains a nonzero vector. (This is the key link to injectivity — see [[injective-and-surjective-linear-transformations]].)

**Advanced** — Prove that $\ker(T)$ is always a subspace of $V$ and $R(T)$ is always a subspace of $W$, using the two-condition test from [[subspaces]] together with Theorem 1.
