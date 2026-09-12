---
tags:
  - status/seed
  - probability
related:
  - "[[sample-space-and-events]]"
  - "[[probability-fundamentals]]"
  - "[[three-methods-of-assigning-probability]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-2 (Ejemplo 10)."
---

> **TL;DR** — The **complement** $\bar{A}$ of an event is "$A$ does *not* happen." Since $A$ and $\bar{A}$ together cover the whole [[sample-space-and-events|sample space]], $P(A) + P(\bar{A}) = 1$.

---

## Intuition

Sometimes the event you care about is a mess to count directly, but its *opposite* is trivial. "At least one defect in a batch" is tangled; "zero defects" is one clean case. The complement rule lets you compute the easy side and subtract: $P(\text{at least one}) = 1 - P(\text{none})$. This "count the opposite" move is one of the most-used shortcuts in all of probability.

The rule works because $A$ and $\bar{A}$ are **exhaustive and mutually exclusive**: every outcome is in exactly one of them, so their probabilities must sum to the certainty value, 1.

## Mechanics

$$P(A) + P(\bar{A}) = 1 \quad\Longrightarrow\quad P(\bar{A}) = 1 - P(A)$$

Notation for the complement varies: $\bar{A}$, $A^c$, or $A'$ — all mean "not $A$."

**Worked — SAT guessing.** One of 5 answers (A–E) is correct, so $P(\text{correct}) = 1/5 = 0.2$. The complement:

$$P(\text{incorrect}) = 1 - P(\text{correct}) = 1 - 0.2 = 0.8$$

**Where it earns its keep** — "at least one" problems. For $n$ independent trials each with success prob $p$:

$$P(\text{at least one success}) = 1 - P(\text{no successes}) = 1 - (1-p)^n$$

Computing this directly (exactly one, exactly two, … , exactly $n$) is painful; the complement collapses it to one term.

## In ML

**Binary classification lives on the complement.** For a two-class model, $P(\text{spam}) + P(\text{ham}) = 1$, so a single sigmoid output $\hat{p}$ encodes *both* classes — the other is just $1-\hat{p}$. Binary cross-entropy loss is written directly in terms of this complement pair: $-[y\log\hat p + (1-y)\log(1-\hat p)]$.

**"At least one" reasoning appears everywhere.** Coverage probabilities, the chance a random search finds ≥1 good configuration, dropout keeping ≥1 unit active, the birthday-paradox collision bound behind hashing — all are cleanest as $1 - P(\text{none})$.

## Exercises

**Basic** — A die is rolled. Using the complement rule, find P(not a 6). Confirm it matches direct counting.

**Intermediate** — A component works with probability 0.9. In a system of 4 independent such components, what's the probability that *at least one* fails? Which side (event or complement) did you compute, and why?

**Advanced** — Show that for 23 people, P(at least two share a birthday) > 0.5, by computing the complement P(all 23 distinct) $= \frac{365}{365}\cdot\frac{364}{365}\cdots\frac{343}{365}$. Why is the complement essential here rather than direct enumeration?
