**Related**: [[vectors-and-vector-spaces]], [[basis-and-dimension]], [[Matrix Operations and Properties]]
**Tags**: #status/seed

## Core Idea

Linear independence asks: "does every vector in this set bring something new
to the table?" If one vector can be built from the others, it's redundant —
it carries no new information. In ML, redundant features waste parameters,
cause numerical instability, and make your model harder to interpret.

## Details

### Intuition: The Team Analogy

Think of a team of workers. Each person has a skill:
- Person A: can build walls
- Person B: can do plumbing
- Person C: can build walls AND do plumbing (but nothing new)

Person C is **linearly dependent** on A and B. Hiring C adds no new capability.
You're paying for redundancy.

Now replace "workers" with "vectors" and "skills" with "directions in space":
- If a vector points in a direction you can already reach by combining others,
  it's dependent — it adds nothing.
- If a vector points in a genuinely new direction, it's independent — it
  expands what you can reach.

### Formal Definition

Vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k$ are **linearly independent** if the only way to combine them and get zero is the boring way (all coefficients = 0):

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \implies c_1 = c_2 = \cdots = c_k = 0$$

If you CAN find non-zero coefficients that produce zero, at least one vector is a
combination of the others — they're **dependent**.

### Geometric Intuition

- **2 vectors in 2D**: Independent if they don't lie on the same line. Two arrows
  pointing along the same line (even at different scales) are dependent — one is
  just a stretched version of the other.
- **3 vectors in 3D**: Independent if they don't all lie on the same plane. If
  all three are on a plane, you can't reach "above" or "below" it.
- **Key rule**: You can never have more than $n$ independent vectors in
  $\mathbb{R}^n$. In $\mathbb{R}^3$, a 4th vector is ALWAYS dependent — there
  are only 3 directions to go.

### Worked Example: Testing Independence

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad \mathbf{v}_3 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$$

**Question**: Can we build $\mathbf{v}_3$ from $\mathbf{v}_1$ and $\mathbf{v}_2$?

Set up $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$:

$$\begin{bmatrix} c_1 + c_3 \\ c_2 + c_3 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

Row 1: $c_1 = -c_3$
Row 2: $c_2 = -c_3$

Pick $c_3 = 1$: then $c_1 = -1$, $c_2 = -1$. Non-zero solution exists!

This means: $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$. Vector 3 is just the
sum of vectors 1 and 2 — it's redundant. **Dependent.**

Now try with $\mathbf{v}_3 = \begin{bmatrix}0\\0\\1\end{bmatrix}$ instead:

$$c_1 + 0 = 0 \implies c_1 = 0$$
$$c_2 + 0 = 0 \implies c_2 = 0$$
$$c_3 = 0$$

Only the trivial solution. No vector can be built from the others. **Independent.**

### How to Test: Matrix Rank

Solving the system by hand is tedious. The shortcut: stack your vectors as rows
of a matrix and check the **rank**.

$$A = \begin{bmatrix} — \mathbf{v}_1^T — \\ — \mathbf{v}_2^T — \\ \vdots \\ — \mathbf{v}_k^T — \end{bmatrix}$$

**Rank** = the number of genuinely independent rows (after eliminating redundancies).

- $\text{rank}(A) = k$ (equals number of vectors) → all independent
- $\text{rank}(A) < k$ → at least one vector is redundant

Why does this work? Row reduction (Gaussian elimination) systematically
eliminates dependent rows by subtracting combinations. What survives is
the independent core. The count of surviving rows is the rank.

### Connection to Rank

The rank of a matrix tells you several equivalent things:

| Rank equals... | Meaning |
|---------------|---------|
| Number of independent rows | How many non-redundant data points |
| Number of independent columns | How many non-redundant features |
| Dimension of the column space | How many dimensions the data actually spans |

A matrix is **full rank** if $\text{rank}(A) = \min(m, n)$ — no redundancy at all.
**Rank-deficient** means something is redundant.

### Why It Matters in ML

**The core problem**: If features are dependent, your model is trying to solve
an equation that has infinite solutions — like asking "what two numbers add to 10?"
There's no unique answer.

| Situation | What happens | Real consequence |
|-----------|-------------|-----------------|
| Dependent features in regression | $X^TX$ is singular, can't invert | No unique solution, training crashes |
| Multicollinearity (near-dependence) | $X^TX$ is almost singular | Weights swing wildly between runs |
| Redundant neurons | Multiple neurons learn the same thing | Wasted compute, slower training |
| High-quality embeddings | Each dimension captures something unique | Rich, compact representations |

**Example**: A dataset with features "temperature in Celsius" and "temperature
in Fahrenheit" has a perfect linear dependency ($F = 1.8C + 32$). Including
both gives the model infinite ways to split the weight between them. Drop one.

## Code Example

```python
import numpy as np

# Independent: standard basis
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])
rank = np.linalg.matrix_rank(np.array([v1, v2, v3]))  # 3 — independent

# Dependent: v3 = v1 + v2
v3_dep = np.array([1, 1, 0])
rank_dep = np.linalg.matrix_rank(np.array([v1, v2, v3_dep]))  # 2 — dependent
# One vector is redundant: only 2 independent directions
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Independence determines [[basis-and-dimension]] — a basis is a maximal independent set
- Rank connects to [[Matrix Operations and Properties]] — rank-deficient matrices can't be inverted
- Multicollinearity (near-dependence) motivates [[Regularization (L1/L2)]] and [[PCA]]
- In [[vectors-and-vector-spaces]], independence determines how many dimensions a subspace has
- [[projection-onto-subspaces]] requires independent columns for $(A^TA)^{-1}$ to exist

## Sources

- [3Blue1Brown — Linear combinations, span, and basis](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- [MIT 18.06 — Strang, Lecture 9: Independence, Basis, Dimension](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.6](https://mml-book.github.io/book/mml-book.pdf)
