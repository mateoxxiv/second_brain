---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[vectors-and-vector-spaces]]"
  - "[[vector-norms]]"
  - "[[cosine-similarity]]"
  - "[[projection]]"
  - "[[linear-combination]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=LyGKycYT2v0"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Three operations form all of linear algebra: addition (combine two effects), scalar multiplication (amplify or shrink), dot product (measure alignment). Every ML algorithm is built from these three.

---

## Intuition

**Addition** — you're in a boat. Current pushes East at 3 km/h, you row North at 4 km/h. Your actual path is the diagonal sum of both forces. Vector addition works the same way: combine component-by-component.

**Scalar multiplication** — doubling a recipe multiplies every ingredient by 2. Same proportions, different amount. Negative scalar flips direction; zero collapses the vector to a point.

**Dot product** — a solar panel facing directly at the sun generates maximum power. At 90° it generates zero. The dot product measures this alignment: how much two vectors "agree" on direction.

## Mechanics

$$\mathbf{u} + \mathbf{v} = \begin{bmatrix}u_1+v_1\\ \vdots\\ u_n+v_n\end{bmatrix} \qquad c\mathbf{v} = \begin{bmatrix}cv_1\\ \vdots\\ cv_n\end{bmatrix} \qquad \mathbf{u}\cdot\mathbf{v} = \sum_i u_i v_i = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

| Dot product value | Angle | Meaning |
|---|---|---|
| $> 0$ | $< 90°$ | Vectors agree |
| $= 0$ | $90°$ | Orthogonal — zero shared information |
| $< 0$ | $> 90°$ | Vectors disagree |
| $\mathbf{u}\cdot\mathbf{u}$ | — | $= \|\mathbf{u}\|_2^2$ (squared length) |

The geometric identity $\mathbf{u}\cdot\mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ follows from the law of cosines applied to the triangle formed by the two vectors.

```python
import numpy as np
u, v = np.array([2.0, 3.0]), np.array([-1.0, 4.0])

print(u + v)          # [1. 7.]
print(-2 * u)         # [-4. -6.]
print(u @ v)          # 10.0 — dot product
print(np.dot(u, u))   # 13.0 — squared L2 norm

# Orthogonality check
print(np.dot([1,0], [0,1]))  # 0.0 — orthogonal
```


## In ML

**Gradient descent** — $\mathbf{w} \leftarrow \mathbf{w} - \alpha\nabla L$ uses scalar multiplication (the learning rate $\alpha$ scales the gradient) and vector subtraction.

**Neural network neurons** — each neuron computes $z = \mathbf{w}\cdot\mathbf{x} + b$, a dot product plus bias. The entire forward pass is organized dot products.

**Residual connections** — $\mathbf{y} = f(\mathbf{x}) + \mathbf{x}$ uses vector addition to let the network learn modifications rather than full transformations. Gradient accumulation across batches is also vector addition.

## Exercises

**Basic** — Compute $\mathbf{u}\cdot\mathbf{v}$ for $\mathbf{u}=[1,2,3]$, $\mathbf{v}=[4,-1,2]$. Are they orthogonal?

**Intermediate** — Derive the geometric formula $\mathbf{u}\cdot\mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ from the law of cosines. Start with the triangle formed by $\mathbf{u}$, $\mathbf{v}$, and $\mathbf{u}-\mathbf{v}$.

**Advanced** — Why can't the dot product alone tell you if two vectors are similar in "meaning"? What additional operation do you need, and why? (Hint: think about a sentence vs the same sentence in uppercase.)
