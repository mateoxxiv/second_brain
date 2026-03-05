**Related**: [[vectors-and-vector-spaces]], [[vector-operations]], [[linear-combination]], [[basis-and-dimension]], [[cosine-similarity]], [[projection-onto-subspaces]], [[gaussian-elimination]], [[determinant]], [[Matrix Operations and Properties]]
**Tags**: #status/growing

## Core Idea

Linear independence asks one question: **"does every vector in this set bring
something new to the table?"**

If one vector can be built as a [[linear-combination]] of the others, it's
redundant — like hiring someone whose skills your team already covers. In ML,
redundant features waste parameters, cause numerical instability, and make your
model harder to interpret.

## Details

### The Team Analogy

You're building a team:
- Person A: can build walls
- Person B: can do plumbing
- Person C: can build walls AND do plumbing (but nothing A and B can't already do)

Person C is **dependent** — hiring them adds no new capability.

Vectors work the same way. Each vector is a "direction." If a vector points
somewhere you can already reach by combining the others, it's redundant.

### How to Spot It: The Scaling Test

**Two vectors** — the simplest case. Just ask: is one a scaled copy of the other?

```
DEPENDENT                          INDEPENDENT

v1 = [1, 2]                       v1 = [1, 0]
v2 = [3, 6]  ← that's 3 × v1!    v2 = [0, 1]  ← no scaling works

v2 →→→→→→                            v2 ↑
v1 →→                                   |
  Same line. Redundant.                  *--→ v1
                                     Different directions. Both essential.
```

For v1 = [1, 2] and v2 = [3, 6]: can you find `c` where `c * v1 = v2`?

```
c * [1, 2] = [3, 6]
c * 1 = 3  →  c = 3
c * 2 = 6  →  c = 3  ✓  Same c works → DEPENDENT
```

For v1 = [1, 0] and v2 = [0, 1]:

```
c * [1, 0] = [0, 1]
c * 1 = 0  →  c = 0
c * 0 = 1  →  0 = 1  ✗  Impossible → INDEPENDENT
```

### The Formal Definition (and Why It's Written That Way)

Vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$ are **linearly
independent** if:

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \implies c_1 = c_2 = \cdots = c_k = 0$$

In plain English: the ONLY [[linear-combination]] that produces the zero vector
is the boring one where all coefficients are zero.

**Why this definition?** Because if non-zero coefficients exist, you can
rearrange and express one vector in terms of the others:

```
Suppose:   2*v1 + (-1)*v2 = 0
Rearrange: 2*v1 = v2
So:        v2 = 2*v1  ← v2 is redundant!
```

Finding non-zero coefficients = finding a redundancy.

### Geometric Picture

```
DEPENDENT (2D)                    INDEPENDENT (2D)

      v2 = [2,1]                       v2 = [0,1]
       *                                |  *
      /                                 | /
     /   v1 = [4,2]                     |/
    /     (same line!)                  *------→
   *                                  origin   v1 = [1,0]

All on one line.                  Span the whole plane.
Span = just a line.               Span = all of R^2.
```

Rules of thumb:
- **2 vectors in 2D**: dependent if they lie on the same line
- **3 vectors in 3D**: dependent if they all lie on the same plane
- **You can never have more than n independent vectors in R^n** — in R^3,
  a 4th vector is ALWAYS dependent. There are only 3 directions to go.

### Worked Example: 3 Vectors

```
v1 = [1, 0, 0]
v2 = [0, 1, 0]
v3 = [1, 1, 0]
```

Can v3 be built from v1 and v2?

```
c1 * [1,0,0] + c2 * [0,1,0] = [1,1,0]

Component 1: c1 = 1
Component 2: c2 = 1
Component 3: 0 = 0  ✓

Solution: c1 = 1, c2 = 1
```

Check: 1 * [1,0,0] + 1 * [0,1,0] = [1,1,0] = v3 ✓

v3 is just v1 + v2 — **dependent**. The third vector doesn't add a new direction.

Now replace v3 with [0, 0, 1]:

```
c1 * [1,0,0] + c2 * [0,1,0] = [0,0,1]

Component 1: c1 = 0
Component 2: c2 = 0
Component 3: 0 = 1  ✗  IMPOSSIBLE
```

No combination of v1 and v2 can produce [0,0,1]. It points "up" — a direction
they can't reach. **Independent.**

### Three Methods to Test Independence

#### Method 1: Determinant (quick, only for square matrices)

Put vectors as columns, compute the determinant:

For v1 = [1, 2], v2 = [3, 6]:

```
         | 1  3 |
det =    | 2  6 |  = (1)(6) - (3)(2) = 6 - 6 = 0  → DEPENDENT
```

For v1 = [1, 0], v2 = [0, 1]:

```
         | 1  0 |
det =    | 0  1 |  = (1)(1) - (0)(0) = 1  → INDEPENDENT
```

**2x2 determinant formula**: for matrix [[a, b], [c, d]], det = a*d - b*c.

**3x3 determinant step-by-step** (using v1=[1,0,0], v2=[0,1,0], v3=[1,1,0]):

```
| 1  0  1 |
| 0  1  1 |
| 0  0  0 |

Expand along the first row:

det = 1 * det|1  1| - 0 * det|0  1| + 1 * det|0  1|
             |0  0|          |0  0|          |0  0|

    = 1 * (1*0 - 1*0) - 0 + 1 * (0*0 - 1*0)
    = 1 * 0 - 0 + 1 * 0
    = 0  → DEPENDENT
```

The rule:

```
det ≠ 0  →  INDEPENDENT (full space is covered)
det = 0  →  DEPENDENT (some dimension is collapsed)
```

**What does the determinant measure?** It tells you how much a transformation
stretches or squishes space. If det = 0, the transformation squishes everything
into a lower dimension — at least one vector was redundant.

#### Method 2: Rank (works for any shape)

Stack vectors as rows, count how many are genuinely independent:

```
rank = number of vectors  →  all independent
rank < number of vectors  →  some are redundant
```

| Rank equals... | What it means |
|---------------|---------------|
| Number of independent rows | How many non-redundant data points |
| Number of independent columns | How many non-redundant features |
| Dimension of the column space | How many dimensions the data actually spans |

A matrix is **full rank** = no redundancy. **Rank-deficient** = something is redundant.

#### Method 3: SVD null space (most robust, handles floating point)

```python
from numpy.linalg import svd
_, s, _ = svd(matrix)
# Count non-zero singular values
rank = np.sum(s > 1e-10)
```

This is what NumPy uses internally for `matrix_rank`. It handles near-zero
values better than determinant (which can be numerically unstable).

### Independence vs Orthogonality

These are related but NOT the same:

```
Orthogonal:          Independent but         Dependent:
                     NOT orthogonal:

  u ↑                  b /                   a →→→
    |                   /                    b →→→→→→
    |                  / 45°                 (same line)
    *---→ v           *---→ a
   90° apart         not 90°, but           one is just a
   dot product = 0   can't build            scaled copy
                     one from other
```

- **Orthogonal → always independent.** If two vectors are perpendicular
  (dot product = 0, [[cosine-similarity]] = 0), neither can be built from the
  other. Perpendicular directions are always unique.

- **Independent → NOT always orthogonal.** [1, 0] and [1, 1] are independent
  (can't scale one to get the other) but their dot product = 1, not zero.

Orthogonality is a **stronger** condition. Think of it as:

```
All orthogonal sets are independent.
But most independent sets are NOT orthogonal.
Orthogonal ⊂ Independent
```

### Why This Matters in ML

Redundant features cause real problems:

| Situation | What happens | Consequence |
|-----------|-------------|-------------|
| Dependent features in regression | $X^TX$ is singular, can't invert | Training crashes — no unique solution |
| Multicollinearity (near-dependence) | $X^TX$ is almost singular | Weights swing wildly between runs |
| Redundant neurons | Multiple neurons learn the same thing | Wasted compute, slower training |
| High-quality embeddings | Each dimension captures something unique | Rich, compact representations |

**Concrete example**: a dataset with "temperature in Celsius" and "temperature
in Fahrenheit" has a perfect linear dependency ($F = 1.8C + 32$). The model has
infinite ways to split weight between them — is the coefficient 3.0 on Celsius
or 1.67 on Fahrenheit? Both give the same prediction. This ambiguity = instability.

**Fix**: drop one feature, or use [[Regularization (L1/L2)]] which handles
near-dependence by adding a penalty, or use [[PCA]] which creates new
independent features from the correlated ones.

## Code Example

```python
import numpy as np

# --- Method 1: Determinant (square matrices only) ---
A = np.array([[1, 0], [0, 1]])       # independent
B = np.array([[1, 3], [2, 6]])       # dependent (row2 = 2 * row1)
print(np.linalg.det(A))   # 1.0 → independent
print(np.linalg.det(B))   # 0.0 → dependent

# --- Method 2: Rank (any shape) ---
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3_dep = np.array([1, 1, 0])        # v1 + v2
v3_ind = np.array([0, 0, 1])        # new direction

print(np.linalg.matrix_rank([v1, v2, v3_dep]))  # 2 → dependent
print(np.linalg.matrix_rank([v1, v2, v3_ind]))  # 3 → independent

# --- Method 3: SVD null space (most robust) ---
from numpy.linalg import svd
def is_independent(vectors):
    """Check independence via singular values."""
    A = np.array(vectors, dtype=float)
    _, s, _ = svd(A)
    return np.sum(s > 1e-10) == len(vectors)

print(is_independent([v1, v2, v3_ind]))  # True
print(is_independent([v1, v2, v3_dep]))  # False
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Independence is tested via [[linear-combination]] — can you combine others to reproduce a vector?
- Independence determines [[basis-and-dimension]] — a basis is a maximal independent set
- Orthogonal vectors ([[cosine-similarity]] = 0) are always independent, but not vice versa
- Rank connects to [[Matrix Operations and Properties]] — rank-deficient matrices can't be inverted
- Multicollinearity (near-dependence) motivates [[Regularization (L1/L2)]] and [[PCA]]
- In [[vectors-and-vector-spaces]], independence determines how many dimensions a subspace has
- [[projection-onto-subspaces]] requires independent columns for $(A^TA)^{-1}$ to exist

## Sources

- [3Blue1Brown — Linear combinations, span, and basis](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- [MIT 18.06 — Strang, Lecture 9: Independence, Basis, Dimension](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.6](https://mml-book.github.io/book/mml-book.pdf)
