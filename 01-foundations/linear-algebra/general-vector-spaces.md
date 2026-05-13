---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[vectors-and-vector-spaces]]"
  - "[[euclidean-n-space]]"
  - "[[linear-combination]]"
  - "[[basis-and-dimension]]"
  - "[[linear-independence]]"
  - "[[inner-product-spaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.2 — Espacios Vectoriales Generales."
---

> **TL;DR** — A vector space is any set V where objects can be added and scaled by real numbers under 10 axioms; "vector" means any object in such a space — not just arrows or number tuples.

---

## Intuition

In R^n, vectors are lists of numbers and the operations are obvious. But the 10 axioms that make R^n work are not tied to the shape of the objects at all — they describe *how addition and scaling must behave*. Any collection of objects where those rules hold is a vector space, and its objects earn the name "vector."

Polynomials, matrices, and continuous functions are all vector spaces. R^n is just the most concrete instance.

The key leverage: the 10 axioms are a **certification**. Verify them once for any set of objects → the entire linear algebra toolkit (linear combinations, basis, dimension, projections, Gram-Schmidt, eigendecomposition) applies automatically, regardless of what those objects physically are. One proof covers infinite cases — that's why the abstract definition exists.

## Mechanics

**Definition (Anton §4.2)** — Let V be an arbitrary set with two operations:
- **Addition**: u, v ∈ V → u + v
- **Scalar multiplication**: k ∈ ℝ, u ∈ V → ku

V is a **vector space** (and its objects are called **vectors**) if all 10 axioms hold for all u, v, w ∈ V and scalars k, l:

| # | Axiom | Plain English |
|---|---|---|
| 1 | u + v ∈ V | Adding two vectors always stays inside the space |
| 2 | u + v = v + u | Order of addition doesn't matter |
| 3 | u + (v + w) = (u + v) + w | Grouping of addition doesn't matter |
| 4 | ∃ **0** ∈ V : **0** + u = u | There is a neutral element — adding it changes nothing |
| 5 | ∃ (−u) ∈ V : u + (−u) = **0** | Every vector has an opposite that cancels it to zero |
| 6 | ku ∈ V | Scaling a vector always stays inside the space |
| 7 | k(u + v) = ku + kv | Scaling distributes over vector addition |
| 8 | (k + l)u = ku + lu | Adding scalars distributes over the vector |
| 9 | k(lu) = (kl)u | Chaining two scalings equals one combined scaling |
| 10 | 1u = u | Scaling by 1 leaves the vector unchanged |

**Three vector spaces beyond R^n:**

- **Polynomials** $P_n$ — all polynomials of degree ≤ n. Add $(x^2+1)+(2x-3) = x^2+2x-2$, scale $3(x^2+1) = 3x^2+3$. Zero vector: the zero polynomial. All 10 axioms hold.
- **Matrices** $M_{m \times n}$ — all m×n matrices with element-wise addition and scaling. Zero vector: the zero matrix.
- **Functions** $C[a,b]$ — all continuous functions on [a,b]. Add pointwise: $(f+g)(x) = f(x)+g(x)$. Zero vector: $f(x) = 0$.

In all three cases, the operations look different from R^n but satisfy the exact same 10 rules — which is why they qualify.

```python
import numpy as np

# Polynomials as coefficient arrays: [a0, a1, a2] ↔ a0 + a1·x + a2·x²
p = np.array([1., 0., 1.])   # 1 + x²
q = np.array([-3., 2., 0.])  # -3 + 2x

print(p + q)       # [-2.  2.  1.]  →  -2 + 2x + x²   (axiom 1 ✓)
print(3 * p)       # [ 3.  0.  3.]  →  3 + 3x²          (axiom 6 ✓)
print(p + (-p))    # [ 0.  0.  0.]  →  zero polynomial   (axiom 5 ✓)
print(1 * p)       # [ 1.  0.  1.]  →  same p            (axiom 10 ✓)
```

> Runnable: [[code/foundations/general_vector_spaces.py]]

## In ML

**Model parameter spaces** — the set of all possible weight vectors θ for a neural network is a vector space. Gradient descent is valid because the space is closed: θ − α·∇L stays inside it (axioms 1 and 6). Without closure, the update rule would escape the space.

**Kernel methods and function spaces** — SVMs and Gaussian Processes operate in infinite-dimensional vector spaces of functions, not R^n. The kernel trick computes dot products in that function space without constructing the vectors explicitly. This only works because the function space satisfies the same 10 axioms — the entire linear algebra machinery transfers. See [[inner-product-spaces]].

**Superposition in transformers** — research suggests neural networks represent more features than dimensions by storing them as overlapping [[linear-combination]]s in the residual stream. Understanding this requires thinking of activations as vectors in a general space, not just coordinates in R^n.

## Exercises

**Basic** — Is the set of all 2×2 matrices a vector space? Identify: the zero vector, the negative of A = [[1,2],[3,4]], and verify axiom 7 with one concrete example.

**Intermediate** — Is the set $\{(x, y) \in \mathbb{R}^2 : x \geq 0\}$ (the right half-plane) a vector space? Check all 10 axioms. Which one fails and why?

**Advanced** — Prove that the zero vector in any vector space is unique. Assume two zero vectors **0** and **0'** both satisfy axiom 4, then derive a contradiction using only the axioms.
