---
tags:
  - status/seed
  - calculus
related:
  - "[[algebraic-operation-properties]]"
  - "[[exponent-log-root-properties]]"
  - "[[linear-independence]]"
  - "[[derivative-rules]]"
domain: calculus
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal."
  - "https://www.khanacademy.org/math/trigonometry"
---

> **TL;DR** — All trig identities derive from sin²x + cos²x = 1 and the angle addition formulas — everything else is algebraic manipulation of those two facts.

---

## Intuition

sin and cos are coordinates of a point on the unit circle (radius 1). The Pythagorean theorem applied to that circle gives sin²x + cos²x = 1 — this is the root identity. Every other identity is a consequence of rotating that circle or combining two angles.

## Mechanics

**Pythagorean (root identity):**

| Identity | Derived from |
|---|---|
| sin²x + cos²x = 1 | unit circle + Pythagorean theorem |
| 1 + tan²x = sec²x | divide above by cos²x |
| 1 + cot²x = csc²x | divide above by sin²x |

**Half-angle (power reduction) — most used in linear algebra:**

```
sin²x = (1 - cos 2x) / 2
cos²x = (1 + cos 2x) / 2
```

Derived from cos 2x = cos²x - sin²x → substitute sin²x = 1 - cos²x.

**Angle addition:**

```
sin(a+b) = sin a cos b + cos a sin b
cos(a+b) = cos a cos b - sin a sin b
```

**Double angle (set b = a in angle addition):**

```
sin 2x = 2 sin x cos x
cos 2x = cos²x - sin²x = 1 - 2sin²x = 2cos²x - 1
```

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)

# Pythagorean
assert np.allclose(np.sin(x)**2 + np.cos(x)**2, 1)

# Power reduction
assert np.allclose(np.sin(x)**2, (1 - np.cos(2*x)) / 2)
assert np.allclose(np.cos(x)**2, (1 + np.cos(2*x)) / 2)

# Double angle
assert np.allclose(np.sin(2*x), 2*np.sin(x)*np.cos(x))
assert np.allclose(np.cos(2*x), np.cos(x)**2 - np.sin(x)**2)
```

> Runnable: [[code/foundations/trigonometric_identities.py]]

## In ML

**Linear independence of function spaces** — the Pythagorean identity is why {2, 4sin²x, cos²x} is dependent and {cos 2x, sin²x, cos²x} is dependent. See [[linear-independence]].

**Positional encoding (Transformers)** — BERT and GPT encode token position using sin(pos/10000^(2i/d)) and cos(pos/10000^(2i/d)). The orthogonality of sin/cos at different frequencies guarantees these encodings are linearly independent across positions.

**Fourier transforms** — any signal decomposes into sin/cos components. The double angle and product formulas are the algebraic engine behind fast Fourier transforms (FFT) used in audio, image, and time-series ML.

## Exercises

**Basic** — Use the Pythagorean identity to show that {4sin²x, 4cos²x, 1} is linearly dependent in the function space V. Find c₁, c₂, c₃.

**Intermediate** — Show that {sin²x, cos²x} is linearly independent, but {sin²x, cos²x, 1} is dependent. What changes when you add 1?

**Advanced** — Prove that {1, cos x, cos 2x, cos 3x, ..., cos nx} is linearly independent in V. (Hint: evaluate at strategic x values to force each coefficient to zero.)
