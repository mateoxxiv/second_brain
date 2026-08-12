---
tags:
  - status/seed
  - probability
related:
  - "[[dot-plot]]"
  - "[[histogram]]"
  - "[[frequency-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A stem-and-leaf plot splits each value into a **stem** (leading digits) and a **leaf** (last digit), grouping leaves by stem — it shows distribution shape like a [[histogram]] **while keeping every original value**, and it sorts the data as a side effect.

---

## Intuition

Write each number as a stem (the tens) and a leaf (the units): 67 becomes stem **6**, leaf **7**. List the stems in a column and hang each value's leaf next to its stem. Turned on its side, the rows of leaves look just like [[histogram]] bars — but you can still read every exact number, and once the leaves are in order the whole dataset is sorted for free.

## Mechanics

**Definition** — separate each value into a **stem** (leftmost digit(s)) and a **leaf** (rightmost digit). Rows are stems; leaves are written in increasing order to the right.

Triola's Example 5 (women's pulses), values 60, 60, 60, 64, …, 124:

```
Stem (tens) | Leaves (units)
   6        | 0 0 0 4 4 4 4 8 8 8 8 8   → 60,60,60,64,...,68
   7        | 2 2 2 2 2 2 2 2 6 6 6 6 6 6
   8        | 0 0 0 0 0 0 8 8 8 8 8
   9        | 6                          → 96
  10        | 4                          → 104
  11        |
  12        | 4                          → 124
```

**Three properties Triola stresses:**
1. **Lossless** — like the [[dot-plot]], the original list is fully recoverable.
2. **Shape** — a row of leaves ≈ a histogram bar; turned sideways it *is* a distribution. So the **5–20 classes** guideline for [[histogram|histograms]] applies to stems too.
3. **Sorts data** — arranging leaves in order sorts the dataset, which is needed for the **median** and **percentiles**.

**Adjusting rows** — expand (split each stem into two rows, leaves 0–4 / 5–9) or condense stems to keep the row count in the 5–20 range. Rounding the raw values first usually gives a cleaner plot.

## In ML

**Quick sorted EDA on paper** — rarely used in code, but its logic (bucket by leading digits) is the intuition behind **radix bucketing** and the shape-plus-values idea that motivates keeping raw data in **`describe()` + histogram** together.

**Order statistics** — because it sorts the data, a stem-and-leaf directly exposes **median, quartiles, and percentiles** — the order statistics underlying box plots and robust summaries.

## Exercises

**Basic** — Put the values 52, 55, 61, 61, 67, 73 into a stem-and-leaf plot with stems 5, 6, 7.

**Intermediate** — Explain the two advantages of a stem-and-leaf plot over a [[histogram]], and the one situation where the histogram is clearly better.

**Advanced** — You have 3-digit values ranging 100–899. Design a sensible stem/leaf split that keeps the row count within 5–20, and justify any rounding.
