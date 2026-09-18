---
tags:
  - status/seed
  - probability
related:
  - "[[conditional-probability]]"
  - "[[law-of-total-probability]]"
  - "[[probability-fundamentals]]"
  - "[[complementary-events]]"
  - "[[beta-distribution]]"
  - "[[bernoulli-distribution]]"
domain: probability
sources:
  - "Bayes' Theorem for the Clinician — PMC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5114972/"
  - "Bayes' Theorem — formula, medical-test example & base rates (Cogn-IQ). https://www.cogn-iq.org/learn/theory/bayes-theorem/"
---

> **TL;DR** — **Bayes' theorem** flips a [[conditional-probability|conditional]] you *have*, $P(B\mid A)$, into the one you *want*, $P(A\mid B)$, by weighting it with the **base rate** $P(A)$: $P(A\mid B)=\dfrac{P(B\mid A)\,P(A)}{P(B)}$.

---

## Intuition

You know P(positive test | disease) = 99%. But the question a patient asks is the *reverse*: P(disease | positive test)? These are **not** the same (the [[conditional-probability|confusion of the inverse]]), and Bayes is the machine that converts one into the other. The missing ingredient is the **base rate** — how common the disease is *before* any test. When a disease is rare, even a 99%-accurate test yields mostly *false* positives, so P(disease | positive) can be shockingly low.

The deeper reading: Bayes is **belief-updating**. You start with a *prior* (what you believed before), see *evidence*, and end with a *posterior* (your revised belief). Evidence doesn't overwrite your prior — it *reweights* it.

## Mechanics

**Where it comes from** (don't memorize it — derive it). Start from the definition of [[conditional-probability]], written both directions:

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)} \qquad\text{and}\qquad P(B\mid A)=\frac{P(A\cap B)}{P(A)}$$

Solve each for the *same* joint probability $P(A\cap B)$ (this is the [[multiplication-rule]]):

$$P(A\cap B)=P(A\mid B)\,P(B) \qquad P(A\cap B)=P(B\mid A)\,P(A)$$

Both equal $P(A\cap B)$, so set them equal and divide by $P(B)$:

$$\underbrace{P(A\mid B)\,P(B)}_{\text{what you want}} = \underbrace{P(B\mid A)\,P(A)}_{\text{what you have}} \;\Longrightarrow\; \boxed{P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}}$$

That's the whole theorem — it's just the two conditional definitions glued at their shared $P(A\cap B)$. The denominator $P(B)$ expands by the law of total probability, $P(B)=P(B\mid A)P(A)+P(B\mid \bar A)P(\bar A)$ (splitting the evidence across $A$ and its [[complementary-events|complement]]).

| Term | Name | Meaning |
|------|------|---------|
| $P(A)$ | **prior** | belief before evidence (base rate) |
| $P(B\mid A)$ | **likelihood** | how well $A$ predicts the evidence |
| $P(B)$ | **evidence** | total probability of what you saw |
| $P(A\mid B)$ | **posterior** | revised belief after evidence |

So: **posterior ∝ likelihood × prior**.

**Worked — rare disease.** Prevalence 1% (prior), test sensitivity $P(+\mid D)=0.99$, false-positive rate $P(+\mid \bar D)=0.05$:
$$P(D\mid +)=\frac{0.99\cdot 0.01}{0.99\cdot 0.01 + 0.05\cdot 0.99}=\frac{0.0099}{0.0594}\approx 0.167$$
A positive test means only a **17%** chance of disease — the base-rate fallacy in action.

```python
prior, sens, fpr = 0.01, 0.99, 0.05
post = sens*prior / (sens*prior + fpr*(1-prior))
print(round(post, 3))   # 0.167
```

## In ML

**Naive Bayes classifiers apply it directly.** Predict $P(\text{class}\mid \text{features}) \propto P(\text{features}\mid \text{class})\,P(\text{class})$; "naive" = assume features are conditionally independent so the likelihood factorizes (see [[bernoulli-distribution]] for the binary-feature case).

**Bayesian inference is prior → posterior on parameters.** Instead of a point estimate, you keep a *distribution* over parameters and update it with data. With a conjugate prior the posterior stays in the same family — the [[beta-distribution|Beta]] is the conjugate prior for Bernoulli/Binomial, so updating is "just add counts." MAP estimation maximizes the posterior; MLE is the special case of a flat prior.

**Base-rate reasoning fixes evaluation traps.** A 99%-accurate classifier on a 0.1%-prevalence event is nearly useless (precision collapses) — the same math as the medical test, and why precision/recall on the rare class matter more than accuracy.

## Exercises

**Basic** — A box is 70% likely to be Box 1 (prior). Box 1 has 3 red / 7 blue; you draw red. If $P(\text{red}\mid\text{Box 1})=0.3$ and $P(\text{red}\mid\text{Box 2})=0.6$, find $P(\text{Box 1}\mid\text{red})$.

**Intermediate** — Redo the disease example with prevalence raised to 10%. Recompute $P(D\mid +)$ and explain *why* the same test now gives a much higher posterior.

**Advanced** — Show that "posterior ∝ likelihood × prior" implies MAP = MLE when the prior is uniform. Then explain how repeatedly applying Bayes (yesterday's posterior = today's prior) formalizes sequential learning.
