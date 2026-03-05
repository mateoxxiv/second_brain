**Related**: [[linear-independence]], [[linear-combination]], [[basis-and-dimension]], [[determinant]], [[Matrix Operations and Properties]]
**Tags**: #status/seed

## Core Idea

You have a system of equations — multiple unknowns, multiple constraints. How
do you solve it? **Gaussian elimination** is the universal algorithm: simplify
the system step by step until the answer is obvious.

**Analogy**: You're untangling a knot. You don't pull everything at once — you
find one strand, free it, then use that freedom to untangle the next strand,
and the next. Gaussian elimination does the same: solve for one variable, use
that to simplify the rest, repeat.

This algorithm is foundational because it's how we compute **rank**
([[linear-independence]]), solve **linear systems** (regression, least squares),
and understand what makes a matrix **invertible**.

## Details

### The Problem: Solving a System of Equations

You want to find x, y, z that satisfy all equations simultaneously:

```
 x + 2y + 3z = 9
2x + 5y + 2z = 14
 x + 3y +  z = 7
```

Three equations, three unknowns. Instead of guessing, we'll systematically
eliminate variables.

### Step 0: Write It as a Matrix

Instead of writing x, y, z over and over, pack everything into a matrix.
The **augmented matrix** puts coefficients on the left and answers on the right:

```
| 1  2  3 | 9  |       ← from:  x + 2y + 3z = 9
| 2  5  2 | 14 |       ← from: 2x + 5y + 2z = 14
| 1  3  1 | 7  |       ← from:  x + 3y +  z = 7
```

Now we work only with numbers.

### The Three Allowed Moves (Row Operations)

You can do three things without changing the solution:

```
1. SWAP two rows         (reorder equations — doesn't change answers)
2. SCALE a row           (multiply equation by a constant — same equation)
3. ADD a multiple of     (subtract equations to cancel a variable)
   one row to another
```

These are the only moves in the game. Everything in Gaussian elimination is
built from these three.

### Step 1: Eliminate Column 1 (below the first row)

The goal: make everything below the first entry in column 1 become zero.

The element we use to eliminate is called the **pivot** — here it's the 1 in
position (1,1).

**Row 2**: has a 2 in column 1. Subtract 2 × Row 1:

```
Row 2 = Row 2 - 2 × Row 1
[2, 5, 2, 14] - 2×[1, 2, 3, 9]
= [2, 5, 2, 14] - [2, 4, 6, 18]
= [0, 1, -4, -4]
```

**Row 3**: has a 1 in column 1. Subtract 1 × Row 1:

```
Row 3 = Row 3 - 1 × Row 1
[1, 3, 1, 7] - [1, 2, 3, 9]
= [0, 1, -2, -2]
```

Matrix now:

```
| 1  2   3 |  9 |    ← pivot row (untouched)
| 0  1  -4 | -4 |    ← x is gone
| 0  1  -2 | -2 |    ← x is gone
```

Column 1 below the pivot is clean (all zeros). Variable x is eliminated from
rows 2 and 3.

### Step 2: Eliminate Column 2 (below row 2)

New pivot: the 1 in position (2,2).

**Row 3**: has a 1 in column 2. Subtract 1 × Row 2:

```
Row 3 = Row 3 - 1 × Row 2
[0, 1, -2, -2] - [0, 1, -4, -4]
= [0, 0, 2, 2]
```

Matrix now:

```
| 1  2   3 |  9 |
| 0  1  -4 | -4 |
| 0  0   2 |  2 |
```

This is **row echelon form** — a staircase shape where everything below the
diagonal is zero.

### What is Row Echelon Form?

The "staircase" pattern — each row's first non-zero entry (pivot) is to the
right of the row above:

```
| *  *  * |        * = pivot or non-zero
| 0  *  * |        0 = zero
| 0  0  * |

The staircase goes down-right.
```

At this point you can already read the **rank**: count the non-zero rows.

```
3 non-zero rows → rank = 3 → all vectors independent
```

### Step 3: Back Substitution (solve from bottom up)

Now read off the answers, starting from the last row:

**Row 3**: `2z = 2` → `z = 1`

**Row 2**: `y - 4z = -4` → `y - 4(1) = -4` → `y = 0`

**Row 1**: `x + 2y + 3z = 9` → `x + 0 + 3 = 9` → `x = 6`

**Solution: x = 6, y = 0, z = 1**

Verify in the original equations:

```
 6 + 2(0) + 3(1) = 6 + 0 + 3 = 9  ✓
2(6) + 5(0) + 2(1) = 12 + 0 + 2 = 14  ✓
 6 + 3(0) + 1(1) = 6 + 0 + 1 = 7  ✓
```

### What Happens When Vectors Are Dependent?

Let's try with a redundant row:

```
v1 = [1, 2, 3]
v2 = [2, 4, 6]     ← this is 2 × v1!
v3 = [0, 1, 1]

| 1  2  3 |
| 2  4  6 |
| 0  1  1 |
```

