---
tags:
  - status/seed
  - probability
related:
  - "[[sample-space-and-events]]"
  - "[[complementary-events]]"
  - "[[probability-fundamentals]]"
  - "[[three-methods-of-assigning-probability]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-3 (Ejemplos 1–3)."
---

> **TL;DR** — The **addition rule** finds $P(A \text{ or } B)$: add the ways each event can happen, but **subtract the overlap** so shared outcomes aren't counted twice — $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.

---

## Intuition

"Or" means addition — but with a catch. If you count everyone who tested positive *and* everyone who lied, anyone who did **both** gets tallied twice. So you add the two groups, then subtract the double-counted middle once. That subtraction is the entire idea; the formula is just bookkeeping to avoid counting a shared outcome more than once.

Picture two overlapping circles (a Venn diagram). Adding the two full circles counts the football-shaped middle twice, so you remove one copy. When the circles *don't* overlap — the events can't both happen — there's nothing to subtract, and the rule collapses to plain addition. Note this "or" is **inclusive**: *A, or B, or both*.

## Mechanics

A **compound event** combines two or more [[sample-space-and-events|simple events]]. The rule:

$$P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$$
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

where $P(A \cap B)$ is the probability both occur *in the same trial*.

**Disjoint (mutually exclusive)** events *cannot* both happen, so $P(A\cap B)=0$ and:

$$P(A \cup B) = P(A) + P(B) \qquad \text{(disjoint only)}$$

| Case | Overlap $P(A\cap B)$ | Rule |
|------|------|------|
| Not disjoint (overlap) | $>0$ | $P(A)+P(B)-P(A\cap B)$ |
| Disjoint (no overlap) | $0$ | $P(A)+P(B)$ |
| Complement ($B=\bar A$) | $0$, and covers all | $P(A)+P(\bar A)=1$ → [[complementary-events]] |

**Worked (Triola polygraph table, 98 subjects).** Positive results = 57, liars = 51, but 42 are *both*:
$$P(\text{positive or lied}) = \tfrac{57}{98}+\tfrac{51}{98}-\tfrac{42}{98} = \tfrac{66}{98} = 0.673$$
Adding $57+51=108$ without subtracting the 42 overlap would give $>1$ — the classic double-counting error.

```python
def p_a_or_b(p_a, p_b, p_and):
    return p_a + p_b - p_and          # p_and = 0 if disjoint
p_a_or_b(57/98, 51/98, 42/98)          # 0.673
```

## In ML

**Multi-class vs. multi-label = disjoint vs. not.** Softmax assumes the classes are **mutually exclusive** (an image is a cat *or* a dog, not both), so their probabilities are disjoint and sum to 1 — the addition rule for disjoint events. Multi-*label* problems drop that assumption (a photo can be "beach" *and* "sunset"), so each label gets an independent sigmoid instead of one shared softmax.

**The union bound (Boole's inequality).** Since subtracting the overlap only shrinks the total, $P(A_1\cup\dots\cup A_n)\le\sum P(A_i)$. This upper bound underpins generalization bounds and multiple-hypothesis correction (e.g. Bonferroni): the chance that *at least one* of many rare bad events fires is at most the sum of their probabilities.

## Exercises

**Basic** — A card is drawn from a 52-card deck. Find P(king or heart). (Watch the king of hearts — is it double-counted?)

**Intermediate** — In a class, P(passes math)=0.7, P(passes English)=0.6, P(passes both)=0.5. Find P(passes at least one). Are the two events disjoint? How do you know?

**Advanced** — Derive the three-event addition rule $P(A\cup B\cup C)$ by applying the two-event rule twice, and show it equals $\sum P(\text{singles}) - \sum P(\text{pairs}) + P(A\cap B\cap C)$ (inclusion–exclusion). Explain why the union bound drops every subtracted term.
