---
tags:
  - status/seed
  - probability
related:
  - "[[sampling-methods]]"
  - "[[population-and-sample]]"
  - "[[binomial-distribution]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-5."
---

> **TL;DR** — A *random sample* only promises each **individual** an equal chance; a *simple random sample* promises each **possible group of size n** an equal chance — so every SRS is a random sample, but not the reverse.

---

## Intuition

The two terms sound interchangeable and aren't. The trap is that "everyone is equally likely to be picked" (fair to *people*) does **not** guarantee "every possible team is equally likely" (fair to *groups*). A design can be fair to individuals while secretly forbidding most of the groups they could form. The 4-person example below is the smallest case that exposes the gap — and it's the one to remember, because most procedures later in statistics require an *SRS specifically*, not just any random sample.

The mechanism behind the gap: when picks are **bundled** (choosing one element drags another along), individuals can still be balanced while whole combinations get blocked.

## Mechanics

**Definitions** (the object each constrains is the whole point):

- **Random sample** — each *individual* member has an equal chance of selection.
- **Simple random sample (SRS)** — every *possible sample of size n* (every combination) has an equal chance.

SRS is strictly stronger: SRS ⟹ random sample, but random sample ⇏ SRS.

**The A/B/C/D example** — population {A, B, C, D}, sample size *n* = 2. The 6 possible pairs are AB, AC, AD, BC, BD, CD.

| Design | Rule | Pairs possible | Per-person chance | Verdict |
|--------|------|----------------|-------------------|---------|
| **1** | put all 6 pairs in a hat, draw one | all 6, each 1/6 | each = 1/2 | **SRS** (and random) |
| **2** | glue into couples {A,B}, {C,D}; flip a coin | only AB, CD (each 1/2); other 4 = **0** | each = 1/2 | random, **not SRS** |

In Design 2 every *person* still has probability 1/2 — so it *is* a random sample — yet four of six pairs (AC, AD, BC, BD) can **never** occur, because A is chained to B and C to D. Fair individuals, rigged groups.

> One-line test: *"Is there any group of size n this method could never produce?"* If yes → not an SRS (may still be a random sample).

Note "simple" governs **grouping**, not replacement: an SRS is drawn *without replacement*, so no element repeats within a sample (there is no "AA"). See the [[binomial-distribution]] for how with/without replacement changes independence.

```python
from itertools import combinations
pop = "ABCD"
all_pairs = list(combinations(pop, 2))                 # 6 pairs -> SRS space
couples   = [("A", "B"), ("C", "D")]                    # Design 2 support
possible  = {p: (1/6 if p in all_pairs else 0) for p in all_pairs}
design2   = {p: (1/2 if p in couples else 0) for p in all_pairs}
print(possible)   # every pair 1/6  -> SRS
print(design2)    # only AB, CD > 0 -> random but not SRS
```

## In ML

**Cross-validation splits are supposed to be SRS-like** — a plain `train_test_split` aims for every subset of rows being equally likely; if rows are *bundled* (e.g. multiple records per patient), you get Design-2 behavior and must use group-aware splitting so the "impossible combinations" (splitting a patient across folds) are handled deliberately.

**Stratified sampling is a deliberate non-SRS** — `stratify=y` guarantees class proportions, which *blocks* certain combinations (an all-one-class fold), exactly like Design 2 trades the SRS property for a different guarantee. Knowing it's *not* an SRS explains why some statistical tests assuming an SRS shouldn't be applied naively to stratified data.

## Exercises

**Basic** — For {A, B, C, D}, *n* = 2, list all six pairs and give their probability under Design 1. Confirm each person's selection probability is 1/2.

**Intermediate** — Design: *"always include A, then coin-flip to add one of B, C, or D."* Is it a random sample? An SRS? Compute A's chance vs. B's chance to justify your answer.

**Advanced** — Prove in general that any design which first partitions the population into fixed blocks and then selects whole blocks cannot be an SRS whenever at least one cross-block pair exists, by exhibiting a size-*n* sample with probability zero.
