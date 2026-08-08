---
tags:
  - status/seed
  - probability
related:
  - "[[population-and-sample]]"
  - "[[observational-study-vs-experiment]]"
  - "[[common-misuses-of-statistics]]"
  - "[[principles-of-statistical-thinking]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-5."
---

> **TL;DR** — How you pick the sample decides whether any later analysis means anything; the gold standard is the *simple random sample*, defined not on individuals but on every possible sample of size *n* having an equal chance.

---

## Intuition

> *"If sample data are not collected properly, they may be so useless that no amount of statistical torture can salvage them."* — Triola

Every statistical method downstream assumes the sample **represents** the population. Sampling method is the single decision that determines representativeness — so it comes *before* any formula, and no formula can repair a bad one. This note is the taxonomy of *how* to draw a sample; a [[common-misuses-of-statistics|voluntary response sample]], where people self-select, is the anti-pattern all of these try to avoid.

The one subtlety worth burning in early: **"random" is a family, and simple random is the strictest member.** Equal chance for each *person* is not the same as equal chance for each *group of people*.

## Mechanics

**The three "random" definitions — read the object each one constrains:**

| Term | Equal/known chance applies to… | Key point |
|------|-------------------------------|-----------|
| **Random sample** | each *individual* member | every person equally likely |
| **Simple random sample (SRS)** | every *possible sample of size n* | strictest; every *combination* equally likely |
| **Probability sample** | each member has a *known* chance | chances need **not** be equal |

The distinction is not pedantic: **most procedures later in the book require an SRS specifically**, and stratified/cluster/systematic samples do *not* qualify.

**The senators example (why random ≠ SRS)** — Write each of the 50 US states on a card, shuffle, draw one card, take *both* senators of that state as a sample of size 2:
- **Random sample?** ✅ each senator has a 1/50 chance.
- **SRS?** ❌ not every pair of size 2 is possible — two senators from *different* states can never be chosen together.
- **Probability sample?** ✅ each has a *known* chance (1/50).

**The five practical methods:**

| Method | Procedure | Note |
|--------|-----------|------|
| **Simple random** | every sample of size *n* equally likely | the requirement for most later methods |
| **Systematic** | pick a start, take every *k*-th element | fails if the list has a hidden periodic cycle |
| **Convenience** | use whatever is easiest to obtain | highly bias-prone |
| **Stratified** | split into homogeneous strata, sample *from every stratum* | reduces variability of results |
| **Cluster** | split into clusters, randomly pick *some clusters*, take *everyone* in them | cheaper, usually more variable |

**Stratified vs. cluster** (the classic mix-up — both make subgroups):
- **Stratified** → *some* members from *all* subgroups.
- **Cluster** → *all* members from *some* (randomly chosen) subgroups.
- Mnemonic: **s**tratified = **s**ome from all; **cluster** = all from chosen clusters.

**Multistage sampling** — real surveys (e.g. the US *Current Population Survey* for unemployment) chain several methods across stages (random → stratified → cluster). Complex, but far cheaper and more practical than a nationwide SRS.

```python
import numpy as np
rng = np.random.default_rng(0)
pop = np.arange(1, 101)          # population of 100

srs        = rng.choice(pop, size=10, replace=False)   # simple random
start      = rng.integers(0, 10)
systematic = pop[start::10]                             # every 10th element
print(sorted(srs), list(systematic))
```

## In ML

**Sampling method = how you build train/val/test sets** — a [[common-misuses-of-statistics|convenience sample]] (whatever logs were easy to grab) bakes selection bias into the model exactly as it biases a survey.

**Stratified sampling is standard practice** — `train_test_split(..., stratify=y)` preserves class proportions in every split, the ML use of stratification to reduce variance and keep rare classes represented. Stratified k-fold cross-validation is the same idea applied to evaluation.

**Cluster structure breaks the i.i.d. assumption** — if rows come in natural clusters (patients, users, sessions), a naive random split leaks information across folds; *group*-aware splitting (GroupKFold) is the ML analogue of respecting cluster boundaries.

## Exercises

**Basic** — A university takes its alphabetical enrollment list and surveys every 25th student. Name the sampling method. Is it an SRS? Justify by asking whether *every possible group* of students could be selected.

**Intermediate** — You want 200 students split evenly by year (freshman → senior). Describe a stratified design and a cluster design for this, and state which gives more consistent results and why.

**Advanced** — Prove that a stratified sample (one person drawn at random from each of several strata) is generally **not** a simple random sample, by exhibiting a possible sample of the correct total size that has probability zero under the design.
