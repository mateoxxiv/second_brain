---
tags:
  - status/seed
  - probability
related:
  - "[[bar-graph]]"
  - "[[pie-chart]]"
  - "[[data-types-and-levels-of-measurement]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A Pareto chart is a [[bar-graph]] for qualitative data whose bars are sorted in **descending frequency**, so the most important categories line up on the left — it directs attention to what matters most.

---

## Intuition

An ordinary [[bar-graph]] leaves categories in whatever order they came. A Pareto chart **sorts them tallest-first**, so your eye lands immediately on the dominant category. That ordering *is* the message: it makes the "vital few vs. trivial many" pattern (the Pareto principle) visible at a glance.

## Mechanics

**Definition** — a bar graph for **[[data-types-and-levels-of-measurement|qualitative]]** data with bars arranged in **descending order of frequency** (tallest on the left, decreasing to the right).

- Vertical axis: **frequencies and/or relative frequencies**.
- Horizontal axis: the **categories**, reordered by height.
- The defining feature is the **sort**, not the bars themselves.

Triola's Example 7 (Minitab): how people found jobs — the **networking** bar towers over job boards and newspaper ads, so the chart's takeaway is "work your network first." Same data as the [[pie-chart]] in Example 8, drawn to emphasize *rank* instead of *share*.

![[pareto-chart-job-search.png]]
*Pareto chart — how people found jobs (illustrative, networking = 61% per Triola): bars sorted tallest-first.*

## In ML

**Prioritization / error analysis** — sorting failure categories by frequency is exactly Pareto logic: fix the tallest bar first for the biggest gain. Standard in **model error analysis** and triaging label-noise sources.

**Feature-importance and cardinality** — a descending bar chart of `feature_importances_` or category counts is a Pareto chart, surfacing the **few features/categories that dominate** and the long tail you might prune or group into "other."

## Exercises

**Basic** — Given complaint counts (billing 30, shipping 18, quality 9, other 3), sketch the Pareto chart order and name the leftmost bar.

**Intermediate** — Compare a Pareto chart with the [[pie-chart]] of the same data (Triola's Examples 7 vs. 8). What does each emphasize better?

**Advanced** — When would sorting bars by frequency *mislead* — e.g. if categories are **ordinal** (small/medium/large)? Argue whether a Pareto sort is appropriate there.
