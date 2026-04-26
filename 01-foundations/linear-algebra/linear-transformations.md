---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[matrix-operations]]"
  - "[[vectors-and-vector-spaces]]"
  - "[[basis-and-dimension]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[gram-schmidt]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=kYB8IZa5AuE"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — A linear transformation is a function between vector spaces where "transform the sum = sum of transforms." Every matrix is a linear transformation, and every linear transformation is a matrix — they're the same thing.

---

## Intuition

Two rules define linearity:
```
T(u + v) = T(u) + T(v)    ← transform the sum = sum of transforms
T(c·v) = c·T(v)            ← transform the scaled = scale the transform
```

**Linear:** $T(\mathbf{v}) = 2\mathbf{v}$ (doubling everything). $T([1,3]+[2,1]) = T([3,4]) = [6,8]$. Also $T([1,3]) + T([2,1]) = [2,6]+[4,2] = [6,8]$. Same result.

**NOT linear:** $f(\mathbf{v}) = \mathbf{v} + [1,0]$ (shift). Adding a constant breaks linearity because the zero vector no longer maps to zero: $f(\mathbf{0}) = [1,0] \neq \mathbf{0}$.

## Mechanics

A linear transformation is completely determined by what it does to the **basis vectors**. To find the matrix, apply $T$ to each basis vector and use the results as columns.

$$T(\mathbf{e}_1) = \text{column 1}, \quad T(\mathbf{e}_2) = \text{column 2}$$

**Common 2D transformations:**

| Matrix | Effect |
|---|---|
| $\begin{bmatrix}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{bmatrix}$ | Rotation by $\theta$ |
| $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ | Reflection over x-axis |
| $\begin{bmatrix}k&0\\0&k\end{bmatrix}$ | Uniform scaling by $k$ |
| $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ | Projection onto x-axis |

Composition of two transformations = matrix multiplication: $(T_2 \circ T_1)(\mathbf{x}) = A_2 A_1 \mathbf{x}$.

```python
import numpy as np

# Rotation by 90°
T = np.array([[0,-1],[1,0]])
v = np.array([1,0])
print(T @ v)           # [0, 1] — right becomes up

# Check linearity
u, v = np.array([1,2]), np.array([3,1])
print(T @ (u+v))       # same as T@u + T@v
print(T @ u + T @ v)   # ✓
```

> Runnable: [[code/foundations/matrix_operations.py]]

## In ML

**Neural network layers** — each layer is a linear transformation ($\mathbf{z} = W\mathbf{x} + \mathbf{b}$) followed by a nonlinearity. Without the nonlinearity, all layers compose into a single matrix — the network collapses to linear regression.

**Activation functions** are precisely what breaks linearity and lets the network learn curved decision boundaries.

**[[eigenvalues-and-eigenvectors|Eigenvectors]]** — special vectors where the linear transformation only stretches or shrinks (no rotation). They reveal the "natural axes" of a transformation.

## Exercises

**Basic** — Is $T(\mathbf{v}) = \|\mathbf{v}\|\cdot\mathbf{v}$ linear? Check both linearity conditions. What fails?

**Intermediate** — Find the matrix that rotates 2D vectors by 45° counterclockwise. Apply it to $[1, 0]$ and $[0, 1]$. Verify both rules of linearity.

**Advanced** — A neural network without activation functions can be collapsed to a single matrix multiplication, no matter how many layers. Prove this using the composition property of linear transformations.
