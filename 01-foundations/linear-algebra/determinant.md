**Related**: [[linear-independence]], [[gaussian-elimination]], [[basis-and-dimension]], [[Matrix Operations and Properties]]
**Tags**: #status/seed

## Core Idea

The determinant answers: **"does this set of vectors collapse space, or does it
preserve it?"**

Take a set of vectors and imagine them as the edges of a shape — two vectors
form a parallelogram, three vectors form a 3D box. The determinant measures
the **area** (2D) or **volume** (3D) of that shape.

- **det ≠ 0**: the shape has actual area/volume. The vectors span full space.
  They're [[linear-independence|independent]].
- **det = 0**: the shape is flat — a parallelogram collapsed to a line, or a
  box collapsed to a flat sheet. Something is redundant.

This one number tells you whether a matrix is invertible, whether a system has
a unique solution, and whether your features carry redundant information.

## Details

### Geometric Intuition: Area and Volume

**2D**: Two vectors form a parallelogram. The determinant is its signed area.

```
v2 = [0, 2]
  |     ________
  |    /       /
  |   /       /     Area = det = ?
  |  /       /
  | /       /
  |/-------/
  origin     v1 = [3, 0]
```

With v1 = [3, 0] and v2 = [0, 2]:

```
det = 3 × 2 - 0 × 0 = 6
```

The parallelogram has area 6. The vectors span a 2D region — they're
independent.

Now try v1 = [1, 2] and v2 = [2, 4]:

```
v2 = [2, 4]         Both on the same line!
   /                The "parallelogram" is flat.
  /                 Area = 0.
 /
/
v1 = [1, 2]

det = 1×4 - 2×2 = 4 - 4 = 0
```

Zero area = flat = dependent. The vectors collapsed from 2D to a line.

**3D**: Three vectors form a parallelepiped (a 3D box). The determinant is its
signed volume. If volume = 0, the box is flat — the vectors are all on a plane.

### The 2x2 Determinant

For a 2×2 matrix:

```
| a  b |
| c  d |

det = a*d - b*c
```

That's it. Multiply the diagonals, subtract:

```
| a  b |
|  \   |       Main diagonal: a*d
|   \  |
| c  d |

| a  b |
|   /  |       Anti-diagonal: b*c
|  /   |
| c  d |

det = main - anti = a*d - b*c
```

**Examples**:

```
| 1  0 |
| 0  1 |  det = 1×1 - 0×0 = 1    (identity — no change)

| 3  0 |
| 0  2 |  det = 3×2 - 0×0 = 6    (stretches space by 6×)

| 1  2 |
| 2  4 |  det = 1×4 - 2×2 = 0    (collapses — dependent!)

| 0  1 |
| 1  0 |  det = 0×0 - 1×1 = -1   (flips orientation — reflection)
```

### What Does the Sign Mean?

- **Positive det**: the transformation preserves orientation (no flipping)
- **Negative det**: the transformation flips orientation (mirror image)
- **det = 0**: the transformation squishes to a lower dimension

Think of it like a glove. Positive det = right hand stays right hand.
Negative det = right hand becomes left hand (reflected).

For [[linear-independence]], we only care about zero vs non-zero. The sign
doesn't matter for that test.

### The 3x3 Determinant: Cofactor Expansion

For larger matrices, we break it down using **cofactor expansion** along the
first row:

```
| a  b  c |
| d  e  f |
| g  h  i |

det = a × det|e f| - b × det|d f| + c × det|d e|
             |h i|          |g i|          |g h|

    = a(ei - fh) - b(di - fg) + c(dh - eg)
```

The pattern: walk along the first row. For each element, cross out its row and
column, take the determinant of what's left (the "minor"), and alternate signs
(+, -, +).

### Worked Example: 3x3 Determinant

```
| 1  2  3 |
| 0  1  4 |
| 0  0  5 |
```

Expand along row 1:

```
det = 1 × det|1  4| - 2 × det|0  4| + 3 × det|0  1|
             |0  5|          |0  5|          |0  0|

    = 1 × (1×5 - 4×0) - 2 × (0×5 - 4×0) + 3 × (0×0 - 1×0)
    = 1 × 5 - 2 × 0 + 3 × 0
    = 5
```

**Shortcut for triangular matrices** (zeros below the diagonal): the
determinant is just the product of the diagonal entries: 1 × 1 × 5 = 5.

This connects directly to [[gaussian-elimination]] — if you reduce a matrix
to row echelon form (triangular), the determinant is the product of the pivots.

### Another Worked Example: Detecting Dependence

Are these vectors independent?

```
v1 = [1, 3]
v2 = [2, 6]
```

```
det = | 1  2 |  = 1×6 - 2×3 = 6 - 6 = 0
      | 3  6 |
```

det = 0 → **dependent**. And indeed, v2 = 2 × v1.

Now v2 = [2, 5] instead:

