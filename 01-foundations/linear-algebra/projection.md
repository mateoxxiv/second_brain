---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[vector-operations]]"
  - "[[vector-norms]]"
  - "[[cosine-similarity]]"
  - "[[projection-onto-subspaces]]"
  - "[[gram-schmidt]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Projection finds the closest point on a line to a given vector. The shadow is the projection; the gap between the vector and its shadow (the residual) is always perpendicular to the line.

---

## Intuition

A flashlight shines straight down onto a clothesline. The shadow of a ball on that line is the **projection**. The string from the ball to its shadow is the **residual** — and it's always perpendicular to the line.

The residual is the *minimum possible* distance from the vector to the line. Any other point on the line would produce a longer string. This "perpendicular = minimum error" principle is the geometric engine behind least squares regression.

This note covers projection onto a **single vector** (a line). For projection onto planes and higher spaces, see [[projection-onto-subspaces]].

## Mechanics

**Scalar projection** (the signed length of the shadow):
$$\text{comp}_\mathbf{a}\mathbf{b} = \frac{\mathbf{b}\cdot\mathbf{a}}{\|\mathbf{a}\|}$$

**Vector projection** (the actual shadow vector):
$$\text{proj}_\mathbf{a}\mathbf{b} = \frac{\mathbf{b}\cdot\mathbf{a}}{\mathbf{a}\cdot\mathbf{a}}\,\mathbf{a} = \frac{\mathbf{b}\cdot\mathbf{a}}{\|\mathbf{a}\|^2}\,\mathbf{a}$$

**Residual** (the perpendicular gap): $\mathbf{e} = \mathbf{b} - \text{proj}_\mathbf{a}\mathbf{b}$, always satisfies $\mathbf{e}\cdot\mathbf{a} = 0$.

```python
import numpy as np

a = np.array([2.0, 1.0])   # line direction
b = np.array([3.0, 3.0])   # vector to project

proj = (np.dot(b, a) / np.dot(a, a)) * a   # [3.6, 1.8]
residual = b - proj                          # [-0.6, 1.2]

print(np.dot(residual, a))  # ≈ 0.0 — perpendicular ✓
```

> Runnable: [[code/foundations/vectors_and_spaces.py]]

## In ML

**Least squares** — when $A\mathbf{x} = \mathbf{b}$ has no exact solution (noisy data), we find the closest solution: project $\mathbf{b}$ onto the column space of $A$. The residual $\mathbf{e}$ is perpendicular to that space.

**[[gram-schmidt|Gram-Schmidt orthogonalization]]** — builds orthonormal bases by repeatedly projecting and subtracting the projection (removing the "shadow" component to extract the perpendicular part).

**Attention mechanism** — query-key dot products measure how much each query "projects" onto each key direction. High projection = high attention weight.

## Exercises

**Basic** — Project $\mathbf{b} = [4, 3]$ onto $\mathbf{a} = [2, 0]$. Compute both the scalar and vector projection. Verify the residual is perpendicular to $\mathbf{a}$.

**Intermediate** — Project $\mathbf{b} = [1, 2, 3]$ onto $\mathbf{a} = [1, 1, 0]$. Show that $\mathbf{b} = \text{proj} + \text{residual}$.

**Advanced** — Prove that the projection minimizes distance: show that $\|\mathbf{b} - c\mathbf{a}\|^2$ is minimized at $c = \frac{\mathbf{b}\cdot\mathbf{a}}{\mathbf{a}\cdot\mathbf{a}}$ by completing the square or taking the derivative.
