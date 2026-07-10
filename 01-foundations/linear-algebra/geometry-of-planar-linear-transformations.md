---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[linear-transformations]]"
  - "[[matrix-of-linear-transformation]]"
  - "[[matrix-operations]]"
  - "[[orthogonal-matrix]]"
  - "[[singular-value-decomposition]]"
  - "[[elementary-matrices-as-geometric-transformations]]"
  - "[[inverse-linear-transformations]]"
  - "[[linear-transformations-map-lines-to-lines]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.3"
---

> **TL;DR** — Every geometric effect a $2\times 2$ matrix can have — rotate, mirror, stretch, or slant — is one of five named transformations, and chaining several of them in sequence is just multiplying their standard matrices in the order applied.

---

## Intuition

$T(x,y) = (ax+by,\ cx+dy)$ can be read two equally valid ways: as mapping arrows-to-arrows (vectors), or points-to-points (coordinates). Nothing in the analysis depends on which picture you hold in your head — points-to-points is the more useful one for visualizing shapes deforming. Concrete anchor: reflecting every point across the $y$-axis sends $(x,y) \mapsto (-x,y)$. Evaluate on the basis — $T(e_1) = (-1,0)$, $T(e_2)=(0,1)$ — and the standard matrix drops out: $A = \begin{bmatrix}-1&0\\0&1\end{bmatrix}$ ([[matrix-of-linear-transformation]]).

## Mechanics

Five families of $2\times 2$ linear maps, all built the same way — evaluate on $e_1, e_2$, stack as columns:

| Transformation | Standard matrix | Effect |
|---|---|---|
| Rotation by $\theta$ | $\begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}$ | turns every point about the origin (derivation in [[linear-transformations]]) |
| Reflection about $y$-axis | $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$ | mirrors left/right |
| Reflection about $x$-axis | $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ | mirrors up/down |
| Reflection about $y=x$ | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ | swaps coordinates |
| Expansion/compression in $x$, factor $k>0$ | $\begin{bmatrix}k&0\\0&1\end{bmatrix}$ | stretches ($k>1$) or shrinks ($0<k<1$) horizontally |
| Expansion/compression in $y$, factor $k>0$ | $\begin{bmatrix}1&0\\0&k\end{bmatrix}$ | stretches or shrinks vertically |
| Shear in $x$, factor $k$ | $\begin{bmatrix}1&k\\0&1\end{bmatrix}$ | slides each point by $ky$ parallel to the $x$-axis; the $x$-axis itself stays fixed |
| Shear in $y$, factor $k$ | $\begin{bmatrix}1&0\\k&1\end{bmatrix}$ | slides each point by $kx$ parallel to the $y$-axis; the $y$-axis itself stays fixed |

**Shears, precisely** — an $x$-shear moves $(x,y) \mapsto (x+ky, y)$: points already on $y=0$ don't move at all, and displacement grows with distance from the $x$-axis. It's linear (check both axioms), even though it looks like it "should" be an affine translation — the key is the displacement is proportional to $y$, not constant.

**The identity is a degenerate case of all five families** — rotation with $\theta=0$, shear with $k=0$ (either direction), or scaling with $k=1$ all reduce to $\begin{bmatrix}1&0\\0&1\end{bmatrix}$.

**Composition = matrix product, order matters** — applying $T_1$ then $T_2$ then ... then $T_k$ (each $T_i(\mathbf{x})=A_i\mathbf{x}$) collapses to *one* standard matrix:

$$A = A_k \cdots A_2 A_1 \quad (5.12)$$

Reading (5.12) **right to left** recovers the order the transformations were actually applied — $A_1$ (applied first) sits rightmost, closest to $\mathbf{x}$.

**Order matters, concretely (Anton Example 23)** — let $A_1=\begin{bmatrix}1&2\\0&1\end{bmatrix}$ ($x$-shear, factor 2) and $A_2=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ (reflection about $y=x$). Shear-then-reflect gives $A_2A_1=\begin{bmatrix}0&1\\1&2\end{bmatrix}$; reflect-then-shear gives $A_1A_2=\begin{bmatrix}2&1\\1&0\end{bmatrix}$ — different matrices, so **the order of geometric operations changes the result**, exactly mirroring $AB\neq BA$ in general.

```python
import numpy as np

shear_x2 = np.array([[1, 2], [0, 1]])
reflect_yx = np.array([[0, 1], [1, 0]])

shear_then_reflect = reflect_yx @ shear_x2   # shear applied first (rightmost)
reflect_then_shear = shear_x2 @ reflect_yx   # reflection applied first (rightmost)

print(shear_then_reflect)   # [[0,1],[1,2]]
print(reflect_then_shear)   # [[2,1],[1,0]]
assert not np.allclose(shear_then_reflect, reflect_then_shear)   # order matters
```

## In ML

**Data augmentation is this table** — random rotations, shears, and scale jitter applied to training images are exactly these matrices applied to pixel coordinate grids; stacking several augmentations is the same matrix product shown above.

**Spatial Transformer Networks** learn the entries of an affine matrix (rotation + shear + scale + translation) end-to-end via backprop, letting a CNN warp its own input to cancel out pose variation — the five families here are precisely the degrees of freedom it's allowed to learn.

**SVD generalizes this to any matrix, any dimension** — [[singular-value-decomposition]] shows every matrix factors as rotation · scaling · rotation ($A = U\Sigma V^T$). The five planar primitives above are the $2\times 2$, axis-aligned special case of that same idea: any linear map, however complex, decomposes into rotate–stretch–rotate.

## Exercises

**Basic** — Write the standard matrix for reflection about the $x$-axis, then verify it sends $(3,4) \mapsto (3,-4)$.

**Intermediate** — Find the single matrix equivalent to rotating the plane by $90°$ and then applying an $x$-shear of factor $k=2$ (same order as the worked code above). Apply it to $(1,1)$ and sanity-check the result against applying the two steps separately.

**Advanced** — Using $2\times2$ matrices, show concretely that shear-then-rotate and rotate-then-shear give different results for some point, and connect this to the general fact that matrix multiplication is non-commutative. Under what condition on the two transformations (hint: think about [[orthogonal-matrix]]) would the order *not* matter?
