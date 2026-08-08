---
tags:
  - status/seed
  - probability
related:
  - "[[sampling-methods]]"
  - "[[population-and-sample]]"
  - "[[common-misuses-of-statistics]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-5."
---

> **TL;DR** — In an observational study you watch and measure without intervening; in an experiment you *apply a treatment* and observe its effect — and only the experiment, done with randomization, can support causal claims.

---

## Intuition

Data comes from two fundamentally different acts. Either you are a **spectator** — recording what already happens — or you are an **intervener** — you change something and see what follows. This single distinction is *why* one design can claim causation and the other usually cannot, which connects directly to the "[[common-misuses-of-statistics|correlation ≠ causation]]" trap.

The reason the intervention matters: when subjects *choose* their own condition (observational), the people who choose treatment often differ systematically from those who don't — a **confounding variable** that mimics or hides a real effect. Randomly *assigning* the treatment (experiment) breaks that link.

## Mechanics

| | **Observational study** | **Experiment** |
|---|---|---|
| What you do | measure characteristics, no intervention | apply a **treatment**, observe effect |
| Subjects called | subjects | *experimental units* |
| Causation? | generally **no** (association only) | **yes**, if randomized & controlled |
| Example | *Literary Digest* poll of voter preference | Salk polio-vaccine trial (200,745 vaccine vs. 201,229 placebo) |

**Why the experiment is the "gold standard"** — the hormone-therapy case (Denise Grady, *NYT*): observational studies suggested hormone replacement was beneficial, but the women who *chose* it were already healthier with better habits. Randomized controlled trials, which *assign* treatment vs. placebo, removed that self-selection and told a different story. In an observational study, subjects self-select → confounding; in an experiment, random assignment balances confounders across groups.

**Confounding effects an experiment must guard against:**

| Effect | What happens |
|--------|--------------|
| **Placebo effect** | an *untreated* subject who *believes* they got treatment reports improvement |
| **Hawthorne effect** | subjects behave differently simply *because they know they're being studied* |
| **Experimenter (Rosenthal) effect** | the researcher *unconsciously* influences subjects via tone, expression, attitude |

Controls against them: a **placebo** for the control group, **blinding** (subjects don't know their group), and **double-blinding** (neither subjects nor the people interacting with them know).

**Observational studies split further by *when* they observe** — cross-sectional (one moment), retrospective (looks backward), prospective (follows forward, e.g. the *National Children's Study* tracking 100,000 children birth→age 21). Full treatment in [[types-of-observational-studies]].

## In ML

**Observational data is what most models are trained on** — logs, clickstreams, historical records: nobody randomized anything, so a model can learn associations but the features it relies on are **not** proven causes. Acting on them as causal is the deployment failure behind harmful automated policy.

**A/B testing is the experiment** — randomly assigning users to variant A vs. B is a controlled experiment; random assignment is exactly what licenses "the new UI *caused* the lift," which observational log analysis never could.

**Confounding = the core threat to causal ML** — the whole field of causal inference (propensity scoring, do-calculus, uplift modeling) exists to recover experiment-like causal claims from observational data by explicitly modeling confounders.

## Exercises

**Basic** — Classify each as observational or experiment: (a) recording the resting heart rate of 500 volunteers; (b) giving half of 500 volunteers a new drug and half a placebo, then comparing heart rates. Justify by asking whether a treatment was applied.

**Intermediate** — A study finds coffee drinkers have lower rates of depression. Name a plausible confounding variable, and describe an experiment that would settle whether coffee *causes* the reduction.

**Advanced** — Explain why the placebo and Hawthorne effects are *different* threats, and design a single trial whose controls (placebo, blinding, double-blinding) neutralize both plus the experimenter effect.
