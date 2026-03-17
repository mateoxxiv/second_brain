**Related**: [[derivatives-and-partial-derivatives]], [[gradient-descent]], [[derivative-rules]], [[eigenvalues-and-eigenvectors]]
**Tags**: #status/growing

## Core Idea

Optimization finds the minimum (or maximum) of a function. The first derivative
tells you WHERE the critical points are (slope = 0). The second derivative tells
you WHAT KIND they are (minimum, maximum, or saddle point). **Convexity**
guarantees there's only one minimum — making optimization easy.

## Details

### Finding Critical Points

Set the first derivative to zero and solve:

```
f(x) = x^2 - 4x + 3
f'(x) = 2x - 4 = 0
x = 2             ← critical point
```

### Second Derivative Test — What Kind of Critical Point?

The second derivative measures **curvature** — is the function curving up or down?

```
f''(x) > 0  →  curving UP (bowl)    →  MINIMUM
f''(x) < 0  →  curving DOWN (hill)  →  MAXIMUM
f''(x) = 0  →  inconclusive         →  need more analysis
```

**Worked Example:** f(x) = x^3 - 3x

```
f'(x) = 3x^2 - 3 = 0  →  x = 1 or x = -1
f''(x) = 6x

At x = 1:  f''(1) = 6 > 0   →  MINIMUM
At x = -1: f''(-1) = -6 < 0  →  MAXIMUM
```

### Intuition: First vs Second Derivative

```
First derivative = speed       (how fast is f changing?)
Second derivative = acceleration (is the speed increasing or decreasing?)
```

At a minimum: speed is zero (f' = 0) and accelerating upward (f'' > 0).
The function has stopped going down and is about to go back up — the bottom.

### Convexity — The Best Case for ML

A function is **convex** when it curves upward everywhere — like a bowl.
f''(x) >= 0 for all x.

```
Convex (one valley):     Not convex (bumpy):

    \     /                  /\    /\
     \   /                  /  \  /  \
      \_/                  /    \/    \
   one minimum           multiple minima
```

**Why convexity matters:**
- **Convex** → gradient descent ALWAYS finds the global minimum. Only one valley.
- **Not convex** → might get stuck in a local minimum (not the best).

**Checking convexity:**

```
f(x) = x^2      f''(x) = 2 > 0       always → CONVEX
f(x) = x^4      f''(x) = 12x^2 >= 0  always → CONVEX
f(x) = e^x      f''(x) = e^x > 0     always → CONVEX
f(x) = x^3      f''(x) = 6x          negative for x<0 → NOT CONVEX
```

### Convexity in ML

| Loss function | Convex? | Consequence |
|--------------|---------|-------------|
| MSE (linear regression) | Yes | Guaranteed global minimum |
| Log-loss (logistic regression) | Yes | Guaranteed global minimum |
| Neural network loss | No | Local minima, saddle points exist |

This is why linear/logistic regression are "solved" problems — convex loss
means [[gradient-descent]] always works. Neural networks are harder — the loss
landscape is bumpy.

### Saddle Points (Multiple Variables)

In 1D: critical points are minima or maxima.
In multiple dimensions: a third option — **saddle points**.

```
f(x, y) = x^2 - y^2

gradient = [2x, -2y] = [0, 0]  at (0, 0)

Along x-direction: f = x^2  (curves UP — minimum)
Along y-direction: f = -y^2 (curves DOWN — maximum)
```

Minimum in one direction, maximum in another — like a horse saddle.

In neural networks with millions of weights, most critical points are saddle
points. Mini-batch SGD noise helps escape them by pushing the parameters
sideways off the saddle.

### Multivariable Second Derivative Test (Hessian)

For functions of multiple variables, the second derivative becomes the
**Hessian matrix** — a matrix of all second partial derivatives. Its
[[eigenvalues-and-eigenvectors|eigenvalues]] classify the critical point:

```
All eigenvalues > 0  →  minimum (bowl in every direction)
All eigenvalues < 0  →  maximum (hill in every direction)
Mixed signs           →  saddle point
```

This connects back to [[eigenvalues-and-eigenvectors]] — eigenvalues of the
Hessian tell you the curvature in each eigenvector direction.

### Quick Reference

| Test | Result | Meaning |
|------|--------|---------|
| f' = 0, f'' > 0 | Minimum | Bowl — GD converges here |
| f' = 0, f'' < 0 | Maximum | Hill — GD runs away |
| f' = 0, f'' = 0 | Inconclusive | Could be saddle or flat |
| f'' >= 0 everywhere | Convex | Guaranteed global minimum |
| Hessian eigenvalues all > 0 | Convex at that point | Positive definite Hessian |

## Code Example

```python
import numpy as np

# Find critical points and classify them
# f(x) = x^3 - 3x
f = lambda x: x**3 - 3*x
f_prime = lambda x: 3*x**2 - 3
f_double_prime = lambda x: 6*x

# Critical points: f'(x) = 0
# 3x^2 - 3 = 0 → x = +-1
for x in [-1, 1]:
    fpp = f_double_prime(x)
    kind = "minimum" if fpp > 0 else "maximum" if fpp < 0 else "inconclusive"
    print(f"x={x}: f={f(x)}, f''={fpp} → {kind}")
# x=-1: f=2, f''=-6 → maximum
# x=1:  f=-2, f''=6 → minimum

# Check convexity of x^2
x_range = np.linspace(-10, 10, 100)
print(f"x^2 convex: {all(2 > 0 for _ in x_range)}")  # True

# Saddle point: f(x,y) = x^2 - y^2
def hessian_eigenvalues(x, y):
    # Hessian = [[d2f/dx2, d2f/dxdy], [d2f/dydx, d2f/dy2]]
    H = np.array([[2, 0], [0, -2]])
    return np.linalg.eigvalsh(H)

eigs = hessian_eigenvalues(0, 0)
print(f"Eigenvalues at saddle: {eigs}")  # [-2, 2] — mixed signs!
```

## Connections

- [[derivatives-and-partial-derivatives]] — first derivative finds critical points
- [[gradient-descent]] — the algorithm that navigates the loss landscape to find minima
- [[eigenvalues-and-eigenvectors]] — Hessian eigenvalues classify critical points
- [[special-matrices]] — positive definite Hessian = minimum
- Forward link: loss functions — MSE is convex, neural net loss is not
- Forward link: regularization — makes the loss more convex

## Sources

- [3Blue1Brown — Gradient Descent (covers minima)](https://www.youtube.com/watch?v=IHZwWFHWa-w)
- [Khan Academy — Second Derivative Test](https://www.khanacademy.org/math/calculus-1)
- [Sebastian Ruder — Saddle Points and Plateaus](https://ruder.io/optimizing-gradient-descent/)
- [Mathematics for Machine Learning — Chapter 7.1](https://mml-book.github.io/book/mml-book.pdf)
