---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[people-analytics]]"
  - "[[data-driven-culture]]"
  - "[[people-analytics-employee-lifecycle]]"
  - "[[kpi-design]]"
  - "[[platzi-people-analytics-excel]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — Classifying HR data by type (quantitative vs qualitative) and category before analysis is not housekeeping — it determines which statistical tools are valid and whether results can be trusted.

---

## Intuition

Using the wrong statistical tool on the wrong data type is like averaging zip codes — the math runs but the result is nonsense. In People Analytics, whether your data is a number, a yes/no, or a string of text determines which analyses are valid. A mean salary is meaningful; a mean "reason for leaving" is not.

The classification also shapes how findings land with non-technical stakeholders: numeric results feel objective, qualitative ones feel like stories — both are evidence, both require different framing.

## Mechanics

**Base taxonomy:**

| Type | Subtype | HR example | Valid operations |
|---|---|---|---|
| Quantitative | Integer | Headcount, years in role | Mean, correlation, regression |
| Quantitative | Real | Salary, eNPS score | Mean, std dev, histogram |
| Quantitative | Logical (bool) | Benefits used? Active employee? | Frequency, proportion |
| Qualitative | Categorical | Department, exit reason | Mode, frequency, chi-square |
| Qualitative | Free text | Survey comments, interviews | NLP, sentiment, topic modeling |

**HR data categories present in most projects:**

- **Demographics** — age, gender, marital status. Usually centralized in payroll. Base for segmenting every analysis.
- **Performance** — KPIs, OKRs, evaluation scores. Type depends on methodology (numeric if scored, text if narrative).
- **Compensation** — salary, bonuses, commissions, benefits usage. Most structured and reliable category.
- **Engagement** — eNPS (1–10 scale), climate surveys. eNPS adapts the customer NPS logic to internal workforce satisfaction.
- **Training & development** — program usage, training hours (internal/external), individual progress rates.
- **Turnover** — exit reason (qualitative), rotation rate by area (quantitative), average tenure (quantitative).

**Data readiness checklist** — before any analysis, verify for each dataset:
1. Type correctly identified
2. Source known and trustworthy
3. Reliability confirmed (consistent measurement over time)
4. Cleaning needed? (nulls, encoding errors, duplicates)

**Collection principles from successful projects:**
- Centralize sources — avoid hunting dispersed files each cycle
- Digital-first — paper-based data bottlenecks every downstream phase
- Keep collection simple — complexity in collection predicts failure in analysis

## In ML

**Feature engineering starts here** — numeric features enter models directly; categoricals need encoding (one-hot, ordinal, target encoding); free text needs embedding or vectorization. Misclassifying a categorical as numeric (e.g., treating department codes as integers) silently corrupts model training.

**eNPS as a regression target** — the 1–10 score is quantitative and can be modeled as a regression target with demographics and performance as predictors. Classic People Analytics question: "which factors predict low engagement?"

**Qualitative → structured via NLP** — exit interview text can be converted into structured signals using sentiment analysis, topic extraction, or embedding similarity — essentially a [[rag]] pattern applied to internal HR data.

## Exercises

**Basic** — Classify each: (a) employee age, (b) reason for leaving, (c) whether onboarding was completed, (d) eNPS score. State the type and one valid statistical operation for each.

**Intermediate** — You want to test whether compensation level correlates with eNPS. Both variables are numeric — which test is appropriate? What changes if you collapse eNPS into three categories (promoter / neutral / detractor)?

**Advanced** — Design a pipeline to convert 500 free-text exit interview responses into a structured categorical feature. Which NLP techniques would you use, and how would you validate the resulting categories are meaningful?
