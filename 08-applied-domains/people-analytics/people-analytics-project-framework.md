---
tags:
  - status/seed
  - people-analytics
related:
  - "[[people-analytics]]"
  - "[[people-analytics-employee-lifecycle]]"
  - "[[hr-data-types]]"
  - "[[hr-data-ethics]]"
  - "[[data-driven-culture]]"
  - "[[kpi-design]]"
domain: people-analytics
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — Before touching data, define the phenomenon, map its causes and consequences, and pick the analytics level that matches your capacity — 80% of organizations never get past descriptive analysis.

---

## Intuition

Starting a people analytics project without defining the problem is like assembling a puzzle without knowing what image you're building — any piece seems to fit.

The instinct is to jump to data first: pull turnover numbers, run a survey, build a dashboard. But if the phenomenon isn't defined, you won't know what to measure, who to talk to, or whether the project succeeded.

The framework forces clarity before action: what is happening, why could it be happening, what would count as an answer, and only then — what data do you actually need.

## Mechanics

**8-step project structure:**

| Step | Action | Key question |
|------|--------|-------------|
| 1 | Define the phenomenon | What exactly is happening, where, and at what scale? |
| 2 | Build a knowledge map | What are the likely causes? What are the consequences? |
| 3 | Write research questions | Which explanations can be tested with data? |
| 4 | Choose the analytics level | Descriptive, diagnostic, predictive, or prescriptive? |
| 5 | Collect data | What sources exist? Are they reliable and complete? |
| 6 | Prepare and analyze | Clean, transform, run models or descriptive stats |
| 7 | Extract insights | Do the findings answer your research questions? |
| 8 | Communicate results | Even "data was insufficient" is a valid deliverable |

**4 levels of analytics (Gartner model):**

| Level | Question answered | Tools | Org reach |
|-------|------------------|-------|-----------|
| Descriptive | What happened? | Tables, trend charts | ~80% |
| Diagnostic | Why is it happening? | Correlation, regression | ~80% |
| Predictive | What will happen? | ML models, AI | ~10% |
| Prescriptive | What should we do? | Recommendation algorithms | <10% |

**Knowledge map — structure:**

Place the phenomenon at the center with its key metrics (rate, time window, scope). Causes and antecedents go on the left; consequences validated with stakeholders go on the right.

Example — 20% annual turnover in commercial areas:

Causes: compensation below market, authoritarian leadership style, unclear career paths, bureaucratic culture.

Consequences: higher recruitment cost, rising training cost per new hire, climate deterioration from overtime, sales budget risk from operational gaps.

![[Pasted image 20260629153636.png]]

## In Practice

**Step 2 is underrated** — most teams skip the knowledge map and jump to step 5. This is where projects fail. The map tells you which variables to capture, which stakeholders to interview, and whether turnover is driven by compensation or leadership — before a single query is run.

**Level choice drives resource requirements** — predictive analytics requires enough historical labeled data, data science skills, and model maintenance. Committing to predictive without these is a common failure mode. Descriptive or diagnostic is often more impactful precisely because it is immediately actionable. See [[people-analytics]].

**Research questions constrain scope** — "why is turnover high?" is not a research question. "Does manager satisfaction score predict 6-month attrition in commercial roles?" is. The second one tells you exactly what data to collect and what statistical test to run. See [[kpi-design]].

## Exercises

**Basic** — A company reports 18% annual turnover in operations. Write the step-1 phenomenon definition: include the rate, time window, and department scope. Then list 3 candidate causes and 2 consequences for the knowledge map.

**Intermediate** — A team wants to know if a new performance bonus will reduce turnover. Classify this question into the correct analytics level and explain what data and methods they would need to answer it properly.

**Advanced** — The knowledge map for a high-absenteeism phenomenon includes 6 candidate causes. Rewrite each as a testable research question. For each, specify the data source, the statistical method (correlation, regression, chi-square), and what result would confirm or reject the hypothesis.
