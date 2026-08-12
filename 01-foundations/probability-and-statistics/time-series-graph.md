---
tags:
  - status/seed
  - probability
related:
  - "[[scatterplot]]"
  - "[[characteristics-of-data]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-4."
---

> **TL;DR** — A time-series graph plots data collected at successive **points in time** against time on the horizontal axis, revealing **trends over time** — the one distribution feature (the "T" in CVDVT) that a [[histogram]] cannot show.

---

## Intuition

Some data come with timestamps — a stock index each year, temperature each hour. Put **time on the x-axis** and the measurement on the y-axis, connect the points, and the *trend* appears: rising, falling, cyclic, or flat. A [[histogram]] deliberately throws away order, so it can never show change over time; a time-series graph exists precisely to recover it.

## Mechanics

**Definition** — a graph of **time-series data** (values gathered at successive times): horizontal axis = **time**, vertical axis = the measured variable, points usually connected by a line.

- It's essentially a [[scatterplot]] whose x-variable is time, with points joined to emphasize sequence.
- Reveals **trend, seasonality, and change points** — none visible in a binned distribution.

Triola's Example 11 (SPSS): yearly highs of the **Dow Jones Industrial Average** — a steady climb 1980–2007, then less consistent highs in later years.

![[spss-time-series-djia.png]]
*Placeholder — SPSS time-series graph: DJIA annual highs (add image)*

**CVDVT connection** — Triola's checklist for describing data is **Center, Variation, Distribution, outliers, Time**. The final **Time** element only applies to time-ordered data, and the time-series graph is the tool that exposes it — which is why the [[characteristics-of-data|histogram checklist]] drops it.

## In ML

**Time-series EDA** — a line plot over time is the first step in any forecasting task: eyeballing **trend, seasonality, and stationarity** before ARIMA / Prophet / RNN modeling (`df.plot()` on a datetime index).

**Order matters — no shuffling** — because the x-axis is time, temporal data must **not** be randomly shuffled for train/test splits; you split chronologically, a discipline the time-series graph makes intuitive.

## Exercises

**Basic** — You have monthly sales for 2 years. Describe the axes of the time-series graph and what a rising line would mean.

**Intermediate** — Why can a [[histogram]] never reveal a trend that a time-series graph shows? Tie it to what binning discards.

**Advanced** — A time-series shows a repeating yearly bump. Name the pattern, explain why a plain [[scatterplot]] without the time axis would hide it, and how you'd model it.
