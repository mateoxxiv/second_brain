---
tags:
  - status/seed
  - probability
related:
  - "[[experimental-design-principles]]"
  - "[[observational-study-vs-experiment]]"
  - "[[random-sample-vs-simple-random-sample]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-5."
---

> **TL;DR** — Four designs isolate a treatment's effect from confounding: **completely randomized**, **randomized block**, **rigorously controlled**, and **matched pairs** — each a different strategy for making the treatment and control groups comparable.

---

## Intuition

The [[experimental-design-principles|control pillar]] says "leave no room for confounding." *How* you achieve that is the design. The core problem is always the same: you want the treated and untreated groups to differ in *only* the treatment. These four methods are four answers, trading off simplicity against how tightly they balance nuisance variables (sex, age, health...). The more you *know* about which variables matter, the more structure you can add — from pure chance (completely randomized) up to one-to-one twinning (matched pairs).

## Mechanics

| Design                    | How groups are made comparable                                               | Best when                                                                  |
| ------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Completely randomized** | assign subjects to treatment/control purely by chance                        | you trust randomization to balance everything (large *n*) — the Salk trial |
| **Randomized block**      | group similar subjects into **blocks**, then randomize *within each block*   | a known variable strongly affects outcome (block by sex for a heart drug)  |
| **Rigorously controlled** | *deliberately* assign so each group has matching profiles on relevant traits | you can enumerate the relevant variables (hard, error-prone)               |
| **Matched pairs**         | pair related/similar subjects; compare within the pair                       | natural pairs exist (twins; or same subject before/after)                  |


**Completely randomized** — chance alone assigns groups; the [[experimental-design-principles|randomization]] pillar does all the balancing work. Simplest and, with enough subjects, very effective.

**Randomized block** — a *block* is a set of similar subjects; blocks differ on a factor that affects the result. Procedure: (1) form blocks of similar subjects, (2) randomize treatments *within* each block. Example: block men and women separately (hearts behave differently), randomize within each. This removes the blocking variable's confounding *by construction*.

**Rigorously controlled** — you hand-match group compositions: if the placebo group has a 27-year-old smoker who drinks heavily, the treatment group must include a similar person. Powerful in principle but **fragile** — it's hard to be sure you accounted for every relevant factor.

**Matched pairs** — compare two treatments using subjects tied one-to-one: the Crest toothpaste trial used **twins** (one used Crest, one didn't); or measure the *same* subject **before vs. after** a treatment. Pairing cancels between-subject variation.

## In ML

**Randomized block ≈ stratified evaluation** — blocking by a known nuisance variable is the experimental twin of [[random-sample-vs-simple-random-sample|stratified sampling]]: you guarantee balance on that variable instead of hoping chance provides it, reducing variance in the estimated effect.

**Matched pairs ≈ paired/within-subject comparison** — testing two models on the *same* inputs (paired predictions) is a matched-pairs design; it cancels input-difficulty variation, giving a far more sensitive comparison than running each model on separate random samples.

**Completely randomized ≈ standard A/B testing** — random traffic assignment with no blocking is the completely randomized design, valid when traffic volume (large *n*) makes chance balancing reliable.

## Exercises

**Basic** — Match each design to its defining idea: (a) block-then-randomize, (b) pure chance assignment, (c) one-to-one twinning, (d) hand-matched group profiles.

**Intermediate** — You test a fertilizer on crop yield, and soil type strongly affects yield. Which design best removes soil type as a confounder, and how would you set it up?

**Advanced** — Explain why a matched-pairs (before/after same subject) design can detect a smaller treatment effect than a completely randomized design with the same number of measurements — reason in terms of variance between vs. within subjects.
