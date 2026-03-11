**Related**: [[vector-operations]], [[basis-and-dimension]], [[linear-independence]], [[vectors-and-vector-spaces]], [[projection-onto-subspaces]]
**Tags**: #status/growing

## Core Idea

A linear combination is the most fundamental operation in all of ML: pick some
vectors, scale each one by a number, add them up. That's it.

**Analogy**: Think of mixing paint. You have base colors (vectors) and you
choose how much of each to use (coefficients). The result is a new color
(a new vector). Different amounts of the same bases produce different results.
The bases are fixed — the coefficients are your degrees of freedom.

Why is this so important? Because almost every ML computation — a neuron firing,
a gradient update, a PCA reconstruction, a regression prediction — is a linear
combination. If you understand this operation deeply, you can read any ML equation.

## Details

### Definition

Given vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$ and scalars
$c_1, c_2, \ldots, c_k$:

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$$

The vectors are the **building blocks**. The scalars $c_i$ are the
**coefficients** (also called "weights" — same word ML uses for model parameters,
and that's not a coincidence).

Note: [[vector-operations|addition]] and [[vector-operations|scalar multiplication]]
are just special cases of linear combination:
- Addition: $1 \cdot \mathbf{u} + 1 \cdot \mathbf{v}$ (both coefficients = 1)
- Scalar multiplication: $c \cdot \mathbf{v}$ (one vector, one coefficient)

### Worked Example: Building a Point from Basis Vectors

The standard basis in 2D:

$$\mathbf{e}_1 = \begin{bmatrix}1\\0\end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix}0\\1\end{bmatrix}$$

Build the point $[3, 2]$:

$$3\begin{bmatrix}1\\0\end{bmatrix} + 2\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}3\\0\end{bmatrix} + \begin{bmatrix}0\\2\end{bmatrix} = \begin{bmatrix}3\\2\end{bmatrix}$$

The numbers [3, 2] aren't just "components" — they're the coefficients that
tell you how much of each basis vector to use. **Coordinates ARE linear
combination coefficients.** This is why [[basis-and-dimension|change of basis]]
changes the numbers: different building blocks need different amounts to reach
the same point.

### Worked Example: Non-Standard Basis

Same point $\begin{bmatrix}3\\2\end{bmatrix}$, different basis:

$$\mathbf{b}_1 = \begin{bmatrix}1\\1\end{bmatrix}, \quad \mathbf{b}_2 = \begin{bmatrix}1\\-1\end{bmatrix}$$

What coefficients do we need?

$$c_1\begin{bmatrix}1\\1\end{bmatrix} + c_2\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}3\\2\end{bmatrix}$$

This gives the system:
- $c_1 + c_2 = 3$
- $c_1 - c_2 = 2$

Add both: $2c_1 = 5 \implies c_1 = 2.5$
Subtract: $2c_2 = 1 \implies c_2 = 0.5$

Verify: $2.5\begin{bmatrix}1\\1\end{bmatrix} + 0.5\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}2.5\\2.5\end{bmatrix} + \begin{bmatrix}0.5\\-0.5\end{bmatrix} = \begin{bmatrix}3\\2\end{bmatrix}$ ✓

Same point, different recipe, different coefficients.

### What Can You Reach? The Span

The set of ALL possible linear combinations of a set of vectors is called the
**span** (explored fully in [[basis-and-dimension]]):

$$\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_k) = \{c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k \mid c_i \in \mathbb{R}\}$$

```
1 vector:           span is a LINE
[1, 0] →            all points [c, 0] for any c

                    <--------*-------->
                             origin

2 independent        span is a PLANE
vectors:             all points [c1, c2] for any c1, c2
[1,0] and [0,1]
                         * * * * *
                        * * * * *
                       * * * * *
                        * * * * *
                         * * * * *

2 dependent          span is still a LINE
vectors:             [2,0] = 2 * [1,0] — no new direction
[1,0] and [2,0]
                    <--------*-------->
                             origin
```

**Key question**: If you add a new vector, does the span grow? Only if the new
vector is [[linear-independence|linearly independent]] — pointing in a direction
you can't already reach.

### When Coefficients Are Unique (and When They're Not)

If your vectors are [[linear-independence|independent]] (they form a
[[basis-and-dimension|basis]]), then every point has **exactly one** recipe.
One c1, one c2. No ambiguity.

**Independent example** — unique recipe:

