---
tags:
  - status/growing
  - calculus
related:
  - "[[derivative-rules]]"
  - "[[derivatives-and-partial-derivatives]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[determinant]]"
domain: calculus
sources:
  - "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring"
  - "https://www.youtube.com/watch?v=M1KOzFseR-o"
  - "https://tutorial.math.lamar.edu/Classes/Alg/Factoring.aspx"
---

> **TL;DR** — Break a polynomial into (x−r1)(x−r2)... to find roots. Needed for characteristic equations in eigenvalue problems.

---

## Intuition

A product equals zero only when at least one factor is zero: (x−2)(x−3) = 0 means x = 2 or x = 3. Factoring converts a hard equation (solve this polynomial) into easy equations (set each factor to zero).

You need this every time you solve the characteristic equation det(A − λI) = 0 to find eigenvalues, since that equation is always a polynomial in λ.

## Mechanics

**Quadratic formula** — always works for ax² + bx + c = 0:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Discriminant** b² − 4ac:
- > 0: two real roots
- = 0: one repeated root
- < 0: no real roots (complex eigenvalues — rotation matrices)

**Notable products (expand ↔ factor both ways):**

| Expanded | Factored |
|---|---|
| a² + 2ab + b² | (a+b)² |
| a² − 2ab + b² | (a−b)² |
| a² − b² | (a+b)(a−b) |
| a³ + 3a²b + 3ab² + b³ | (a+b)³ |
| a³ − 3a²b + 3ab² − b³ | (a−b)³ |
| a³ + b³ | (a+b)(a²−ab+b²) |
| a³ − b³ | (a−b)(a²+ab+b²) |

**Other methods (in order of preference):**

1. Pull out common factor: 6x² + 9x = 3x(2x + 3)
2. Inspect: find two numbers that multiply to c and add to b
3. Notable products — recognize the pattern from the table above
4. Completing the square: x² + bx + c = (x + b/2)² − (b/2)² + c

```python
import numpy as np

# Find roots of any polynomial via numpy
# x^2 - 5x + 6 → coefficients [1, -5, 6]
roots = np.roots([1, -5, 6])
print(roots)           # [3.  2.]
print(np.poly(roots))  # [1. -5.  6.]  — verify factors

def quadratic(a, b, c):
    disc = b**2 - 4*a*c
    if disc < 0:
        return "No real roots"
    return (-b + disc**0.5)/(2*a), (-b - disc**0.5)/(2*a)

print(quadratic(1, -5, 6))   # (3.0, 2.0)
print(quadratic(1, -3, 1))   # (2.618, 0.382)
print(quadratic(1, 0, 1))    # No real roots (rotation matrix)
```

> Runnable: [[code/foundations/polynomial_factorization.py]]

## In ML

**Characteristic equation for eigenvalues.** Finding eigenvalues of A requires solving det(A − λI) = 0, which is a degree-n polynomial in λ. Factoring it gives the eigenvalues. For 2×2 matrices, this is a quadratic you solve by inspection or the quadratic formula.

**Factoring simplifies derivatives.** Factored form is often easier to differentiate than expanded form. (x−2)(x−3) differentiated with the product rule is cleaner than x²−5x+6 differentiated term by term, especially for higher degrees.

**Discriminant < 0 → no real eigenvalues.** Rotation matrices have characteristic equations with negative discriminant — their eigenvalues are complex. This confirms that rotations have no fixed directions (no real eigenvectors), which is geometrically correct.

## Exercises

**Basic** — Factor x² − 7x + 12 by inspection. Find two numbers that multiply to 12 and add to −7.

**Intermediate** — Use the quadratic formula on x² − 3x + 1. Then verify numerically with np.roots.

**Advanced** — Show that a 2D rotation matrix R(θ) has no real eigenvalues for θ ≠ 0, π. Compute the characteristic polynomial and evaluate its discriminant.
