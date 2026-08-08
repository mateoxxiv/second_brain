---
tags:
  - status/seed
  - probability
related:
  - "[[observational-study-vs-experiment]]"
  - "[[experimental-designs-for-controlling-variables]]"
  - "[[statistical-significance]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-5."
---

> **TL;DR** — A good experiment rests on three pillars — **randomization** (assign by chance), **replication** (enough subjects), and **control** (blinding + design to isolate the treatment) — so that any difference you see comes from the treatment, not from confounding.

---

## Intuition

An experiment's whole job is to answer "did the *treatment* cause the effect?" — and the enemy is [[observational-study-vs-experiment|confounding]], where you can't tell the treatment's effect apart from some other variable's. The three pillars are the defenses against that enemy. The Salk polio trial (1954) is the textbook success: 200,745 children got the vaccine, 201,229 got a placebo, assignment was by coin-flip-equivalent chance, nobody knew who got what, and the samples were huge. That combination is *why* the result (33 vs. 115 polio cases) was believable.

## Mechanics

**The three pillars (Triola's design summary):**

| Pillar | What it means | Why it works |
|--------|---------------|--------------|
| **Randomization** | assign subjects to groups by a chance process | uses probability to make groups *similar* on all variables at once — even ones you never thought to measure |
| **Replication** | repeat the treatment on enough subjects | large samples let real effects surface above small-sample noise |
| **Control** | blinding + a design that isolates the treatment | removes the placebo effect and prevents confounding |

**Randomization** — you cannot manually match two groups on age, health, sex, weight, diet, etc.; some variable always slips through. Letting *chance* assign subjects balances all variables probabilistically. Counterintuitively, leaving assignment to chance is the *most* rigorous choice.

**Replication** — the sample must be big enough that the erratic behavior of tiny samples doesn't mask true treatment effects. **But bigger is not automatically better**: a large sample collected badly (biased) is worse than a smaller, properly [[random-sample-vs-simple-random-sample|randomly selected]] one. *Right method first, then adequate size.*

**Control via blinding:**
- **Blind** — the *subject* doesn't know if they got treatment or placebo → neutralizes the **placebo effect** (improvement reported by untreated subjects who *believe* they're treated).
- **Double-blind** — *neither the subjects nor the researchers* administering/evaluating know → also blocks the **experimenter effect**. The Salk trial was double-blind.

**Confounding** — when the effects of two factors can't be separated (e.g. treating only women, placebo only men: was it the treatment or the sex?). Good design leaves *no room* for it — see [[experimental-designs-for-controlling-variables]].

## In ML

**Randomization = random assignment in A/B tests** — splitting users to variant A vs. B by chance is exactly Salk-style randomization; it's what lets you claim the change *caused* the metric move rather than merely correlating with it.

**Replication ↔ statistical power and sample size** — needing "enough subjects to see the effect" is the experimental-design face of [[statistical-significance|power analysis]]: too few samples and a real lift stays statistically invisible.

**Blinding ↔ leakage and evaluator bias** — a model evaluator that "peeks" at labels, or a metric contaminated by the treatment, is the ML analogue of an unblinded trial; held-out, blinded evaluation keeps the comparison honest.

## Exercises

**Basic** — Name the three pillars of good experimental design and give a one-sentence justification for each.

**Intermediate** — A trial gives the drug to volunteers and a placebo to whoever declined. Identify which pillar is violated and what confounding this creates.

**Advanced** — Explain why a double-blind design is needed *in addition* to randomization — i.e., what specific bias randomization alone does **not** remove, and how blinding closes that gap.
