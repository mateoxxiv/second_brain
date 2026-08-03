---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[people-analytics]]"
  - "[[hr-data-types]]"
  - "[[data-driven-culture]]"
  - "[[platzi-people-analytics-excel]]"
  - "[[ai-in-hr-applications]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — HR data is uniquely sensitive because it describes real people's livelihoods; ethical People Analytics requires data classification, access control, informed consent, and active bias awareness before any model runs.

---

## Intuition

Imagine a manager who uses gut feeling to decide who gets promoted — biased, unaccountable, invisible. Now imagine that same bias encoded into an algorithm that runs at scale across 10,000 employees. The algorithm feels objective, but it's amplifying the same bias, faster and with more authority.

Ethics in People Analytics is not a legal checkbox — it's the difference between data science that improves people's work lives and data science that harms them at scale without anyone noticing.

## Mechanics

**HR data sensitivity classification:**

| Level | Examples | Default access |
|---|---|---|
| Public | Job title, department, office location | Anyone in org |
| Internal | Salary bands, team structure, tenure | HR + managers |
| Confidential | Individual salaries, performance reviews, disciplinary records | HR + direct manager |
| Restricted | Health data, biometric data, psychometric test results | HR leadership only |

**Four ethical pillars:**

- **Consent & transparency** — employees must know what data is collected, why, how long it's retained, and who can access it. Collecting eNPS without disclosing it feeds an attrition model is a consent violation.
- **Access control (least privilege)** — each role accesses only the data it needs. A hiring manager doesn't need salary history; a data analyst doesn't need disciplinary records. Enforce at the system level, not by convention.
- **Anonymization vs pseudonymization** — anonymized data cannot be re-identified (aggregates, k-anonymity). Pseudonymized data replaces identifiers with codes but can be reversed — still falls under privacy regulation (GDPR Art. 4). Most HR analytics uses pseudonymization, not true anonymization.
- **Bias awareness** — historical HR data encodes past decisions. A model trained on who was promoted historically will likely reproduce gender, ethnicity, or age biases embedded in those decisions. Identify protected attributes before training and audit outcomes by group.

**Bias entry points in a typical People Analytics pipeline:**

```
Data collection → Feature selection → Model training → Decision output
      ↑                  ↑                  ↑                 ↑
  Underreporting    Proxy variables    Historical bias    Unchecked output
  (who gets         (zip code →        (past promotions   (no disparate
  surveyed?)        neighborhood)      reflect bias)       impact audit)
```

## In ML

**Proxy variables** — a model that includes commute distance, zip code, or graduation year as features may appear neutral but correlates strongly with protected attributes (race, socioeconomic status, age). Removing the protected attribute is not enough — you must audit feature correlations.

**Disparate impact** — even a "fair" model (same accuracy across groups) can produce discriminatory outcomes if the base rates differ. The 4/5ths rule (selection rate for any group must be ≥ 80% of the highest-selected group) is the standard legal threshold used in employment law and ML fairness audits.

**Explainability as an ethical requirement** — when an algorithm affects hiring, promotion, or termination, affected employees have a right to understand the decision. Black-box models (deep nets, ensembles) without SHAP or LIME explanations create accountability gaps that violate both ethics and emerging regulation (EU AI Act).

## Exercises

**Basic** — Classify the following HR data points by sensitivity level: (a) employee's job title, (b) individual performance score from last review, (c) result of a pre-employment psychometric test, (d) number of sick days taken this year.

**Intermediate** — An attrition model uses these features: age, gender, salary, zip code, years at company, manager rating, performance score. Identify which features are protected attributes or likely proxies. Which would you remove and why?

**Advanced** — A company's hiring model has 85% accuracy overall, but acceptance rates are: Group A — 60%, Group B — 42%. Does this violate the 4/5ths rule? What three interventions could reduce disparate impact while preserving predictive value?
