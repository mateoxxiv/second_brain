---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[people-analytics-project-framework]]"
  - "[[impact-evaluation-in-people-analytics]]"
  - "[[data-driven-culture]]"
  - "[[people-analytics]]"
  - "[[ai-in-hr-applications]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
  - "Green, David. Excellence in People Analytics."
---

> **TL;DR** — A people analytics function survives long-term only if three pillars are in place — organizational bases, adequate resources, and demonstrated added value — backed by a data expert and a business stakeholder involved from day one, not just at the final presentation.

---

## Intuition

Good tools don't make a strategy. Without the right people at the table and the right foundations underneath, a people analytics effort stays a string of disconnected pilot projects that never earns a dedicated budget or team — no matter how good any single analysis was.

## Mechanics

**Team composition** — two roles beyond HR's own:

- **A data expert**, ideally an internal data scientist. Without one, external consultancies fill the gap.
- **A business stakeholder** — the leader who validates whether an initiative's impact is real. This person is the first guarantor of success, which is why they must join in early phases, not only see the final deck.

**David Green's three pillars** (from *Excellence in People Analytics*) — the minimum structure a long-term strategy needs:

1. **Bases** — internal policy and organizational/stakeholder backing. Without this floor, any initiative stays a good intention.
2. **Resources** — tools, data availability, and — most decisive — whether the organization actually has the skills to analyze that data. This pillar sets the ceiling on how far the strategy can go.
3. **Added value** — do the insights produced actually shift culture and get recognized as valuable by the business? This recognition is what decides whether people analytics graduates into a dedicated function or keeps running as exploratory pilots.

| Pillar | Question to ask | Failure mode if missing |
|---|---|---|
| Bases | Do I have organizational and stakeholder backing? | Initiatives stay good intentions, no traction |
| Resources | Do I have the tools, data, and in-house skill to analyze it? | Analyses stall or depend entirely on outside help |
| Added value | Are my insights recognized as impacting the business? | The effort never graduates past pilot projects |

**The pilot-vs-dedicated-area decision rule** — whether an organization needs a standing people analytics team or should keep running pilot projects depends entirely on the added-value pillar: measurable, recognized impact is what justifies the next step of consolidating a dedicated area.

## In ML

**Domain expert + data scientist is the standard applied-ML pairing** — HR defines the phenomenon and validates business relevance; the data scientist builds and validates the analysis. Neither role alone reliably produces a trustworthy, actionable result.

**The resources pillar gates which analytics level is even possible** — [[people-analytics-project-framework]]'s four analytics levels (descriptive → prescriptive) require progressively more of exactly this pillar: skilled people, sufficient historical data, and tooling. An organization missing the resources pillar cannot responsibly commit to predictive or prescriptive work, regardless of ambition.

**Added value is a deployment gate, not a vibe** — in ML terms, this pillar is equivalent to a model clearing a business-impact evaluation before promotion from experiment to production. [[impact-evaluation-in-people-analytics]] is exactly that gate, applied to people analytics projects specifically.

## Exercises

**Basic** — Your organization has strong stakeholder backing and a working data pipeline, but no one outside HR has ever acted on an insight you produced. Which pillar is missing, and what's the direct consequence per this note?

**Intermediate** — You have an available data scientist, but your last three pilot projects only looped in a business stakeholder at the final presentation. Which principle does this violate, and why does the note treat early stakeholder involvement as the "first guarantor of success" rather than a nice-to-have?

**Advanced** — Design a 3-question self-assessment (one per pillar) an HR leader could answer today to find their organization's weakest pillar. For each question, specify what a "strong" vs. "weak" answer looks like, and the concrete next action for a weak result.
