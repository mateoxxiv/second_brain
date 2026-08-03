---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[data-cleaning-for-people-analytics]]"
  - "[[hr-dashboard-in-excel]]"
  - "[[kpi-design]]"
  - "[[bias-in-people-analytics]]"
  - "[[people-analytics-employee-lifecycle]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — Merge survey responses into your HR base with a shared ID (VLOOKUP), then read them with averages instead of sums, a heat map to spot weak spots, an NPS donut chart for loyalty, and an external benchmark before calling any number "good" or "bad."

---

## Intuition

A satisfaction survey almost never arrives already sitting inside your main HR base — it's a separate export, differently shaped. Before any insight, you have a plumbing problem: get both files to share rows through a common key. Once merged, the second trap is drowning in decimals — a table of raw scores tells you nothing until it's aggregated, colored, and compared to something outside itself.

## Mechanics

**Step 1 — merge with VLOOKUP**, using employee ID as the shared key:

```
=VLOOKUP(lookup_value, table_array, col_index_num, 0)
```

| Argument | Meaning |
|---|---|
| `lookup_value` | The shared key — usually employee ID |
| `table_array` | The range in the *other* file holding the data to pull in |
| `col_index_num` | Which column to return, counted from 1 (not by letter) |
| `0` | Forces exact match — without it, VLOOKUP silently returns approximate, wrong matches |

**Step 2 — aggregate with a pivot table.** Excel defaults pivot values to *Sum*; for survey variables (trust, recognition, camaraderie) switch each field to **Average**, and reduce decimals to keep the table readable. Break down by department to see which one drags the company average down.

**Step 3 — highlight with a heat map.** Home → Conditional Formatting → Color Scales over the pivot output. Low scores render in warm colors, so the weakest cells are visible before reading a single number.

**Step 4 — compute NPS.** Bucket each response into detractors / passives / promoters (typically 0–6 / 7–8 / 9–10 on a 0–10 loyalty scale), count the distribution with a pivot table, and:

$$\text{NPS} = \%\text{promoters} - \%\text{detractors}$$

Visualize the three buckets as a donut chart, with colors matched to each group's meaning (e.g. warm for detractors, cool for promoters).

**Step 5 — benchmark externally.** An internal average means little in isolation — compare it against same-sector, same-geography companies before deciding whether a score is actually a problem. This is exactly the comparability check in [[bias-in-people-analytics]].

```python
import pandas as pd

hr_base = pd.DataFrame({"id": [1, 2, 3], "dept": ["Sales", "Eng", "Sales"]})
survey  = pd.DataFrame({"id": [1, 2, 3], "trust": [8, 6, 9], "nps_score": [9, 5, 10]})

merged = hr_base.merge(survey, on="id")                      # VLOOKUP, but for the whole table at once
dept_avg = merged.groupby("dept")["trust"].mean().round(1)    # pivot table "average" step

def nps_bucket(score: int) -> str:
    if score >= 9: return "promoter"
    if score >= 7: return "passive"
    return "detractor"

buckets = merged["nps_score"].apply(nps_bucket).value_counts(normalize=True) * 100
nps = buckets.get("promoter", 0) - buckets.get("detractor", 0)
```

## In ML

**Merges at scale** — VLOOKUP is a manual, single-key version of what `pandas.merge` or a SQL `JOIN` do systematically: match on a shared key, pull columns across. The logic is identical; a DataFrame merge just scales past the row-by-row limit where VLOOKUP becomes slow and error-prone.

**NPS as binning** — collapsing a continuous 0–10 score into detractor/passive/promoter is the same operation as binning a continuous variable into ordinal classes, e.g. turning a regression target into a classification target elsewhere in a pipeline.

**Heat maps generalize** — the "color flags what to look at first" idea behind a pivot heat map is the same one behind correlation matrices and confusion matrices in any ML report — draw the eye to the extremes before the reader parses a single cell.

## Exercises

**Basic** — Two sheets share an `id` column. Write the exact VLOOKUP formula to pull the 4th column of `Survey!A1:D200` into a base sheet, matched by `id` in column A. Explain what each argument does.

**Intermediate** — A department's average trust score is 3.2/5 against a 4.1/5 company average. Using this note's Step 5 and [[bias-in-people-analytics]], what two questions must be answered before concluding that department has a real problem?

**Advanced** — Design the full pipeline from two raw files (HR base + survey export) to a one-page slide showing department-level trust/recognition/camaraderie averages, one heat map, and one NPS donut. Order every step from this note, and mark where [[hr-dashboard-in-excel]]'s pivot-table and slicer techniques take over.
