---
tags:
  - status/seed
  - probability
related:
  - "[[frequency-distribution]]"
  - "[[probability-fundamentals]]"
  - "[[characteristics-of-data]]"
  - "[[probability-distributions]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-2."
---

> **TL;DR** — A relative frequency distribution replaces each class count with its *proportion* (or percentage) of the total, so classes become comparable across datasets of different sizes and the table reads as an empirical probability distribution.

---

## Intuition

A raw [[frequency-distribution|frequency]] of 12 means nothing until you know "out of how many." Divide by the total and 12 becomes **12/40 = 0.30 = 30%** — now it's self-explanatory and, crucially, **comparable**: you can put the 40 women's pulses next to the 40 men's, or next to a sample of 400, and the shapes line up on the same 0–100% scale. Relative frequency is the bridge from *counting* to *proportion*, and proportion is one step from **probability** — the relative frequency of a class is the empirical estimate of the probability a random value lands there ([[probability-fundamentals]]).

## Mechanics

Replace each class frequency with either form (Triola uses "relative frequency" to mean either):

$$\text{relative frequency} = \frac{\text{class frequency}}{\text{sum of all frequencies}} \qquad \text{percentage} = \frac{\text{class frequency}}{\text{sum of all frequencies}} \times 100\%$$

**Worked example — women's pulses (n = 40), from Triola Table 2-3:**

| Pulse (class) | Frequency | Relative freq. |
|---|---|---|
| 60–69 | 12 | 12/40 = 30% |
| 70–79 | 14 | 14/40 = 35% |
| 80–89 | 11 | 11/40 = 27.5% |
| 90–99 | 1 | 2.5% |
| 100–109 | 1 | 2.5% |
| 110–119 | 0 | 0% |
| 120–129 | 1 | 2.5% |

**The key check:** relative frequencies must **sum to 1 (or 100%)** — that's what makes them a valid distribution. Small rounding discrepancies are fine: **99% or 101% is acceptable.** A sum far from 100% signals a construction error.

```python
freqs = [12, 14, 11, 1, 1, 0, 1]
total = sum(freqs)                       # 40
rel = [f / total for f in freqs]         # proportions
pct = [round(r * 100, 1) for r in rel]   # [30.0, 35.0, 27.5, 2.5, 2.5, 0.0, 2.5]
print(pct, "sum:", round(sum(rel), 3))   # sum: 1.0  -> valid distribution
```

Only the *counts* change to proportions; the [[frequency-distribution|class limits, boundaries, midpoints, and width]] are identical.

## In ML

**Relative frequency is the empirical probability** — the frequentist definition of probability *is* the limit of relative frequency, so a relative-frequency table is a discrete empirical [[probability-distributions|distribution]]; normalizing a histogram to sum to 1 (`density=True`) turns counts into an estimated probability density.

**Normalization makes distributions comparable** — the same divide-by-total move underlies converting logits to a probability vector (softmax outputs sum to 1) and comparing class proportions across datasets of different sizes.

**Class balance is a relative-frequency check** — the relative frequency of each label is exactly the class-balance diagnostic; a heavily skewed relative-frequency (e.g. 99% / 1%) flags an imbalanced-classification problem before training.

## Exercises

**Basic** — A class has frequency 18 out of a total of 72. Give its relative frequency as a proportion and a percentage.

**Intermediate** — Convert this frequency distribution to relative frequencies and verify the sum: {A: 8, B: 12, C: 5, D: 15}. Which class is the mode?

**Advanced** — Two samples (n = 50 and n = 500) have identical *relative* frequency distributions. What can and cannot you conclude by comparing them, and why is relative — not raw — frequency the right tool for the comparison?
