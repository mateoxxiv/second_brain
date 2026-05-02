---
tags:
  - status/growing
  - calculus
related:
  - "[[derivatives-and-partial-derivatives]]"
  - "[[linear-transformations]]"
domain: calculus
sources:
  - "https://www.3blue1brown.com/topics/calculus"
  - "https://www.youtube.com/watch?v=Ilg3gGewQ5U"
  - "https://github.com/karpathy/micrograd"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — The chain rule computes derivatives of nested functions: df/dx = g'(h(x)) · h'(x). This IS backpropagation.

---

## Intuition

When one function is nested inside another, the rate of change of the outer function depends on how both functions change. Think of gears: if gear A turns at 2x the input and gear B turns at 3x gear A, then B turns at 6x the input — you multiply the rates.

For f(x) = g(h(x)): how fast f changes with x equals how fast g changes with h, times how fast h changes with x. Multiply rates along the chain.

## Mechanics

For f = g(h(x)):
$$\frac{df}{dx} = g'(h(x)) \cdot h'(x)$$

**Example 1:** f(x) = (3x + 1)² — inner h = 3x+1, outer g = u²
$$f'(x) = 2(3x+1) \cdot 3 = 6(3x+1)$$

**Multi-layer chain** — f = g(h(k(x))):
$$\frac{df}{dx} = g'(h(k)) \cdot h'(k) \cdot k'(x)$$

```python
import numpy as np

def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Manual backprop: 2-layer network (no libraries)
def backward(x, w1, w2):
    z1 = w1 * x
    a1 = np.tanh(z1)          # layer 1 activation
    # chain rule backward
    da1 = (1 - a1**2)         # tanh derivative
    dw2 = a1                  # d(w2*a1)/dw2
    dw1 = w2 * da1 * x        # chain: output → a1 → z1 → w1
    return dw1, dw2

print(backward(2.0, 3.0, 4.0))
```

> Runnable: [[code/foundations/chain_rule.py]]

## In ML

**Backpropagation is chain rule on computation graphs.** A neural network is a composition of functions. To update weights, you need the gradient of the loss w.r.t. every weight. Backprop applies the chain rule layer by layer — from output back to input — accumulating gradients.

**Vanishing gradients.** Deep networks multiply many derivatives together. If each derivative < 1 (e.g., 0.1 per sigmoid layer), the gradient shrinks exponentially: 0.1^n → 0. Early layers stop learning. ReLU and residual connections fix this.

**Autograd** (PyTorch, JAX) implements the chain rule automatically. Every operation builds a computation graph; `.backward()` traverses it in reverse applying the chain rule at each node.

## Exercises

**Basic** — Derive the chain rule for f(x) = (3x + 1)². Show every step using inner/outer notation.

**Intermediate** — Trace backprop by hand through a 3-layer network: loss = (y_pred − y_true)², y_pred = w3 · tanh(w2 · tanh(w1 · x)). Compute dL/dw1.

**Advanced** — Prove that vanishing gradients are inevitable with sigmoid activations at depth n. Show that sigmoid'(x) < 0.25 everywhere, so gradient magnitude ≤ 0.25^n → 0.
