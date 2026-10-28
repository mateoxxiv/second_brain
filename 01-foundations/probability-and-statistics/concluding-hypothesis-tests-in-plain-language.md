---
tags:
  - status/seed
  - probability
related:
  - "[[null-and-alternative-hypotheses]]"
  - "[[p-value]]"
  - "[[statistical-power]]"
  - "[[interpreting-confidence-intervals]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Redacción de la conclusión final; Figura 8-7; Advertencias; Ejemplo 9)"
---

> **TL;DR** — Write the conclusion as a statement about the original claim, not as "reject H0". Only one case in the table supports the claim: H0 rejected when the claim was H1.

---

## Intuition

A test result is about evidence, not about proof. Stating the conclusion in terms of the original claim keeps the reader from confusing "H0 rejected" with "the claim is proven", and from confusing "not rejected" with "the claim is disproven".

## Mechanics

Triola's Figura 8-7, simplified. Does the original claim contain equality?

| Original claim | Reject H0 | Do not reject H0 |
|---|---|---|
| Contains "=" (it is H0-like) | "There is sufficient evidence to reject the claim that…" | "There is not sufficient evidence to reject the claim that…" |
| No "=" (it became H1) | "The sample data **support** the claim that…" | "There is not sufficient sample evidence to support the claim that…" |

Only the bottom-left cell supports the original claim. For XSORT, with H1 $p > 0.5$ and H0 rejected, the conclusion is: "There is sufficient evidence to support the claim that the XSORT method increases the probability of a girl."

Rules from the text:
- Never end with "H0 is rejected" or "H0 is not rejected" on its own.
- Do not write "accept H0". Failing to reject means the evidence is not strong enough, not that H0 is shown.
- Avoid stacked negatives. The book allows up to three, but prefers rewriting. Instead of "There is not enough evidence to justify rejecting the claim that there is no difference…", write "We continue to assume the proportion is 0.5 until stronger evidence appears."

## In ML

**"Failed to reject" is not "equal"** — a model comparison with no significant difference does not show the two models are equivalent, especially if the test had low power ([[statistical-power]]).

**Plain-language reports** — stakeholders need the claim, the decision and the evidence in one sentence. Compose the sentence from the original claim, not from the test jargon.

## Exercises

**Basic** — The claim is "the mean is 195 lb" (contains "="). H0 is not rejected. Write the conclusion.

**Intermediate** — The claim is "$p > 0.5$". Write the conclusion when H0 is rejected, then when it is not.

**Advanced** — Rewrite this double-negative conclusion in plain language and check that the meaning is preserved: "We do not have insufficient evidence to reject the claim that there is no difference between 0.5 and the population proportion."
