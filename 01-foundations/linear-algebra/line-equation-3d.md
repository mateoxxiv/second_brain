---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[plane-equation]]"
  - "[[point-to-plane-distance]]"
  - "[[dot-product]]"
  - "[[vector-norms]]"
  - "[[vectors-and-vector-spaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 3 — Euclidean Vector Spaces."
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
---

> **TL;DR** — A line in 3D is pinned by one point and a direction vector; the parametric form r(t) = r₀ + t·d traces every point on the line as t sweeps over all real numbers.

---

## Intuition

Stand at a point P₀ and pick a direction to walk — that's your direction vector d. The parametric parameter t is simply how many steps you've taken: t = 0 puts you at P₀, t = 1 puts you one full step forward, t = −1 puts you one step back.

Unlike a plane (which needs a normal and a point), a line needs a *tangent* — something that points along it. The plane's normal [a, b, c] serves as that tangent when the line is perpendicular to the plane.

## Mechanics

**Geometric origin (Anton)** — a line through P₀ with direction v is the set of all points P such that the vector P₀P is parallel to v:

$$\overrightarrow{P_0 P} = t\,\mathbf{v}$$

Since P₀P = P − P₀, rearranging gives the **vector form**:

$$\mathbf{r}(t) = \mathbf{r_0} + t\,\mathbf{v} \qquad t \in \mathbb{R}$$

This is the same equation — P₀P = tv is just the Anton way of saying "every point on the line is reached by walking t steps in direction v from P₀." The key geometric fact: **any vector connecting two points on the line is parallel to v**.

**Parametric (component) form** — one scalar equation per axis:

$$x = x_0 + at \qquad y = y_0 + bt \qquad z = z_0 + ct$$

where d = (a, b, c) is the direction vector.

**Symmetric (Cartesian) form** — derived by solving each parametric equation for t and equating, since all three must give the same t for any point on the line:

$$x = x_0 + at \;\Rightarrow\; t = \frac{x-x_0}{a} \qquad y = y_0 + bt \;\Rightarrow\; t = \frac{y-y_0}{b} \qquad z = z_0 + ct \;\Rightarrow\; t = \frac{z-z_0}{c}$$

$$\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}$$

**Use: checking if a point lies on the line** — plug (x, y, z) into all three ratios. If they all agree, the point is on the line (there exists a valid t). If any ratio differs, no single t can produce it — the point is off the line.

*(Undefined when any of a, b, c = 0 — that axis has no freedom, handle it with an equality instead: e.g. if c = 0 then z = z₀ must hold exactly.)*

**Connection to [[plane-equation]]** — when d = n = [a, b, c] (the plane's normal), the line is perpendicular to the plane ax + by + cz + D = 0. This is the line used to drop a perpendicular from any point to the plane (see [[point-to-plane-distance]]).

| Property | Formula |
|---|---|
| Anton form | P₀P = tv (vector from P₀ to any point P is parallel to v) |
| Vector form | r(t) = r₀ + t·v |
| Parametric | x=x₀+at, y=y₀+bt, z=z₀+ct |
| Symmetric | (x−x₀)/a = (y−y₀)/b = (z−z₀)/c |
| Point on line at t=0 | r₀ (reference point) |
| Direction vector | v = (a, b, c) |
| Line ⊥ to plane | use v = n = plane normal |

```python
import numpy as np

r0 = np.array([1., 0., 0.])   # point on line
d  = np.array([2., 1., -1.])  # direction (e.g. plane normal)

def line(t: float) -> np.ndarray:
    return r0 + t * d

print(line(0))    # [1. 0. 0.]  — starting point
print(line(1))    # [3. 1. -1.] — one step forward
print(line(-1))   # [-1. -1. 1.] — one step backward
```

> Runnable: [[code/foundations/line_equation_3d.py]]

## In ML

**Gradient descent step** — the update rule θ ← θ − α·∇L is exactly the parametric line r(t) = θ − t·∇L, where the direction is −∇L (negative gradient) and t = α is the step size. Gradient descent walks along this line to find a lower loss.

**Ray marching in Neural Radiance Fields (NeRF)** — NeRF casts rays through a scene as r(t) = origin + t·direction. Each sample along the ray is a point on this parametric line. The line equation is the literal query sent to the neural network.

**Linear interpolation** — interpolating between two embeddings v₀ and v₁ is r(t) = v₀ + t·(v₁ − v₀), a parametric line in embedding space. Spherical linear interpolation (slerp) is the curved generalization on a unit sphere.

## Exercises

**Basic** — Write the parametric and symmetric equations for the line through P₀ = (2, −1, 3) with direction d = (1, 2, −2). What point does t = 2 give? Verify it satisfies the symmetric form.

**Intermediate** — A plane has equation 3x − y + 2z = 6. Write the line through Q = (1, 1, 0) that is perpendicular to the plane. Find where this line intersects the plane (substitute into the plane equation and solve for t).

**Advanced** — Two lines: r₁(t) = (1,0,0) + t(1,1,0) and r₂(s) = (0,1,0) + s(1,−1,0). Do they intersect? If yes, find the point. If no, are they parallel or skew? (Skew lines are non-parallel, non-intersecting — only possible in 3D.)
