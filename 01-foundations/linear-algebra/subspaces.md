---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[general-vector-spaces]]"
  - "[[linear-combination]]"
  - "[[linear-independence]]"
  - "[[basis-and-dimension]]"
  - "[[projection-onto-subspaces]]"
  - "[[linear-transformations]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.3 — Subespacios."
---

> **TL;DR** — A subspace is a subset of a vector space that is itself a vector space under the same operations; you only need to verify two conditions (closed under addition and scalar multiplication) because the other 8 axioms are inherited for free.

---

## Intuition

Imagine V is all of R³ — every point in 3D space. Some subsets of R³ are "well-behaved" under the vector operations: any plane through the origin, any line through the origin. These are subspaces. Others are not: a plane that doesn't pass through the origin fails immediately because the zero vector isn't in it.

The key insight from Anton §4.3: when W sits inside a known vector space V, most axioms are already guaranteed — they hold for all vectors in V, so they automatically hold for vectors in W. The only axioms that can fail are closure ones (can the operations escape W?). Everything else is inherited.

## Mechanics

**Definition (Anton §4.3)** — A subset W of a vector space V is a **subspace** of V if W is itself a vector space under the same addition and scalar multiplication defined on V.

**Which axioms are inherited?** Axioms 2, 3, 7, 8, 9, 10 hold for all vectors in V — so they automatically hold for any u, v ∈ W ⊆ V. Only axioms 1, 4, 5, 6 can fail.

**Theorem 4 (Anton §4.3) — Two-Condition Test:**

W is a subspace of V **if and only if**:

| Condition | Statement |
|---|---|
| (a) Closed under addition | u, v ∈ W → u + v ∈ W |
| (b) Closed under scalar multiplication | u ∈ W, k ∈ ℝ → ku ∈ W |

**Why only two conditions?** Condition (b) implies axioms 4 and 5:
- k = 0 → 0·u = **0** ∈ W (zero vector exists in W)
- k = −1 → (−1)·u = −u ∈ W (additive inverse exists in W)

So verifying (a) and (b) is equivalent to verifying all 10 axioms for W.

**Examples in R³:**

| Set | Subspace? | Why |
|---|---|---|
| Any plane through the origin | ✓ | Both conditions hold |
| Any line through the origin | ✓ | Both conditions hold |
| Plane NOT through origin | ✗ | Zero vector not in it (axiom 4 fails) |
| Right half-space {x ≥ 0} | ✗ | k = −1 escapes the set (condition b fails) |
| {**0**} (just the zero vector) | ✓ | Trivial subspace, always valid |
| V itself | ✓ | Always a subspace of itself |

```python
import numpy as np

def is_subspace_check(vectors, scalar=-2.0):
    """Check two conditions on a sampled set of vectors."""
    n = len(vectors)
    # Condition (a): closure under addition
    for i in range(n):
        for j in range(n):
            s = vectors[i] + vectors[j]
            # caller must verify s is in the set
    # Condition (b): closure under scalar multiplication
    for v in vectors:
        sv = scalar * v
        # caller must verify sv is in the set
    return True  # verification is problem-specific

# Example: line through origin in R³ — span of [1,2,3]
# Any point on the line: t·[1,2,3]
line = [np.array([1,2,3]) * t for t in [0, 1, -1, 2.5]]
u, v = line[1], line[3]
print(f"u + v on line? {np.allclose((u+v), np.array([1,2,3]) * 3.5)}")  # True ✓
print(f"-2·u on line?  {np.allclose(-2*u, np.array([1,2,3]) * -2)}")   # True ✓
```

> Runnable: [[code/foundations/subspaces.py]]

## In ML

**Null space (kernel)** — the set of all x where Ax = 0 is always a subspace (closure: A(x+y) = Ax+Ay = 0, A(kx) = kAx = 0). In ML, the null space of a weight matrix represents directions the model is completely blind to — understanding it reveals model capacity and parameter redundancy.

**Column space (image)** — the set of all vectors Ax is always a subspace. In linear regression, the column space of X determines what target vectors ŷ are achievable. If y is not in the column space, a perfect fit is impossible — the residual is the component of y orthogonal to the column space. See [[projection-onto-subspaces]].

**Attention heads as subspace projections** — each attention head in a transformer projects queries and keys into a lower-dimensional subspace of the embedding space (via Wq, Wk matrices). Multi-head attention learns different subspaces in parallel, each capturing different semantic relationships. The subspace structure is why heads specialize.

## Exercises

**Basic** — Is the set of all vectors (x, y, z) in R³ where x + y + z = 0 a subspace? Apply the two-condition test. What geometric object is this set?

**Intermediate** — The function space from Anton Example 8: is the set of functions where f(1) = 0 a subspace of all real-valued functions? Verify both conditions. Then check: is the set where f(1) = 1 a subspace? Which condition fails and why?

**Advanced** — Prove that the intersection W₁ ∩ W₂ of two subspaces is always a subspace. Is the union W₁ ∪ W₂ always a subspace? If not, find a counterexample in R².
