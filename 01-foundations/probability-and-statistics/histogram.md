---
tags:
  - status/seed
  - probability
related:
  - "[[frequency-distribution]]"
  - "[[relative-frequency-distribution]]"
  - "[[characteristics-of-data]]"
  - "[[normal-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-3."
---

> **TL;DR** — A histogram is the *graphical version of a [[frequency-distribution]]*: adjacent, equal-width bars whose heights are class frequencies — its whole purpose is to reveal the **shape** of the data's distribution, not to be drawn for its own sake.

---

## Intuition

A [[frequency-distribution|frequency table]] already tells you how many values fall in each class — a histogram just *draws* it so your eye can read the **shape** instantly: where the data centers, how it spreads, whether it's symmetric or skewed, and whether an outlier sticks out. Derived from [[triola-estadistica|Triola Ch. 2]], the message is the same as for the table: the point is *understanding the data*, not the picture. Software builds histograms automatically; your job is to *interpret* one.

## Mechanics

**Definition** — a bar graph where bars have **equal width** and sit **directly adjacent (no gaps)**. Horizontal axis = classes of quantitative values; vertical axis = frequencies; bar height = that class's frequency.

**Why the bars touch (the class-boundary point — emphasized):** the gaps between [[frequency-distribution|class limits]] (…69, 70…) are *artificial*. It's the [[frequency-distribution|class boundaries]] (59.5, 69.5, 79.5, …) that are contiguous — the upper boundary of one class *is* the lower boundary of the next. Because boundaries leave no gap, the bars leave no gap. This is exactly why boundaries, not limits, define where bars meet.

**Labeling the horizontal axis** — three options, and the choice matters:

| Label used | Correct? |
|------------|----------|
| **Class boundaries** (59.5, 69.5, …) | ✅ technically correct — bars meet exactly at them |
| **Class midpoints / marks** (64.5, 74.5, …) | ✅ technically correct — one mark centered under each bar |
| **Lower [[frequency-distribution|class limits]]** (60, 70, …) | ⚠️ introduces a small error (shifts the bars) |

> **Rule:** label the horizontal axis with **class boundaries or class marks** (never lower limits); label the vertical axis with **class frequencies**; label *both* axes clearly.

**Relative-frequency histogram** — identical shape and horizontal scale, but the vertical axis shows [[relative-frequency-distribution|relative frequencies]] (proportions/percentages) instead of raw counts.

**Interpreting a histogram (CVDOT)** — read [[characteristics-of-data|Center, Variation, Distribution shape, Outliers]]. Triola's Fig. 2-3 (women's pulses): centered around **80**, values span roughly **60–130**, shape is **left-heavy (skewed)**, and the lone far-right bar flags a dubious **125 bpm** outlier.

**Checking for normality** — a [[normal-distribution|normal distribution]] graphs as a **symmetric bell**: frequencies rise to a peak then fall, with the left half a near mirror of the right. Many statistical procedures require approximately normal data, and a histogram is the quick visual check of that assumption.

## In ML

**Histograms are the first EDA move** — plotting each feature's histogram exposes skew, multimodality, and outliers before modeling; `matplotlib.hist` / `numpy.histogram` bin exactly as steps 1–2 of building a [[frequency-distribution]].

**Normality checks gate classical methods** — many tests and models assume near-normal features; the histogram (and its cousin the Q–Q plot) is the fast eyeball check, prompting log/Box–Cox transforms when the bell is skewed.

**Bin width is a bias–variance knob** — too few bins oversmooth and hide structure; too many turn noise into fake peaks — the same tradeoff as kernel-density bandwidth and model flexibility.

## Exercises

**Basic** — Given classes with boundaries 59.5, 69.5, 79.5 and frequencies 12, 14, 11, describe the histogram: what goes on each axis, and where do the first two bars meet?

**Intermediate** — Why should the horizontal axis use class boundaries rather than lower class limits? What visual error does using limits introduce?

**Advanced** — Two histograms of the same data use 5 vs. 40 bins. Explain how each can mislead, and connect the bin-count choice to the [[normal-distribution|normality]] judgment and to overfitting/underfitting.
