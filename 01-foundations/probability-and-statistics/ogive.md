---
tags:
  - status/seed
  - probability
related:
  - "[[frequency-polygon]]"
  - "[[frequency-distribution]]"
  - "[[cdf-and-quantiles]]"
  - "[[histogram]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — An ogive is a line graph of **cumulative** frequencies: plotted over class **boundaries**, its height at any point answers "how many values fall *below* this value?" — the empirical, discrete cousin of the [[cdf-and-quantiles|cumulative distribution function]].

---

## Intuition

A [[frequency-distribution|frequency table]] tells you how many values land *in* each class. An ogive answers a different question: how many land **below** a cutoff? You accumulate the counts as you sweep left to right, so the line only ever climbs, ending at the total *n*. Read off any x-value and the curve's height tells you how much of the data sits beneath it — perfect for percentiles and "how many under X?" questions.

## Mechanics

**Definition** — a line graph using **cumulative frequencies**: plot a point above each **class boundary** at a height equal to the number of values *at or below* that boundary, then connect the points.

- Horizontal axis: class **boundaries** (59.5, 69.5, 79.5, …) — *not* midpoints (this is the key contrast with the [[frequency-polygon]]).
- Vertical axis: **cumulative frequency**.
- The curve is **monotonically non-decreasing** and reaches *n* (the sample size) at the final boundary.

**Reading it** — Triola's Fig. 2-7 (women's pulses): find 79.5 on the x-axis, read up to the curve, across to the y-axis → **26**, meaning 26 pulses are below 79.5. That "count below a value" lookup is the ogive's entire job.

**Cumulative-frequency table** it's built from:

| Less than boundary | Cumulative frequency |
|---|---|
| 69.5 | 12 |
| 79.5 | 26 |
| 89.5 | 37 |
| … | … |

![[fig-2-7-ogive-women-pulses.png]]
*Placeholder — Figura 2-7: Ogive, women's pulses (add image)*

## In ML

**Empirical CDF** — an ogive is the sample **ECDF** (`statsmodels.distributions.ECDF`, `np.sort` + `np.arange/n`); it's the discrete estimate of the true [[cdf-and-quantiles|CDF]] and the basis for reading percentiles/quantiles straight off the curve.

**Distribution comparison tests** — comparing two ECDF curves is exactly what the **Kolmogorov–Smirnov** test formalizes (max vertical gap between two ogives), used to check whether two samples come from the same distribution.

## Exercises

**Basic** — Using the table above, at what height is the point plotted over the boundary 79.5, and what does it mean in words?

**Intermediate** — Why does an ogive use class *boundaries* while a [[frequency-polygon]] uses *midpoints*? Tie it to the meaning of "at or below."

**Advanced** — Explain how to read the **median** and the **third quartile** off an ogive, and connect this to inverting a [[cdf-and-quantiles|CDF]] to get quantiles.
