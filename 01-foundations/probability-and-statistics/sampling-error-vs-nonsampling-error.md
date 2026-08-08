---
tags:
  - status/seed
  - probability
related:
  - "[[population-and-sample]]"
  - "[[sampling-methods]]"
  - "[[common-misuses-of-statistics]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-5."
---

> **TL;DR** — A **sampling error** is the unavoidable random gap between a sample result and the true population value; a **nonsampling error** is a *fixable* mistake in how data was collected, recorded, or analyzed — and only the first is what statistics is built to handle.

---

## Intuition

Draw 1,000 adults, ask if they finished high school, record the percentage. Draw another 1,000 — you'll get a *different* percentage. That wobble is **sampling error**: pure chance, present even in a perfect study, and it *shrinks predictably as the sample grows*. It is not a mistake — it's the price of looking at a [[population-and-sample|sample]] instead of the whole population.

A **nonsampling error** is different in kind: a biased sample, a broken measuring instrument, a mis-typed value. No amount of clever statistics fixes it, and a *bigger* sample can even make it *worse* (you just collect the same bias faster). The entire toolkit of confidence intervals and hypothesis tests models sampling error — so the hidden danger is always the nonsampling error the math silently ignores.

## Mechanics

| | **Sampling error** | **Nonsampling error** |
|---|---|---|
| Cause | random chance of *which* subjects landed in the sample | flawed collection, recording, or analysis |
| Avoidable? | **No** — inherent to sampling | **Yes** — with careful method |
| Effect of larger *n* | **shrinks** it | does **not** fix it (may entrench bias) |
| Handled by statistics? | **Yes** — this is what the math models | **No** — must be prevented at design time |
| Examples | two random samples give 61% vs. 63% | biased sample, defective scale, data-entry typo |

**Key consequence:** the confidence intervals and *p*-values you compute later quantify **sampling error only**. They assume the data was collected properly. So a beautiful 95% confidence interval built on a [[common-misuses-of-statistics|voluntary-response]] sample is precise nonsense — the interval measures the chance wobble while ignoring the bias that dominates.

```python
import numpy as np
rng = np.random.default_rng(0)
p = 0.62                                   # true population proportion
samples = [rng.binomial(1000, p) / 1000 for _ in range(5)]
print([round(s, 3) for s in samples])      # each differs -> sampling error
# a broken instrument that always adds +0.05 -> nonsampling error (no seed fixes it)
```

## In ML

**Sampling error ≈ variance of a metric across test sets** — evaluating on different random test splits yields different accuracies; that spread is sampling error, and reporting confidence intervals on metrics quantifies exactly it.

**Nonsampling error ≈ label noise and data-collection bias** — mislabeled examples, a sensor miscalibration, or a skewed data-collection pipeline are nonsampling errors: more data doesn't cure them, and they cap achievable performance no matter how good the model — the ML face of "garbage in, garbage out."

## Exercises

**Basic** — Classify each: (a) two polls of 500 people report 48% and 51%; (b) a scale reads 2 kg heavy for everyone; (c) a survey only reaches landline owners.

**Intermediate** — Explain why increasing sample size from 1,000 to 100,000 tightens a confidence interval but would **not** rescue a study whose sample was self-selected.

**Advanced** — A model's test accuracy varies ±2% across random splits, but is systematically 8% lower on one demographic due to labeling errors in that group. Identify which gap is sampling vs. nonsampling error and argue which one more sample data can address.
