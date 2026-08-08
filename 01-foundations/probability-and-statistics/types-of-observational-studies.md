---
tags:
  - status/seed
  - probability
related:
  - "[[observational-study-vs-experiment]]"
  - "[[experimental-design-principles]]"
  - "[[population-and-sample]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-5."
---

> **TL;DR** — Observational studies split by *when* the data is observed: **cross-sectional** (one moment), **retrospective** (look back at the past), and **prospective** (follow subjects forward in time).

---

## Intuition

All three are [[observational-study-vs-experiment|observational]] — nobody applies a treatment; researchers only watch and measure. What separates them is the **time axis**: are you taking a single snapshot, digging into records of what already happened, or committing to track people into the future? The choice matters because it decides *what kind of question you can answer* and *how strong the causal hint can be* — a prospective study that follows exposed vs. unexposed groups forward gives a much cleaner picture of cause than a one-time snapshot.

## Mechanics

| Type | *When* data is observed | How data is gathered | Example |
|------|------------------------|----------------------|---------|
| **Cross-sectional** | a single point in time | measure everything at once | survey today's students' heights and grades |
| **Retrospective** (case-control) | reach into the **past** | records, interviews, archives | compare drivers who *died* in crashes vs. those who didn't |
| **Prospective** (longitudinal / cohort) | into the **future** | follow **cohorts** forward | track cellphone-using vs. non-using drivers going forward |

**The retrospective vs. prospective sampling difference** (Triola stresses this):
- **Retrospective** — you start from the *outcome* (who already has the trait/event) and look **backward** for causes. Groups are defined by *effect*.
- **Prospective** — you start from a *potential causal factor* (exposed vs. not) and look **forward** to see who develops the outcome. Groups are defined by *cause*.

A **cohort** is a group sharing a common factor (e.g. smokers) that a prospective study follows over time — as in the *National Children's Study* tracking 100,000 children birth→age 21.

## In ML

**Retrospective data is what most models train on** — historical logs are a retrospective, observational snapshot: outcomes already happened and you mine backward for predictive features. This is why such models capture *association*, not intervention, echoing the [[observational-study-vs-experiment|correlation≠causation]] limit.

**Prospective design ≈ a proper train/serve split in time** — respecting temporal order (train on past, evaluate on future) mirrors a prospective cohort and prevents look-ahead leakage; a careless random split can secretly behave "retrospectively" and inflate metrics.

## Exercises

**Basic** — Classify each: (a) a one-day census of a city's income; (b) interviewing lung-cancer patients about past smoking; (c) enrolling 1,000 newborns and tracking their diet for 20 years.

**Intermediate** — You want to study whether heavy screen time causes poor sleep. Sketch a retrospective *and* a prospective design, and state which better supports a causal claim and why.

**Advanced** — Explain why retrospective (case-control) studies are efficient for *rare* outcomes but vulnerable to recall bias, while prospective studies avoid recall bias but are costly for rare outcomes.
