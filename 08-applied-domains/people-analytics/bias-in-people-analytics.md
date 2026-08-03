---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[impact-evaluation-in-people-analytics]]"
  - "[[hr-data-ethics]]"
  - "[[people-analytics-project-framework]]"
  - "[[data-cleaning-for-people-analytics]]"
  - "[[likert-scale]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — A metric is only trustworthy once you've checked it's comparable across the populations and data sources involved — the same turnover rate can mean opposite things depending on context.

---

## Intuition

Numbers without context mislead. A 15% turnover rate can be alarming in one country and the market standard in another. The number alone tells you nothing — your criterion for *which reference applies* is what turns it into a real finding.

This matters most in people analytics because HR data is rarely homogeneous: different countries, business units, or job families don't share the same baseline "normal," and their underlying data often isn't even collected with the same rigor.

## Mechanics

**Checklist before drawing conclusions:**

1. **Data-quality homogeneity** — is data equally clean and complete across the countries, areas, or units being compared?
2. **Population-specific norms** — what counts as normal turnover *for this specific population*, before generalizing a single threshold?
3. **Benchmark comparability** — is the reference source's population actually similar to yours? A consultancy benchmark from one industry or region may not transfer.
4. **Statistical validation** — is the observed effect significant, or could it be noise?

| Bias source | Question to ask | Failure mode if skipped |
|---|---|---|
| Data-quality heterogeneity | Is data equally reliable across segments? | False cross-country comparisons |
| Population-specific norms | What's normal turnover for *this* population? | Treating a global benchmark as universal |
| Benchmark comparability | Is the reference population similar to mine? | Comparing incompatible consultancy data |
| Statistical validation | Is the effect real, or noise? | Presenting a spurious pattern as a finding |

## In Practice

**The 15% example, worked through** — without a contextual criterion, a team might launch costly retention interventions for a rate that's actually normal in that market, or dismiss a genuinely bad number because it superficially resembles another region's benchmark. Either mistake comes from skipping the comparability check, not from a data or model error.

**This is the gate for benchmarking, not a separate step** — [[impact-evaluation-in-people-analytics]] relies on comparing findings to past analyses and market references; this checklist is exactly what determines whether that comparison is valid before you run it.

**Analytical bias vs. ethical bias** — this is the analytical counterpart to the bias awareness covered in [[hr-data-ethics]]: one protects against drawing skewed *conclusions*, the other against unfair *treatment* of protected groups. Both come from the same discipline — scrutinizing who your data actually represents before trusting what it says.

## Exercises

**Basic** — A report states "our turnover of 12% is worse than the industry benchmark of 8%." Using the checklist, what two questions should you ask before accepting this conclusion?

**Intermediate** — You're comparing turnover across three countries, but one country's HR system only started logging exit reasons 6 months ago. Which checklist item does this violate, and what comparisons remain valid despite it?

**Advanced** — Design a checklist your team must complete before presenting any cross-geography benchmark comparison to leadership. Justify each item against a specific bias source from this note, and identify which item would have caught a real case where an "outlier" turnover rate turned out to be an artifact of inconsistent data collection rather than a real business problem.
