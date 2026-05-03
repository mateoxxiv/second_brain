---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[dot-product]]"
  - "[[cross-product]]"
  - "[[vectors-and-vector-spaces]]"
  - "[[projection-onto-subspaces]]"
  - "[[vector-norms]]"
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

For any point r on the plane, the vector (r − r₀) lies *in* the plane and so must be perpendicular to n:

$$\mathbf{n} \cdot (\mathbf{r} - \mathbf{r_0}) = 0$$

**Expanding** (let n = [a, b, c], r = [x, y, z], r₀ = [x₀, y₀, z₀]):

$$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$$

Setting d = ax₀ + by₀ + cz₀ gives the **scalar form**:

$$ax + by + cz = d$$

Moving all terms left gives the **general form**:

$$ax + by + cz + D = 0 \quad \text{where } D = -d = -(ax_0 + by_0 + cz_0)$$

The normal vector can be read directly from the coefficients: **n = [a, b, c]**. No reference point needed — just look at the equation.

**Finding n from two vectors in the plane** — if u and v are two non-parallel vectors lying in the plane, the [[cross-product]] gives the normal:

$$\mathbf{n} = \mathbf{u} \times \mathbf{v}$$

**The normal vector and its norm** — n points perpendicular to every vector in the plane. Its *direction* defines the plane's orientation; its *magnitude* ||n|| is free — any scalar multiple kn defines the exact same plane. This matters because:

- The distance formula divides by ||n|| to cancel out the arbitrary scaling
- If you normalize first — **unit normal** n̂ = n / ||n|| — the formula simplifies to just the dot product:

$$\hat{\mathbf{n}} = \frac{\mathbf{n}}{\|\mathbf{n}\|} \qquad \text{dist}(P) = |\hat{\mathbf{n}} \cdot (\mathbf{P} - \mathbf{r_0})|$$

- In the general form ax + by + cz + D = 0, **if** n = [a,b,c] is already a unit vector, then |D| equals the distance from the origin to the plane directly.

**Distance from a point P to the plane** (general case):

$$\text{dist}(P, \text{plane}) = \frac{|\mathbf{n} \cdot (\mathbf{P} - \mathbf{r_0})|}{\|\mathbf{n}\|}$$

| Property | Formula |
|---|---|
| Dot-normal form | n · (r − r₀) = 0 |
| Scalar form | ax + by + cz = d |
| General form | ax + by + cz + D = 0, where D = −d |
| Normal from general form | n = [a, b, c] (read directly from coefficients) |
| Unit normal | n̂ = n / \|\|n\|\| |
| Normal from two plane vectors | n = u × v |
| Plane through origin | D = 0, so ax + by + cz = 0 |
| Distance point → plane | \|n · (P − r₀)\| / \|\|n\|\| = \|n̂ · (P − r₀)\| |
| Distance from origin (unit n) | \|D\| when \|\|n\|\| = 1 |

```python
import numpy as np

r0 = np.array([1, 0, 0])   # point on plane
u  = np.array([0, 1, 0])   # vector in plane
v  = np.array([0, 0, 1])   # another vector in plane

n = np.cross(u, v)         # normal via cross product: [1, 0, 0]
d = np.dot(n, r0)          # d = 1

P = np.array([3, 2, 1])    # test point
dist = abs(np.dot(n, P - r0)) / np.linalg.norm(n)
print(dist)                # 2.0
```

> Runnable: [[code/foundations/plane_equation.py]]

## In ML

**Support Vector Machines (SVMs)** — the decision boundary of a linear SVM is a hyperplane w · x = b, where w is the normal vector. This is the dot-normal form generalized from 3D to n dimensions. The entire SVM algorithm is about finding the optimal n (w) that maximizes the margin to the two classes.

**Neuron decision boundary** — a single neuron computes z = w · x + b. Setting z = 0 defines the boundary between "fires" and "doesn't fire" — a hyperplane with normal w. Every linear classifier is geometrically a hyperplane, derived from the same dot-normal idea.

**Signed distance and margin** — the distance formula (n · (P − r₀) / ||n||) gives a *signed* distance: positive on one side, negative on the other. This signed distance is exactly the margin quantity in SVMs and the raw logit before sigmoid in logistic regression.

## Exercises

**Basic** — Find the equation of the plane that passes through point (1, 2, 3) with normal vector [2, −1, 4]. Write it in dot-normal form, scalar form ax + by + cz = d, and general form ax + by + cz + D = 0. What is D?

**Intermediate** — Three points: A = (1, 0, 0), B = (0, 2, 0), C = (0, 0, 3). Find the normal vector using the [[cross-product]] of AB and AC. Then write the plane equation and compute the distance from point P = (1, 1, 1) to the plane.

**Advanced** — Show that the distance formula dist = |n · (P − r₀)| / ||n|| is equivalent to projecting the vector (P − r₀) onto the unit normal n̂. Connect this to [[projection-onto-subspaces]] and explain why it gives the *shortest* distance from P to any point on the plane.
