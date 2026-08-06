---
tags:
  - status/growing
  - probability
related:
  - "[[population-and-sample]]"
  - "[[probability-fundamentals]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1."
---

> **TL;DR** — Before trusting any statistical analysis — yours or someone else's — check it against four factors: the context of the data, its source, the sampling method used, and the conclusions drawn.

---

## Intuition

A calculation can be arithmetically flawless and still mislead, because the numbers alone don't say whether they answer the right question, come from a trustworthy source, were collected fairly, or were interpreted honestly. Statistical thinking means never accepting a computed result on its own — the calculation is only one part of the picture; these four factors are the surrounding check.

**Table 1-1 (Triola) — data used for analysis:**

| x | 56 | 67 | 57 | 60 | 64 |
|---|---|---|---|---|---|
| y | 53 | 66 | 58 | 61 | 68 |

Handed just this table, you could compute a mean, a correlation, anything you like — and still know nothing, because *x* and *y* have no stated meaning yet. That gap is the point: the arithmetic is available immediately, but it's worthless until context is attached.

**Revealed context** — these are *paired* weights (kg) of Rutgers University students: *x* is each student's weight in September of freshman year, *y* is the same student's weight the following April. Student 1 went from 56 kg to 53 kg, student 2 from 67 kg to 66 kg, and so on. The data feeds a real study (Hoffman, Policastro, Quick & Lee, *Journal of American College Health*, vol. 55) testing the popular "Freshman 15" belief — that students gain about 15 lb (~7 kg) in their first year.

## Mechanics

**The four factors (Triola, Ch. 1):**

| Factor | Core question | Definition |
|---|---|---|
| Context | What do the values represent, where from, and why collected? | The circumstances surrounding the data. Without it, correctly computed numbers are still meaningless — and context also determines *which* statistical procedure is even valid to apply |
| Source | Who collected it, and do they have a stake in the outcome? | Whether the source is objective or has a reason (financial, reputational) to bias results |
| Sampling method | How was the sample obtained? | The selection process — some methods (e.g. voluntary response) systematically bias who ends up in the data |
| Conclusions | Do the stated conclusions actually follow from the analysis, and what do they mean in practice? | Claims must be understandable to non-statisticians, not overreach beyond what the data justifies, and — beyond the bare conclusion — should flag any **practical implications** the result carries |

**Table 1-1, walked through all four factors:**

- **Context** — beyond just *meaning* something, context decides *validity*: because these are paired before/after weights for the same students, a paired-data procedure applies ([[population-and-sample|§9-4 in Triola]]). Contrast: if the same five x/y number pairs had instead been jersey numbers of Rutgers' men's and women's basketball teams, *no* meaningful statistical procedure would apply at all — jersey numbers don't measure or count anything, they just label. Same numbers, same arithmetic possible, but one context supports real analysis and the other doesn't.
- **Source** — the weights were measured by Rutgers' own Nutrition Science researchers, who had no financial or reputational stake in a particular result — a source with no incentive to bias the numbers. Contrast: Kiwi Brands (a shoe-polish maker) once commissioned a study concluding that scuffed shoes were the main reason male job applicants failed interviews — a textbook conflict of interest. Pharmaceutical-funded drug trials face the same risk, which is why journals like *JAMA* now require researchers to disclose funding sources.
- **Sampling method** — of 217 students who joined the September assessment, only 67 volunteered for the April follow-up: a **voluntary response (self-selected) sample**. The researchers themselves flagged this as non-random with likely self-selection bias — speculating that only students comfortable with their current weight may have agreed to be measured twice. Contrast: ABC's *Nightline* once polled viewers by asking them to call in with an opinion on UN headquarters staying in the US — a voluntary response sample skewed toward whoever cared enough to dial in. Valid statistical methods can still be run on voluntary-response data, but the results aren't automatically trustworthy — see [[population-and-sample]] for why collection method outweighs raw sample size.
- **Conclusions** — the study concluded students *do* gain weight freshman year, but in this small, non-random sample the gain was less than 15 lb and not universal — so the specific "Freshman 15" figure is a myth, even though the general direction (weight gain happens) held up. This mirrors a broader trap: a valid statistical result (e.g. smoking correlates with pulse rate) never by itself justifies a causal claim ("smoking *causes* pulse rate to change") — correlation is not causation. The researchers went a step further into **practical implications**: they noted that seemingly small, harmless-looking changes in diet and exercise habits can compound into large weight and body-fat changes over a long period — a takeaway freshmen can act on regardless of whether the "15 lb" figure itself holds.

**A conclusion also needs to survive a significance check** — a result can be *statistically* significant (unlikely to be due to chance) while carrying no *practical* significance (too small to matter) — see [[statistical-significance]] for the full distinction, worked through the Atkins-diet and MicroSort examples from the same chapter.

**What the book means by "statistical thinking"** — synthesizing all of the above: the ability to see the big picture by weighing context, source, and sampling method; to draw sound conclusions and flag their practical implications; and to judge whether a result is [[statistical-significance|statistically significant]]. It is critical thinking about data, not just the ability to run calculations.

## In ML

**Context ↔ dataset documentation** — Datasheets for Datasets and Model Cards ask exactly this factor's questions (what does each feature mean, where did it come from, why was it collected) before anyone should trust a dataset or a reported metric.

**Source ↔ funding and incentive bias in ML research** — a benchmark result published by the same lab selling the model, or an eval funded by a vendor with a stake in the outcome, carries the same skepticism flag as Kiwi Brands' shoe-polish study.

**Sampling method ↔ selection bias in training data** — opt-in feedback, user-generated content, and self-selected survey respondents are all voluntary-response samples; a model trained on them inherits whatever bias made certain users more likely to participate, exactly like the 67-of-217 Rutgers follow-up.

**Conclusions ↔ correlation vs. causation in model claims** — a model finding that feature A correlates with label B never by itself justifies claiming A *causes* B; conflating the two is one of the most common overreach errors in reporting ML results.

## Exercises

**Basic** — A company reports "customers who use our app daily spend 3x more" and concludes the app *causes* higher spending. Which of the four factors does this conclusion violate, and why?

**Intermediate** — Using the Table 1-1 basketball-jersey contrast, explain in your own words why *context* determines not just meaning but which statistical procedures are even valid — give one other example of numeric data where no meaningful statistical analysis would apply.

**Advanced** — A pharmaceutical company funds a study showing its new drug outperforms a competitor's, using a sample of 5,000 patients who volunteered after seeing an ad for the trial. Apply all four factors to this scenario and identify the specific weakness each one exposes.
