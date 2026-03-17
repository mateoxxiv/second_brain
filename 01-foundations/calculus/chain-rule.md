**Related**: [[derivatives-and-partial-derivatives]], [[linear-transformations]]
**Tags**: #status/growing

## Core Idea

The chain rule computes derivatives of **nested functions** — a function inside
a function. Multiply the derivatives along the chain.

```
f(x) = outer(inner(x))

df/dx = (derivative of outer) * (derivative of inner)
```

This is **backpropagation**. A neural network is just nested functions, and
the chain rule tells you how to compute gradients through all the layers.

## Details

### The Formula

For f(x) = g(h(x)):

```
df/dx = g'(h(x)) * h'(x)
```

Derivative of the outer (evaluated at the inner) times derivative of the inner.

### Worked Examples

**f(x) = (3x + 1)^2**

```
inner: u = 3x + 1     →  du/dx = 3
outer: u^2             →  d/du = 2u

df/dx = 2(3x+1) * 3 = 6(3x+1)
```

**f(x) = (x^2 + 1)^3**

```
inner: u = x^2 + 1    →  du/dx = 2x
outer: u^3             →  d/du = 3u^2

df/dx = 3(x^2+1)^2 * 2x = 6x(x^2+1)^2
```

**f(x) = (5x - 2)^4**

```
inner: u = 5x - 2     →  du/dx = 5
outer: u^4             →  d/du = 4u^3

df/dx = 4(5x-2)^3 * 5 = 20(5x-2)^3
```

### Chains of Three or More

For f(x) = a(b(c(x))), multiply all derivatives:

```
df/dx = da/db * db/dc * dc/dx
```

**f(x) = ((2x)^2 + 1)^3**

```
innermost: a = 2x           →  da/dx = 2
middle:    b = a^2 + 1       →  db/da = 2a = 4x
outer:     f = b^3           →  df/db = 3b^2 = 3(4x^2+1)^2

df/dx = 3(4x^2+1)^2 * 4x * 2 = 24x(4x^2+1)^2
```

### This IS Backpropagation

A neural network is nested functions:

```
loss = L(f3(f2(f1(x))))

layer 1: f1(x)  = ReLU(W1 @ x + b1)
layer 2: f2(a)  = ReLU(W2 @ a + b2)
layer 3: f3(b)  = softmax(W3 @ b + b3)
loss:    L(y)   = cross_entropy(y, target)
```

To find how the loss changes with a weight in layer 1:

```
d(loss)/d(W1) = d(loss)/d(f3) * d(f3)/d(f2) * d(f2)/d(f1) * d(f1)/d(W1)
```

Multiply derivatives backwards through each layer. That's backprop — the
chain rule applied to a computation graph.

### Why It's Called "Back" Propagation

```
FORWARD pass:  input → layer1 → layer2 → layer3 → loss  (compute outputs)
BACKWARD pass: loss → layer3 → layer2 → layer1          (compute gradients)
```

The forward pass computes the function values. The backward pass applies
the chain rule in reverse — starting from the loss and multiplying
derivatives back through each layer.

### The Vanishing Gradient Problem

If each layer's derivative is small (say 0.1), the chain multiplies them:

```
0.1 * 0.1 * 0.1 * 0.1 = 0.0001
```

By layer 1, the gradient is nearly zero — the early layers can't learn.
This is the **vanishing gradient problem**. Solutions:
- ReLU activation (derivative is 0 or 1, not small fractions)
- Skip connections (ResNets — add a shortcut around layers)
- Careful initialization (keep [[eigenvalues-and-eigenvectors|eigenvalues]] near 1)

## Code Example

```python
import numpy as np

# Chain rule numerically
def chain_derivative(f, x, h=1e-7):
    """Same as regular derivative — chain rule is automatic numerically."""
    return (f(x + h) - f(x - h)) / (2 * h)

# f(x) = (x^2 + 1)^3
f = lambda x: (x**2 + 1)**3
# Analytical: f'(x) = 6x(x^2+1)^2
analytical = lambda x: 6 * x * (x**2 + 1)**2

x = 2.0
print(f"Numerical:  {chain_derivative(f, x):.4f}")   # 600.0
print(f"Analytical: {analytical(x):.4f}")              # 600.0

# Backprop example: two-layer network (simplified)
def forward(x, w1, w2):
    """layer1 → ReLU → layer2 → output"""
    z1 = w1 * x           # layer 1
    a1 = max(0, z1)       # ReLU
    z2 = w2 * a1          # layer 2
    return z2

# Manual backprop using chain rule
def backward(x, w1, w2):
    # Forward
    z1 = w1 * x
    a1 = max(0, z1)
    z2 = w2 * a1

    # Backward (chain rule)
    dz2_da1 = w2              # d(layer2)/d(relu_output)
    da1_dz1 = 1 if z1 > 0 else 0  # d(relu)/d(layer1)
    dz1_dw1 = x               # d(layer1)/d(w1)

    # Chain: d(output)/d(w1)
    dout_dw1 = dz2_da1 * da1_dz1 * dz1_dw1
    return dout_dw1

print(f"Gradient w.r.t. w1: {backward(2.0, 3.0, 4.0)}")  # 8.0
```

## Connections

- [[derivatives-and-partial-derivatives]] — chain rule extends single derivatives to compositions
- [[eigenvalues-and-eigenvectors]] — eigenvalues of weight matrices control gradient magnitude
- [[linear-transformations]] — each layer is a linear transformation + nonlinearity
- Forward link: gradient descent — uses chain rule gradients to update weights
- Forward link: backpropagation — chain rule applied to computation graphs
- Forward link: vanishing/exploding gradients — chain rule multiplication problem

## Sources

- [3Blue1Brown — Chain Rule (Essence of Calculus, Ch. 4)](https://www.3blue1brown.com/topics/calculus)
- [3Blue1Brown — Backpropagation](https://www.youtube.com/watch?v=Ilg3gGewQ5U) — chain rule in neural networks
- [Andrej Karpathy — Micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — build autograd from scratch
- [Mathematics for Machine Learning — Chapter 5.2](https://mml-book.github.io/book/mml-book.pdf)
