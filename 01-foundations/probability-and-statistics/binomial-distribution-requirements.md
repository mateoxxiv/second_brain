---
tags:
  - status/seed
  - probability
related:
  - "[[binomial-distribution]]"
  - "[[bernoulli-distribution]]"
  - "[[multiplication-rule]]"
  - "[[hypergeometric-distribution]]"
  - "[[discrete-probability-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-3 (Distribuciones de probabilidad binomial)"
---

> **TL;DR** — A procedure is binomial only if it has a **fixed number of independent trials, each with two outcomes and the same success probability** — check these four before ever using the [[binomial-distribution|binomial formula]].

---

## Intuition

Before you *compute* a binomial probability, you have to earn the right to use the formula. The binomial model isn't a universal tool — it fits a very specific shape of problem: repeat the *same* yes/no experiment a *fixed* number of times, where each repeat is independent and the odds never drift. Coin flips, defective/OK parts, survived/died, recognizes-the-brand/doesn't.

The most common way it silently breaks is **sampling without replacement** — drawing people from a survey pool changes the pool, so trials stop being independent. That's the trap this checklist exists to catch (and the 5% guideline is the escape hatch).

## Mechanics

**The four requirements** (all must hold):

| # | Requirement | The trap it rules out |
|---|-------------|-----------------------|
| 1 | **Fixed** number of trials $n$ | "keep going until…" is *not* fixed |
| 2 | Trials are **independent** | without-replacement sampling breaks this |
| 3 | Each trial has **two categories** (success / failure) | 3+ outcomes → not binomial (→ multinomial) |
| 4 | $p$ (success prob.) is **constant** across trials | drifting odds → not binomial |

**Notation.** $P(S)=p$ (success), $P(F)=1-p=q$; $n$ = number of trials; $x$ = number of successes ($0 \le x \le n$); $P(x)$ = probability of exactly $x$ successes. Always $q = 1-p$.

**Two warnings.**
- "Success" is **arbitrary** — either category can be the success, as long as $p$ is *its* probability.
- $x$ and $p$ must name the **same** category. If $x$ counts green pods, $p$ must be P(green), not P(not-green).

**The 5% guideline** (from the [[multiplication-rule]]). Without-replacement draws violate requirement 2, but if the sample is $\le 5\%$ of the population, the [[multiplication-rule|dependence]] is negligible — treat the trials as independent anyway. This is what lets real surveys use the binomial despite sampling without replacement. When the sample is a *large* fraction of a finite pool, use the [[hypergeometric-distribution|hypergeometric]] instead.

```python
# Recognition check (pea pods): n=5 offspring, success = "green pod", p=0.75
n, p = 5, 0.75
# 1 fixed n ✓  2 offspring independent ✓  3 green/not-green ✓  4 p constant ✓
q = 1 - p                    # 0.25  → binomial applies
```

## In ML

**The i.i.d. assumption *is* requirements 2 and 4.** "Independent and identically distributed" — the backbone assumption of nearly all supervised learning — is exactly binomial requirement 2 (independent) plus requirement 4 (identical $p$). When you count correct predictions over a test set, you're implicitly asserting a binomial setup; if the test examples are correlated (e.g. frames from one video), requirement 2 fails and your accuracy confidence interval is wrong.

**Recognizing the model prevents misuse.** Choosing a loss or a statistical test starts with "what generates this data?" A/B conversion counts satisfy the four requirements → binomial/[[bernoulli-distribution|Bernoulli]] likelihood → cross-entropy. A three-way outcome breaks requirement 3 → you need the multinomial/softmax instead. The checklist is the modeling decision, not bureaucracy.

## Exercises

**Basic** — For each, do the four requirements hold? (a) flip a coin 20 times, count heads; (b) draw cards until you get an ace; (c) roll a die 10 times, count the number shown.

**Intermediate** — A jar has 8 red / 2 blue marbles; draw 3 *without replacement* and count red. Which requirement fails, and why? Would the 5% guideline rescue it here? Which distribution is correct instead?

**Advanced** — A factory's defect rate rises through the day as a machine heats up. You inspect 50 parts across a shift and count defects. Which requirement is violated, and what does that do to a binomial-based prediction of total defects?
