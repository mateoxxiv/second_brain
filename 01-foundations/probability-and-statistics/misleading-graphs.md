---
tags:
  - status/seed
  - probability
related:
  - "[[principles-of-effective-graphs]]"
  - "[[common-misuses-of-statistics]]"
  - "[[bar-graph]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-5."
---

> **TL;DR** — Two tricks make an *arithmetically correct* graph lie: an axis that doesn't start at zero (exaggerates differences) and pictures scaled by area or volume for one-dimensional data (multiplies differences) — both work by decoupling what the eye measures from what the number says.

---

## Intuition

A graph can contain no false numbers and still deceive, because the eye reads *visual magnitude* (bar height, blob area), not the label. If the visual magnitude and the number stop being proportional, the graph lies while staying "technically correct." Triola isolates the two most common ways this happens. Both are honesty failures of the same kind flagged in [[common-misuses-of-statistics]], but here the medium is the picture, not the sampling.

The reflex to build: don't read the labels first — ask *does the ink track the numbers?*

## Mechanics

**Trick 1 — nonzero baseline ("suppressed zero").** When a bar/line axis starts above zero, the eye compares the *drawn* heights, but those heights are proportional to (value − baseline), not to value. A small real gap becomes a visually huge one.

*Triola's Fig. 2-1 (CNN / Terri Schiavo poll):* Republicans 54%, Democrats 62%, Independents 54%. With the y-axis starting at **53%**, the Democrat bar looks *many times* taller than the others — creating the false impression that far more Democrats agreed. Redrawn from **0** (Fig. 2-9), the three bars are nearly equal, which is the truth. The exaggeration factor is roughly (spread)/(spread from baseline): a real 8-point gap on a 53–63 window reads like the *whole* bar.

**Trick 2 — area/volume for 1-D data (pictograms).** Replace bars with drawings (money bags, cubes, people). If the artist scales *every dimension* by the ratio, area grows as the ratio² and volume as the ratio³, so the picture overstates a one-dimensional quantity.

| You double a… | Linear ×2 | Area becomes | Volume becomes |
|---|---|---|---|
| Square side | 2 | **4×** | — |
| Cube edge | 2 | — | **8×** |

*Triola's Fig. 2-10 (income by education):* postgraduate \$74,602 vs. no-diploma \$18,734 is about a **4×** ratio. Drawn as 3-D cubes scaled on each edge, the postgraduate cube has ~4³ ≈ **64×** the volume — the eye "sees" a 64-fold gap for a 4-fold fact. The honest fix (Fig. 2-10c) is a plain [[bar-graph]] from zero.

```python
# why a 4x number looks like ~64x when drawn as a scaled cube
ratio = 74602 / 18734          # ~3.98  (the true 1-D fact)
volume_ratio = ratio ** 3      # ~63.0  (what the eye reads from the cube)
print(round(ratio, 2), round(volume_ratio, 1))
```

**Two-question audit (Triola's checklist):**
1. Does an axis fail to start at zero, so differences are exaggerated?
2. Is area or volume used to depict data that are really one-dimensional?

## In ML

**Truncated y-axes in results plots** — the single most common way accuracy/loss curves oversell a gain: a y-axis from 0.90–0.92 turns a 1-point bump into a cliff. This is the nonzero-baseline trick in a paper figure — see the reporting caveat in [[principles-of-effective-graphs]].

**Bubble charts inherit the pictogram trap** — encoding a scalar as a circle's *radius* makes it read as area (radius²); when a marker should encode magnitude, map the value to **area**, not radius, or differences quietly square themselves.

## Exercises

**Basic** — A bar chart shows monthly revenue of \$102k, \$104k, \$103k with the y-axis starting at \$100k. Why does it mislead, and what one change fixes it?

**Intermediate** — Quantity B is 3× quantity A. An artist draws A and B as squares, scaling *each side* by 3. By what factor do the square *areas* differ, and what false impression does the reader get?

**Advanced** — Give a case where a nonzero baseline is *legitimate* (not deceptive), and state the rule that separates honest axis-cropping from the Fig. 2-1 abuse.
