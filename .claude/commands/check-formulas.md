Audit the formulas and concepts in: $ARGUMENTS

The scope can be a single note path, a folder (e.g. `01-foundations/linear-algebra`), or `all`. If no scope is given, ask the user which one.

**This is a diagnosis only. Do NOT edit any note until the user approves the fixes.**

The standard is **rigor, not plausibility**. A formula or concept passes only when you have *evidence* that it is right. "Looks familiar" is not evidence. When in doubt, verify.

## 1. Find the notes with math

- Resolve the scope to a list of `.md` files. For `all`, use folders `01-` through `06-`.
- Keep notes that contain math (LaTeX, inline formulas, computing code) **or** that define concepts. Concepts get checked too, not just formulas.
- Skip notes where `=` only appears in config or non-mathematical code (API and tooling notes).
- Tell the user how many notes are in scope before starting.

## 2. Verify every claim with evidence

Read each note in full, never in excerpts. For every formula, definition, theorem, and worked example, apply the checks below.

### 2a. Formulas: derive first, then compare

- **Derive independently.** Derive or recall the formula from first principles *before* comparing it with the note. Don't let the note's version anchor you.
- **Verify symbolically with SymPy** (via Bash) whenever it's feasible: identities, derivatives, integrals, expansions, matrix identities. `sympy.simplify(lhs - rhs) == 0` is proof; a quick glance is not.
- **Randomized test.** Evaluate both sides at several random inputs with NumPy (random matrices, random probabilities). A single mismatch disproves the formula.
- **Edge cases and limits.** Plug in special values: n = 1, p = 0 or 1, x = 0, identity matrix, zero vector, k → ∞. Check that the formula reduces to known special cases (e.g. Binomial with n = 1 → Bernoulli; hypergeometric with N → ∞ → binomial).
- **Consistency checks.**
  - Dimensions and units match on both sides.
  - Probabilities stay in [0, 1] and sum to 1.
  - Variances are ≥ 0.
  - Matrix shapes are compatible.
  - Signs are right.
  - Complexity orders multiply correctly.
- **Common failure patterns to hunt for:**
  - swapped conditionals (P(A)·P(A|B) instead of P(A)·P(B|A))
  - a missing factor (A(AᵀA)⁻¹Aᵀ written as (AᵀA)⁻¹Aᵀ)
  - ‖·‖ used where |·| is meant
  - an off-by-one error (n vs. n−1)
  - a wrong exponent or sign

### 2b. Concepts and definitions: match the canonical source

- **Compare every definition and theorem statement with an authoritative reference.** Use them in this order:
  1. The book cited in the note's `sources`, via its literature note in `07-resources/`.
  2. A standard textbook: Anton, Strang, Triola, Blitzstein & Hwang, ISLR/ESL, Goodfellow, or MML.
  3. WebSearch/WebFetch of reputable pages: Wikipedia, MathWorld, Stanford, MIT OCW, official library docs.
- **Hypotheses.** Does each theorem state *all* its conditions? Examples:
  - x ≠ 0 and symmetry in positive-definiteness
  - a nonempty set in the subspace test
  - a, b > 0 in log rules
  - strict convexity plus existence for a unique minimum
  - centering before PCA variances
- **Intuition sections.** Is the analogy actually faithful to the math, or does it imply something false (e.g. "same direction" when opposite directions also qualify)?
- **Terminology.** Is each term used in its standard meaning? For example, cosine *distance* is not a metric, and L1 is not L0.

### 2c. Worked examples and code

- **Recompute every number.** Re-run anything non-trivial in Python: solves, eigenvalues, probabilities, simulations (seeded).
- **Run code snippets** (or trace them exactly). Check for undefined names and bad imports, and check that output comments like `# 0.3` match the real output.
- **Check that each check tests the right thing** (e.g. the triangle inequality compared against a sum, not a product).

### 2d. Derivations and proofs

- Check each step. Does it follow? Does the proof use only the axioms or facts it claims to?
- Look for circularity: using the result to prove itself.

### 2e. "In ML" claims

- Verify factual claims about algorithms, architectures, and libraries against papers or official docs. Examples: attention uses unnormalized dot products; BERT uses learned positions; LAPACK uses Schur, not Jordan.

### 2f. Cross-note consistency

- Notation, counts ("10 axioms" vs. "8"), and theorem numbers must agree across vault notes on the same topic and with the cited source.

## 3. Confidence rule

Label every finding with one of:

- **Verified error:** shown by a counterexample, a recomputed value, a symbolic check, or a quoted reference. Report the evidence.
- **Likely error:** strong reasoning, but no independent confirmation. Say what would confirm it.
- **Unverifiable:** needs the physical book or information you can't access (e.g. theorem numbers). Say what the user should check.

A note is **clean** only if every formula and concept in it passed a check. Don't report stylistic preferences as errors.

## 4. Report

Group the findings by severity, most serious first. Link each item as `[file.md:line](path:line)` with "what's wrong → correct version", its confidence label, and the evidence in one line:

1. **Wrong formula or wrong result.**
2. **Theorem or definition missing a condition.**
3. **Wrong concept, intuition, or ML claim.**
4. **Code bugs and small slips** (notation, stale comments, inconsistencies).

End with:
- a one-line **Clean** summary
- the values and identities you verified (and how: SymPy, NumPy, or a reference)
- the unverifiable items

Follow CLAUDE.md in the chat: plain-text math (no LaTeX), a Socratic check question, and the 📝 Lang block.

## 5. Fix only on approval

Ask whether to apply the fixes. When the user approves:
- Apply sections 1 and 4 directly.
- Show the proposed wording for sections 2 and 3 before editing.
- After editing, **re-run the same symbolic and numeric checks** on the corrected versions to confirm that the fixes are right.
- Commit only the files you fixed, with the message `fix formulas found in audit: <scope>`.
