---
tags:
  - status/seed
  - calculus
related:
  - "[[algebraic-operation-properties]]"
  - "[[derivative-rules]]"
  - "[[polynomial-factorization]]"
  - "[[probability-distributions]]"
  - "[[probability-fundamentals]]"
domain: calculus
sources:
  - "https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs"
  - "https://mathworld.wolfram.com/Logarithm.html"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Roots are fractional exponents and logarithms are inverse exponents; all rules for all three operations follow from a single idea: exponentiation is repeated multiplication.

---

## Intuition

a² = a·a, a³ = a·a·a — exponentiation is just counting how many times you multiply. Every power rule follows from this by counting carefully. Roots undo exponentiation (√a asks "what squared gives a?" → a^(1/2)). Logarithms answer "what exponent do I need?" — so every log rule is a power rule written from the other direction.

Learn the exponent rules once; the log and root rules come for free.

## Mechanics

**Exponent rules** — all derived from counting repeated multiplications:

| Rule | Formula | Why |
|---|---|---|
| Product | $a^m \cdot a^n = a^{m+n}$ | m then n multiplications |
| Quotient | $a^m / a^n = a^{m-n}$ | cancel n factors |
| Power of power | $(a^m)^n = a^{mn}$ | n copies of a^m |
| Power of product | $(ab)^n = a^n b^n$ | distribute n multiplications |
| Zero exponent | $a^0 = 1$ | $a^n/a^n = a^{n-n}$ |
| Negative exponent | $a^{-n} = 1/a^n$ | extends zero rule |
| Fractional exponent | $a^{1/n} = \sqrt[n]{a}$ | $(a^{1/n})^n = a$ |

**Logarithm rules** — each mirrors an exponent rule:

| Rule | Formula | Mirror |
|---|---|---|
| Product | $\log(ab) = \log a + \log b$ | product rule |
| Quotient | $\log(a/b) = \log a - \log b$ | quotient rule |
| Power | $\log(a^n) = n \cdot \log a$ | power of power |
| Identity | $\log_b b = 1$ | $b^1 = b$ |
| Zero | $\log_b 1 = 0$ | $b^0 = 1$ |
| Change of base | $\log_b x = \ln x / \ln b$ | derived below |

**Root rules** (all follow from $\sqrt[n]{a} = a^{1/n}$):

$$\sqrt[n]{ab} = \sqrt[n]{a}\cdot\sqrt[n]{b} \qquad \sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}} \qquad \sqrt[n]{a^m} = a^{m/n}$$

```python
import numpy as np

a, b, m, n = 4.0, 9.0, 3.0, 2.0

assert np.isclose(a**m * a**n, a**(m+n))            # product rule
assert np.isclose((a**m)**n, a**(m*n))              # power of power
assert np.isclose((a*b)**n, a**n * b**n)            # power of product
assert np.isclose(np.log(a*b), np.log(a)+np.log(b)) # log product
assert np.isclose(np.log(a**n), n*np.log(a))         # log power
assert np.isclose(np.sqrt(a), a**0.5)                # root as exponent
```

> Runnable: [[code/foundations/exponent_log_root_properties.py]]

## In ML

**Cross-entropy and log product rule** — log(∏ pᵢ) = Σ log(pᵢ) converts a product of probabilities into a sum. This is critical: probabilities multiply to numbers near zero (underflow), but their logs sum to manageable negatives. Every likelihood-based model (logistic regression, language models) exploits this rule to avoid numerical collapse.

**Log-sum-exp trick** — softmax requires computing log(Σ eˣⁱ). For large xᵢ, eˣⁱ overflows. The power rule gives the stable form: log(Σ eˣⁱ) = c + log(Σ e^(xᵢ−c)) where c = max(xᵢ). Shifting exponents by a constant cancels out (quotient rule), leaving a numerically safe computation.

**Learning rate schedules** — exponential decay lr(t) = lr₀ · γᵗ uses the product rule: each step multiplies by γ. The power-of-power rule explains cosine and polynomial schedules. Log scale on the learning rate axis is standard because multiplicative steps look linear on a log scale.

## Exercises

**Basic** — Simplify without a calculator: (a) 2³ · 2⁴, (b) (3²)³, (c) log₂(32), (d) log(1000) − log(10).

**Intermediate** — Compute log(e^1000 + e^1001) both directly (observe overflow) and using the log-sum-exp trick with c = 1001. Verify both give the same result when possible.

**Advanced** — Derive the change of base formula log_b(x) = ln(x)/ln(b) from scratch. Start from y = log_b(x) → b^y = x, apply ln to both sides, use the power rule, and solve for y.
