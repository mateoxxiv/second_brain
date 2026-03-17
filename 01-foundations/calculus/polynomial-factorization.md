**Related**: [[derivative-rules]], [[derivatives-and-partial-derivatives]], [[eigenvalues-and-eigenvectors]]
**Tags**: #status/growing

## Core Idea

Factorization breaks a polynomial into simpler pieces multiplied together.
Instead of solving x^2 - 5x + 6 = 0 directly, you rewrite it as
(x-2)(x-3) = 0, which immediately tells you x = 2 or x = 3.

You need this every time you solve a characteristic equation for
[[eigenvalues-and-eigenvectors]], and to simplify derivatives.

## Details

### Why Factor?

A product equals zero only when one of the pieces is zero:

```
(x - 2)(x - 3) = 0

Either x - 2 = 0  →  x = 2
Or     x - 3 = 0  →  x = 3
```

That's the whole point — turn a hard equation into easy ones.

### Method 1: Common Factor (Pull Out)

Look for something every term shares:

```
6x^2 + 9x = 3x(2x + 3)
   ↑
   both have 3x

x^3 - x^2 = x^2(x - 1)
```

Always try this first — it's the easiest.

### Method 2: Quadratic Formula

For ax^2 + bx + c = 0, the roots are:

```
x = (-b +- sqrt(b^2 - 4ac)) / 2a
```

This **always works** for degree-2 polynomials. No guessing needed.

```
x^2 - 5x + 6 = 0

a = 1, b = -5, c = 6
x = (5 +- sqrt(25 - 24)) / 2
x = (5 +- 1) / 2
x = 3 or x = 2

So: x^2 - 5x + 6 = (x - 3)(x - 2)
```

### The Discriminant

The part under the square root (b^2 - 4ac) tells you what to expect:

```
b^2 - 4ac > 0   →  two real roots (factors nicely)
b^2 - 4ac = 0   →  one repeated root (perfect square)
b^2 - 4ac < 0   →  no real roots (complex numbers)
```

This is exactly what happened with rotation matrices in [[eigenvalues-and-eigenvectors]] —
discriminant < 0, so no real eigenvalues.

### Method 3: Factor by Inspection (Guess and Check)

For x^2 + bx + c, find two numbers that:
- **Multiply** to c
- **Add** to b

```
x^2 - 5x + 6

Need: multiply to 6, add to -5
Try: -2 * -3 = 6  ✓
     -2 + -3 = -5 ✓

So: (x - 2)(x - 3)
```

```
x^2 + 7x + 12

Need: multiply to 12, add to 7
Try: 3 * 4 = 12  ✓
     3 + 4 = 7   ✓

So: (x + 3)(x + 4)
```

This is fast but only works when the numbers are nice. Use the quadratic
formula when you can't guess.

### Method 4: Difference of Squares

```
a^2 - b^2 = (a + b)(a - b)
```

```
x^2 - 9 = (x + 3)(x - 3)
x^2 - 1 = (x + 1)(x - 1)
4x^2 - 25 = (2x + 5)(2x - 5)
```

This pattern appeared in our eigenvalue calculations:

```
(2 - lambda)^2 - 1 = 0
((2-lambda) + 1)((2-lambda) - 1) = 0
(3 - lambda)(1 - lambda) = 0
lambda = 3 or lambda = 1
```

### Method 5: Perfect Square

```
a^2 + 2ab + b^2 = (a + b)^2
a^2 - 2ab + b^2 = (a - b)^2
```

```
x^2 + 6x + 9 = (x + 3)^2
x^2 - 10x + 25 = (x - 5)^2
```

### Method 6: Completing the Square

When it doesn't factor nicely, rewrite to isolate x:

```
x^2 + 6x + 2 = 0

Move constant:      x^2 + 6x = -2
Half of 6 is 3:     x^2 + 6x + 9 = -2 + 9
Perfect square:     (x + 3)^2 = 7
Square root:        x + 3 = +-sqrt(7)
Solve:              x = -3 +- sqrt(7)
```

This is actually how the quadratic formula is derived — completing the square
on ax^2 + bx + c = 0 in general.

### Quick Decision Tree

```
Can you pull out a common factor?
  YES → do it first, then continue
  NO  ↓

Is it degree 2 (quadratic)?
  YES → try inspection (find two numbers)
        if stuck → quadratic formula (always works)
  NO  ↓

Is it a special pattern?
  a^2 - b^2 → (a+b)(a-b)
  a^2 +- 2ab + b^2 → (a+-b)^2
  NO  ↓

Degree 3 or higher?
  → try pulling out common factor to reduce degree
  → for cubics, try rational root theorem or use computer
```

### Worked Example: Eigenvalue Problem

From [[eigenvalues-and-eigenvectors]], finding eigenvalues of A = [[1,2],[2,1]]:

```
det(A - lambda*I) = 0

(1-L)(1-L) - 2*2 = 0
L^2 - 2L + 1 - 4 = 0
L^2 - 2L - 3 = 0

Factor by inspection:
  multiply to -3, add to -2
  -3 * 1 = -3  ✓
  -3 + 1 = -2  ✓

(L - 3)(L + 1) = 0
L = 3 or L = -1
```

### Worked Example: Messy Quadratic

From our SVD session: L^2 - 3L + 1 = 0

```
Can't factor by inspection (no integers multiply to 1 and add to -3)

Quadratic formula:
L = (3 +- sqrt(9 - 4)) / 2
L = (3 +- sqrt(5)) / 2
L = 2.618 or L = 0.382
```

## Code Example

```python
import numpy as np

# Find roots of a polynomial
# x^2 - 5x + 6 → coefficients [1, -5, 6]
roots = np.roots([1, -5, 6])
print(roots)  # [3. 2.]

# Verify: (x-3)(x-2) = x^2 - 5x + 6
print(np.poly(roots))  # [1. -5. 6.]

# Quadratic formula
def quadratic(a, b, c):
    disc = b**2 - 4*a*c
    if disc < 0:
        return "No real roots"
    return (-b + disc**0.5)/(2*a), (-b - disc**0.5)/(2*a)

print(quadratic(1, -5, 6))     # (3.0, 2.0)
print(quadratic(1, -3, 1))     # (2.618, 0.382)
print(quadratic(1, 0, 1))      # "No real roots" (rotation matrix)
```

## Connections

- [[eigenvalues-and-eigenvectors]] — characteristic equation is a polynomial you need to factor
- [[derivatives-and-partial-derivatives]] — factoring simplifies derivative expressions
- [[determinant]] — computing determinants produces polynomials
- [[derivative-rules]] — factored form is often easier to differentiate

## Sources

- [Khan Academy — Factoring Quadratics](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring) — interactive practice
- [3Blue1Brown — Quadratic Formula](https://www.youtube.com/watch?v=M1KOzFseR-o) — visual derivation
- [Paul's Online Math Notes — Factoring](https://tutorial.math.lamar.edu/Classes/Alg/Factoring.aspx)
