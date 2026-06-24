---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[dot-product]]"
  - "[[cross-product]]"
  - "[[vectors-and-vector-spaces]]"
  - "[[vector-norms]]"
  - "[[line-equation-3d]]"
  - "[[point-to-plane-distance]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 3 — Euclidean Vector Spaces."
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
---

> **TL;DR** — A plane is fully defined by one point on it and a normal vector; the dot product condition n · (r − r₀) = 0 captures every point on the plane at once.

---

## Intuition

A plane is like the floor of a room. You need two things to pin it down: one point on the floor (a reference), and which way is "up" (the normal direction). Any other point on the floor forms a vector with your reference point — and that vector is always horizontal, never vertical. Horizontal means perpendicular to "up", which means their [[dot-product]] is zero.

That single condition — dot product with the normal equals zero — defines every point on the plane.

## Mechanics

**Setup**: given a known point r₀ on the plane and a normal vector n perpendicular to it.

For any point r on the plane, the vector (r − r₀) lies *in* the plane and must be perpendicular to n:

$$\mathbf{n} \cdot (\mathbf{r} - \mathbf{r_0}) = 0$$

**Expanding** (let n = [a, b, c], r = [x, y, z], r₀ = [x₀, y₀, z₀]):

$$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0 \quad \textbf{(punto-normal form)}$$

Setting d = ax₀ + by₀ + cz₀ gives the **scalar form**:

$$ax + by + cz = d$$

Moving all terms left gives the **general form**:

$$ax + by + cz + D = 0 \quad \text{where } D = -d$$

The normal vector is read directly from coefficients: **n = [a, b, c]**.

**Normal vector and unit normal** — direction defines the plane; magnitude is free (kn gives the same plane). Normalizing gives the unit normal used in distance calculations (see [[point-to-plane-distance]]):

$$\hat{\mathbf{n}} = \frac{\mathbf{n}}{\|\mathbf{n}\|}$$

**Finding n from two vectors in the plane** — if u and v lie in the plane, [[cross-product]] gives the normal:

$$\mathbf{n} = \mathbf{u} \times \mathbf{v}$$

| Property | Formula |
|---|---|
| Dot-normal form | n · (r − r₀) = 0 |
| Scalar form | ax + by + cz = d |
| General form | ax + by + cz + D = 0, D = −d |
| Normal from general form | n = [a, b, c] (read from coefficients) |
| Unit normal | n̂ = n / \|\|n\|\| |
| Normal from two plane vectors | n = u × v |
| Plane through origin | D = 0 |

```python
import numpy as np

r0 = np.array([1., 0., 0.])
u  = np.array([0., 1., 0.])
v  = np.array([0., 0., 1.])

n = np.cross(u, v)          # [1, 0, 0]
d = np.dot(n, r0)           # 1.0
n_hat = n / np.linalg.norm(n)
print(n, d, n_hat)
```


→ Line perpendicular to this plane: [[line-equation-3d]]
→ Distance from a point to this plane: [[point-to-plane-distance]]

## In ML

**Support Vector Machines** — the SVM decision boundary is a hyperplane w · x = b where w is the normal. The same dot-normal form, generalized from 3D to n dimensions.

**Neuron decision boundary** — a neuron computes z = w · x + b. Setting z = 0 gives the hyperplane separating "fires" from "doesn't fire" — normal vector w, read directly from the weights.

## Exercises

**Basic** — Find the equation of the plane through point (1, 2, 3) with normal [2, −1, 4]. Write it in punto-normal, scalar, and general form. What is D?

**Intermediate** — Three points: A = (1, 0, 0), B = (0, 2, 0), C = (0, 0, 3). Use [[cross-product]] of AB and AC to find the normal. Write the plane equation in general form.

**Advanced** — Prove that any scalar multiple kn defines the same plane as n. Show that the set of points satisfying n · (r − r₀) = 0 is unchanged when n is replaced by kn.
