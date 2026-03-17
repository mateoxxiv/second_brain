**Related**: [[derivatives-and-partial-derivatives]], [[chain-rule]]
**Tags**: #status/growing

## Core Idea

Derivative rules are the **toolbox** for computing derivatives. Every derivative
you'll ever need — no matter how complex — breaks down into combinations of
these rules. Learn them once, use them forever.

## Details

### 1. Power Rule

```
f(x) = x^n   →   f'(x) = n * x^(n-1)
```

Bring the exponent down, subtract 1.

```
x^2  →  2x
x^3  →  3x^2
x^5  →  5x^4
x^1  →  1
x^0  →  0        (constant)
x^(-1) → -x^(-2)  (works for negative exponents too)
x^(1/2) → (1/2)x^(-1/2)  (works for fractions — this is sqrt(x))
```

### 2. Constant Rule

```
f(x) = c   →   f'(x) = 0
```

A constant doesn't change — slope is zero.

```
f(x) = 7   →  f'(x) = 0
f(x) = -3  →  f'(x) = 0
```

### 3. Constant Multiple Rule

```
f(x) = c * g(x)   →   f'(x) = c * g'(x)
```

Constants just pass through.

```
f(x) = 5x^2   →  f'(x) = 5 * 2x = 10x
f(x) = -3x^4  →  f'(x) = -3 * 4x^3 = -12x^3
```

### 4. Sum / Difference Rule

```
f(x) = g(x) + h(x)   →   f'(x) = g'(x) + h'(x)
f(x) = g(x) - h(x)   →   f'(x) = g'(x) - h'(x)
```

Differentiate each term separately.

```
f(x) = x^3 + 2x^2 - 5x + 1

f'(x) = 3x^2 + 4x - 5
```

### 5. Product Rule

```
f(x) = g(x) * h(x)   →   f'(x) = g'(x)*h(x) + g(x)*h'(x)
```

"First times derivative of second, plus second times derivative of first."

```
f(x) = x^2 * (3x + 1)

g = x^2,       g' = 2x
h = 3x + 1,    h' = 3

f'(x) = 2x*(3x+1) + x^2*3
      = 6x^2 + 2x + 3x^2
      = 9x^2 + 2x
```

### 6. Quotient Rule

```
f(x) = g(x) / h(x)   →   f'(x) = (g'*h - g*h') / h^2
```

"Low d-high minus high d-low, over the square of what's below."

```
f(x) = x^2 / (x + 1)

g = x^2,      g' = 2x
h = x + 1,    h' = 1

f'(x) = (2x*(x+1) - x^2*1) / (x+1)^2
      = (2x^2 + 2x - x^2) / (x+1)^2
      = (x^2 + 2x) / (x+1)^2
```

### 7. Chain Rule

See [[chain-rule]] for the full note.

```
f(x) = g(h(x))   →   f'(x) = g'(h(x)) * h'(x)
```

Derivative of outer times derivative of inner.

```
f(x) = (3x+1)^4   →   f'(x) = 4(3x+1)^3 * 3 = 12(3x+1)^3
```

### 8. Exponential Rule

```
f(x) = e^x    →   f'(x) = e^x         (e^x is its own derivative!)
f(x) = e^(g(x)) → f'(x) = e^(g(x)) * g'(x)   (chain rule)
f(x) = a^x    →   f'(x) = a^x * ln(a)
```

e^x is special — it's the only function that equals its own derivative. This
is why e appears everywhere in ML (softmax, log-loss, exponential decay).

```
f(x) = e^(3x)   →  f'(x) = e^(3x) * 3 = 3e^(3x)
f(x) = e^(x^2)  →  f'(x) = e^(x^2) * 2x = 2x*e^(x^2)
```

### 9. Logarithm Rule

```
f(x) = ln(x)     →   f'(x) = 1/x
f(x) = ln(g(x))  →   f'(x) = g'(x) / g(x)    (chain rule)
f(x) = log_a(x)  →   f'(x) = 1 / (x * ln(a))
```

