---
tags:
  - status/seed
  - probability
related:
  - "[[common-misuses-of-statistics]]"
  - "[[pie-chart]]"
  - "[[characteristics-of-data]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A good statistical graph makes the viewer focus on the **true nature of the data**, not on decoration — Tufte's principles (maximize data-ink, never distort, avoid chartjunk) are the design side of the same honesty demanded by [[common-misuses-of-statistics]].

---

## Intuition

Choosing *which* graph is half the job; drawing it honestly is the other half. A graph can be technically a "line graph" yet lie — by distorting scale, wasting ink on 3-D effects, or dressing one-dimensional data as areas. Edward Tufte's design rules, which Triola summarizes, all reduce to one idea: **let the data, and only the data, carry the message.**

## Mechanics

**Tufte's principles (Triola §2-4):**

| Principle | What it means |
|---|---|
| Small data → table, not graph | For ≤ 20 values, a table beats a graph. |
| Focus on the data | The eye should land on the data's nature, not on attractive-but-distracting design. |
| Don't distort | Build the graph to reveal the true data; no misleading scales. |
| Maximize **data-ink** | Almost all ink should represent data, not decoration. |
| No chartjunk | Avoid diagonal lines, dots, shading that create a false sense of motion. |
| No area/volume for 1-D data | Don't use pictures scaled by area/volume to show one-dimensional quantities (e.g. money-bill drawings for budgets). |
| Never use [[pie-chart\|pie charts]] | They waste ink and lack a proper scale. |

**A creative counter-example** — Triola's Example 12 / Fig. 2-8 (Firebrand vs. Speedster car reliability): a compact grid of shaded cells packs *many* variables (repair categories × years × two cars) into a simple, honest display — showing that originality *serves* clarity rather than fighting it.

![[car-reliability-grid.png]]
*Figura 2-8 — car reliability grid (schematic): black = poor, gray/white = good; Firebrand is cleaner than Speedster overall.*

**The point of graphs (conclusion)** — graphs are tools to **describe, explore, and compare** data: describe via [[characteristics-of-data|CVDVT]], explore by hunting revealing patterns (the [[scatterplot|cricket scatterplot]]), compare via overlaid [[frequency-polygon|relative-frequency polygons]].

## In ML

**Honest reporting of results** — the same rules govern ML dashboards and papers: truncated y-axes exaggerate accuracy gains, dual axes imply false correlation — chartjunk in a results plot is a [[common-misuses-of-statistics|misuse of statistics]].

**Data-ink as a review habit** — favoring clean, high-data-ink plots (small multiples, direct labels) makes model diagnostics readable and reproducible, not decorative.

## Exercises

**Basic** — You have 8 data values to present. Per Tufte, should you use a graph or a table? Why?

**Intermediate** — Give two concrete ways a bar chart's *design* (not its data) can mislead a viewer, and how to fix each.

**Advanced** — Critique a real infographic you've seen against Tufte's list: identify its chartjunk, any distortion, and redesign it to maximize data-ink.
