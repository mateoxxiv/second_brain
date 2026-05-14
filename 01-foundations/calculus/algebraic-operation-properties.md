---
tags:
  - status/seed
  - calculus
related:
  - "[[general-vector-spaces]]"
  - "[[polynomial-factorization]]"
  - "[[derivative-rules]]"
  - "[[exponent-log-root-properties]]"
domain: calculus
sources:
  - "https://www.khanacademy.org/math/algebra"
  - "Anton, Howard. Introducción al Álgebra Lineal."
---

> **TL;DR** — Commutativity, associativity, distributivity, identity, and inverse are the five rules that govern + and ×; they are the same rules that define a [[general-vector-spaces|vector space]], so mastering them unlocks both algebra and abstract linear algebra at once.

---

## Intuition

When you write 3 + 5 = 5 + 3 you're using commutativity. When you write 2 × (3 + 4) = 6 + 8 you're using distributivity. These feel obvious for numbers, but they are *rules* that numbers happen to satisfy — not inevitable truths. Mathematicians package them as axioms precisely because other systems (matrices, functions, polynomials) satisfy some but not others.

This is why the [[general-vector-spaces|vector space axioms]] look familiar: axioms 2, 3, 4, 5, 7, 8 are exactly these five properties applied to vector addition and scalar multiplication.

## Mechanics

| Property | Addition | Multiplication |
|---|---|---|
| Commutativity | a + b = b + a | a · b = b · a |
| Associativity | (a+b)+c = a+(b+c) | (a·b)·c = a·(b·c) |
| Distributivity | a·(b+c) = a·b + a·c | — (bridges + and ×) |
| Identity | a + 0 = a | a · 1 = a |
| Inverse | a + (−a) = 0 | a · (1/a) = 1, a ≠ 0 |
| Absorption | a · 0 = 0 | — |

**Distributivity is the bridge** — all other properties are self-contained within one operation; distributivity is the only rule that links + and × together.

```python
a, b, c = 3, 5, 7

assert a + b == b + a                        # commutativity +
assert a * b == b * a                        # commutativity ×
assert (a + b) + c == a + (b + c)           # associativity +
assert (a * b) * c == a * (b * c)           # associativity ×
assert a * (b + c) == a * b + a * c        # distributivity
assert a + 0 == a and a * 1 == a           # identities
assert a + (-a) == 0 and a * (1/a) == 1   # inverses
```

> Runnable: [[code/foundations/algebraic_operation_properties.py]]

## In ML

**Vector space foundation** — axioms 2, 3, 4, 5 in [[general-vector-spaces]] are commutativity, associativity, identity, and inverse for vector addition. Axioms 7 and 8 are distributivity linking scalar multiplication to addition. Proving a set satisfies these properties certifies it as a vector space.

**Gradient computation** — backpropagation relies on distributivity. The gradient of a sum distributes: ∇(L₁ + L₂) = ∇L₁ + ∇L₂. This lets you compute gradients per-sample and sum them, or split the computation graph.

**Floating-point trap** — associativity of + breaks in hardware: `(a + b) + c ≠ a + (b + c)` due to rounding. Libraries use pairwise summation and Kahan summation to control the order of additions and minimize accumulated error.

## Exercises

**Basic** — Expand (x + 2)(x − 3) using distributivity step by step. Show each application of the rule explicitly.

**Intermediate** — Check which properties matrix multiplication satisfies. For 2×2 matrices A, B, C: verify associativity A(BC) = (AB)C, verify distributivity A(B+C) = AB+AC, and find a counterexample showing AB ≠ BA.

**Advanced** — Prove the additive inverse is unique using only commutativity and associativity: assume u has two inverses v and w, both satisfying u + v = 0 and u + w = 0. Derive v = w without using any other property.
