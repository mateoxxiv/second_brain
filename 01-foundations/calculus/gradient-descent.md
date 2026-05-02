---
tags:
  - status/growing
  - calculus
related:
  - "[[derivatives-and-partial-derivatives]]"
  - "[[chain-rule]]"
  - "[[derivative-rules]]"
  - "[[linear-transformations]]"
  - "[[eigenvalues-and-eigenvectors]]"
domain: calculus
sources:
  - "https://www.youtube.com/watch?v=IHZwWFHWa-w"
  - "https://www.coursera.org/learn/machine-learning"
  - "https://ruder.io/optimizing-gradient-descent/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — w_new = w_old − lr · ∇L(w). Compute the gradient (which way is uphill), step the opposite direction, repeat. This is how every ML model trains.

---

## Intuition

Imagine being blindfolded on a hilly surface and trying to reach the lowest point. You can feel the slope under your feet. The smartest move is to take a small step in whichever direction slopes downward most steeply, then re-check the slope. Repeat until flat.

That is gradient descent: at every point, compute the gradient (steepest uphill direction), step the opposite direction by a small amount controlled by the learning rate, repeat until gradient ≈ 0 (minimum reached).

## Mechanics

**Update rule:**
$$w \leftarrow w - \alpha \cdot \nabla L(w)$$

**Worked example — f(x) = x², starting at x = 10, lr = 0.1:**
```
Step 1: x = 10 − 0.1·2(10) = 8.0
Step 2: x = 8.0 − 0.1·2(8) = 6.4
Step 3: x = 6.4 − 0.1·2(6.4) = 5.12 ...
```
Steps shrink naturally as gradient shrinks near the minimum.

**Three variants:**

| Variant | Data per step | Speed | Stability |
|---------|--------------|-------|-----------|
| Batch GD | all N samples | slow | very stable |
| SGD | 1 sample | fast | noisy |
| Mini-batch | 32–128 samples | fast | stable enough |

Mini-batch is the standard in practice — fits in GPU memory and parallelizes well.

```python
import numpy as np

def gradient_descent_1d(f_prime, x0, lr=0.1, steps=50):
    x = float(x0)
    for _ in range(steps):
        x = x - lr * f_prime(x)
    return x

# f(x) = x^2, f'(x) = 2x, minimum at 0
result = gradient_descent_1d(lambda x: 2*x, x0=10.0, lr=0.1)
print(f"Minimum at x = {result:.6f}")  # ≈ 0

# Learning rate comparison
for lr in [0.01, 0.1, 0.5, 1.0]:
    r = gradient_descent_1d(lambda x: 2*x, x0=10.0, lr=lr, steps=10)
    print(f"lr={lr}: after 10 steps x = {r:.4f}")
```

> Runnable: [[code/foundations/gradient_descent.py]]

## In ML

**Mini-batch is standard.** Computing gradients over all N training samples each step is prohibitive for large datasets. Mini-batch GD averages the gradient over 32–128 random samples per step — fast enough for GPUs, stable enough to converge.

**Saddle points and failure modes.** In high-dimensional neural network loss landscapes, most critical points are saddle points (flat in some directions, curved in others), not local minima. Mini-batch noise helps escape saddle points. Plateaus (near-zero gradient over a wide region) are where training stalls — momentum-based optimizers (Adam, RMSProp) push through.

**Learning rate is the most important hyperparameter.** Too small: converges painfully slowly. Too large: overshoots and bounces or diverges. Learning rate schedules (warmup, cosine decay) and adaptive methods (Adam) largely solve the tuning problem in practice.

## Exercises

**Basic** — Implement gradient descent on f(x) = x² − 4x + 3 from scratch. Find the minimum and verify analytically.

**Intermediate** — Explain why mini-batch GD is preferred over full-batch GD in practice. What are the tradeoffs in terms of computation, memory, and convergence?

**Advanced** — Derive the update rule for 2D quadratic f(x,y) = ax² + by². Show that the optimal learning rate depends on the largest eigenvalue of the Hessian.
