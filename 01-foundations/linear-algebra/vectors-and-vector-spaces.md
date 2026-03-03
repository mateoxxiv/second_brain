**Related**: [[vector-operations]], [[vector-norms]], [[basis-and-dimension]], [[linear-independence]], [[projection]]
**Tags**: #status/seed

## Core Idea

A vector is a container for multiple related numbers — a way to represent a
"thing" that has many attributes at once. A vector space is the universe those
vectors live in: a set of rules that guarantee you can add, scale, and combine
vectors without breaking anything. If ML is a language, vectors are the nouns
and vector spaces are the grammar.

## Details

### Intuition: What IS a vector?

Forget "arrows" for a moment. A vector is **an ordered list of numbers that
together describe something**:

```
A patient:        [age, weight, blood_pressure, heart_rate]
                  [35,  72,     120,            68]
                  → a vector in R^4

A grayscale image: [pixel_1, pixel_2, ..., pixel_784]
                   → a vector in R^784

A word embedding:  [0.23, -0.87, 0.41, ..., 1.05]
                   → a vector in R^1536
```

Each number is a **coordinate** — a measurement along one dimension. The
vector is the complete description. When you load a dataset with 1000 rows
and 10 columns, you have 1000 vectors in $\mathbb{R}^{10}$.

### Formal Definition

A vector in $\mathbb{R}^n$ is an ordered tuple of $n$ real numbers:

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

The $n$ is the **dimensionality** — how many numbers you need to describe
each object. More features = higher dimension.

### What is a Vector Space?

A vector space is the "playground" where vectors live. It guarantees two
things:

1. **Closure under addition**: Add two vectors → get another valid vector
2. **Closure under scalar multiplication**: Scale a vector → get another valid vector

**Why does closure matter?** Think of it this way: if you're training a model
and compute a gradient update $\mathbf{w}_{\text{new}} = \mathbf{w} - \alpha \nabla L$,
you need the result to still be a valid vector in the same space. If
subtraction or scaling could "escape" the space, gradient descent would break.

Closure guarantees that **operations keep you inside the space.** You can
combine vectors freely without worrying about producing something invalid.

### Example: What's NOT a vector space?

The set of all 2D vectors with positive components: $\{(x, y) : x > 0, y > 0\}$

Is it closed under scalar multiplication? Take $\mathbf{v} = (3, 4)$ and
multiply by $c = -1$: you get $(-3, -4)$ — negative components! You've
"escaped" the set. **Not a vector space.**

This is why the axioms exist: to prevent this kind of breakdown.

### The 8 Axioms: Rules of the Game

A vector space $V$ over $\mathbb{R}$ must satisfy these 8 rules. They're not
arbitrary — each one prevents a specific kind of pathological behavior:

