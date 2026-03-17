**Related**: [[derivatives-and-partial-derivatives]], [[chain-rule]], [[derivative-rules]], [[linear-transformations]]
**Tags**: #status/growing

## Core Idea

Gradient descent finds the minimum of a function by repeatedly taking small
steps in the direction the function decreases fastest. It's THE algorithm that
trains every ML model.

```
w_new = w_old - lr * gradient(loss, w_old)
```

One line. Compute the gradient (which way is uphill), go the opposite direction
(downhill), repeat until gradient is near zero (you're at the bottom).

## Details

### The Algorithm

```
1. Start at a random point
2. Compute the gradient (direction of steepest increase)
3. Take a small step in the OPPOSITE direction (decrease)
4. Repeat until gradient ≈ 0 (minimum reached)
```

### Worked Example

f(x) = x^2, minimum at x = 0. f'(x) = 2x.

```
lr = 0.1, start at x = 10

Step 1: x = 10  - 0.1 * 2(10) = 10  - 2.0 = 8.0
Step 2: x = 8.0 - 0.1 * 2(8)  = 8.0 - 1.6 = 6.4
Step 3: x = 6.4 - 0.1 * 2(6.4)= 6.4 - 1.28 = 5.12
...
Step 50: x ≈ 0.0001
```

Each step gets smaller as the gradient shrinks near the minimum — naturally
slows down as it approaches the bottom.

### Learning Rate — The Most Important Hyperparameter

```
lr too small (0.01):  10 → 9.8 → 9.6 → ...  takes forever
lr just right (0.1):  10 → 8 → 6.4 → ...    converges smoothly
lr too big (1.0):     10 → -10 → 10 → -10    bounces forever
lr way too big (1.5): 10 → -20 → 50 → -130   EXPLODES
```

**Why lr = 1.0 bounces:**

```
x = 10,  grad = 20,   new_x = 10 - 1.0*20 = -10
x = -10, grad = -20,  new_x = -10 + 20 = 10    ← back to start!
```

Overshoots the minimum and lands on the other side at the same distance.

**Why lr = 0.5 is perfect for x^2:**

```
x = 10,  new_x = 10 - 0.5*20 = 0    ← minimum in one step!
```

But this only works for a perfect bowl. Real loss functions are complex —
no magic lr exists. In practice: start with 0.001 or 0.01 and tune.

### Three Variants

In ML, the loss is computed over training data. With millions of samples,
computing the gradient over ALL of them each step is expensive.

**Batch Gradient Descent** — use ALL data each step:

```
gradient = average over all N samples
```

Accurate direction but slow — one step requires the entire dataset.

**Stochastic Gradient Descent (SGD)** — use ONE random sample:

```
gradient = computed from 1 random sample
```

Fast but noisy — each sample pulls in a slightly different direction.

**Mini-batch Gradient Descent** — use a small batch (32, 64, 128):

```
gradient = average over 128 random samples
```

The standard in practice. Fast (fits in GPU memory, parallel processing),
and stable enough to converge. Almost everyone uses this.

| Variant | Data per step | Speed | Stability |
|---------|--------------|-------|-----------|
| Batch | all N | slow | very stable |
| Stochastic | 1 | fast | noisy |
| Mini-batch | 32-128 | fast | stable enough |

### Multivariable Gradient Descent

Real models have thousands of weights. Same algorithm — the gradient is
just a vector of partial derivatives from
[[derivatives-and-partial-derivatives]]:

```
f(w1, w2) = w1^2 + w2^2

gradient = [df/dw1, df/dw2] = [2*w1, 2*w2]

w1_new = w1 - lr * 2*w1
w2_new = w2 - lr * 2*w2
```

Each weight gets updated independently using its own partial derivative.

### When Gradient Descent Fails

**Local minima** — gets stuck in a dip that isn't the deepest point. In high
dimensions (neural networks), this is actually rare — most critical points
are saddle points, not local minima.

**Saddle points** — gradient is zero but it's not a minimum (flat in some
directions, curved in others). Mini-batch noise actually helps escape these.

**Flat regions (plateaus)** — gradient is near zero, progress stalls. This is
where momentum-based optimizers (Adam) help — they use velocity to push through.

## Code Example

```python
import numpy as np

def gradient_descent_1d(f_prime, x0, lr=0.1, steps=50):
    """Gradient descent for a 1D function.
    f_prime: the derivative function
    x0: starting point
    """
    x = x0
    history = [x]
    for _ in range(steps):
        x = x - lr * f_prime(x)
        history.append(x)
    return x, history

# f(x) = x^2, f'(x) = 2x, minimum at 0
result, hist = gradient_descent_1d(lambda x: 2*x, x0=10.0, lr=0.1)
print(f"Minimum at x = {result:.6f}")  # ≈ 0

# Multivariable: f(w1,w2) = w1^2 + w2^2
def gradient_descent_nd(grad_f, w0, lr=0.1, steps=100):
    w = np.array(w0, dtype=float)
    for _ in range(steps):
        w = w - lr * grad_f(w)
    return w

grad_f = lambda w: np.array([2*w[0], 2*w[1]])
result = gradient_descent_nd(grad_f, [5.0, 3.0], lr=0.1, steps=50)
print(f"Minimum at w = {result}")  # ≈ [0, 0]

# Learning rate comparison
for lr in [0.01, 0.1, 0.5, 1.0]:
    r, h = gradient_descent_1d(lambda x: 2*x, x0=10.0, lr=lr, steps=10)
    print(f"lr={lr}: after 10 steps x = {r:.4f}")
```

> For runnable implementation with exercises, see: [[code/foundations/gradient_descent.py]]

## Connections

- [[derivatives-and-partial-derivatives]] — gradient = direction of steepest ascent
- [[chain-rule]] — backpropagation computes gradients through layers using chain rule
- [[linear-transformations]] — each layer is a linear transformation being optimized
- [[eigenvalues-and-eigenvectors]] — eigenvalues of loss surface determine convergence speed
- Forward link: optimizers (SGD + momentum, Adam) — improvements on basic gradient descent
- Forward link: backpropagation — chain rule applied to compute gradients in neural networks
- Forward link: learning rate schedules — changing lr during training

## Sources

- [3Blue1Brown — Gradient Descent (Neural Networks Ch. 2)](https://www.youtube.com/watch?v=IHZwWFHWa-w)
- [Andrew Ng — Machine Learning (Coursera) — Gradient Descent](https://www.coursera.org/learn/machine-learning)
- [Sebastian Ruder — An Overview of Gradient Descent Optimization](https://ruder.io/optimizing-gradient-descent/) — comprehensive guide to all variants
- [Mathematics for Machine Learning — Chapter 7](https://mml-book.github.io/book/mml-book.pdf)