Step 1: Row 2 = Row 2 - 2 × Row 1:

```
[2, 4, 6] - 2×[1, 2, 3] = [0, 0, 0]
```

```
| 1  2  3 |
| 0  0  0 |    ← DEAD. Entire row vanished.
| 0  1  1 |
```

Swap rows 2 and 3 (move the zero row down):

```
| 1  2  3 |    ← alive
| 0  1  1 |    ← alive
| 0  0  0 |    ← dead

Rank = 2 (only 2 non-zero rows)
```

The dead row means: "v2 was entirely built from the others. It contributed
nothing." This is exactly what [[linear-independence]] detects.

### The Three Possible Outcomes

```
Outcome 1: UNIQUE SOLUTION (rank = number of unknowns)
| 1  *  * | * |
| 0  1  * | * |      → one specific answer
| 0  0  1 | * |

Outcome 2: INFINITE SOLUTIONS (rank < unknowns, consistent)
| 1  *  * | * |
| 0  1  * | * |      → free variables, infinite answers
| 0  0  0 | 0 |

Outcome 3: NO SOLUTION (inconsistent)
| 1  *  * | * |
| 0  1  * | * |      → 0 = 5 is impossible, system contradicts
| 0  0  0 | 5 |
```

### Why This Matters in ML

Linear regression solves exactly this kind of system. When you fit
$\hat{y} = X\mathbf{w}$, you need to find the weights $\mathbf{w}$. Behind
the scenes, that's a system of equations.

| Outcome | In ML terms |
|---------|------------|
| Unique solution (full rank) | One best set of weights. Model is stable. |
| Infinite solutions (rank-deficient) | Features are redundant. Model is unstable — many weight sets fit equally well. |
| No solution (inconsistent) | Data contradicts itself. Perfect fit is impossible. Use least squares to find the closest approximation → [[projection-onto-subspaces]]. |

The third outcome is actually the most common — real data is noisy, so there's
no perfect solution. That's where projection (least squares) comes in: find the
**closest** answer instead of the exact one.

## Code Example

```python
import numpy as np

# The system:
# x + 2y + 3z = 9
# 2x + 5y + 2z = 14
# x + 3y + z = 7

A = np.array([
    [1, 2, 3],
    [2, 5, 2],
    [1, 3, 1]
], dtype=float)

b = np.array([9, 14, 7], dtype=float)

# Solve using NumPy (Gaussian elimination inside)
x = np.linalg.solve(A, b)
print(x)  # [6. 0. 1.]

# Verify: A @ x should equal b
print(A @ x)  # [9. 14. 7.]

# Check rank
print(np.linalg.matrix_rank(A))  # 3 — full rank, unique solution

# --- From scratch: row echelon form ---
def row_echelon(matrix):
    """Reduce to row echelon form. Returns (reduced matrix, rank)."""
    M = matrix.astype(float).copy()
    rows, cols = M.shape
    pivot_row = 0

    for col in range(cols):
        # Find non-zero entry in this column at or below pivot_row
        found = False
        for row in range(pivot_row, rows):
            if abs(M[row, col]) > 1e-10:
                # Swap to pivot position
                M[[pivot_row, row]] = M[[row, pivot_row]]
                found = True
                break

        if not found:
            continue  # no pivot in this column, skip

        # Eliminate below
        for row in range(pivot_row + 1, rows):
            if abs(M[row, col]) > 1e-10:
                factor = M[row, col] / M[pivot_row, col]
                M[row] -= factor * M[pivot_row]

        pivot_row += 1

    rank = sum(any(abs(M[r, :]) > 1e-10) for r in range(rows))
    return M, rank

# Test with dependent vectors
dep = np.array([
    [1, 2, 3],
    [2, 4, 6],  # 2 × row 1
    [0, 1, 1]
])
reduced, rank = row_echelon(dep)
print(f"Rank: {rank}")  # 2
print(reduced)
# [[1. 2. 3.]
#  [0. 1. 1.]
#  [0. 0. 0.]]  ← dead row
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Gaussian elimination reveals **rank** — the core test for [[linear-independence]]
- Rank determines [[basis-and-dimension]] — rank = dimension of the column space
- The [[determinant]] can be computed via Gaussian elimination (product of pivots)
- When no exact solution exists, we use [[projection-onto-subspaces]] (least squares) to find the closest one
- [[Linear Regression]] uses this algorithm (or variations of it) to solve for weights
- [[Matrix Operations and Properties]] — invertibility requires full rank (unique solution exists)

## Sources

- [3Blue1Brown — Inverse matrices, column space and null space](https://www.youtube.com/watch?v=uQhTuRlWMxw)
- [MIT 18.06 — Strang, Lecture 2: Elimination](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.3](https://mml-book.github.io/book/mml-book.pdf)
- [Khan Academy — Row echelon form](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/matrices-elimination/v/matrices-reduced-row-echelon-form-1)
