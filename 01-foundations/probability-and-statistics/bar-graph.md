---
tags:
  - status/seed
  - probability
related:
  - "[[pareto-chart]]"
  - "[[pie-chart]]"
  - "[[histogram]]"
  - "[[data-types-and-levels-of-measurement]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A bar graph uses equal-width bars to show frequencies of **qualitative (categorical)** data — the categorical counterpart of the [[histogram]] — and a *multiple* bar graph places several bar sets side by side to compare datasets.

---

## Intuition

When your data are **categories** (job source, gender, brand) rather than numbers, you can't bin them into ranges — so instead of a [[histogram]] you draw one bar per category, its height the count. The bars can have gaps because categories don't touch on a number line (unlike histogram classes, which do). Add a second colored bar per category and you can compare two groups at once.

## Mechanics

**Definition** — equal-width bars showing frequencies (or [[relative-frequency-distribution|relative frequencies]]) of **[[data-types-and-levels-of-measurement|qualitative]]** data.

- Vertical axis: **frequencies or relative frequencies**.
- Horizontal axis: the **categories** (nominal/ordinal labels).
- Bars may be **separated by gaps or not** — unlike the [[histogram]], where touching bars carry the meaning that classes are contiguous.

**Histogram vs. bar graph** — same visual, different data type: histogram = quantitative (ordered numeric classes, bars touch); bar graph = qualitative (categories, gaps allowed).

**Multiple bar graph** — two or more sets of bars for comparing datasets. Triola's Example 6 (Minitab): median income of men vs. women across years — men's bars are consistently taller, both rise over time, and the **shrinking height ratio** left-to-right suggests the gender income gap is narrowing.

![[minitab-multiple-bar-graph-income.png]]
*Placeholder — Minitab multiple bar graph: median income by gender and year (add image)*

## In ML

**Categorical EDA** — `sns.countplot` / `value_counts().plot.bar` is the first look at any categorical feature: spotting **class imbalance**, rare categories, and label errors before encoding.

**Grouped bars for slice comparison** — a multiple/grouped bar graph (`hue=` in seaborn) compares a metric across a categorical dimension, the standard way to inspect subgroup performance or fairness across cohorts.

## Exercises

**Basic** — You survey favorite fruit: apple 12, banana 7, cherry 5. Describe the bar graph — what's on each axis and how many bars?

**Intermediate** — Explain why a [[histogram]]'s bars touch but a bar graph's may have gaps. What data-type fact does the touching encode?

**Advanced** — Design a multiple bar graph comparing model accuracy across 3 datasets for 2 algorithms. What comparison does the eye make left-to-right, and how could bar ordering mislead?
