---
tags:
  - status/seed
  - literature
type: course
domain: linear-algebra
sources:
  - "https://platzi.com/cursos/algebra-lineal/"
author: "Daniel Erazo (AI Software Engineer)"
date_read: "2026-08-30 (in progress)"
---

## Summary

*Curso de Álgebra Lineal: Fundamentos y Aplicaciones* (Platzi) is a beginner, **geometry-first** tour of linear algebra in 29 short classes, motivated throughout as "the language of AI." It builds from vectors (span, dot product, norm, angle) through matrices as space transformations, linear systems (`AX=B`, column/null spaces, Gaussian elimination, Gram-Schmidt, least squares), inverses and determinants, change of basis, and finishes with eigenvectors and diagonalization. Unlike the ML-fundamentals Platzi course, it is a **math** course — no libraries, pure concept and geometric intuition.

> **Role in the vault — read this before deriving notes.** This course is an **intuition/review companion, not a source of new coverage.** The vault's `01-foundations/linear-algebra/` folder already holds 60+ rigorous notes (Anton/Strang-level: proofs, derivations, general vector spaces) that cover essentially *every* class here at greater depth. So it **originates almost no permanent notes** — every class below maps to an *existing* deeper note, with rare exceptions where a class exposes a genuinely missing *atomic angle* (e.g. Class 2's geometric point-vs-arrow reading, which the "forget arrows" [[vectors-and-vector-spaces]] deliberately skips). Its real value is threefold: (1) **geometric intuition** — the "matrix as a transformation of space," 3Blue1Brown-style framing that makes the algebra visual; (2) a **fast review pass** over the whole track; (3) the explicit **"language of AI" motivation** connecting each concept forward to ML/DL. For rigor and proofs, stay with the textbook-derived notes; for *seeing* it, use this. Pair with **3Blue1Brown's *Essence of Linear Algebra*** (the definitive visual companion) and **Strang's *Linear Algebra and Its Applications*** for depth.

---

## Chapter / Class Map

| Module | Class | Topic | Vault notes |
|---|---|---|---|
| 1 — Vectores | 1 | Linear algebra as the language of AI | *(motivational)* |
| | 2 | What a vector is; graphing it | [[geometric-interpretation-of-a-vector]], [[vectors-and-vector-spaces]], [[vector-operations]] |
| | 3 | Add/subtract/scale vectors geometrically | [[vector-operations]] |
| | 4 | Linear combinations and span | [[linear-combination]] |
| | 5 | What makes a vector redundant | [[linear-independence]] |
| | 6 | Dot product: measuring alignment | [[dot-product]] |
| | 7 | Vector norm via Pythagoras | [[vector-norms]] |
| | 8 | Angle between vectors from the dot product | [[angles-and-orthogonality]] |
| 2 — Matrices | 9 | What a matrix is; how to read it | [[what-is-a-matrix]] |
| | 10 | Element-wise add/subtract | [[matrix-operations]] |
| | 11 | Matrices as transformations of space | [[linear-transformations]], [[matrix-of-linear-transformation]] |
| | 12 | Matrix multiplication as composition | [[matrix-operations]], [[linear-transformations]] |
| | 13 | Transposition for multiplication | [[matrix-operations]] |
| 3 — Linear systems | 14 | Systems in matrix form `AX=B` | [[planes-as-linear-systems]] |
| | 15 | Column space vs. null space in `Ax=b` | [[row-and-column-spaces]], [[kernel-and-range]] |
| | 16 | Orthogonality of row and null spaces | [[row-and-column-spaces]], [[angles-and-orthogonality]] |
| | 17 | Gaussian elimination | [[gaussian-elimination]] |
| | 18 | Rank and nullity | [[rank-nullity-theorem]] |
| | 19 | Diagnosing a system without solving it | [[rank-nullity-theorem]], [[determinant]] |
| | 20 | Orthogonal projection for inconsistent systems | [[projection-onto-subspaces]], [[projection]] |
| | 21 | Gram-Schmidt: skewed basis → orthonormal | [[gram-schmidt]], [[orthonormal-bases]] |
| | 22 | Least squares for imperfect data | [[least-squares]], [[projection-onto-subspaces]] |
| 4 — Inverses & determinants | 23 | The matrix inverse | [[matrix-inverse]] |
| | 24 | What the determinant means | [[determinant]] |
| | 25 | Zero determinant → no inverse | [[determinant]], [[matrix-inverse]] |
| 5 — Change of basis | 26 | Change of basis between coordinate systems | [[change-of-basis]], [[coordinate-vector]] |
| 6 — Eigen & diagonalization | 27 | Eigenvectors: vectors that resist transformation | [[eigenvalues-and-eigenvectors]] |
| | 28 | Computing eigenvalues via determinants | [[eigenvalues-and-eigenvectors]] |
| | 29 | Diagonalization with eigenvectors | [[diagonalization]] |

---

## All Topics at a Glance