| # | Axiom | What it prevents |
|---|-------|-----------------|
| 1 | $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ | Order of addition shouldn't matter |
| 2 | $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ | Grouping shouldn't matter |
| 3 | $\exists \mathbf{0}: \mathbf{v} + \mathbf{0} = \mathbf{v}$ | There must be a "do nothing" element |
| 4 | $\exists (-\mathbf{v}): \mathbf{v} + (-\mathbf{v}) = \mathbf{0}$ | You can always "undo" addition |
| 5 | $c(d\mathbf{v}) = (cd)\mathbf{v}$ | Scaling twice = scaling by the product |
| 6 | $1 \cdot \mathbf{v} = \mathbf{v}$ | Scaling by 1 does nothing |
| 7 | $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ | Scaling distributes over addition |
| 8 | $(c + d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$ | Addition of scalars distributes |

In practice, you rarely check all 8 — for subsets of $\mathbb{R}^n$, you just
verify closure (axioms 1-8 are inherited from $\mathbb{R}^n$ automatically).

### Why This Abstraction Matters

The power of vector spaces is **generality**. Once you prove something works
for any vector space, it works for ALL of these simultaneously:

| Object | Why it's a vector space |
|--------|----------------------|
| $\mathbb{R}^n$ | The vectors you work with daily in ML |
| Matrices | A $3 \times 3$ matrix is a vector in $\mathbb{R}^9$ (just reshape it) |
| Functions | $f(x) + g(x)$ and $c \cdot f(x)$ produce new functions. Key for kernel methods |
| Polynomials | $p(x) + q(x)$ is a polynomial. Polynomial regression lives here |

This means PCA, projection, and eigendecomposition work on ALL of these — not
just lists of numbers. The abstraction pays for itself.

### Subspaces: "Spaces within spaces"

A **subspace** is a smaller vector space living inside a bigger one. It must:
- Contain the zero vector $\mathbf{0}$ (the "origin")
- Be closed under addition and scalar multiplication (operations don't escape it)

**Analogy**: Think of a building (3D space). A specific floor is a 2D subspace —
you can walk anywhere on that floor (add, scale), but you're constrained
to that plane. A hallway on that floor is a 1D subspace — even more constrained.

```
R^3 (all of 3D space)
 │
 ├── A plane through the origin (2D subspace)
 │    │
 │    └── A line through the origin (1D subspace)
 │         │
 │         └── Just the origin {0} (0D subspace)
```

### Why Subspaces Matter in ML

**Your data almost never fills the full space.** 784-dimensional images don't
use all 784 dimensions equally — most pixels are correlated. The data actually
lives on a lower-dimensional subspace.

| Concept | The subspace is... |
|---------|-------------------|
| **PCA** | The top-$k$ principal components. Project data onto this subspace to reduce dimensions |
| **Linear regression** | The column space of $X$. The prediction $\hat{\mathbf{y}}$ lives here; the residual is perpendicular to it |
| **Null space** | The set of inputs a matrix maps to zero. Dead neurons in a neural network live here |
| **Feature subspace** | If 3 of your 10 features are always correlated, the data lives on a 7D subspace of $\mathbb{R}^{10}$ |

Finding and exploiting subspaces is how you reduce complexity, speed up
computation, and build models that generalize.

### Worked Example: Is This a Subspace?

**Test**: Is the set $S = \{(x, y, 0) : x, y \in \mathbb{R}\}$ (the xy-plane in
$\mathbb{R}^3$) a subspace?

1. Contains $\mathbf{0}$? Yes — $(0, 0, 0)$ has the form $(x, y, 0)$. ✓
2. Closed under addition? $(x_1, y_1, 0) + (x_2, y_2, 0) = (x_1+x_2, y_1+y_2, 0)$ — still has $z = 0$. ✓
3. Closed under scaling? $c(x, y, 0) = (cx, cy, 0)$ — still has $z = 0$. ✓

**Yes, it's a subspace.** This is the subspace that [[projection-onto-subspaces]]
projects onto when you "drop" the z-coordinate.

**Counter-test**: Is $S = \{(x, y, 1) : x, y \in \mathbb{R}\}$ (a plane at
height $z = 1$) a subspace?

Contains $\mathbf{0}$? $(0, 0, 0)$ has $z = 0 \neq 1$. **No.** Fails immediately.
Subspaces must pass through the origin.

## Code Example

```python
import numpy as np

# A vector in R^4: a patient's measurements
patient = np.array([35.0, 72.0, 120.0, 68.0])

# Vector space guarantees: operations stay in R^4
another_patient = np.array([28.0, 65.0, 110.0, 72.0])
combined = patient + another_patient      # still R^4
scaled = 0.5 * patient                    # still R^4

# Subspace check: does the xy-plane in R^3 contain the zero vector?
zero = np.zeros(3)
print(zero[2] == 0)  # True — (0,0,0) is in the xy-plane

# Verify closure: adding two xy-plane vectors stays in the xy-plane
v1 = np.array([3.0, 4.0, 0.0])   # z = 0
v2 = np.array([1.0, -2.0, 0.0])  # z = 0
v3 = v1 + v2                      # [4, 2, 0] — z still 0 ✓
print(f"Sum stays in subspace: z = {v3[2]}")
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Vector spaces enable [[vector-operations]] — the computational building blocks
- [[vector-norms]] give vectors a notion of "size" within the space
- [[basis-and-dimension]] defines the coordinate system of a vector space
- [[linear-independence]] determines whether vectors are redundant in a space
- Subspaces are the target of [[projection]] and [[projection-onto-subspaces]]
- Subspaces connect directly to [[PCA]] — finding optimal low-dimensional representations
- [[Linear Transformations]] are functions between vector spaces — neural network layers

## Sources

- [3Blue1Brown — Essence of Linear Algebra (Chapter 1)](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- [3Blue1Brown — Span and linear combinations](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- [MIT 18.06 — Gilbert Strang, Lecture 1](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.1-2.4](https://mml-book.github.io/book/mml-book.pdf)
