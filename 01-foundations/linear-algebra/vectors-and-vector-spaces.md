**Related**: [[vector-operations]], [[basis-and-dimension]], [[linear-independence]]
**Tags**: #status/seed

## Core Idea

A vector is an element of a vector space — an abstract object that can be added to other vectors and scaled by numbers. In ML, we work primarily in $\mathbb{R}^n$: ordered tuples of real numbers that represent data points, embeddings, weights, and gradients.

## Details

### Vector in $\mathbb{R}^n$

An ordered tuple of $n$ real numbers:

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

Examples in ML:
- A data point with 4 features (age, income, height, weight) → vector in $\mathbb{R}^4$
- A flattened 28x28 image → vector in $\mathbb{R}^{784}$
- A GPT embedding → vector in $\mathbb{R}^{1536}$ or higher

### What is a Vector Space?

A **vector space** $V$ over $\mathbb{R}$ is a set of objects closed under two operations:

1. **Addition**: $\mathbf{u}, \mathbf{v} \in V \implies \mathbf{u} + \mathbf{v} \in V$
2. **Scalar multiplication**: $\mathbf{v} \in V, c \in \mathbb{R} \implies c\mathbf{v} \in V$

### The 8 Axioms

These ensure everything "behaves well":

| # | Axiom | Meaning |
|---|-------|---------|
| 1 | $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ | Commutativity |
| 2 | $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ | Associativity of addition |
| 3 | $\exists \mathbf{0}: \mathbf{v} + \mathbf{0} = \mathbf{v}$ | Zero vector exists |
| 4 | $\exists (-\mathbf{v}): \mathbf{v} + (-\mathbf{v}) = \mathbf{0}$ | Additive inverse exists |
| 5 | $c(d\mathbf{v}) = (cd)\mathbf{v}$ | Associativity of scalar mult |
| 6 | $1 \cdot \mathbf{v} = \mathbf{v}$ | Multiplicative identity |
| 7 | $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ | Distributivity over vector add |
| 8 | $(c + d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$ | Distributivity over scalar add |

### Why This Abstraction Matters

Once you prove something for *any* vector space, it works for ALL of these:
- $\mathbb{R}^n$ — the vectors you're used to
- Matrices — a matrix is a vector in a higher-dimensional space
- Functions — functions form a vector space (key for kernel methods in ML)
- Polynomials — polynomial regression lives here

### Subspaces

A **subspace** is a subset of a vector space that is itself a vector space. It must:
- Contain the zero vector $\mathbf{0}$
- Be closed under addition and scalar multiplication

Example: A plane through the origin in $\mathbb{R}^3$ is a 2D subspace. Your dataset might live in a low-dimensional subspace of a high-dimensional space — this is the core insight behind [[PCA]] and dimensionality reduction.

## Code Example

```python
import numpy as np

# R^3 is a vector space — verify closure
u = np.array([1.0, 2.0, 3.0])
v = np.array([4.0, 5.0, 6.0])

# Closure under addition: result is still in R^3
print(u + v)  # [5. 7. 9.]

# Closure under scalar multiplication: result is still in R^3
print(3.5 * u)  # [3.5 7. 10.5]

# Zero vector exists
zero = np.zeros(3)
print(u + zero)  # [1. 2. 3.] — identity holds
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Vector spaces enable [[vector-operations]] — the computational building blocks
- [[basis-and-dimension]] defines the "coordinate system" of a vector space
- [[linear-independence]] determines whether vectors are redundant in a space
- Subspaces connect directly to [[PCA]] — finding optimal low-dimensional representations
- [[Linear Transformations]] are functions between vector spaces — neural network layers

## Sources

- [3Blue1Brown — Essence of Linear Algebra (Chapter 1)](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- [MIT 18.06 — Gilbert Strang, Lecture 1](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.1-2.4](https://mml-book.github.io/book/mml-book.pdf)
