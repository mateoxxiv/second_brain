---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[exit-interview-nlp-analysis]]"
  - "[[employee-satisfaction-survey-analysis]]"
  - "[[kpi-design]]"
  - "[[bias-in-people-analytics]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — A Likert scale turns a subjective perception into an ordered number (e.g. 1–5), which makes attitudes comparable across people and time — but it stays ordinal underneath, so averaging it is a modeling choice, not a mathematical guarantee.

---

## Intuition

You can't average "I feel good about my manager." You *can* average how someone rates that feeling on a fixed 1–5 scale. But the scale only orders the responses — it never proves that the gap between 3 and 4 equals the gap between 1 and 2. It looks like a number, which tempts everyone to treat it like one; formally, it's a labeled category with a direction.

## Mechanics

**Definition** — an ordinal scale with *k* anchored points (commonly 5 or 7), each end labeled to fix its meaning (e.g. "Strongly disagree" → "Strongly agree"), used to quantify a perception or attitude that has no natural numeric unit.

**Item vs. scale** — a single question is a *Likert-type item*. A composite built from several related items (summed or averaged per respondent) is a *Likert scale* proper. The composite is what you should trust for analysis — a single item is noisy; several items measuring the same underlying construct average out individual noise.

**The ordinal-vs-interval tension** — statistically, a Likert item is ordinal: order matters, equal spacing doesn't. Treating it as interval (computing a mean) is the field-standard shortcut, defensible for a *composite* of several items but shakier for a single 1–5 item with only 4–6 respondents.

| Property | What it means | Why it matters |
|---|---|---|
| Ordinal | Order is meaningful; spacing between points is not guaranteed equal | Median is always valid; mean requires assuming equal spacing |
| Anchored endpoints | Labels fix what each extreme means | Makes scores comparable across respondents |
| Odd vs. even point count | Odd includes a neutral midpoint; even forces a lean | A design choice that shifts the response distribution |
| Single item vs. composite | One question vs. several averaged items on the same construct | Composite is more reliable — check with Cronbach's alpha |

**Reliability check** — before trusting a composite score, Cronbach's alpha measures whether the items that make it up are internally consistent (i.e. actually measuring one underlying thing).

```python
import numpy as np

# 5 respondents x 4 items, all rating "engagement" 1-5
responses = np.array([
    [4, 5, 4, 5],
    [3, 3, 4, 3],
    [5, 5, 5, 4],
    [2, 3, 2, 3],
    [4, 4, 5, 4],
])

def cronbach_alpha(data: np.ndarray) -> float:
    n_items = data.shape[1]
    item_var_sum = data.var(axis=0, ddof=1).sum()
    total_var = data.sum(axis=1).var(ddof=1)
    return (n_items / (n_items - 1)) * (1 - item_var_sum / total_var)

print(cronbach_alpha(responses))   # > 0.7 is the usual "reliable enough" threshold
```

## In ML

**Feature engineering choice** — a Likert response can enter a model as an ordinal integer (1–5) or as one-hot categories. Ordinal encoding assumes the equal-spacing simplification above; one-hot avoids that assumption but loses the ordering information a linear model could otherwise exploit.

**Reliability gates trust** — Cronbach's alpha isn't optional polish: a composite Likert score with low alpha is a noisy, unreliable feature or target no matter how clean the rest of the pipeline is. Check it before feeding the composite into any downstream model.

**Likert complements, doesn't replace, open text** — a Likert item only measures the dimension you predefined. [[exit-interview-nlp-analysis]] pairs Likert composites with sentiment scores as two independent features precisely because neither instrument alone captures the full picture.

## Exercises

**Basic** — Five respondents rate "trust in leadership" as 4, 5, 3, 4, 5 on a 1–5 scale. Compute the mean and the median. Which statistic assumes equal spacing between points, and is that assumption guaranteed by the scale itself?

**Intermediate** — You have 4 Likert items all intended to measure "engagement" (each 1–5). Using the code above, explain why the composite (average across the 4 items per respondent) is more defensible than trusting any single item's raw score, and what a low Cronbach's alpha would tell you before you trust that composite.

**Advanced** — You're comparing two departments' "trust" Likert composite scores and considering a straightforward mean comparison (t-test). Given the ordinal nature of the underlying items, what alternative test would be more defensible, and why? Connect your answer to the comparability caution in [[bias-in-people-analytics]].
