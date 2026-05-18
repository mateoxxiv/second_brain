---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[people-analytics]]"
  - "[[kpi-design]]"
  - "[[hr-data-ethics]]"
  - "[[platzi-people-analytics-excel]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — People Analytics is not a dashboard or a tool — it's a data-driven culture applied at every stage of the employee lifecycle, from recruiting to exit.

---

## Intuition

Think of a company as a product. Products have a user journey: awareness → acquisition → activation → retention → churn. Employees have the exact same structure: attraction → onboarding → development → retention → offboarding. People Analytics puts measurement at every stage of that journey.

The key mindset shift: data doesn't replace human judgment — it *informs* it. "I think this candidate is good" becomes "candidates with this profile have a 15% lower churn rate in the first six months."

**What it is NOT** — four common misconceptions:

- Not just buying software. You can run meaningful PA projects in Excel.
- Not just building dashboards. A dashboard that doesn't trigger action is decoration.
- Not collecting data without a question. Data without a hypothesis is noise.
- Not only for data scientists. Simple analyses run by HR professionals create real value.

## Mechanics

**The employee lifecycle as an analytics framework:**

| Stage | Question PA answers | Key data source |
|---|---|---|
| Attraction | Which channels bring the best candidates? | Job board conversion, referral quality |
| Onboarding | How fast do new hires become productive? | 30/60/90-day performance scores |
| Development | Where are the competency gaps? | Skill assessments, training completion |
| Retention | Who is at risk of leaving? | Engagement surveys, tenure, salary band |
| Offboarding | Why did they leave? | Exit interview themes, manager ratings |

**Data-driven culture prerequisites:**
1. Leadership buys in — analytics must have a seat at the decision table
2. Data quality — HRIS records, survey responses, performance reviews must be clean
3. Privacy by design — see [[hr-data-ethics]]

```python
# Lifecycle stage → KPI mapping
lifecycle_kpis = {
    "attraction":  ["time_to_fill", "offer_acceptance_rate", "source_quality"],
    "onboarding":  ["ramp_time_days", "day_90_performance_score", "early_attrition_rate"],
    "development": ["training_completion_rate", "promotion_rate", "skill_gap_score"],
    "retention":   ["eNPS", "absenteeism_rate", "flight_risk_score"],
    "offboarding": ["voluntary_attrition_rate", "exit_interview_themes"],
}

for stage, kpis in lifecycle_kpis.items():
    print(f"{stage}: {', '.join(kpis)}")
```

## In ML

**Attrition prediction (retention stage)** — the lifecycle framework tells you *when* to intervene. A flight-risk model trained on engagement scores, tenure, and manager ratings fires at the retention stage — not at offboarding, when it's too late. See [[people-analytics]] for the classification framing.

**NLP on exit interviews (offboarding stage)** — exit interviews are unstructured text. Embedding + clustering extracts the dominant themes: "manager relationship," "growth opportunities," "compensation." This converts qualitative lifecycle data into quantitative signals.

**Onboarding optimization** — ramp time (days to productivity) can be modeled as a regression target. Features: role complexity, manager experience, team size, remote vs. on-site. Output informs onboarding program redesign.

## Exercises

**Basic** — Map three KPIs to each lifecycle stage for a 200-person tech company. What data source would feed each KPI?

**Intermediate** — A company sees high early attrition (departures in the first 90 days). Which lifecycle stage does this problem belong to? Which KPIs would you instrument first, and what hypothesis would you form before analyzing?

**Advanced** — Design an end-to-end People Analytics pipeline for the retention stage: define the ML task (features, target, eval metric), the data sources required, the privacy constraints that apply, and the business action triggered by the model output.
