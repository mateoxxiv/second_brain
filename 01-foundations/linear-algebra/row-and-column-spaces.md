---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[subspaces]]"
  - "[[basis-and-dimension]]"
  - "[[linear-independence]]"
  - "[[gaussian-elimination]]"
  - "[[matrix-inverse]]"
  - "[[linear-combination]]"
  - "[[projection-onto-subspaces]]"
  - "[[general-vector-spaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.6"
---

> **TL;DR** — The row space and column space of a matrix are [[subspaces]] that describe what the transformation produces; they always have the same dimension — the **rank** — which controls whether $Ax = \mathbf{b}$ has solutions.

---

## Intuition

A matrix $A$ is a transformation machine. Two natural questions:

- *What outputs are reachable?* → **column space**: every $A\mathbf{x}$ you can ever get
- *Which input directions survive (aren't killed)?* → **row space**: the "active" input subspace

Think of a projector. The column space is the set of images it can cast on the wall. If two input dimensions collapse into one (rank < n), some structure is permanently lost. The rank measures how much the machine preserves.

The surprising fact: even though the row space lives in $\mathbb{R}^n$ and the column space in $\mathbb{R}^m$, they always have the **same dimension**.

## Mechanics

**Definition (Anton §4.6):** For an $m \times n$ matrix $A$:

| Space | Spanned by | Lives in |
|---|---|---|
| Row space of $A$ | row vectors $\mathbf{r}_1, \ldots, \mathbf{r}_m$ | $\mathbb{R}^n$ |
| Column space of $A$ | column vectors $\mathbf{c}_1, \ldots, \mathbf{c}_n$ | $\mathbb{R}^m$ |

Both are [[subspaces]] (span of any set is always a subspace).

**Theorem 10:** Elementary row operations do not change the row space.

*Why:* each operation replaces a row with a linear combination of existing rows — new rows are already in the span, so the span is unchanged.

**Theorem 11:** The nonzero row vectors of a row echelon form of $A$ form a basis for the row space of $A$.

**Procedure — basis for row space:**
1. Row-reduce $A$ to echelon form $E$
2. Take all nonzero rows of $E$

**Procedure — basis for column space:**

The column space of $A$ equals the row space of $A^T$. So: row-reduce $A^T$, take nonzero rows.

**Example (Anton §4.6, Ex. 38):** basis for $\text{span}\{(1,-2,0,0,3),\,(2,-5,-3,-2,6),\,(0,5,15,10,0),\,(2,6,18,8,6)\}$.

Stack as rows, row-reduce:
$$\begin{bmatrix}1&-2&0&0&3\\2&-5&-3&-2&6\\0&5&15&10&0\\2&6&18&8&6\end{bmatrix} \longrightarrow \begin{bmatrix}1&-2&0&0&3\\0&1&3&2&0\\0&0&1&1&0\\0&0&0&0&0\end{bmatrix}$$

Basis: $\mathbf{w}_1=(1,-2,0,0,3)$, $\mathbf{w}_2=(0,1,3,2,0)$, $\mathbf{w}_3=(0,0,1,1,0)$.

> Note: echelon-form rows span the same space but are **not** necessarily from the original vector set. To find a basis made of original vectors, use the dependency equation method (Anton §4.6, Ex. 40).

**Theorem 12:** For any matrix $A$, $\dim(\text{row space of }A) = \dim(\text{col space of }A)$.

**Definition — Rank:** $\text{rank}(A) = \dim(\text{row space}) = \dim(\text{col space})$.

**Theorem 14:** $A\mathbf{x} = \mathbf{b}$ is consistent $\iff$ $\mathbf{b} \in \text{col}(A)$.

*Why:* $A\mathbf{x} = x_1\mathbf{c}_1 + \cdots + x_n\mathbf{c}_n$ is a linear combination of columns. A solution exists iff $\mathbf{b}$ can be written as such a combination.

```python
import numpy as np

A = np.array([[1,-2,0,0,3],[2,-5,-3,-2,6],[0,5,15,10,0],[2,6,18,8,6]], float)

print(np.linalg.matrix_rank(A))   # 3 — matches Example 38

def in_column_space(A: np.ndarray, b: np.ndarray) -> bool:
    """Theorem 14: b ∈ col(A) iff rank([A|b]) == rank(A)."""
    return np.linalg.matrix_rank(A) == np.linalg.matrix_rank(np.column_stack([A, b]))
```


## In ML

**[[projection-onto-subspaces|Least squares as projection]]** — When $A\mathbf{x} = \mathbf{b}$ is inconsistent (overdetermined), the least-squares solution $\hat{\mathbf{x}}$ projects $\mathbf{b}$ onto $\text{col}(A)$. The residual $\mathbf{b} - A\hat{\mathbf{x}}$ is orthogonal to the entire column space. Theorem 14 tells you when the residual is zero (perfect fit).

**Rank as model capacity** — A weight matrix of rank $r < n$ can only express $r$-dimensional output. LoRA fine-tuning of LLMs exploits this: it decomposes weight updates as $\Delta W = BA$ where $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times k}$, with $r \ll \min(d,k)$. The update is constrained to a low-dimensional column space, drastically reducing trainable parameters.

**Consistent labels and linear models** — Theorem 14 reframes linear regression: the label vector $\mathbf{y}$ is almost never in $\text{col}(X)$ for real data. We minimize $\|X\boldsymbol{\beta} - \mathbf{y}\|^2$ precisely because an exact solution doesn't exist.

## Exercises

**Basic** — For $A = \begin{bmatrix}2&1&0\\3&-1&4\end{bmatrix}$, write down the row vectors and column vectors. What are the dimensions of the row space and column space? (Don't compute — reason from shape and independence.)

**Intermediate** — Find a basis for the row space and column space of $A = \begin{bmatrix}1&0&1&1\\3&2&5&1\\0&4&4&-4\end{bmatrix}$. Verify that both bases have the same size. Is $\mathbf{b} = (1,3,0)$ in the column space?

**Advanced** — Prove Theorem 12 from first principles: why must $\dim(\text{row space}) = \dim(\text{col space})$ for any matrix? (Hint: both equal the number of pivot positions in any echelon form of $A$. Argue why the pivot count is the same whether you row-reduce $A$ or $A^T$.)
