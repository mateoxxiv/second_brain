**Related**: [[vectors-and-vector-spaces]], [[basis-and-dimension]], [[Matrix Operations and Properties]]
**Tags**: #status/seed

## Core Idea

Vectors are linearly independent if none of them can be written as a combination of the others. In ML terms: independent vectors carry non-redundant information. If your features are linearly dependent, you're wasting parameters and risking numerical instability (e.g., singular matrices in linear regression).

## Details

### Formal Definition

Vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$ are **linearly independent** if the only solution to:

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$$

is $c_1 = c_2 = \cdots = c_k = 0$ (the trivial solution).

If any non-trivial solution exists (some $c_i \neq 0$), the vectors are **linearly dependent** — meaning at least one vector is redundant.

### Intuition

- **2 vectors in $\mathbb{R}^2$**: Independent if they don't lie on the same line
- **3 vectors in $\mathbb{R}^3$**: Independent if they don't lie on the same plane
- **$n$ vectors in $\mathbb{R}^n$**: Independent if no vector is a combination of the others
- **$k > n$ vectors in $\mathbb{R}^n$**: Always dependent (pigeonhole — can't have more independent vectors than dimensions)

### Worked Example: Checking Independence

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad \mathbf{v}_3 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$$

Set up $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$:

$$\begin{bmatrix} c_1 + c_3 \\ c_2 + c_3 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

From rows 1 and 2: $c_1 = -c_3$ and $c_2 = -c_3$. Choose $c_3 = 1 \implies c_1 = -1, c_2 = -1$.

Non-trivial solution exists: $-\mathbf{v}_1 - \mathbf{v}_2 + \mathbf{v}_3 = \mathbf{0}$, or equivalently $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$.

These vectors are **dependent**. $\mathbf{v}_3$ is redundant.

### How to Test Independence: Rank

Stack the vectors as rows of a matrix and compute the **rank** (number of linearly independent rows):

$$A = \begin{bmatrix} \mathbf{v}_1^T \\ \mathbf{v}_2^T \\ \vdots \\ \mathbf{v}_k^T \end{bmatrix}$$

- If $\text{rank}(A) = k$: all $k$ vectors are independent
- If $\text{rank}(A) < k$: some vectors are redundant

### Why It Matters in ML

| Situation | Problem | Consequence |
|-----------|---------|-------------|
| Dependent features in regression | $X^TX$ is singular, can't invert | No unique solution for weights |
| Multicollinearity | Features are nearly dependent | Unstable weights, high variance |
| Neural network weights | Redundant neurons compute the same thing | Wasted parameters |
| Embedding dimensions | Independent dimensions capture distinct information | Rich, non-redundant representations |

### Connection to Rank

The **rank** of a matrix equals:
- The number of linearly independent rows
- The number of linearly independent columns
- The dimension of the column space

A matrix is **full rank** if $\text{rank}(A) = \min(m, n)$. Rank-deficient matrices signal redundancy in your data or model.

## Code Example

```python
import numpy as np

# Independent vectors
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])
rank = np.linalg.matrix_rank(np.array([v1, v2, v3]))  # 3 — independent

# Dependent: v3 = v1 + v2
v3_dep = np.array([1, 1, 0])
rank_dep = np.linalg.matrix_rank(np.array([v1, v2, v3_dep]))  # 2 — dependent
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Independence determines [[basis-and-dimension]] — a basis is a maximal independent set
- Rank connects to [[Matrix Operations and Properties]] — rank-deficient matrices are non-invertible
- Multicollinearity (near-dependence) motivates [[Regularization (L1/L2)]] and [[PCA]]
- In [[vectors-and-vector-spaces]], independence determines how many dimensions a subspace has

## Sources

- [3Blue1Brown — Linear combinations, span, and basis](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- [MIT 18.06 — Strang, Lecture 9: Independence, Basis, Dimension](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.6](https://mml-book.github.io/book/mml-book.pdf)