```
det = | 1  2 |  = 1×5 - 2×3 = 5 - 6 = -1
      | 3  5 |
```

det ≠ 0 → **independent**. The negative sign means the transformation
flips orientation, but that doesn't affect independence.

### Properties of the Determinant

| Property | Formula | Why it matters |
|----------|---------|---------------|
| Identity | det(I) = 1 | The identity doesn't change space |
| Scaling a row | Multiplies det by that scalar | Doubling a vector doubles the area |
| Swapping rows | Flips the sign | Reordering flips orientation |
| Row of zeros | det = 0 | One vector is the zero vector — no contribution |
| Two equal rows | det = 0 | Duplicate = dependent |
| Product rule | det(AB) = det(A) × det(B) | Chaining transformations multiplies their scaling |
| Transpose | det(A) = det(A^T) | Rows and columns carry the same independence info |

### The Big Connection: det = 0 Means...

Everything below is equivalent — they all mean the same thing:

```
det(A) = 0
  ↕
A is NOT invertible (singular)
  ↕
Columns are linearly DEPENDENT
  ↕
Rank < n (rank-deficient)
  ↕
System Ax = b has NO unique solution
  ↕
The transformation squishes space to a lower dimension
```

If any one is true, they're ALL true. This web of equivalences is one of the
most important ideas in linear algebra.

### Computing Determinant via Gaussian Elimination

For large matrices, cofactor expansion is slow. A faster approach:

1. Reduce to row echelon form using [[gaussian-elimination]]
2. The determinant = product of the pivot entries
3. Multiply by $(-1)^s$ where s = number of row swaps

```
Example:
| 2  1 |   Swap rows →  | 1  3 |   (1 swap)
| 1  3 |                | 2  1 |

Row 2 = Row 2 - 2×Row 1:
| 1   3 |
| 0  -5 |

Product of pivots: 1 × (-5) = -5
Adjust for 1 swap: (-1)^1 × (-5) = 5

Verify: det = 2×3 - 1×1 = 5 ✓
```

### Why This Matters in ML

| Context | Role of determinant |
|---------|-------------------|
| **Linear regression** | Need to invert $X^TX$. If det($X^TX$) = 0, features are dependent → no unique solution |
| **Gaussian distributions** | The normalization term includes $\frac{1}{\sqrt{det(\Sigma)}}$ where $\Sigma$ is the covariance matrix |
| **PCA** | Eigenvalues (related to determinant) tell you how much variance each component captures |
| **Change of basis** | det tells you how the transformation scales area/volume — needed for change-of-variable in integrals |

## Code Example

```python
import numpy as np

# --- 2x2 determinant by hand ---
def det_2x2(matrix):
    """det = a*d - b*c"""
    a, b = matrix[0]
    c, d = matrix[1]
    return a * d - b * c

A = np.array([[1, 2], [3, 4]])
print(det_2x2(A))          # -2
print(np.linalg.det(A))    # -2.0 (verify)

# --- 3x3 determinant by hand (cofactor expansion) ---
def det_3x3(matrix):
    """Expand along first row."""
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

B = np.array([[1, 2, 3], [0, 1, 4], [0, 0, 5]])
print(det_3x3(B))          # 5
print(np.linalg.det(B))    # 5.0 (verify)

# --- Independence test ---
independent = np.array([[1, 0], [0, 1]])
dependent = np.array([[1, 2], [2, 4]])

print(f"det = {np.linalg.det(independent):.0f} → independent")  # 1
print(f"det = {np.linalg.det(dependent):.0f} → dependent")      # 0

# --- The equivalence: det=0 ↔ rank-deficient ↔ singular ---
C = np.array([[1, 2, 3], [2, 4, 6], [0, 1, 1]])
print(f"det = {np.linalg.det(C):.0f}")             # 0
print(f"rank = {np.linalg.matrix_rank(C)}")         # 2 (< 3)
# np.linalg.inv(C) would raise LinAlgError: Singular matrix
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- det = 0 is the quick test for [[linear-independence]] (square matrices only)
- Can be computed efficiently via [[gaussian-elimination]] (product of pivots)
- [[basis-and-dimension]] — determinant confirms whether a set of vectors forms a basis
- det appears in the normalization of Gaussian distributions → [[Probability Distributions]]
- Invertibility (det ≠ 0) is required for [[projection-onto-subspaces]] to have a unique solution
- [[Matrix Operations and Properties]] — determinant is one of the key matrix properties alongside rank, trace, eigenvalues

## Sources

- [3Blue1Brown — The determinant](https://www.youtube.com/watch?v=Ip3X9LOh2dk)
- [MIT 18.06 — Strang, Lecture 18: Properties of Determinants](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 4.1](https://mml-book.github.io/book/mml-book.pdf)
- [Khan Academy — Determinant of a 3x3 matrix](https://www.khanacademy.org/math/linear-algebra/matrix-transformations/determinant-depth/v/linear-algebra-determinant-when-row-multiplied-by-scalar)