**Module 1 — Vectors**
- [[geometric-interpretation-of-a-vector]] — *(created)* the point-vs-arrow dual reading, direction/magnitude, graphing in $\mathbb{R}^n$
- [[vectors-and-vector-spaces]] — a vector as a list of data and the space it lives in (closure, axioms)
- [[vector-operations]] — geometric add, subtract, scalar multiply
- [[linear-combination]] — scaled sums of vectors; span as everything reachable
- [[linear-independence]] — when a vector adds nothing new (redundancy)
- [[dot-product]] — alignment measure; sign tells same/opposite direction
- [[vector-norms]] — length via Pythagoras; the $\ell_2$ norm
- [[angles-and-orthogonality]] — angle from the dot product; perpendicular ⇔ zero dot

**Module 2 — Matrices**
- [[what-is-a-matrix]] — grid of numbers, rows × columns, how to index it
- [[matrix-operations]] — element-wise add/subtract, transpose, multiplication
- [[linear-transformations]] — the key reframe: a matrix *is* a transformation of space
- [[matrix-of-linear-transformation]] — columns as images of the basis vectors

**Module 3 — Linear systems**
- [[planes-as-linear-systems]] — `AX=B` as intersecting constraints
- [[row-and-column-spaces]] — column space (reachable outputs) vs. null space
- [[kernel-and-range]] — what maps to zero, what gets hit
- [[gaussian-elimination]] — row reduction to solve systems
- [[rank-nullity-theorem]] — dim(range) + dim(kernel) = n; solvability diagnosis
- [[projection]], [[projection-onto-subspaces]] — nearest point in a subspace
- [[gram-schmidt]] — orthonormalizing a skewed basis
- [[orthonormal-bases]] — bases where the math simplifies
- [[least-squares]] — best fit when `Ax=b` has no exact solution *(gap)*

**Module 4 — Inverses & determinants**
- [[matrix-inverse]] — the undo transformation
- [[determinant]] — signed volume scale factor; zero ⇒ collapse ⇒ non-invertible

**Module 5 — Change of basis**
- [[change-of-basis]] — re-expressing vectors in another coordinate system
- [[coordinate-vector]] — a vector's coordinates *relative to* a basis

**Module 6 — Eigen & diagonalization**
- [[eigenvalues-and-eigenvectors]] — directions preserved by a transformation, scaled by λ
- [[diagonalization]] — rewriting a matrix in its eigenbasis where it acts as pure scaling

---

## Key Takeaways

1. **A matrix is a transformation, not a table** — the course's spine (Class 11) is reframing matrices as *actions on space*; multiplication is composition, the determinant is a volume scale, eigenvectors are the directions that survive. This geometric lens is the whole point.
2. **Everything routes through span and the dot product** — linear combinations/span (what's reachable) and the dot product (alignment/angle/projection) are the two primitives the rest is built on.
3. **Solving `Ax=b` is a geometry question** — column space (is `b` reachable?), null space (how many solutions?), and rank answer solvability *before* you compute; when `b` is unreachable, projection → least squares gives the best approximation.
4. **Eigen-decomposition is the payoff** — diagonalization finds the basis where a transformation is pure scaling, the foundation for PCA, PageRank, and stability analysis downstream.
5. **It's motivation-first for AI** — every concept is pitched as machinery for ML; the value here is *intuition and connection*, deliberately trading proof-level rigor for visual understanding.

## Quotes / Important Passages

> *(Course in progress — quotes/timestamps to be added as classes are watched.)*

## My Thoughts

The honest read: this course teaches me almost **nothing new** — the vault already has deeper, proof-backed notes for every class, derived from a rigorous textbook track. Its value is orthogonal to coverage: it's a **geometric-intuition and review layer**. The single most useful reframe it drills is *matrix = transformation of space* (Class 11), the same insight 3Blue1Brown built a series on — and if I want that visually, **3Blue1Brown's *Essence of Linear Algebra*** does it better and free. Where this course genuinely helps is as a **fast confidence check**: watch a class, and if the existing note feels obvious, that concept is solid; if not, the note needs a revisit. The one thin spot in my vault it exposed is a dedicated **[[least-squares]]** note — Class 22 (`mínimos cuadrados`) is currently only implicit inside [[projection-onto-subspaces]], and least squares is load-bearing enough for ML (it *is* linear regression's normal equations) to deserve its own atomic note. Next: for the *why*, Strang's lectures (MIT 18.06) and Axler's *Linear Algebra Done Right* for the proof-first treatment.

---

## Permanent Notes Created

- [[geometric-interpretation-of-a-vector]] — from Class 2: the point-vs-arrow dual reading, direction + magnitude, and graphing in $\mathbb{R}^n$ — the geometry that [[vectors-and-vector-spaces]] deliberately omits
- [[least-squares]] — from Class 22 (`mínimos cuadrados`): the overdetermined-system framing and normal equations $A^\top A\hat{x}=A^\top b$, split out from [[projection-onto-subspaces]] (which keeps the optimality proof) and linked forward to [[linear-regression]]

## Gaps — Notes Still to Create

- *(None outstanding — the two atomic angles this course exposed beyond the existing corpus are now written.)*
