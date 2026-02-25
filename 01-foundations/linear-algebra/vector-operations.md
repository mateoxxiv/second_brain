**Related**: [[vectors-and-vector-spaces]], [[vector-norms]], [[cosine-similarity]]
**Tags**: #status/seed

## Core Idea

Vector operations are the computational building blocks of linear algebra. Addition, scalar multiplication, and the dot product appear in every ML algorithm — from gradient updates to attention mechanisms. Understanding them mechanically (how to compute) and geometrically (what they mean) is essential.

## Details

### Addition

Component-wise. Both vectors must live in the same space.

$$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix}$$

**Geometric meaning**: Place $\mathbf{v}$ at the tip of $\mathbf{u}$ — the result is the diagonal of the parallelogram.

**ML use**: Gradient accumulation — each mini-batch produces a gradient vector, and they're summed. Residual connections in transformers add the input back to the output: $\mathbf{y} = f(\mathbf{x}) + \mathbf{x}$.

### Worked example (Addition)

$$\mathbf{u} = \begin{bmatrix} 3 \\ -1 \\ 4 \end{bmatrix}, \quad \mathbf{v} = \begin{bmatrix} 1 \\ 5 \\ -2 \end{bmatrix}$$

$$\mathbf{u} + \mathbf{v} = \begin{bmatrix} 3+1 \\ -1+5 \\ 4+(-2) \end{bmatrix} = \begin{bmatrix} 4 \\ 4 \\ 2 \end{bmatrix}$$

### Scalar Multiplication

Scale every component by a constant $c \in \mathbb{R}$.

$$c \cdot \mathbf{v} = \begin{bmatrix} cv_1 \\ cv_2 \\ \vdots \\ cv_n \end{bmatrix}$$

**Geometric meaning**: Stretches ($|c|>1$) or shrinks ($|c|<1$) the vector. Negative $c$ reverses direction.

**ML use**: Learning rate scaling — the gradient descent update $\mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla L$ multiplies the gradient by learning rate $\alpha$.

### Linear Combination

The most important operation in all of ML. A **linear combination** of vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$ is:

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$$

Every neural network layer computes a linear combination of its inputs before applying an activation function. Matrix multiplication is a set of linear combinations computed in parallel.

### Dot Product (Inner Product)

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = u_1v_1 + u_2v_2 + \cdots + u_nv_n$$

**The geometric identity** (derivation below):

$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$$

where $\theta$ is the angle between the vectors.

### Derivation: Why does dot product equal $\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$?

Start from the law of cosines. For a triangle with sides $a, b, c$ and angle $\theta$ opposite to $c$:

$$c^2 = a^2 + b^2 - 2ab\cos\theta$$

Let $a = \|\mathbf{u}\|$, $b = \|\mathbf{v}\|$, and $c = \|\mathbf{u} - \mathbf{v}\|$. Then:

$$\|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

Expand the left side:

$$\|\mathbf{u} - \mathbf{v}\|^2 = \sum_i (u_i - v_i)^2 = \sum_i u_i^2 - 2\sum_i u_iv_i + \sum_i v_i^2 = \|\mathbf{u}\|^2 - 2(\mathbf{u} \cdot \mathbf{v}) + \|\mathbf{v}\|^2$$

Setting both expressions equal:

$$\|\mathbf{u}\|^2 - 2(\mathbf{u} \cdot \mathbf{v}) + \|\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

Cancel $\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$ from both sides:

$$-2(\mathbf{u} \cdot \mathbf{v}) = -2\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

$$\boxed{\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta} \quad \blacksquare$$

### Worked example (Dot Product)

$$\mathbf{u} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}, \quad \mathbf{v} = \begin{bmatrix} -1 \\ 4 \end{bmatrix}$$

$$\mathbf{u} \cdot \mathbf{v} = (2)(-1) + (3)(4) = -2 + 12 = 10$$

Verify via geometric formula:
- $\|\mathbf{u}\| = \sqrt{4+9} = \sqrt{13}$
- $\|\mathbf{v}\| = \sqrt{1+16} = \sqrt{17}$
- $\cos\theta = \frac{10}{\sqrt{13}\sqrt{17}} = \frac{10}{\sqrt{221}} \approx 0.673$
- $\theta \approx 47.7°$ — acute angle, vectors point "roughly the same way"

### Key Dot Product Properties

| Property | Implication |
|----------|-------------|
| $\mathbf{u} \cdot \mathbf{v} > 0$ | Angle < 90° — vectors point in similar directions |
| $\mathbf{u} \cdot \mathbf{v} = 0$ | Angle = 90° — vectors are **orthogonal** (independent) |
| $\mathbf{u} \cdot \mathbf{v} < 0$ | Angle > 90° — vectors point in opposite-ish directions |
| $\mathbf{u} \cdot \mathbf{u} = \|\mathbf{u}\|^2$ | Dot product with itself gives squared magnitude |

## Code Example

```python
import numpy as np

u = np.array([2.0, 3.0])
v = np.array([-1.0, 4.0])

# Manual dot product
dot = sum(u_i * v_i for u_i, v_i in zip(u, v))  # 10.0

# Verify with geometric formula
norm_u = np.sqrt(np.dot(u, u))  # sqrt(13)
norm_v = np.sqrt(np.dot(v, v))  # sqrt(17)
cos_theta = dot / (norm_u * norm_v)  # 0.673
theta_degrees = np.degrees(np.arccos(cos_theta))  # 47.7°
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- The dot product is the foundation of [[cosine-similarity]] — normalize by norms to isolate the angle
- [[vector-norms]] are defined via the dot product: $\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}}$
- Linear combinations lead to [[linear-independence]] — can one vector be "reached" from others?
- Matrix multiplication is organized dot products → [[Matrix Operations and Properties]]
- In neural networks, each neuron computes $\mathbf{w} \cdot \mathbf{x} + b$ — a dot product

## Sources

- [3Blue1Brown — Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0)
- [MIT 18.06 — Strang, Lecture 1: Geometry of Linear Equations](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.2](https://mml-book.github.io/book/mml-book.pdf)