```
v1 = [1, 1],  v2 = [2, -1]      ← independent (not scalar multiples)

Write w = [5, 3] as c1*v1 + c2*v2:

  c1 + 2*c2 = 5
  c1 -   c2 = 3

  Subtract: 3*c2 = 2 → c2 = 2/3
  Back-substitute: c1 = 3 + 2/3 = 11/3

  Only ONE solution. No other recipe works.
```

**Dependent example** — infinite recipes:

If your vectors are [[linear-independence|dependent]], the same point has
**infinitely many** recipes. Concrete example:

```
v1 = [1, 2],  v2 = [2, 4]      ← v2 = 2 * v1 (dependent!)

Write w = [3, 6] as c1*v1 + c2*v2:

  c1=3, c2=0  →  3*[1,2] + 0*[2,4]  = [3,6]  ✓
  c1=1, c2=1  →  1*[1,2] + 1*[2,4]  = [3,6]  ✓
  c1=-1, c2=2 → -1*[1,2] + 2*[2,4]  = [3,6]  ✓
```

You have two ingredients but **they're the same flavor** — you can trade freely
between them. Infinite recipes for the same result.

**Why this breaks ML**: Imagine a house price model with two features:

```
price = c1 * bedrooms + c2 * bedrooms_doubled

If bedrooms_doubled = 2 * bedrooms:
  c1=100, c2=0   →  price = 100 * bedrooms
  c1=0,   c2=50  →  price = 50 * (2*bedrooms) = 100 * bedrooms
  c1=50,  c2=25  →  same prediction, different weights
```

The **prediction is identical** but the weights are wildly different. The model
can't decide which weight to assign. Small data changes make the weights flip
dramatically — that's **instability**. The fix? Remove redundant features
(dependent vectors) so coefficients become unique. The [[determinant]] being
zero is one quick way to detect this problem.

### Where Linear Combinations Appear in ML

| Context | What the linear combination looks like |
|---------|---------------------------------------|
| **Neural network neuron** | $z = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n + b$ |
| **Gradient descent** | $\mathbf{w}_{\text{new}} = 1 \cdot \mathbf{w} - \alpha \cdot \nabla L$ |
| **Matrix-vector multiply** | Each output row is a linear combination of input components |
| **PCA reconstruction** | $\hat{\mathbf{x}} = c_1 \cdot \text{PC}_1 + c_2 \cdot \text{PC}_2 + \cdots$ |
| **Linear regression** | $\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots$ |
| **Projection onto subspace** | $\mathbf{p} = \hat{x}_1 \mathbf{a}_1 + \hat{x}_2 \mathbf{a}_2$ — finding the best coefficients |

**The pattern**: you have building blocks (features, basis vectors, principal
components) and you're choosing coefficients (weights, coordinates, loadings)
to construct the output. The entire field of ML can be seen as: "find the
coefficients that minimize some error."

## Code Example

```python
import numpy as np

# Building [3, 2] from the standard basis
e1, e2 = np.array([1, 0]), np.array([0, 1])
point = 3 * e1 + 2 * e2  # [3, 2]

# Same point, different basis, different coefficients
b1, b2 = np.array([1, 1]), np.array([1, -1])
point2 = 2.5 * b1 + 0.5 * b2  # [3, 2] — same result

# A neuron IS a linear combination
weights = np.array([0.5, -0.3, 0.8])
inputs = np.array([1.0, 2.0, 0.5])
z = np.dot(weights, inputs)  # 0.5 - 0.6 + 0.4 = 0.3

# Span check: can [1, 2] be reached from v1=[1,0], v2=[3,0]?
# Only if there exist c1, c2 such that c1*[1,0] + c2*[3,0] = [1, 2]
# c1 + 3*c2 = 1 and 0 = 2 — IMPOSSIBLE. [1,2] is outside the span.
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Built from [[vector-operations|addition and scalar multiplication]] — linear combination combines both
- The set of all linear combinations = **span**, explored in [[basis-and-dimension]]
- If coefficients are unique, the vectors form a [[basis-and-dimension|basis]]; if not, they're [[linear-independence|dependent]]
- [[projection-onto-subspaces]] finds the best linear combination of column vectors to approximate a target
- Matrix multiplication is organized sets of linear combinations → [[matrix-operations]]
- Neural network layers compute linear combinations before applying activation → [[Neural Network Fundamentals]]
- [[Linear Regression]] is "find the linear combination of features that best predicts the target"

## Sources

- [3Blue1Brown — Linear combinations, span, and basis](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- [MIT 18.06 — Strang, Lecture 9: Independence, Basis, Dimension](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.3](https://mml-book.github.io/book/mml-book.pdf)
