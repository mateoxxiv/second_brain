---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[eigenvalues-and-eigenvectors]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §6.1 — técnica de división para factorizar la ecuación característica."
---

> **TL;DR** — Synthetic division is a compact shortcut for dividing a polynomial by (λ−r): a row of coefficients replaces the full long-division tableau, and the last number tells you the remainder instantly.

---

## Intuition

Once you've found one root r of a characteristic polynomial (via the rational root theorem), you still need to divide it out to shrink the polynomial and find the remaining roots. Full polynomial long division works, but it's slow — you rewrite entire polynomial expressions at every step. Synthetic division strips away everything except the *numbers* (the coefficients), turning the same computation into a few rows of arithmetic.

## Mechanics

**Setup**: write only the dividend's coefficients (include 0 for any missing power of λ), and the root r you're dividing by.

**Algorithm**: bring down the first coefficient; then repeatedly multiply the last number written by r and add it to the next coefficient.

**Worked example** — dividing $\lambda^3-8\lambda^2+17\lambda-4$ by $(\lambda-4)$:

```
4 |  1   -8    17    -4
  |      4    -16     4
  |__________________
     1   -4     1     0
```

Bottom row reads off the answer directly: coefficients **1, -4, 1** give the quotient $\lambda^2-4\lambda+1$, and the final **0** is the remainder (confirming λ=4 really is a root).

**Why it works** — it's the compact version of matching coefficients directly. Writing the quotient as $a\lambda^2+b\lambda+c$ and expanding $(\lambda-4)(a\lambda^2+b\lambda+c)$ forces $a=1$, then $b=-8+4a$, then $c=17+4b$, checked by $-4c=-4$ — exactly the "multiply by r, add" steps above, just without rewriting full polynomial terms each round.

**Bonus — the Remainder Theorem**: synthetic division's last number always equals $p(r)$, even when r is *not* a root. That means you can use synthetic division to **test candidate roots too** (from the rational root theorem's list), not just to divide once you've found one — it's a faster way to evaluate $p(r)$ than substituting directly into the full polynomial, especially for degree 4+.

```python
def synthetic_division(coeffs: list[float], root: float) -> tuple[list[float], float]:
    result = [coeffs[0]]
    for c in coeffs[1:]:
        result.append(result[-1] * root + c)
    return result[:-1], result[-1]   # quotient coefficients, remainder

quotient, remainder = synthetic_division([1, -8, 17, -4], 4)
print(quotient, remainder)   # [1, -4, 1], 0
```

## In ML

**Deflation in eigenvalue algorithms** — numerical eigensolvers (e.g. within the QR algorithm) use a conceptually identical idea called *deflation*: once an eigenvalue is found, it's removed and the problem shrinks to a smaller matrix for finding the rest, mirroring synthetic division's root-then-reduce pattern, just done numerically on matrices instead of symbolically on polynomials.

**Why hand computation still matters** — for the small, integer-friendly matrices common in coursework and unit tests, synthetic division is the practical way to get exact eigenvalues by hand; real ML pipelines never do this (`np.linalg.eig` uses iterative numerical methods), but the by-hand fluency builds the intuition for what those numerical methods are approximating.

## Exercises

**Basic** — Use synthetic division to divide $\lambda^3-6\lambda^2+11\lambda-6$ by $(\lambda-1)$. Confirm the remainder is 0 and identify the resulting quadratic.

**Intermediate** — For $p(\lambda)=\lambda^3+2\lambda^2-5\lambda-6$, use the rational root theorem to list candidates, then use synthetic division itself (via the Remainder Theorem) to test each candidate instead of direct substitution. Find all three roots.

**Advanced** — Prove the Remainder Theorem: show that for any polynomial $p(\lambda)$ and any r, $p(\lambda) = (\lambda-r)Q(\lambda) + p(r)$. (Hint: start from the division algorithm's guarantee that $p(\lambda)=(\lambda-r)Q(\lambda)+R$ for some constant R, then evaluate both sides at $\lambda=r$.)
