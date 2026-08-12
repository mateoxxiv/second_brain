---
tags:
  - status/seed
  - probability
related:
  - "[[pareto-chart]]"
  - "[[bar-graph]]"
  - "[[relative-frequency-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A pie chart shows qualitative data as slices of a circle sized by each category's [[relative-frequency-distribution|relative frequency]] — good for parts-of-a-whole, but Triola and Tufte consider it a **weak** graph compared with a [[pareto-chart]].

---

## Intuition

Cut a circle into wedges, one per category, each wedge's angle proportional to that category's share of the total. It communicates "what fraction of the whole" well — but the human eye compares **angles and areas** poorly, so ranking or precisely comparing slices is hard. That's why a sorted [[bar-graph]] usually beats it.

## Mechanics

**Definition** — a circle divided into slices whose sizes are proportional to the **frequency counts** (equivalently, relative frequencies) of the categories.

**Slice angle** — central angle = relative frequency × 360°. Triola's Example 8: networking is **61%** of job finds, so its slice spans

$$0.61 \times 360° \approx 220°.$$

![[pie-chart-job-search.png]]
*Pie chart — same job-search data as the Pareto chart (illustrative): networking's 61% slice spans ≈220°.*

**Same data, weaker graph** — Example 8 uses the same job-search data as the [[pareto-chart]] in Example 7. Triola's verdict: the **Pareto chart is better** for showing relative sizes, because comparing bar heights is easier than comparing wedge angles.

**Tufte's stance** — in his design principles Triola quotes, Tufte goes further: *"never use pie charts"* — they spend ink on non-data elements and lack a proper scale.

## In ML

**Rarely the right tool** — for class distribution or category shares, a **bar/count plot** conveys magnitude and rank more accurately; pie charts appear in dashboards but are discouraged in analytical EDA for the same angle-perception reason.

**Composition only** — the one defensible use is a **single parts-of-a-whole** snapshot with very few categories; beyond ~4 slices, switch to bars.

## Exercises

**Basic** — A category holds 25% of the data. What central angle does its slice span?

**Intermediate** — Given networking 61%, referrals 20%, job board 12%, ads 7%, compute each slice's central angle and check they sum to 360°.

**Advanced** — State Tufte's objections to pie charts and construct a case with 6 near-equal categories where a pie chart genuinely misleads but a [[pareto-chart]] does not.
