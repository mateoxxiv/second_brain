---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[geometry-of-planar-linear-transformations]]"
  - "[[matrix-inverse]]"
  - "[[orthogonal-matrix]]"
  - "[[matrix-of-linear-transformation]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.3"
---

> **TL;DR** — If $T:\mathbb{R}^2\to\mathbb{R}^2$ is multiplication by an invertible $A$, multiplication by $A^{-1}$ is the transformation that exactly walks every point back to where it started.

---

## Intuition

Invertibility of a matrix is usually framed algebraically ($\det A\neq0$, [[matrix-inverse]] exists). Geometrically it means something simpler: $T$ never merges two different points into one and never collapses a dimension, so there's always a well-defined way back. If $T$ sends $(x,y)\mapsto(x',y')$, then multiplication by $A^{-1}$ sends $(x',y')\mapsto(x,y)$ — undoing the shape distortion exactly. Every entry in [[geometry-of-planar-linear-transformations]]'s catalogue has an obvious "undo": unshrink what was shrunk, un-rotate by the same angle in reverse.

## Mechanics

**Definition** — if $T:\mathbb{R}^2\to\mathbb{R}^2$ is multiplication by invertible $A$ and $T(x,y)=(x',y')$, then multiplication by $A^{-1}$ satisfies $(x,y) = A^{-1}(x',y')$. Multiplication by $A$ and by $A^{-1}$ are called **inverse transformations**.

**Worked example (compression ↔ expansion)** — $T:\mathbb{R}^2\to\mathbb{R}^2$ compresses the plane by factor $\tfrac12$ in $y$: $A=\begin{bmatrix}1&0\\0&\frac12\end{bmatrix}$. Undoing a $\tfrac12$-compression means expanding by $2$ — confirm directly: $A^{-1}=\begin{bmatrix}1&0\\0&2\end{bmatrix}$.

**Worked example (rotation ↔ rotation by $-\theta$)** — $A=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$ (see rotation derivation in [[linear-transformations]]). Undoing a rotation by $\theta$ means rotating by $-\theta$; substituting $\cos(-\theta)=\cos\theta$, $\sin(-\theta)=-\sin\theta$ into the rotation matrix gives
$$A^{-1} = \begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix} = A^T$$
— the inverse of a rotation is just its transpose, no computation needed. This is exactly the [[orthogonal-matrix]] property $Q^{-1}=Q^T$; rotations are the canonical orthogonal matrices.

**Undo-table for the five primitives:**

| Transformation | Inverse |
|---|---|
| Rotation by $\theta$ | Rotation by $-\theta$ |
| Reflection (any axis or $y=x$) | Itself ($A^{-1}=A$; reflecting twice is identity) |
| Expansion/compression by $k$ | Compression/expansion by $1/k$, same axis |
| Shear by $k$ | Shear by $-k$, same direction |

```python
import numpy as np

theta = np.pi / 6
A = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
A_inv = np.linalg.inv(A)
assert np.allclose(A_inv, A.T)          # rotation's inverse = transpose

p = np.array([2.0, -1.0])
assert np.allclose(A_inv @ (A @ p), p)  # apply then undo -> back to start
```

## In ML

**Normalizing flows** require every layer to be invertible for exactly this reason: the model needs to map a data point forward to the base distribution *and* map a base sample back to data space, using the same transformation run in reverse — the "undo" intuition here is literally a flow's inverse pass.

**Whitening and un-whitening** — standardizing features ($\mathbf{x} \mapsto \Sigma^{-1/2}\mathbf{x}$, an axis-aligned compression/expansion) is invertible precisely so predictions can be mapped back to the original feature scale — the same compression/expansion inverse shown above, generalized to $n$ dimensions.

**Cheap-to-invert weight matrices** — because a rotation's inverse is free (just transpose), architectures that constrain weight matrices to be orthogonal (e.g. some invertible ResNets, unitary RNNs) get numerically stable, easily-invertible layers for free — no matrix inversion routine needed at all.

## Exercises

**Basic** — Find the inverse transformation of an expansion by factor $3$ in the $x$-direction, and verify $AA^{-1}=I$.

**Intermediate** — Find the standard matrix for reflection about $y=x$ and its inverse. Show $A^{-1}=A$ (reflections are self-inverse) by computing $A^2$.

**Advanced** — Prove generally that if $T$ is orthogonal ($Q^TQ=I$), then $T^{-1}=T^T$, using only the definition of matrix inverse (not the specific rotation example above). Then explain why this means composing any sequence of rotations and reflections is always invertible "for free."
