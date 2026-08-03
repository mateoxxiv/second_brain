---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[people-analytics-project-framework]]"
  - "[[people-analytics]]"
  - "[[bias-in-people-analytics]]"
  - "[[data-driven-culture]]"
  - "[[kpi-design]]"
  - "[[data-cleaning-for-people-analytics]]"
  - "[[people-analytics-strategy-pillars]]"
  - "[[people-analytics-best-practices]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — Impact evaluation is checking whether your findings answered the original hypotheses, produced actionable recommendations, and translated into quantifiable business value — otherwise the project stayed a descriptive exercise.

---

## Intuition

Finishing the [[people-analytics-project-framework|8-step framework]] doesn't mean the project succeeded — it means you produced *some* result. Impact evaluation is the audit that comes after: did that result actually move the business, or did it just describe a phenomenon nicely?

The gap matters because expectations diverge silently. A stakeholder might picture a decisive recommendation ("cut turnover by fixing X"), while the team quietly delivers a first descriptive snapshot. Both can be legitimate outcomes — but only if that scope was agreed on *before* the analysis, not discovered after.

## Mechanics

**Step 0 — align expectations before measuring anything.** Sit with the business stakeholder and ask: is this an exploratory pilot, or does the business expect a decision-ready recommendation? Then check which of the [[people-analytics-project-framework|4 analytics levels]] you actually reached — staying descriptive is legitimate *if* the available data couldn't support more.

**Definition** — impact evaluation validates three things: (1) did the findings answer the initial hypotheses, (2) were the recommendations actionable, (3) did the project produce quantifiable value (e.g. reduced attrition, higher ROI).

**Hypothesis outcomes are all valid** — a hypothesis can be confirmed, refuted, or inconclusive; all three are legitimate scientific outcomes. Inconclusive results are frequently a data-quality problem, not an analysis problem — e.g. comparing turnover across countries often breaks down because data completeness isn't consistent across geographies. This is precisely why [[data-driven-culture]] upstream determines whether impact evaluation is even possible downstream.

**Benchmarking is conditional** — compare results against the organization's own past analyses and external market references, but *only* when the underlying data is genuinely comparable. Whether it is comparable is itself a judgment call — see [[bias-in-people-analytics]] for the checklist that gates this step.

**Actionability test** — a finding is actionable when it lets you recommend a specific intervention: which geography, which variable, which population to act on — not just "turnover is high."

| Question | What it evaluates | Signal of success |
|---|---|---|
| Were expectations aligned upfront? | Pilot vs. decision-ready scope | Delivered scope matches agreed scope |
| Confirmed / refuted / inconclusive? | Data quality + rigor | Any outcome is valid if data-backed |
| Can we benchmark against past/market data? | Comparability of sources | Only compared when truly comparable |
| Is the finding actionable? | Recommendation specificity | Names a concrete lever to pull |
| Is the impact quantifiable? | Business value | ROI↑, attrition↓, talent availability↑ |

## In Practice

**Leadership is the best-validated predictor** — across studies, leadership quality consistently predicts turnover, climate, and harassment prevention, making it a hypothesis that tends to *confirm* reliably. Other candidates — commute distance, caregiving load, personal wellbeing, work-life balance — are real but more context-dependent, and need local validation before being generalized to your organization.

**The regional benchmark trap** — 15% turnover can be alarming in one country and the market standard in another. The [[people-analytics-project-framework]] generates the hypotheses; impact evaluation is the gate deciding whether the answer is trustworthy enough to act on.

## Exercises

**Basic** — A project only reached the descriptive analytics level, but stakeholders expected prescriptive recommendations. Using the mechanics above, is this project a failure? What single fact would change your answer?

**Intermediate** — A turnover analysis finds 15% attrition in Country A and 22% in Country B. Before concluding Country B has "the worse problem," which gate from this note must be passed first, and why?

**Advanced** — Design an impact-evaluation rubric for a project measuring whether a new onboarding program reduced 6-month attrition. Specify: the hypothesis, the actionability criterion, the benchmark comparison you'd use, and the quantifiable metric that would prove business impact.
