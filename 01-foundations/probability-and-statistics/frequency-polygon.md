---
tags:
  - status/seed
  - probability
related:
  - "[[histogram]]"
  - "[[frequency-distribution]]"
  - "[[relative-frequency-distribution]]"
  - "[[ogive]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A frequency polygon is a [[histogram]] redrawn as a **line**: connect the dots plotted above each [[frequency-distribution|class midpoint]] at its class frequency — same information as the histogram, but the line form makes it easy to **overlay and compare** two datasets on one set of axes.

---

## Intuition

Take a histogram and, instead of bars, put a single dot over each class **midpoint** at the height of its frequency, then join the dots. You get the same shape without the bars — and because it's just a line, you can stack two of them on the same axes to compare distributions at a glance. That's the whole reason it exists: bars overlap messily, lines don't.

## Mechanics

**Definition** — a line graph built from a [[frequency-distribution]]: plot a point directly above each **class midpoint (mark)** at a height equal to that class's frequency, then connect consecutive points with line segments.

**The tails** — extend a segment down to the horizontal axis on both ends (using the midpoint of the next empty class on each side), so the polygon **starts and ends on the axis** and encloses an area. This is what makes it a *polygon* rather than an open line.

- Horizontal axis: class **midpoints** (64.5, 74.5, 84.5, …) — not boundaries.
- Vertical axis: **frequencies**.

**Relative-frequency polygon** — identical construction, but the vertical axis uses [[relative-frequency-distribution|relative frequencies]] (proportions/percentages). Because the scale is normalized, you can compare **two datasets of different sizes** fairly on one graph — e.g. Triola's Fig. 2-6 overlays women's and men's pulses, and the men's line sitting **to the left** instantly shows men's pulses run lower. That comparison is invisible in the raw data tables.

![[fig-2-5-frequency-polygon-women-pulses.png]]
*Placeholder — Figura 2-5: Frequency polygon, women's pulses (add image)*

![[fig-2-6-relative-frequency-polygons.png]]
*Placeholder — Figura 2-6: Relative-frequency polygons, women vs. men (add image)*

## In ML

**Overlaid density comparison** — the relative-frequency polygon is the discrete ancestor of the **kernel density plot** (`sns.kdeplot`, `hist=False`); overlaying class distributions per feature is a standard EDA move to spot class separation before modeling.

**Normalize before comparing groups** — using *relative* frequency to compare unequal-sized groups is the same discipline as normalizing histograms (`density=True`) so distribution shape, not sample size, drives the comparison.

## Exercises

**Basic** — Given classes with midpoints 64.5, 74.5, 84.5 and frequencies 12, 14, 11, describe where the three points go and where the line touches the axis.

**Intermediate** — Why plot points over class *midpoints* rather than boundaries? What would shift if you used lower limits instead?

**Advanced** — You must compare pulse distributions for 40 women and 400 men on one graph. Explain why a *relative*-frequency polygon is required and what a plain frequency polygon would falsely suggest.
