---
tags:
  - status/seed
  - probability
related:
  - "[[random-variable]]"
  - "[[mean-and-variance-of-a-probability-distribution]]"
  - "[[probability-distributions]]"
  - "[[relative-frequency-distribution]]"
  - "[[histogram]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-2 (Variables aleatorias)"
---

> **TL;DR** — A discrete probability distribution lists the probability of every value a [[random-variable|random variable]] can take, and it's only legitimate if those probabilities each sit in $[0,1]$ and sum to exactly 1.

---

## Intuition

Take a [[random-variable|discrete random variable]] and ask, for each value it can take, "how likely is this?" Collect all those answers and you have its **probability distribution** — the theoretical twin of a [[relative-frequency-distribution|relative frequency distribution]]. The difference: relative frequencies come from a *sample you actually ran*; probabilities describe what happens over *infinitely many* trials.

Two sanity checks make a distribution valid. First, the variable *has* to land on some value, so all the probabilities together must account for 100% of the outcomes — they sum to 1. Second, no single probability can be negative or exceed 1. Break either rule and it isn't a probability distribution at all.

## Mechanics

A distribution can be given as a **table**, a **graph**, or a **formula**. It's valid iff both hold:

| # | Requirement | Meaning |
|---|-------------|---------|
| 1 | $\sum P(x) = 1$ | Total certainty: some value must occur (rounding like 0.999 or 1.001 is OK) |
| 2 | $0 \le P(x) \le 1$ for every $x$ | Each probability is a legitimate probability |

**Worked check.** Cell phones per household: $P(0){=}0.19,\ P(1){=}0.26,\ P(2){=}0.33,\ P(3){=}0.13$. Sum $=0.91 \ne 1$ → **not** a distribution. But $P(x)=x/10$ for $x\in\{0,1,2,3,4\}$ gives $\tfrac{0+1+2+3+4}{10}=1$ and every term in $[0,1]$ → **valid**.

**Probability histogram.** Plot $x$ on the horizontal axis, $P(x)$ as bar heights. Because each bar is 1 unit wide, **area = probability** — the same area-equals-probability idea that later powers continuous distributions.

```python
P = {0:0.001, 1:0.015, 2:0.088, 3:0.264, 4:0.396, 5:0.237}  # green pods in 5
assert all(0 <= p <= 1 for p in P.values())      # requirement 2
assert abs(sum(P.values()) - 1) < 1e-9           # requirement 1 (≈1)
```

## In ML

**A softmax layer outputs a probability distribution.** The whole point of the final softmax in a classifier is to satisfy exactly these two requirements — every class score is squashed into $[0,1]$ and the outputs sum to 1 — so the vector is a valid distribution over labels you can sample from or take the argmax of.

**Normalization = enforcing requirement 1.** Any time you divide counts by a total (to get [[relative-frequency-distribution|relative frequencies]], attention weights, or a categorical prior), you're forcing $\sum P(x)=1$. A model that emits unnormalized scores isn't giving probabilities until you normalize.

## Exercises

**Basic** — Is $P(x) = x/5$ for $x \in \{0,1,2,3\}$ a valid distribution? Check both requirements.

**Intermediate** — A distribution has $P(1){=}0.2,\ P(2){=}0.5,\ P(3){=}k$. Find $k$. What constraint from requirement 2 must $k$ also respect?

**Advanced** — Someone proposes $P(x) = c \cdot 2^{-x}$ for $x = 1, 2, 3, \dots$ (infinitely many values). Find $c$ that makes it valid. Why does a *countable-infinite* discrete variable still let $\sum P(x)$ equal 1? (Hint: geometric series.)
