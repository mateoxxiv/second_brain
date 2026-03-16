**Related**: [[matrix-operations]], [[vectors-and-vector-spaces]], [[basis-and-dimension]], [[linear-independence]], [[determinant]], [[eigenvalues-and-eigenvectors]], [[gram-schmidt]]
**Tags**: #status/growing

## Core Idea

A linear transformation is a **function between vector spaces** where the order
of operations doesn't matter — you can add/scale before or after transforming
and get the same result. The key insight: **every matrix is a linear
transformation, and every linear transformation is a matrix.** They're the
same thing.

Two rules define linearity:

```
Rule 1: T(u + v) = T(u) + T(v)     ← transform the sum = sum of transforms
Rule 2: T(c * v) = c * T(v)         ← transform the scaled = scale the transform
```

## Details

### Linear vs Not Linear

**Linear — T(v) = 2*v (doubling):**

```
T([1,3] + [2,1]) = T([3,4]) = [6,8]
T([1,3]) + T([2,1]) = [2,6] + [4,2] = [6,8]  ✓ same!
```

**NOT linear — f(v) = v + [1,0] (shift by 1):**

```
f([0,0] + [0,0]) = f([0,0]) = [1,0]
f([0,0]) + f([0,0]) = [1,0] + [1,0] = [2,0]  ✗ NOT same!
```

Shifting breaks linearity. This is why neural networks need a **separate bias
term** — the matrix handles the linear part, the bias handles the shift.

**NOT linear — f(v) = v^2 (squaring):**

Squaring, absolute value, and any "curved" function breaks linearity. This is
why **activation functions** (ReLU, sigmoid) make neural networks powerful —
they add the nonlinearity that matrices alone can't provide.

### Neural Network Connection

```
layer(x) = ReLU(W @ x + b)
                ↑         ↑
           linear part   nonlinear part
           (matrix)      (activation)
```

Without the nonlinear part, stacking 100 layers would collapse into ONE matrix.
The nonlinearity breaks this, letting the network learn complex patterns.

### Every Matrix = Linear Transformation (and vice versa)

From [[matrix-operations]], matrix-vector multiplication is a [[linear-combination]]
of columns — it automatically satisfies both rules.

The reverse: if T is linear, build its matrix by applying T to each standard
basis vector:

```
T rotates 90 degrees counterclockwise:

T([1,0]) = [0,1]     ← "right" goes to "up"
T([0,1]) = [-1,0]    ← "up" goes to "left"

Matrix = [[0, -1],
          [1,  0]]    ← columns are T(e1) and T(e2)
```

### Kernel — What the Transformation Kills

The **kernel** is all vectors that the matrix sends to zero:

```
kernel = {v : A @ v = 0}
```

Feed every possible vector into the matrix. Some get sent to [0,0]. Those
are the kernel — the directions the matrix is **blind** to.

```
A = [[1, 2],
     [2, 4]]

A @ [-2, 1] = [-2+2, -4+4] = [0, 0]    ← killed!
```

In ML: if your feature matrix has a non-trivial kernel, some combinations of
features are invisible to the model. Redundant features live in the kernel.

### Image — What the Transformation Can Reach

The **image** is all possible outputs — every vector the matrix can produce:

```
image = {A @ v : for all vectors v}
```

Feed every possible vector in. Collect all outputs. That collection is the image.

```
A = [[1, 0],
     [0, 0]]

A @ [1, 0] = [1, 0]
A @ [0, 1] = [0, 0]
A @ [3, 7] = [3, 0]
A @ [-2, 100] = [-2, 0]
```

Every output has second component = 0. The image is the x-axis — the matrix
can never produce [1, 3] or [0, 1]. It crushes everything onto the x-axis.

### Rank-Nullity Theorem

```
number of columns = kernel dimension + image dimension
        n         =     nullity       +      rank
```

What goes in = what gets killed + what gets through.

- **Rank** = number of independent columns = dimension of image
- **Nullity** = dimension of kernel

Example: A = [[1,2],[2,4]] is 2x2, rank 1 (columns are dependent):

```
n = 2,  rank = 1,  nullity = 2 - 1 = 1
```

One direction survives, one gets killed.

### Connection to Determinant

| det(A) | Kernel | Image | What happens |
|--------|--------|-------|-------------|
| != 0 | only {0} | full space | Nothing killed, everything reachable |
| = 0 | non-trivial | smaller than full | Some directions destroyed |

### Types of Linear Transformations

| Transformation | Matrix example | What it does |
|---------------|---------------|-------------|
| Rotation | [[cos,-sin],[sin,cos]] | Turns vectors, preserves lengths |
| Scaling | [[2,0],[0,3]] | Stretches axes independently |
| Projection | [[1,0],[0,0]] | Collapses onto a subspace |
| Reflection | [[1,0],[0,-1]] | Flips across an axis |
| Shear | [[1,1],[0,1]] | Slides one axis along another |

## Code Example

```python
import numpy as np

A = np.array([[1, 2],
              [2, 4]])

# Apply transformation
v = np.array([3, 1])
print(A @ v)                    # [5, 10] = 5*[1,2]

# Kernel: which vectors go to zero?
print(A @ np.array([-2, 1]))    # [0, 0] — in the kernel!

# Rank and nullity
rank = np.linalg.matrix_rank(A)
nullity = A.shape[1] - rank
print(f"rank={rank}, nullity={nullity}")  # rank=1, nullity=1

# Verify linearity: T(u+v) = T(u) + T(v)
u, w = np.array([1, 2]), np.array([3, -1])
print(np.allclose(A @ (u + w), A @ u + A @ w))   # True

# Shift is NOT linear
def shift(x): return x + np.array([1, 0])
print(np.allclose(shift(u + w), shift(u) + shift(w)))  # False
```

## Connections

- [[matrix-operations]] — every matrix IS a linear transformation
- [[determinant]] — det = 0 means kernel is non-trivial
- [[linear-independence]] — independent columns = trivial kernel = full rank
- [[basis-and-dimension]] — rank = dimension of image, nullity = dimension of kernel
- [[eigenvalues-and-eigenvectors]] — eigenvectors are directions T only scales
- [[singular-value-decomposition]] — reveals the geometry of any linear transformation
- Forward link: neural networks — linear layer = matrix @ input + bias

## Sources

- [3Blue1Brown — Linear Transformations and Matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- [3Blue1Brown — Nonsquare Matrices as Transformations](https://www.youtube.com/watch?v=v8VSDg_WQlA)
- [MIT 18.06 — Strang, Lecture 6: Column Space and Null Space](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.7](https://mml-book.github.io/book/mml-book.pdf)
