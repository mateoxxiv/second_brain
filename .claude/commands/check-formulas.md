Audit the formulas in: $ARGUMENTS

The scope can be a single note path, a folder (e.g. `01-foundations/linear-algebra`), or `all`. If no scope is given, ask the user which one.

**This is a diagnosis only. Do NOT edit any note until the user approves the fixes.**

## 1. Find the notes with math

- Resolve the scope to a list of `.md` files. For `all`, use folders `01-` through `06-`.
- Keep only notes that contain math: LaTeX (`$...$`, `$$...$$`), inline formulas (`=`, `≤`, `Σ`, `√`), or code snippets that compute something.
- Skip notes where `=` only appears in config or non-mathematical code (API and tooling notes).
- Tell the user how many notes are in scope before starting.

## 2. Check every note rigorously

Read each note in full (not excerpts) and check all of the following:

1. **Formulas.** Is every formula correct? Watch for:
   - swapped conditionals (P(A)·P(A|B) instead of P(A)·P(B|A))
   - a missing factor (A(AᵀA)⁻¹Aᵀ written as (AᵀA)⁻¹Aᵀ)
   - norm bars used where absolute value is meant (‖k‖ instead of |k|)
   - wrong signs, exponents, or complexity orders
2. **Worked examples.** Recompute every number by hand. Re-run anything non-trivial in Python via Bash (numpy/scipy), including matrix products, solves, eigenvalues, distribution probabilities, and simulations with a fixed seed.
3. **Code snippets.** Would each snippet run? Look for undefined names and bad imports. Do the comments (`# 0.3`, `# [1, 3]`) match the actual output? Is each check testing the right thing (e.g. the triangle inequality compared against a sum, not a product)?
4. **Conditions and domains.** Does each theorem or definition state all its hypotheses? Examples:
   - x ≠ 0 in positive-definiteness
   - a nonempty set in the subspace test
   - a, b > 0 in log rules
   - strict convexity for a unique minimum
   - "at most one root", not "no roots"
5. **Derivations.** Does each step follow? Does the proof use only the axioms it claims to use?
6. **Claims in "In ML".** Are factual statements about algorithms, architectures, and libraries accurate (e.g. attention ≠ cosine similarity, BERT uses learned positions)?
7. **Cross-note consistency.** Do notation, counts ("10 axioms" vs "8"), and theorem numbers agree with the other vault notes on the same topic? Do they agree with the source cited in `sources`?

Be strict but honest. Only report something as an error if you can show why it is wrong (a counterexample, a recomputed value, or a derivation). Don't flag stylistic choices.

## 3. Report

Group the findings by severity, most serious first. Link each item as `[file.md:line](path:line)` with a one-line "what's wrong → correct version":

1. **Wrong formula or wrong result.** Fix these first.
2. **Theorem or definition missing a condition.**
3. **Wrong conceptual or ML claim.**
4. **Code bugs and small slips** (notation, stale comments, inconsistencies).

End with:
- a one-line **Clean** summary of the notes that passed
- the values you verified numerically
- anything you could not verify (e.g. theorem numbers that need the book)

Follow CLAUDE.md in the chat: plain-text math (no LaTeX), a Socratic check question, and the 📝 Lang block.

## 4. Fix only on approval

Ask whether to apply the fixes. When the user approves:
- Apply sections 1 and 4 directly.
- Show the proposed wording for sections 2 and 3 before editing, since those involve wording choices.
- Re-run the numeric checks after editing.
- Commit only the files you fixed, with the message `fix formulas found in audit: <scope>`.
