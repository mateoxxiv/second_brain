---
tags:
  - status/seed
  - probability
related:
  - "[[correlation-and-regression]]"
  - "[[time-series-graph]]"
  - "[[data-types-and-levels-of-measurement]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A scatterplot graphs **paired** quantitative data (x, y) as points on two axes; the pattern of points reveals whether the two variables are **related** — the visual gateway to [[correlation-and-regression|correlation and regression]].

---

## Intuition

When each observation carries **two** numbers — a cricket's chirp rate *and* the temperature — plot one against the other and let the cloud of points speak. If the points drift upward together, the variables move together; if they scatter with no trend, they don't. It's the fastest way to *see* a relationship before quantifying it.

## Mechanics

**Definition** — a plot of **paired (x, y)** quantitative data: horizontal axis = first variable, vertical axis = second. Each observation is **one point**.

- The **pattern** of points signals the relationship: rising cloud → positive association, falling → negative, shapeless blob → none. (Formalized later as [[correlation-and-regression|correlation]], Triola §10-2.)

Triola's Example 9 (crickets): chirps/minute vs. temperature (°F) show a clear upward trend — more chirps at higher temperatures, so crickets work as thermometers.

![[scatterplot-crickets-temperature.png]]
*Scatterplot — cricket chirps vs. temperature (illustrative): points rise together, a clear positive association.*

**⚠️ Watch for clusters/gaps** — Example 10 (penny weight vs. mint year) shows **two clusters split by a gap**: pre-1983 pennies are 97% copper, post-1983 are 97% zinc. Treating them as one population fakes a weight–year relationship; split by group and *within each* there's **no** relationship. Lesson: a scatterplot can expose **hidden subpopulations** that make a spurious trend.

## In ML

**Feature–target and feature–feature relationships** — `plt.scatter` / `sns.scatterplot` is core EDA: seeing linearity/nonlinearity before fitting **[[correlation-and-regression|regression]]**, and pairwise scatter matrices for multicollinearity.

**Clusters, confounding, and Simpson's paradox** — the two-cluster penny example is a **confounding / spurious-aggregate** warning: an apparent overall trend *vanishes* once you condition on a hidden group (metal composition). Its stronger cousin is **Simpson's paradox**, where the trend *reverses* within groups. Both are exactly what `hue=` coloring or clustering surfaces.

## Exercises

**Basic** — For paired data (1,2), (2,4), (3,5), (4,8), plot the points and state whether the association looks positive or negative.

**Intermediate** — Sketch a scatterplot with no linear pattern but an obvious **curved** one. Why would a single correlation number understate the relationship?

**Advanced** — Explain, using the penny example, how a scatterplot can show a strong overall trend that disappears within subgroups. Name the statistical phenomenon and how you'd detect it.
