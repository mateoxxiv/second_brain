---
tags:
  - status/growing
  - calculus
related:
  - "[[derivatives-and-partial-derivatives]]"
  - "[[gradient-descent]]"
  - "[[derivative-rules]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[special-matrices]]"
domain: calculus
sources:
  - "https://www.youtube.com/watch?v=IHZwWFHWa-w"
  - "https://www.khanacademy.org/math/calculus-1"
  - "https://ruder.io/optimizing-gradient-descent/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — f' = 0 finds critical points. f'' > 0 means minimum. f'' < 0 means maximum. Convexity guarantees a single global minimum.

---

## Intuition

Optimization asks: where is f at its lowest? The first derivative tells you *where the function is flat* (slope = 0) — those are the candidates. The second derivative tells you *which candidate is actually a valley* (curving up) versus a hill (curving down).

Convexity is the holy grail: a function that curves upward everywhere has exactly one valley. Any path downhill leads to the same bottom — gradient descent always finds the global minimum.

## Mechanics

**Finding critical points:** set f'(x) = 0 and solve.

**Second derivative test:**
$$f''(x) > 0 \Rightarrow \text{minimum} \quad f''(x) < 0 \Rightarrow \text{maximum} \quad f''(x) = 0 \Rightarrow \text{inconclusive}$$

**Convexity check:** f''(x) ≥ 0 everywhere → convex → single global minimum.

**Multivariable:** replace f'' with the Hessian matrix H = [∂²f/∂xᵢ∂xⱼ]. Its eigenvalues classify the critical point: all positive → minimum; all negative → maximum; mixed → saddle.

| Condition | Type |
|-----------|------|
| f' = 0, f'' > 0 | Minimum |
| f' = 0, f'' < 0 | Maximum |
| H eigenvalues all > 0 | Multivariable minimum |
| H eigenvalues mixed signs | Saddle point |

```python
import numpy as np

# Classify critical points of f(x) = x^3 - 3x
f        = lambda x: x**3 - 3*x
f_prime  = lambda x: 3*x**2 - 3
f_double = lambda x: 6*x

for x in [-1.0, 1.0]:
    fpp  = f_double(x)
    kind = "minimum" if fpp > 0 else "maximum"
    print(f"x={x}: f={f(x):.1f}, f''={fpp:.1f} → {kind}")

# Saddle point Hessian: f(x,y) = x^2 - y^2
H    = np.array([[2.0, 0.0], [0.0, -2.0]])
eigs = np.linalg.eigvalsh(H)
print(f"Hessian eigenvalues: {eigs}")  # [-2, 2] — mixed → saddle
```

> Runnable: [[code/foundations/optimization.py]]

## In ML

**Convex loss functions guarantee convergence.** MSE (linear regression) and log-loss (logistic regression) are both convex — gradient descent always reaches the global minimum. This is why these models are "solved" optimization problems.

**Neural network loss is non-convex.** The loss landscape has saddle points, narrow valleys, and flat plateaus. Most critical points in deep networks are saddle points, not local minima — and surprisingly, gradient descent navigates them well in high dimensions because mini-batch noise provides enough perturbation to escape.

**Hessian eigenvalues control convergence speed.** The condition number (ratio of largest to smallest eigenvalue) determines how fast gradient descent converges. Poorly conditioned Hessians (elongated loss bowls) cause slow oscillating convergence — this is why Adam uses second-moment information to adapt step sizes per dimension.

## Exercises

**Basic** — Find and classify all critical points of f(x) = x³ − 3x. Verify with the second derivative test.

**Intermediate** — Prove that f(x) = x² is convex using the definition: f(λx + (1−λ)y) ≤ λf(x) + (1−λ)f(y) for λ ∈ [0,1].

**Advanced** — Explain why most critical points in deep networks are saddle points, not local minima. Use the argument that a local minimum requires all Hessian eigenvalues to be positive, which becomes exponentially unlikely in high dimensions.
