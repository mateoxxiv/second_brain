---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[vector-operations]]"
  - "[[cosine-similarity]]"
  - "[[projection]]"
  - "[[vector-norms]]"
  - "[[cross-product]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — The dot product has two equivalent definitions: algebraic (sum of element-wise products) and geometric (|a||b|cosθ). Their equivalence means a single number encodes both magnitude and angle between two vectors.

---

## Intuition

Two questions you might ask about two vectors: how long are they, and how much do they point in the same direction? The dot product answers both at once.

Think of a solar panel: maximum power when facing the sun directly (θ=0, cos=1), zero power at 90°, negative when facing away. The dot product is that "facing" measurement, scaled by the lengths of both vectors.

## Mechanics

**Algebraic definition** (coordinates):

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_i b_i = a_1b_1 + a_2b_2 + \cdots + a_nb_n$$

**Geometric definition** (angle):

$$\mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\|\,\|\mathbf{b}\|\cos\theta$$

**Why they're equal** — expand $\|\mathbf{a} - \mathbf{b}\|^2$ using the law of cosines ($c^2 = a^2 + b^2 - 2ab\cos\theta$) and the [[vector-norms]] identity $\|\mathbf{v}\|^2 = \mathbf{v}\cdot\mathbf{v}$. Both sides reduce to the same expression.

| Property | Rule |
|---|---|
| Commutative | $\mathbf{a}\cdot\mathbf{b} = \mathbf{b}\cdot\mathbf{a}$ |
| Distributive | $\mathbf{a}\cdot(\mathbf{b}+\mathbf{c}) = \mathbf{a}\cdot\mathbf{b} + \mathbf{a}\cdot\mathbf{c}$ |
| Self dot product | $\mathbf{a}\cdot\mathbf{a} = \|\mathbf{a}\|^2$ |
| Orthogonality | $\mathbf{a}\cdot\mathbf{b} = 0 \iff \mathbf{a} \perp \mathbf{b}$ |

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

algebraic = np.dot(a, b)                              # 32
geometric = np.linalg.norm(a) * np.linalg.norm(b) * np.cos(
    np.arccos(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))))

print(np.isclose(algebraic, geometric))               # True
print(np.dot(a, a), np.linalg.norm(a)**2)             # 14  14.0
```


## In ML

**Neuron computation** — every neuron computes $z = \mathbf{w}\cdot\mathbf{x} + b$. The entire forward pass of a neural network is a chain of dot products organized as matrix multiplications.

**[[cosine-similarity]]** — dividing the dot product by both norms gives cosθ directly: $\cos\theta = \frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|\|\mathbf{b}\|}$. When vectors are already unit-normalized, dot product IS cosine similarity — this is how attention scores are computed.

**[[projection]]** — the scalar projection of $\mathbf{b}$ onto $\mathbf{a}$ is $\frac{\mathbf{a}\cdot\mathbf{b}}{\|\mathbf{a}\|}$. The dot product is the engine behind every projection operation.

## Exercises

**Basic** — Compute $[1,2,3]\cdot[4,5,6]$ by hand. Then verify with NumPy. What is $[1,0]\cdot[0,1]$, and what does it mean geometrically?

**Intermediate** — Two vectors have dot product 12, norms 3 and 5. Find the angle between them. Are they more parallel or more perpendicular?

**Advanced** — Prove that $|\mathbf{a}\cdot\mathbf{b}| \leq \|\mathbf{a}\|\|\mathbf{b}\|$ (Cauchy-Schwarz inequality) using the geometric definition. When does equality hold?
