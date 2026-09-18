---
tags:
  - status/seed
  - probability
related:
  - "[[multiplication-rule]]"
  - "[[complementary-events]]"
  - "[[addition-rule]]"
  - "[[probability-fundamentals]]"
  - "[[bayes-theorem]]"
  - "[[law-of-total-probability]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-5 (Ejemplos 3–4)."
---

> **TL;DR** — The **conditional probability** $P(B\mid A)$ is the probability of $B$ *given that $A$ already happened*: shrink the sample space down to $A$, then ask how much of it is also $B$ — $P(B\mid A)=\dfrac{P(A\cap B)}{P(A)}$.

---

## Intuition

New information changes probabilities. A random golfer's chance of a hole-in-one is 1/12,000 — but *given* they're a pro in a tournament, it jumps to 1/2375. Same event, extra knowledge, different probability. That's conditioning.

The mental move: **"given A" means throw away every outcome where A didn't happen and zoom into the world where it did.** Your sample space is no longer everything — it's just A. Then you ask: within that smaller world, what fraction is also B? Triola's intuitive method beats plugging into the formula: *assume A occurred, then compute B's probability inside that reduced space.*

The trap: **$P(B\mid A)$ is NOT $P(A\mid B)$.** P(dark | it's midnight) ≈ 1, but P(it's midnight | it's dark) ≈ 0. Swapping them is the **confusion of the inverse** — and it puts innocent people in prison (the prosecutor's fallacy) and terrifies healthy patients.

## Mechanics

$$P(B\mid A) = \frac{P(A \cap B)}{P(A)} \qquad (\text{requires } P(A) > 0)$$

Rearranging gives the [[multiplication-rule]] back: $P(A\cap B)=P(A)\,P(B\mid A)$. Independence is the special case $P(B\mid A)=P(B)$ (knowing A tells you nothing).

**Worked (Triola polygraph table).** Of 98 subjects, 51 lied; of those 51, 42 tested positive:
$$P(\text{positive}\mid\text{lied}) = \frac{42}{51} = 0.824$$
Reverse the condition — of the 57 who tested positive, 42 lied:
$$P(\text{lied}\mid\text{positive}) = \frac{42}{57} = 0.737$$

| | Reduced space | Result |
|---|---|---|
| $P(\text{positive}\mid\text{lied})$ | the 51 liars | 0.824 |
| $P(\text{lied}\mid\text{positive})$ | the 57 positives | 0.737 |

**Same numerator (42), different denominators** — that's why the two conditionals differ. Confusing them is the confusion of the inverse.

```python
# reduce the sample space, then take the fraction
lied, positive_and_lied = 51, 42
p_positive_given_lied = positive_and_lied / lied   # 0.824
```

## In ML

**The base-rate fallacy = confusion of the inverse.** A cancer test with P(positive | cancer) = 0.99 does *not* mean P(cancer | positive) = 0.99 — with a rare disease the latter can be under 10%. ~95% of doctors get this wrong. Fixing it requires [[bayes-theorem]], which flips $P(B\mid A)$ into $P(A\mid B)$ using the base rate P(A).

**Precision and recall are two different conditionals.** Recall = P(predicted positive | actually positive); precision = P(actually positive | predicted positive). They're the polygraph example wearing ML clothes — one fixes the true label, the other fixes the prediction, and they are *not* interchangeable.

**Conditioning is what generative models do.** A language model factorizes text as a chain of conditionals $P(w_i \mid w_1,\dots,w_{i-1})$ — every next-token prediction is a conditional probability over the vocabulary given the context so far.

## Exercises

**Basic** — From the polygraph table, compute P(negative | did not lie) — of the 47 who didn't lie, 32 tested negative. Interpret it in words.

**Intermediate** — A box has 3 red, 2 blue balls. Draw two without replacement. Using conditioning, find P(2nd is red | 1st is red). Why does the answer differ from P(2nd is red)?

**Advanced** — A disease affects 1% of people. A test has P(positive | disease) = 0.99 and P(positive | no disease) = 0.05. Compute P(disease | positive). Explain why it's far below 0.99, and name which conditional the "confusion of the inverse" mistakes for which.
