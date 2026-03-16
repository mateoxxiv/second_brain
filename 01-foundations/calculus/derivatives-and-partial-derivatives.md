**Related**: [[linear-transformations]], [[vectors-and-vector-spaces]]
**Tags**: #status/growing

## Core Idea

A derivative answers: **how fast is f changing when I nudge x?** It's the slope
of the function at a specific point.

```
f(x) = x^2

At x = 3:  nudge x by 0.001
f(3) = 9,  f(3.001) = 9.006001

rate = 0.006001 / 0.001 ≈ 6.0   ← the derivative at x=3
```

The derivative tells you the direction and speed of change:

```
f'(x) > 0  →  function going UP    →  move left to decrease
f'(x) < 0  →  function going DOWN  →  move right to decrease
f'(x) = 0  →  flat — at a minimum, maximum, or saddle point
```

## Details

### The Power Rule

The derivative of f(x) = x^n:

```
f(x) = x^n   →   f'(x) = n * x^(n-1)
```

Bring the exponent down, subtract 1 from it.

### Common Derivatives

```
f(x) = x^2     →  f'(x) = 2x
f(x) = x^3     →  f'(x) = 3x^2
f(x) = x       →  f'(x) = 1           (straight line, constant slope)
f(x) = 5       →  f'(x) = 0           (flat, constant never changes)
f(x) = 3x^2    →  f'(x) = 6x          (constant multiplier stays)
f(x) = x^4 + 3x^2 + 7  →  f'(x) = 4x^3 + 6x
```

Constants disappear (derivative of 7 is 0). Each term is differentiated
independently, then added back.

### Partial Derivatives — Multiple Inputs

In ML, functions have many inputs (weights). A partial derivative differentiates
with respect to ONE variable, treating all others as constants.

```
f(x, y) = x^2 + 3xy + y^2

df/dx = 2x + 3y       (treat y as constant)
df/dy = 3x + 2y       (treat x as constant)
```

Same power rule — just pretend the other variables are numbers.

### The Gradient — All Partials as a Vector

Pack all partial derivatives into a vector. That's the **gradient**:

```
f(x, y) = 5x^2 + 2xy + y^3

gradient = [df/dx, df/dy] = [10x + 2y,  2x + 3y^2]
```

The gradient is a vector that **points in the direction of steepest increase**.
Go the opposite direction for steepest decrease — that's gradient descent.

### Gradient Descent — How Models Learn

```
1. Compute loss (how wrong the model is)
2. Compute gradient of loss w.r.t. each weight
3. Update: w_new = w_old - learning_rate * gradient
4. Repeat until gradient ≈ 0 (minimum reached)
```

The learning rate controls step size. Too big → overshoot. Too small → too slow.

Example at point (1, 1) with learning_rate = 0.01:

```
gradient = [10(1)+2(1), 2(1)+3(1)^2] = [12, 5]

new position = [1, 1] - 0.01 * [12, 5]
             = [1 - 0.12, 1 - 0.05]
             = [0.88, 0.95]
```

Small step downhill. Recompute gradient at new position, repeat.

### Critical Points — Where Gradient = 0

When the gradient is zero, the function is flat. Three possibilities:

```
Minimum     →  valley bottom (where we want to be)
Maximum     →  peak (worst spot)
Saddle point → minimum in one direction, maximum in another
```

In deep learning, saddle points are common in high dimensions and can slow
training because the gradient gives no direction to move.

### Why Derivatives Matter for ML

| Concept | Uses derivatives how |
|---------|---------------------|
| Gradient descent | Follow negative gradient to minimize loss |
| Backpropagation | Chain rule to compute gradients through layers |
| Learning rate | Scales the gradient step size |
| Loss functions | Must be differentiable so we can compute gradients |
| Adam optimizer | Uses first and second derivatives (gradient + curvature) |
| Regularization | Adds derivative penalty to prevent overfitting |

## Code Example

```python
import numpy as np

# Numerical derivative: f'(x) ≈ (f(x+h) - f(x-h)) / 2h
def derivative(f, x, h=1e-7):
    return (f(x + h) - f(x - h)) / (2 * h)

# Numerical gradient for multivariable functions
def gradient(f, point, h=1e-7):
    grad = np.zeros_like(point, dtype=float)
    for i in range(len(point)):
        step = np.zeros_like(point, dtype=float)
        step[i] = h
        grad[i] = (f(point + step) - f(point - step)) / (2 * h)
    return grad

# Test: f(x) = x^2, f'(x) = 2x
f = lambda x: x**2
print(derivative(f, 3.0))       # ≈ 6.0

# Test: f(x,y) = 5x^2 + 2xy + y^3
g = lambda p: 5*p[0]**2 + 2*p[0]*p[1] + p[1]**3
print(gradient(g, np.array([1.0, 1.0])))  # ≈ [12, 5]

# Simple gradient descent
def gradient_descent(f, start, lr=0.01, steps=100):
    point = np.array(start, dtype=float)
    for i in range(steps):
        grad = gradient(f, point)
        point = point - lr * grad
    return point

# Minimize f(x,y) = x^2 + y^2 (minimum at origin)
h = lambda p: p[0]**2 + p[1]**2
result = gradient_descent(h, [5.0, 3.0], lr=0.1, steps=50)
print(result)  # ≈ [0, 0]
```

> For runnable implementation with exercises, see: [[code/foundations/derivatives.py]]

## Connections

- [[linear-transformations]] — the derivative at a point IS the best linear
  approximation of the function
- [[vectors-and-vector-spaces]] — the gradient is a vector in input space
- Forward link: chain rule — derivatives of composed functions (backpropagation)
- Forward link: gradient descent — full optimization algorithm
- Forward link: matrix calculus — Jacobians and Hessians (derivatives of vector functions)

## Sources

- [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus) — best visual intuition for derivatives
- [Khan Academy — Derivatives](https://www.khanacademy.org/math/calculus-1) — interactive exercises
- [MIT 18.01 — Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)
- [Mathematics for Machine Learning — Chapter 5](https://mml-book.github.io/book/mml-book.pdf) — derivatives in ML context
