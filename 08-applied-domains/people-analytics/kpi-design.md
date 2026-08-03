---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[people-analytics]]"
  - "[[people-analytics-employee-lifecycle]]"
  - "[[people-analytics-project-framework]]"
  - "[[data-cleaning-for-people-analytics]]"
  - "[[hr-dashboard-in-excel]]"
  - "[[likert-scale]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — Good HR KPIs fall into three categories — cost, quantity, quality — mapped onto the employee lifecycle; picking fewer, sufficient metrics beats collecting everything.

---

## Intuition

HR manages an organization's most valuable and most expensive resource: people. A KPI is how that management gets translated into a number other departments can act on — finance can't act on "we hired some good people," but it can act on "cost-per-hire dropped 12%."

The trap is the opposite failure: collecting every metric available. More data isn't more insight — it's more noise to sift through before a decision gets made. The goal is a **necessary and sufficient** set: enough to decide, not so much that the signal drowns.

## Mechanics

**Three KPI categories:**

| Category | Answers | Example |
|---|---|---|
| Cost | What % of total org cost is personnel? | Compensation budget vs. sales targets |
| Quantity | How many people, in what roles? | Headcount per department; FTE vs. other contract types |
| Quality | Is the investment in people paying off? | ROI of training/wellbeing initiatives on productivity |

**Lifecycle-aligned KPI examples** — the categories above are a lens; apply them at each stage of the [[people-analytics-employee-lifecycle]]:

- **Selection perception** — how candidates rate the hiring process; directly shapes employer brand.
- **Onboarding & training** — effectiveness of the integration and development process.
- **Leadership & organizational climate** — how leadership quality and work environment affect satisfaction and retention.
- **Exit interviews & satisfaction surveys** — why people actually leave, and where engagement is weakest.

**Selection principle** — before adding a KPI, ask: is it *necessary* (does a decision depend on it) and is the current set *sufficient* (does it already answer the question)? A KPI that fails both tests is overhead, not insight.

## In Practice

**This is the metric layer of the lifecycle framework** — [[people-analytics-employee-lifecycle]] already sketches which question each stage answers; KPI design is choosing the cost/quantity/quality metric that actually answers it, instead of picking whatever the HRIS happens to export.

**KPIs are only as good as the data behind them** — a well-chosen KPI computed on a dirty field (duplicate records, wrong format, unresolved missing data) is worse than no KPI at all, since it looks trustworthy while being wrong. This is exactly what [[data-cleaning-for-people-analytics]] exists to prevent, before any KPI gets reported.

**Once defined, KPIs need a delivery format** — see [[hr-dashboard-in-excel]] for turning a chosen KPI set into something stakeholders can actually read and filter.

## Exercises

**Basic** — Classify each of these as cost, quantity, or quality: (a) average tenure by department, (b) training spend as % of payroll, (c) offer-acceptance rate.

**Intermediate** — A stakeholder asks for 15 KPIs on a new dashboard. Using the "necessary and sufficient" test, what two questions would you ask them to cut that list down, and why does a shorter list usually lead to *better* decisions?

**Advanced** — Design a 5-KPI set (one or two per lifecycle stage) for a company whose main concern is early attrition (departures within the first 90 days). Justify each KPI's category and explain what data source and cleaning step each one depends on.
