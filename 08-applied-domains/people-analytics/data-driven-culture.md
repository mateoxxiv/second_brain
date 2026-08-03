---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[people-analytics]]"
  - "[[people-analytics-employee-lifecycle]]"
  - "[[kpi-design]]"
  - "[[hr-data-ethics]]"
  - "[[platzi-people-analytics-excel]]"
  - "[[people-analytics-strategy-pillars]]"
  - "[[people-analytics-best-practices]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — A data-driven culture is the organizational prerequisite for People Analytics: tools and dashboards are useless if decisions still rely on gut feeling.

---

## Intuition

People Analytics fails not because of bad tools — it fails because of bad culture. A company can buy the best BI platform and still make gut-feel HR decisions. The real change is behavioral: every HR decision must start with a question, not an opinion.

Think of it like a scientific lab. The equipment matters, but what matters more is the habit of forming hypotheses before running experiments.

## Mechanics

**Six steps to implement a data-driven culture:**

| Step | Action | Key question |
|---|---|---|
| 1. Define problem | Identify what you want to solve | What decision are we trying to improve? |
| 2. Collect data | Identify sources, ensure validity | Is this data reliable and available? |
| 3. Analyze | Choose tools and techniques | Do we have the skills to interpret this? |
| 4. Decide | Act only on valid, relevant results | Is this finding strong enough to act on? |
| 5. Track | Feedback loop — did it work? | Do we need to adjust our strategy? |
| 6. Incentivize | Reward data-based decisions | Who is modeling the behavior we want? |

**Data quality prerequisites:**
- **Reliability** — same measurement gives same result
- **Validity** — measuring what you think you're measuring
- **Availability** — data exists and is accessible when needed

**HR team skills required:** hypothesis formation, objective analysis, cross-functional collaboration, data source literacy. Historically HR has been data-averse — the cultural shift is as much about training as tooling.

**Maturity measurement:** self-diagnosis tools assess current state across three dimensions — leadership buy-in, strategic alignment, and team skills. Identifies gaps before scaling.

## In ML

**Feature of culture, not tooling** — the same six-step loop maps directly to the ML project lifecycle: problem framing → data collection → modeling → deployment → monitoring → iteration. A data-driven culture is what makes that loop run continuously rather than as a one-off project.

**Feedback loop (step 5)** — tracking results after a People Analytics intervention is equivalent to model monitoring in MLOps. Without it, you never know if the intervention worked or if the model drifted.

**Incentive design (step 6)** — getting employees to use data mirrors the adoption problem in ML deployment. A technically correct model that nobody uses has zero business value.

## Exercises

**Basic** — Map the six steps to a concrete HR problem: "we want to reduce time-to-fill for engineering roles." What data would you collect in step 2? What decision would step 4 produce?

**Intermediate** — A company runs a People Analytics project but skips step 5 (tracking). What can go wrong six months later? How does this connect to model monitoring in MLOps?

**Advanced** — Design a maturity assessment for a 300-person company. Define 3 levels (beginner, developing, mature) across leadership, strategy, and skills. What specific behaviors or artifacts define each level?
