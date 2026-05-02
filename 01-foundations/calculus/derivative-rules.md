---
tags:
  - status/growing
  - calculus
related:
  - "[[derivatives-and-partial-derivatives]]"
  - "[[chain-rule]]"
domain: calculus
sources:
  - "https://www.3blue1brown.com/topics/calculus"
  - "https://www.khanacademy.org/math/calculus-1"
  - "https://tutorial.math.lamar.edu/Classes/CalcI/DerivativeProofs.aspx"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — The derivative rules are a toolbox: power, product, quotient, chain, exp, log. Master these and you can differentiate any function in ML.

---

## Intuition

Differentiation from the limit definition is always correct but tedious. The rules are shortcuts derived once, applied forever. For ML you need specifically: power rule (polynomials), chain rule (compositions), and the derivatives of exp/log/sigmoid/ReLU (for activations and loss functions).

## Mechanics

| Rule | Formula | Example |
|------|---------|---------|
| Power | d/dx[xⁿ] = nxⁿ⁻¹ | d/dx[x³] = 3x² |
| Constant | d/dx[c] = 0 | d/dx[5] = 0 |
| Product | d/dx[f·g] = f'g + fg' | d/dx[x·eˣ] = eˣ + xeˣ |
| Quotient | d/dx[f/g] = (f'g − fg')/g² | derives sigmoid |
| Chain | d/dx[g(h)] = g'(h)·h' | see [[chain-rule]] |
| Exponential | d/dx[eˣ] = eˣ | self-derivative |
| Logarithm | d/dx[ln x] = 1/x | d/dx[ln x²] = 2/x |

**ML-critical derivatives:**
- Sigmoid: σ'(x) = σ(x)(1 − σ(x)) — evaluate once in forward pass, reuse in backward
- ReLU: ReLU'(x) = 1 if x > 0, else 0 — undefined at x = 0
- tanh: tanh'(x) = 1 − tanh²(x)
- MSE: d/dŷ[(y − ŷ)²] = −2(y − ŷ)
- Log-loss: d/dŷ[−y·ln(ŷ)] = −y/ŷ

```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)   # computed from forward-pass output — no extra work

# Numerical verification: difference should be < 1e-6
h = 1e-5
x = 1.5
numerical = (sigmoid(x + h) - sigmoid(x - h)) / (2 * h)
analytic  = sigmoid_derivative(x)
print(f"Numerical: {numerical:.8f}, Analytic: {analytic:.8f}")
```

> Runnable: [[code/foundations/derivative_rules.py]]

## In ML

**Sigmoid derivative and backprop efficiency.** The sigmoid derivative σ(x)(1−σ(x)) is expressed in terms of σ(x), which was already computed in the forward pass. Backprop reuses it for free — this matters when differentiating millions of activations per batch.

**The dead neuron problem.** ReLU's derivative is 0 for all x < 0. If a neuron always receives negative input, its gradient is permanently zero and it never updates. Careful weight initialization and learning rate choice prevent this.

**Log-loss gradient.** The derivative of −y·ln(ŷ) is −y/ŷ. When ŷ ≈ 0 and y = 1 (confidently wrong), the gradient is very large — the model gets a strong corrective signal automatically.

## Exercises

**Basic** — Differentiate f(x) = x³ · eˣ using the product rule. Show all steps.

**Intermediate** — Derive the sigmoid derivative σ'(x) = σ(x)(1−σ(x)) from scratch using the quotient rule on σ(x) = 1/(1 + e^{−x}).

**Advanced** — Find all points where the ReLU derivative is undefined and explain why this causes no problem in practice for gradient-based optimization (hint: think about measure zero and floating-point representation).
