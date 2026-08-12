---
tags:
  - status/seed
  - probability
related:
  - "[[stem-and-leaf-plot]]"
  - "[[histogram]]"
  - "[[frequency-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A dot plot marks each data value as a dot along a number line, **stacking** dots for repeated values — it shows the distribution's shape while, unlike a [[histogram]], **retaining every original value** so the raw list can be reconstructed.

---

## Intuition

Draw a number line and drop one dot on it for every reading; when a value repeats, pile the dots on top of each other. The height of each stack *is* the frequency of that value, and because each dot is one observation, nothing is lost — you can read the exact data back off the picture. It's the quickest hand-drawn way to see shape for a small dataset.

## Mechanics

**Definition** — each value is plotted as a **dot** above its position on a horizontal scale of values; **equal values stack** vertically. Stack height = frequency of that exact value.

**Key property — lossless.** Unlike a [[histogram]] or [[frequency-distribution]] (which bin values into ranges and discard the individual numbers), a dot plot keeps **one dot per observation**, so the **original data list is recoverable**. It shares this virtue with the [[stem-and-leaf-plot]].

Triola's Example 4 (women's pulses via Minitab): three stacked dots above 60 mean the values 60, 60, 60; four dots above 64 mean four readings of 64 bpm.

![[dot-plot-women-pulses.png]]
*Dot plot, women's pulses (Triola's data): three dots over 60, four over 64, and each stack's height is that value's frequency.*

**When to use** — best for **small** datasets; with many values or a wide range the stacks get unwieldy and a [[histogram]] reads better.

## In ML

**Small-sample distribution view** — for tiny datasets a dot plot (or its jittered `sns.stripplot` / `swarmplot` cousin) shows every point, avoiding the binning artifacts a [[histogram]] introduces when *n* is small.

**Individual points matter** — because no information is discarded, dot plots make **outliers and exact duplicates** visible in a way binned graphs hide — useful when auditing data quality before training.

## Exercises

**Basic** — A dot plot shows 3 dots over 60 and 4 over 64. Write out the raw values these represent.

**Intermediate** — Explain why a dot plot lets you reconstruct the original data but a [[histogram]] does not. What is traded away for that?

**Advanced** — For a dataset of *n* = 5000 continuous values, argue why a dot plot fails and what graph you'd use instead — connect it to the bin/bandwidth tradeoff.
