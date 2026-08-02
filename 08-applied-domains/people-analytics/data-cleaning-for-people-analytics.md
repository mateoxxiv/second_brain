---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[people-analytics-project-framework]]"
  - "[[hr-data-types]]"
  - "[[hr-data-ethics]]"
  - "[[impact-evaluation-in-people-analytics]]"
  - "[[bias-in-people-analytics]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — Before any dashboard or model, run a fixed checklist over your HR data — duplicates, missing values, typos, formats, and period completeness — or every downstream conclusion inherits the dirt.

---

## Intuition

A dashboard built on a dirty base doesn't fail loudly — it fails quietly, by producing confident-looking numbers that are wrong. Cleaning isn't a detour before the "real" analysis; it's the step that decides whether the real analysis is even trustworthy.

This matters more in people analytics than in most domains: HR data is usually exported from another system (an HRIS, a survey tool), so formats, duplicates, and gaps arrive by default, not by exception.

## Mechanics

**Pre-analysis checklist** — five things to verify before touching a formula or chart:

1. **Duplicate records** — same ID or name appearing more than once.
2. **Missing data** — decide per field: delete the row, or backfill from source.
3. **Typographical errors** — inconsistent spelling that silently splits one category into two when filtering.
4. **Format validity** — each variable stored as the type it actually is (date as date, number as number).
5. **Completeness for the period** — e.g. analyzing a full year but only 10 months are loaded; that gap must be resolved, not ignored.

**Fixing each issue in Excel:**

| Problem | Technique | Why it works |
|---|---|---|
| Duplicate IDs | Pivot table: ID in rows, field set to **Count** (not Sum) | Any count > 1 flags a duplicate; filter the count column to isolate them |
| Inconsistent date/number formats | Select column → **Data → Text to Columns → Finish** | Forces Excel to re-parse the column into its real underlying type |
| Typos in text fields (e.g. city names) | Filter reveals every distinct spelling; copy the correct value over the wrong one | Filter afterward to confirm only one category remains |
| Corrupted/unreliable column (e.g. tenure) | Delete it, recalculate from a verified source field | Trusting a damaged field propagates its error everywhere it's used |
| Missing cells | Ask first: does the hypothesis depend on this field? | Strategic decision, not a technical one — only chase it down if it matters |

**Recalculating tenure from scratch** — if a "years of service" column has absurd values (e.g. someone hired in 2024 showing many years of tenure), don't patch it — rebuild it:

```
=YEARFRAC(start_date, TODAY(), 1)
```

`TODAY()` supplies the current date automatically; basis `1` uses actual/actual (real calendar days). The result is a decimal (e.g. 1.86 years) — round to one decimal from the Home tab, then double-click the cell's fill handle to extend the formula down the column.

**Text to Columns is the general-purpose fix** — the same three clicks (Data → Text to Columns → Finish) resolve postal codes stored as text, misformatted dates, and numbers imported as strings, all at once across an entire column — no manual retyping needed.

## In Practice

**This is a gate, not a formality** — [[impact-evaluation-in-people-analytics]] and [[bias-in-people-analytics]] both assume the underlying data is clean and comparable before their checks even make sense. An "inconclusive" hypothesis or a spurious cross-country comparison is frequently just this checklist skipped upstream.

**No step here has an automatic answer** — finding two IDs duplicated with different names, cities, and areas doesn't resolve itself; you decide whether to delete, validate against the source system, or ignore, based on judgment, not a formula.

**Recalculate over repair when trust is broken** — once a column shows physically impossible values, patching individual cells is slower and less reliable than deleting it and deriving it fresh from a verified source column.

## Exercises

**Basic** — A pivot table on `employee_id` set to Count shows three IDs with a count of 2. What does this tell you, and what does it *not* yet tell you about which record is correct?

**Intermediate** — A "city" column has 4 rows spelled "Bogotá" and 6 spelled "Bogota" (missing accent). After using a filter to find this, what are the exact steps to merge them into one category, and how do you confirm the fix worked?

**Advanced** — You inherit a dataset where "tenure" was manually entered and clearly wrong for ~15% of rows, but "hire_date" looks reliable. Design the fix using `YEARFRAC`, and explain why recalculating from `hire_date` is more defensible than trying to correct the bad tenure values row by row.