```
f(x) = ln(x^2 + 1)  →  f'(x) = 2x / (x^2 + 1)
f(x) = ln(3x)       →  f'(x) = 3 / (3x) = 1/x
```

### Quick Reference Table

| Rule | Formula | When to use |
|------|---------|-------------|
| Power | (x^n)' = nx^(n-1) | Polynomials |
| Constant | (c)' = 0 | Standalone numbers |
| Constant multiple | (cf)' = cf' | Coefficient in front |
| Sum/Difference | (f+g)' = f'+g' | Adding terms |
| Product | (fg)' = f'g + fg' | Multiplying functions |
| Quotient | (f/g)' = (f'g-fg')/g^2 | Dividing functions |
| Chain | (f(g))' = f'(g)*g' | Function inside function |
| Exponential | (e^x)' = e^x | Exponential growth/decay |
| Logarithm | (ln x)' = 1/x | Log-loss, information theory |

### ML-Relevant Derivatives

Functions you'll see constantly in deep learning:

```
Sigmoid:   s(x) = 1/(1+e^(-x))     →  s'(x) = s(x)*(1-s(x))
ReLU:      r(x) = max(0,x)          →  r'(x) = 0 if x<0, 1 if x>0
Tanh:      t(x) = tanh(x)           →  t'(x) = 1 - tanh(x)^2
Softmax:   complex (involves Jacobian — [[derivatives-and-partial-derivatives]])
MSE loss:  L = (y-y_hat)^2          →  dL/dy_hat = -2(y-y_hat)
Log loss:  L = -ln(y_hat)           →  dL/dy_hat = -1/y_hat
```

Notice: sigmoid's derivative is expressed in terms of itself. This makes
backpropagation efficient — you already computed s(x) in the forward pass.

## Code Example

```python
import numpy as np

# Numerical derivative for verification
def deriv(f, x, h=1e-7):
    return (f(x + h) - f(x - h)) / (2 * h)

# Power rule: x^3 → 3x^2
f = lambda x: x**3
print(deriv(f, 2.0))          # ≈ 12.0 = 3*(2^2)

# Product rule: x^2 * e^x → 2x*e^x + x^2*e^x
f = lambda x: x**2 * np.exp(x)
analytical = lambda x: 2*x*np.exp(x) + x**2*np.exp(x)
print(deriv(f, 1.0))          # ≈ 8.155
print(analytical(1.0))        # ≈ 8.155

# Chain rule: e^(x^2) → 2x*e^(x^2)
f = lambda x: np.exp(x**2)
print(deriv(f, 1.0))          # ≈ 5.437 = 2*1*e^1

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    s = sigmoid(x)
    return s * (1 - s)

print(deriv(sigmoid, 0.0))    # ≈ 0.25
print(sigmoid_deriv(0.0))     # 0.25
```

## Connections

- [[derivatives-and-partial-derivatives]] — what derivatives are and why they matter
- [[chain-rule]] — the most important rule for ML (backpropagation)
- Forward link: gradient descent — uses these rules to compute weight updates
- Forward link: activation functions — sigmoid, ReLU, tanh derivatives are critical for backprop
- Forward link: loss functions — MSE, cross-entropy derivatives drive optimization

## Sources

- [3Blue1Brown — Essence of Calculus, Ch. 3-4](https://www.3blue1brown.com/topics/calculus) — visual rules
- [Khan Academy — Derivative Rules](https://www.khanacademy.org/math/calculus-1/cs1-derivatives-definition-and-basic-rules)
- [Paul's Online Math Notes — Derivative Rules](https://tutorial.math.lamar.edu/Classes/CalcI/DerivativeProofs.aspx) — proofs of each rule
- [Mathematics for Machine Learning — Chapter 5.1](https://mml-book.github.io/book/mml-book.pdf)
