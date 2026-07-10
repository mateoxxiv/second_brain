---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[geometry-of-planar-linear-transformations]]"
  - "[[inverse-linear-transformations]]"
  - "[[matrix-of-linear-transformation]]"
  - "[[plane-equation]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.3"
---

> **TL;DR** — An invertible linear transformation always sends lines to lines, parallel lines to parallel lines, and collinear points to collinear points — so it maps triangles to triangles and parallelograms to parallelograms, never to curved or broken shapes.

---

## Intuition

Knowing the five geometric primitives ([[geometry-of-planar-linear-transformations]]) tells you *how* a matrix distorts space, but not *what structure survives* the distortion. Theorem 6 answers that: however much an invertible $T$ shears, stretches, or rotates the plane, it can never bend a straight line into a curve, break a line into pieces, or turn two parallel lines into intersecting ones. That's a strong, checkable guarantee — and it's exactly why applying $A$ to a square's four vertices is enough to know the whole image shape is a parallelogram, without checking every point in between.

## Mechanics

**Theorem 6 (Anton §5.3)** — If $T:\mathbb{R}^2\to\mathbb{R}^2$ is multiplication by invertible $A$, then:

(a) the image of a line is a line;
(b) the image of a line through the origin is a line through the origin;
(c) images of parallel lines are parallel;
(d) the image of the segment joining $P,Q$ is the segment joining the images of $P,Q$;
(e) three points are collinear if and only if their images are collinear.

**Corollary** — by (c), (d), (e): multiplication by an invertible $A$ maps triangles to triangles and parallelograms to parallelograms. (Invertibility is essential — a singular $A$ can collapse a whole plane onto a line, destroying all of this.)

**Worked example (Anton Example 28)** — $A=\begin{bmatrix}-1&2\\2&-1\end{bmatrix}$ applied to the unit square's vertices $(0,0),(1,0),(0,1),(1,1)$:
$$A\begin{bmatrix}0\\0\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix},\quad A\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}-1\\2\end{bmatrix},\quad A\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}2\\-1\end{bmatrix},\quad A\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}1\\1\end{bmatrix}$$
By the corollary the image is guaranteed to be a **parallelogram** with these four vertices — no need to trace the square's edges point by point.

**Worked example — image of a line (Anton Example 29)** — find the image of the line $y=2x+1$ under invertible $A=\begin{bmatrix}3&1\\2&1\end{bmatrix}$. Since $(x,y)$ maps to $(x',y')=A(x,y)$, substitute the *inverse* map $(x,y)=A^{-1}(x',y')$ into the original equation rather than trying to solve forward:
$$A^{-1}=\begin{bmatrix}1&-1\\-2&3\end{bmatrix} \implies x=x'-y',\quad y=-2x'+3y'$$
Substituting into $y=2x+1$: $-2x'+3y' = 2(x'-y')+1$, which simplifies to $y' = \tfrac{4}{3}x'+\tfrac13$ — the image line.

```python
import numpy as np

A = np.array([[3, 1], [2, 1]])
A_inv = np.linalg.inv(A)

# sample two points on y = 2x + 1, transform them, confirm the images are collinear
p1, p2 = np.array([0, 1]), np.array([1, 3])
q1, q2 = A @ p1, A @ p2
slope = (q2[1] - q1[1]) / (q2[0] - q1[0])
print(slope, q1)   # slope ~ 1.333 (4/3), matching y' = (4/3)x' + 1/3
```

## In ML

**Decision boundaries under linear layers** — a linear classifier's decision boundary is a line (or hyperplane); Theorem 6 guarantees that composing it with any invertible linear preprocessing (whitening, PCA rotation) still yields a line/hyperplane boundary in the new coordinates — linearity of the boundary is preserved exactly, which is why "linear model" claims survive reasonable invertible preprocessing.

**Data augmentation validity** — augmenting images with invertible affine transforms (rotate, shear, scale) preserves straight edges and parallel structure in the scene (e.g. building edges, road lines) — exactly the guarantee that makes such augmentations *label-preserving* for tasks like object detection with axis-aligned or oriented boxes.

**Convex hulls and simplices** — because triangles map to triangles and segments map to segments (parts (c)-(e)), invertible linear maps send convex polytopes to convex polytopes; this underlies why linear transformations of feature space preserve convexity assumptions used in optimization.

## Exercises

**Basic** — Using $A=\begin{bmatrix}-1&2\\2&-1\end{bmatrix}$ from the worked example, verify part (e) of Theorem 6 directly: pick three collinear points on the unit square's diagonal, transform them, and confirm the images are still collinear.

**Intermediate** — Find the image of the line $y=x$ under $A=\begin{bmatrix}3&1\\2&1\end{bmatrix}$ using the inverse-substitution technique from Example 29. Does the image still pass through the origin? Explain using part (b) of the theorem.

**Advanced** — Theorem 6 requires $A$ invertible. Take a singular matrix like $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$ and show it maps the entire plane onto a single line, so two *non-parallel* lines can have parallel (in fact identical) images — which part of Theorem 6 fails, and why does the proof's use of $A^{-1}$ break down?
