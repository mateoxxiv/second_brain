---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[plane-equation]]"
  - "[[line-equation-3d]]"
  - "[[dot-product]]"
  - "[[projection-onto-subspaces]]"
  - "[[vector-norms]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 3 — Euclidean Vector Spaces."
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
---

> **TL;DR** — The shortest path from any point to a plane is always along the normal; the distance is |n · (P − r₀)| / ||n||, which collapses to a single dot product when n is a unit vector.

---

## Intuition

Drop a vertical line from a point floating above the floor — the shortest path to the floor is straight down, not diagonal. "Straight down" means along the normal direction. The [[dot-product]] n · (P − r₀) measures how far P has drifted from the plane in that normal direction; dividing by ||n|| corrects for the arbitrary scale of n.

The sign tells you which side: positive means P is on the side n points toward, negative means the opposite side.

## Mechanics

Given plane [[plane-equation]] with normal n = [a, b, c] and reference point r₀, and an external point P:

**Distance formula** (general):

$$\text{dist}(P) = \frac{|\mathbf{n} \cdot (\mathbf{P} - \mathbf{r_0})|}{\|\mathbf{n}\|}$$

**With unit normal** n̂ = n / ||n|| — the denominator disappears:

$$\text{dist}(P) = |\hat{\mathbf{n}} \cdot (\mathbf{P} - \mathbf{r_0})|$$

**From general form** ax + by + cz + D = 0 — substitute P = (x₁, y₁, z₁) directly:

$$\text{dist}(P) = \frac{|ax_1 + by_1 + cz_1 + D|}{\sqrt{a^2 + b^2 + c^2}}$$

When n is already a unit vector, ||n|| = 1 and |D| equals the distance from the origin to the plane.

**Signed distance** — removing the absolute value gives orientation:

$$\text{sd}(P) = \frac{\mathbf{n} \cdot (\mathbf{P} - \mathbf{r_0})}{\|\mathbf{n}\|}$$

Positive: P is on the same side as n. Negative: opposite side.

**Foot of the perpendicular** — the closest point on the plane to P. Walk from P along the normal until you hit the plane. Using the [[line-equation-3d]] r(t) = P + t·n and substituting into the plane equation:

$$t^* = \frac{-(\mathbf{n} \cdot \mathbf{P} + D)}{\|\mathbf{n}\|^2} \qquad \text{foot} = \mathbf{P} + t^*\mathbf{n}$$

Note: dist(P) = |t*| · ||n|| — the foot derivation recovers the distance formula.

| Property | Formula |
|---|---|
| Distance (general) | \|n · (P − r₀)\| / \|\|n\|\| |
| Distance (unit normal) | \|n̂ · (P − r₀)\| |
| Distance (general form) | \|ax₁+by₁+cz₁+D\| / sqrt(a²+b²+c²) |
| Distance from origin | \|D\| when \|\|n\|\| = 1 |
| Signed distance | n · (P − r₀) / \|\|n\|\| |
| Foot of perpendicular | P + t*·n, t* = −(n·P + D) / \|\|n\|\|² |

```python
import numpy as np

def distance_to_plane(P, n, D):
    return abs(np.dot(n, P) + D) / np.linalg.norm(n)

def signed_distance(P, n, D):
    return (np.dot(n, P) + D) / np.linalg.norm(n)

def foot_of_perpendicular(P, n, D):
    t = -(np.dot(n, P) + D) / np.dot(n, n)
    return P + t * n

n = np.array([1., 0., 0.])   # plane x = 1 → general form: x - 1 = 0, D = -1
D = -1.
P = np.array([4., 2., 3.])

print(distance_to_plane(P, n, D))         # 3.0
print(signed_distance(P, n, D))           # 3.0 (same side as n)
print(foot_of_perpendicular(P, n, D))     # [1. 2. 3.]
```


## In ML

**SVM margin** — in a support vector machine, the margin is the distance between the two support hyperplanes. For hyperplane w · x + b = 0, the margin equals 2 / ||w||. Maximizing the margin = minimizing ||w|| = the SVM optimization objective.

**Logistic regression logit** — the raw score w · x + b before the sigmoid is exactly the signed distance from x to the decision hyperplane (scaled by ||w||). Positive logit = positive class side, negative = negative class side.

**Level set methods** — in differentiable rendering and physics simulation, signed distance functions (SDFs) represent surfaces as the set of points at signed distance 0. Querying an SDF at any point gives its exact distance to the surface — this is the point-to-plane formula generalized to curved surfaces.

## Exercises

**Basic** — Plane: 2x − y + 2z = 6. Point: P = (3, 1, 2). Compute the distance using the general form formula. Verify ||n|| first.

**Intermediate** — Find the foot of the perpendicular from Q = (4, 0, 0) to the plane x + y + z = 3. Confirm the foot lies on the plane (substitute back) and that the vector from foot to Q is parallel to n.

**Advanced** — Derive the distance formula from the foot of the perpendicular. Start from r(t) = P + t·n, substitute into n · r + D = 0, solve for t*, compute ||t*·n||, and show it equals |n·P + D| / ||n||.
