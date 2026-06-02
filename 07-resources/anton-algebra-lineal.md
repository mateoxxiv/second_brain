---
tags:
  - status/seed
  - literature
  - linear-algebra
type: book
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Limusa Wiley."
date_read: "2026-05-02 (in progress)"
---

## Summary

Classic undergraduate linear algebra textbook, rigorous yet accessible. Builds from
systems of equations up through abstract vector spaces, eigenvalues, inner product
spaces, and linear transformations. Derives every result from first principles with
worked examples at each step. The Spanish edition is widely used across Latin America
as the standard introduction to the subject.

Structure: 8 core chapters progressing from concrete (matrices, determinants) to
abstract (general vector spaces, inner product spaces), with applications woven in.

**Chapter map → vault coverage:**

| Chapter | Topic                                               | Vault status                                                                                     |
| ------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 1       | Systems of equations, matrices                      | ✓ [[gaussian-elimination]], [[matrix-operations]]                                                |
| 2       | Determinants                                        | ✓ [[determinant]], [[cofactor]], [[adjugate-matrix]], [[sarrus-rule]], [[cramer-rule]]           |
| 3       | Euclidean vector spaces (dot, cross, lines, planes) | ✓ [[dot-product]], [[cross-product]], [[vector-norms]]                                           |
| 4       | General vector spaces, subspaces, basis, row/col spaces, rank | ✓ [[vectors-and-vector-spaces]], [[basis-and-dimension]], [[linear-independence]], [[row-and-column-spaces]] |
| 5       | Eigenvalues and eigenvectors                        | ✓ [[eigenvalues-and-eigenvectors]], [[spectral-decomposition]], [[singular-value-decomposition]] |
| 6       | Inner product spaces, Gram-Schmidt, QR              | gap → [[inner-product-spaces]] (to create)                                                       |
| 7       | Diagonalization, quadratic forms, Cholesky          | gap → [[quadratic-forms]] (to create)                                                            |
| 8       | Linear transformations, kernel, range               | ✓ [[linear-transformations]], [[projection]]                                                     |

## Key Takeaways

1. Every result is derived — Anton never just states formulas. Following his derivations builds the intuition that short study sessions skip.
2. Chapter 6 (inner product spaces) generalizes the dot product to abstract spaces — this is the bridge from geometric vectors to kernels and Gaussian processes in ML.
3. Chapter 7 (quadratic forms) connects directly to second-order optimization theory: Hessians, positive definite matrices, and the shape of loss surfaces.
4. The progression from Euclidean → general → inner product spaces is exactly the abstraction ladder needed before studying kernel methods and functional analysis.

## Quotes / Important Passages

> "Un espacio con producto interior es un espacio vectorial V sobre el que se ha definido una operación llamada producto interior."
> — Ch. 6, foundation of inner product spaces

## My Thoughts

Most vault notes were generated from sessions rather than reading — they are correct but sometimes miss the derivation depth Anton provides. Using this book as the primary source for the remaining linear algebra gaps (Ch. 6–7) will produce much stronger notes.

The chapter map shows linear algebra is nearly done. The two real gaps are:
- **Inner product spaces** (Ch. 6) — generalizes everything already in the vault
- **Quadratic forms** (Ch. 7) — directly supports optimization and deep learning

After finishing Anton, transition to *Mathematics for Machine Learning* (Deisenroth) for calculus and probability — it picks up exactly where Anton leaves off.

## Permanent Notes to Create

- [[inner-product-spaces]] — from Ch. 6: abstract inner products, angle, orthogonality, generalized Gram-Schmidt
- [[quadratic-forms]] — from Ch. 7: x^T A x, positive definiteness, connection to Hessians and loss surface geometry
