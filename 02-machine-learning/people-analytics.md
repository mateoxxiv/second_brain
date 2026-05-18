---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[probability-fundamentals]]"
  - "[[probability-distributions]]"
  - "[[cdf-and-quantiles]]"
  - "[[general-vector-spaces]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
  - "McKinsey & Harvard Business Review — People Analytics impact data"
---

> **TL;DR** — People Analytics is applying data science to HR decisions — replacing gut-feel management with measurable patterns in employee behavior, performance, and retention.

---

## Intuition

Every company has a massive dataset it ignores: its own employees. Who leaves, who stays, who performs, who burns out — all of this follows patterns. People Analytics treats HR the same way a data scientist treats any business problem: define a metric, collect data, find patterns, act, measure the outcome.

The shift: from "I think this candidate is a good fit" to "candidates with these three measurable traits have a 40% lower attrition rate in the first six months."

## Mechanics

**The People Analytics workflow:**

```
Define KPI → Collect HR data → Identify patterns → Redesign process → Measure impact
```

**Key KPIs tracked:**

| KPI | What it measures |
|---|---|
| Rotation / attrition rate | % employees leaving in a time window |
| Time to fill | How long to hire for an open role |
| Performance score | Output quality relative to expectations |
| Employee satisfaction (eNPS) | Likelihood to recommend the company |
| Absenteeism rate | Unplanned days off — early burnout signal |

**Case study — Spanish services company:**

- Problem: 25% of employees left within first 6 months
- Variables found to predict early attrition:
  - Distance > 25 km from office → 40% higher attrition probability
  - < 2 years sector experience → 30% lower success probability
  - Psychometric test scores correlated with low engagement
- After redesigning hiring and onboarding:
  - Attrition dropped from 25% → 15%
  - Recruitment cost savings: 20%
  - New employee satisfaction: +15%

**Known industry results (McKinsey / HBR):**
- Companies using People Analytics report +30% productivity
- -25% employee rotation on average

## In ML

**Attrition prediction** — classic binary classification problem: given employee features (tenure, distance, salary, performance score, manager rating), predict P(leave within 6 months). IBM uses this at scale to proactively intervene before high-value employees quit.

**Qualitative analysis with LLMs** — exit interviews and open-ended satisfaction surveys are unstructured text. Embedding + clustering (or LLM summarization) extracts patterns: which themes appear most in exit interviews from high performers? This is a direct RAG/embedding use case applied to HR data. See [[platzi-people-analytics-excel]].

**Google Project Oxygen** — used internal data to identify which manager behaviors correlated with team performance. Result: 8 key skills that became the basis for manager training programs. This is feature importance analysis (random forest, SHAP values) applied to HR.

## Exercises

**Basic** — A company has 200 employees and loses 40 per year. Calculate the annual attrition rate. If they reduce it by 25% using People Analytics, how many employees do they retain?

**Intermediate** — Design a KPI dashboard for a 500-person company. Choose 5 KPIs, define how each is measured, what data source feeds it, and what threshold triggers an alert.

**Advanced** — Frame the Spanish company's attrition problem as an ML classification task. Define: target variable, features, training data requirements, evaluation metric, and what business action the model output triggers.
