---
tags:
  - status/growing
  - calculus
related:
  - "[[linear-transformations]]"
  - "[[vectors-and-vector-spaces]]"
domain: calculus
sources:
  - "https://www.3blue1brown.com/topics/calculus"
  - "https://www.khanacademy.org/math/calculus-1"
  - "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — The derivative is instantaneous rate of change (slope at a point). The gradient collects all partial derivatives into a vector that points in the direction of steepest increase.

---

## Intuition

A derivative answers: "if I nudge x by a tiny amount, how much does f(x) change?" It is the slope of the function at a single point.

For functions of multiple variables, a **partial derivative** fixes all variables except one and asks the same question for that variable alone. The **gradient** bundles all the partial derivatives into a vector — it points in the direction where f increases fastest.

To minimize a loss function, move in the *opposite* direction of the gradient.

## Mechanics

**Derivative** (single variable):
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

**Partial derivative** — hold all variables fixed except xᵢ:
$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x + h \cdot e_i) - f(x)}{h}$$

**Gradient** — vector of all partials:
$$\nabla f = \left[\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right]$$

**Critical points**: ∇f = 0. Could be minimum, maximum, or saddle point.

```python
import numpy as np

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def numerical_gradient(f, x: np.ndarray, h=1e-5) -> np.ndarray:
    grad = np.zeros_like(x, dtype=float)
    for i in range(len(x)):
        xp, xm = x.copy(), x.copy()
        xp[i] += h; xm[i] -= h
        grad[i] = (f(xp) - f(xm)) / (2 * h)
    return grad

f = lambda x: 3*x[0]**2 + 2*x[0]*x[1]
print(numerical_gradient(f, np.array([1.0, 2.0])))  # [10, 2]
```

> Runnable: [[code/foundations/derivatives.py]]

## In ML

**Gradient descent** uses the gradient to update model parameters. ∇L(w) tells us the direction of steepest increase of the loss — move opposite: w ← w − α·∇L(w). See [[gradient-descent]].

**Backpropagation** computes ∇L w.r.t. every weight using the chain rule applied to partial derivatives. Each partial derivative tells how much the loss changes if that one weight is nudged.

**Critical points in high dimensions.** In neural networks, critical points (∇L = 0) are almost never true local minima — they are overwhelmingly saddle points. A point that is a minimum in some directions but a maximum in others. SGD naturally escapes saddle points via gradient noise.

## Exercises

**Basic** — Compute the gradient of f(x, y) = 3x² + 2xy by hand. Evaluate it at (1, 2).

**Intermediate** — Implement gradient descent from scratch on f(x) = x² starting from x = 5. Print x at each step until |f'(x)| < 0.01.

**Advanced** — Explain why saddle points dominate in high-dimensional neural network loss landscapes. Use the argument that a random critical point in n dimensions requires all n curvature eigenvalues to have the same sign.
