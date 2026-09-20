---
tags:
  - status/seed
  - probability
related:
  - "[[addition-rule]]"
  - "[[complementary-events]]"
  - "[[sample-space-and-events]]"
  - "[[probability-fundamentals]]"
  - "[[conditional-probability]]"
  - "[[bernoulli-distribution]]"
  - "[[hypergeometric-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-4 (Ejemplos 1–6)."
---

> **TL;DR** — The **multiplication rule** finds $P(A \text{ and } B)$ for a sequence of events: $P(A\cap B)=P(A)\cdot P(B\mid A)$ — multiply, but **adjust the second probability** for the fact that $A$ already happened.

---

## Intuition

"Or" meant addition ([[addition-rule]]); **"and" means multiplication**. To get *both* A and B, chain them: the fraction of times A happens, times the fraction of *those* in which B then happens. Guess a true/false question (1/2) and a 5-option question (1/5), and the chance of nailing both is 1/2 × 1/5 = 1/10 — exactly the 10 equally-likely branches of a tree diagram.

The one subtlety: **does A change B's odds?** If you draw two subjects *without replacement*, the first draw shrinks the pool, so B's probability must be recomputed *given* A. If A leaves B untouched (coin tosses, separate lotteries), the events are **independent** and no adjustment is needed. Getting this wrong is the classic error — treating dependent events as independent.

## Mechanics

$$P(A \text{ and } B) = P(A)\cdot P(B\mid A)$$

$P(B\mid A)$ = "probability of B **given** A already occurred." Two cases:

| Events | Condition | Rule |
|--------|-----------|------|
| **Independent** | $P(B\mid A)=P(B)$ | $P(A\cap B)=P(A)\cdot P(B)$ |
| **Dependent** | $P(B\mid A)\ne P(B)$ | $P(A\cap B)=P(A)\cdot P(B\mid A)$ |

- **With replacement** → independent (pool resets). **Without replacement** → dependent (pool shrinks).
- **Extends to many events** as a running product: $P(A_1\cap\dots\cap A_n)=P(A_1)P(A_2\mid A_1)\cdots$. For independent events it's just $\prod P(A_i)$.

**Worked (pacemakers, 3 good B / 2 defective D).** Pick two:
- *With* replacement (independent): $P(B,B)=\tfrac35\cdot\tfrac35=0.36$
- *Without* replacement (dependent): $P(B,B)=\tfrac35\cdot\tfrac24=0.3$ ← second term adjusted

**5% guideline** — if the sample is ≤ 5% of the population, treating without-replacement draws as *independent* is accurate enough (the shrink is negligible), saving painful exact products.

```python
# without replacement, sequential adjustment
good, total = 3, 5
p = (good/total) * ((good-1)/(total-1))   # 0.3
```

## In ML

**Independence makes likelihoods factorize.** The i.i.d. assumption lets the joint probability of a dataset split into a *product* over samples: $P(\text{data})=\prod_i P(x_i)$. Taking logs turns that product into the **sum** that every maximum-likelihood loss (and cross-entropy) optimizes. Repeated independent [[bernoulli-distribution|Bernoulli]] trials multiplied this way *are* the binomial distribution.

**The chain rule powers autoregressive models.** The dependent form generalizes to $P(w_1,\dots,w_n)=\prod_i P(w_i\mid w_1,\dots,w_{i-1})$ — exactly how a language model factorizes a sentence's probability into next-token predictions. "And," conditioned step by step, is the backbone of GPT-style generation.

**Redundancy = multiplying failure probabilities.** If a component fails with prob 0.001, two *independent* copies both fail with prob 0.001² = 0.000001 — the reliability-engineering rationale for backup systems.

## Exercises

**Basic** — A coin is tossed 3 times. Using the multiplication rule for independent events, find P(three heads).

**Intermediate** — From a 52-card deck, draw two cards *without replacement*. Find P(both aces). Now find it *with* replacement. Which is larger, and why?

**Advanced** — Two people are chosen at random. (a) P(born on the same day of the week)? (b) P(both born on Monday)? Explain why these differ (1/7 vs. 1/49) even though the wording looks nearly identical — what event is being fixed in each?
