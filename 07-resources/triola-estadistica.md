---
tags:
  - status/seed
  - literature
  - probability-and-statistics
type: book
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición (technology update). Pearson Educación, México, 2013. ISBN 978-607-32-1768-2."
author: "Mario F. Triola"
date_read: "2026-08-02 (in progress)"
---

## Summary

*Elementary Statistics* (Spanish edition: *Estadística*) is one of the most widely used introductory statistics textbooks, known for building every technique from real, worked datasets rather than abstract formulas alone. It moves from descriptive statistics and probability through the standard inferential toolkit — estimation, hypothesis testing, regression, and ANOVA — with a strong emphasis on interpreting results, not just computing them. Only the front/copyright matter has been captured so far; the chapter-by-chapter content below will fill in as pages are shared.

---

## Chapter / Class Map

> Provisional — based on this book's well-known standard structure for the 11th edition (technology update). To be confirmed/corrected chapter-by-chapter as we actually read through it.

| Ch  | Topic                                                    | Vault notes                                                                     |
| --- | -------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 1   | Introduction to Statistics                               | [[population-and-sample]], [[parameter-vs-statistic]], [[data-types-and-levels-of-measurement]], [[principles-of-statistical-thinking]], [[statistical-significance]], [[common-misuses-of-statistics]] |
| 2   | Summarizing and Graphing Data                            | [[frequency-distribution]], [[relative-frequency-distribution]], [[histogram]], [[characteristics-of-data]], [[frequency-polygon]], [[ogive]], [[dot-plot]], [[stem-and-leaf-plot]], [[bar-graph]], [[pareto-chart]], [[pie-chart]], [[scatterplot]], [[time-series-graph]], [[principles-of-effective-graphs]] |
| 3   | Statistics for Describing, Exploring, and Comparing Data | [[measures-of-center]], [[skewness]], [[weighted-mean]], [[measures-of-variation]], [[chebyshevs-theorem]], [[coefficient-of-variation]], [[z-score]], [[percentiles]], [[quartiles-and-iqr]], [[five-number-summary-and-boxplots]] |
| 4   | Probability                                              | [[probability-fundamentals]], [[sample-space-and-events]], [[three-methods-of-assigning-probability]], [[law-of-large-numbers]], [[complementary-events]], [[addition-rule]], [[odds]] |
| 5   | Discrete Probability Distributions                       | [[bernoulli-distribution]], [[binomial-distribution]], [[poisson-distribution]] |
| 6   | Normal Probability Distributions                         | [[normal-distribution]], [[cdf-and-quantiles]]                                  |
| 7   | Estimates and Sample Sizes                               |                                                                                 |
| 8   | Hypothesis Testing                                       |                                                                                 |
| 9   | Inferences from Two Samples                              |                                                                                 |
| 10  | Correlation and Regression                               |                                                                                 |
| 11  | Multinomial Experiments and Contingency Tables           |                                                                                 |
| 12  | Analysis of Variance (ANOVA)                             |                                                                                 |

---

## All Topics at a Glance

**Ch 1 — Introduction to Statistics**
- [[population-and-sample]] — core vocabulary (data, statistics, population, census, sample) and why sample *collection method* matters more than sample size
- [[principles-of-statistical-thinking]] — the four factors (context, source, sampling method, conclusions) to check before trusting any statistical claim, walked through Table 1-1's "Freshman 15" study
- [[statistical-significance]] — a result is significant when it's too unlikely to be chance; statistical vs. practical significance (Atkins diet, MicroSort examples)
- [[parameter-vs-statistic]] — a parameter describes a whole population (μ, σ, p), a statistic describes a sample (x̄, s, p̂); the target of inference vs. the estimate you have (§1-3, senators vs. Literary Digest examples)
- [[data-types-and-levels-of-measurement]] — categorical vs. quantitative, discrete vs. continuous, and the four measurement levels (nominal/ordinal/interval/ratio) that decide which methods are valid (§1-3)
- [[common-misuses-of-statistics]] — §1-4's field guide to how statistics mislead: voluntary-response samples, correlation≠causation, loaded/order-biased questions, misleading percentages, small samples, nonresponse, precise≠accurate, sponsored studies

**Ch 2 — Summarizing and Graphing Data**
- [[frequency-distribution]] — §2-2: grouping raw data into non-overlapping classes and counting each; limits, boundaries, midpoints, width, and the 6-step construction
- [[relative-frequency-distribution]] — §2-2: same table with proportions/percentages instead of counts, for fair comparison across unequal-sized datasets
- [[histogram]] — §2-3: the graphical frequency distribution; why bars touch (boundaries), axis labeling, and reading shape (CVDOT)
- [[characteristics-of-data]] — §2-3/§3: the CVDVT checklist (center, variation, distribution, outliers, time) for describing any dataset
- [[frequency-polygon]] — §2-4: histogram as a line over class midpoints; relative-frequency variant overlays two datasets on one axis
- [[ogive]] — §2-4: line graph of cumulative frequencies over class boundaries; the empirical CDF, answers "how many below X?"
- [[dot-plot]] — §2-4: each value a dot on a number line, stacked for repeats; lossless, reconstructs the raw data
- [[stem-and-leaf-plot]] — §2-4: split each value into stem/leaf; shape like a histogram but lossless, and sorts the data
- [[bar-graph]] — §2-4: bars for qualitative-data frequencies (categorical histogram); multiple bar graph compares datasets
- [[pareto-chart]] — §2-4: bar graph sorted by descending frequency to spotlight the most important categories
- [[pie-chart]] — §2-4: circle sliced by relative frequency; parts-of-a-whole, but Tufte/Triola rate it a weak graph
- [[scatterplot]] — §2-4: paired (x,y) quantitative data; pattern reveals relationships, and can expose hidden clusters (penny example)
- [[time-series-graph]] — §2-4: data over time on the x-axis; reveals trends, the one feature a histogram can't show
- [[principles-of-effective-graphs]] — §2-4: Tufte's design rules (maximize data-ink, no distortion, no chartjunk) for honest graphs

**Ch 3 — Statistics for Describing, Exploring, and Comparing Data**
- [[measures-of-center]] — §3-2: the four measures of center (mean, median, mode, midrange) and the *resistance* axis (outlier sensitivity) that separates them
- [[skewness]] — §3-2: lopsidedness of a distribution; the mean/median/mode ordering as a shape fingerprint, and why mean-vs-median alone can't reliably identify shape
- [[weighted-mean]] — §3-2 Part 2: values counting unequally, Σ(w·x)/Σw; the mean of a frequency distribution as its special case (frequencies as weights)
- [[measures-of-variation]] — §3-3: range, variance, and the standard deviation (both formulas, sample s vs. population σ, why n−1, why not MAD); interpreting s via the range rule (s≈range/4) and the Empirical Rule (68-95-99.7)
- [[chebyshevs-theorem]] — §3-3: the distribution-free "at least 1−1/K²" bound (≥75% within 2 SD, ≥89% within 3); the universal but weaker cousin of the Empirical Rule
- [[coefficient-of-variation]] — §3-3: CV = s/x̄ as a unitless %, for comparing relative spread across different units or very different means (heights vs. weights)
- [[z-score]] — §3-4: value restated as SDs from the mean, $z=(x-\bar{x})/s$; unit-free comparison across distributions and the $|z|>2$ unusual-value rule
- [[percentiles]] — §3-4: rank-based position ($P_k$), the value↔percentile procedures via the locator $L$, and the empirical-CDF connection
- [[quartiles-and-iqr]] — §3-4: $Q_1/Q_2/Q_3$, the outlier-resistant $\text{IQR}=Q_3-Q_1$, and the semi-IQR/midquartile family
- [[five-number-summary-and-boxplots]] — §3-4: min/Q1/median/Q3/max, skeletal vs. modified boxplots, and the $1.5\times\text{IQR}$ outlier fence

**Ch 4 — Probability**
- [[sample-space-and-events]] — §4-2: procedure/outcome/event/simple-event/sample-space vocabulary and the granularity trap (ffm is simple, "2 girls 1 boy" is not)
- [[three-methods-of-assigning-probability]] — §4-2: relative frequency ($s/n$ from data), classical ($s/n$, equally-likely required), and subjective; the equal-likelihood warning and simulation as a practical stand-in
- [[law-of-large-numbers]] — §4-2: relative-frequency estimates converge to the true probability as trials grow; the $1/\sqrt n$ shrink and the gambler's-fallacy caveat
- [[complementary-events]] — §4-2: $\bar A$ = "$A$ doesn't happen", $P(A)+P(\bar A)=1$, and the "at least one" = $1-P(\text{none})$ shortcut (SAT-guessing example)
- [[addition-rule]] — §4-3: $P(A\text{ or }B)=P(A)+P(B)-P(A\cap B)$, disjoint events as the no-overlap special case, the double-counting trap, and the softmax / union-bound connections
- [[odds]] — §4-2 Part 2: actual odds against/in-favor vs. payoff odds, the house edge (roulette 37:1 vs. 35:1), and the logit link to logistic regression

*(remaining chapters to fill in as read — see [[probability-distributions]] for the overview note this book's Ch. 4-6 will extend)*

---

## Key Takeaways

1. **Statistics infers population truths from sample data** — the whole discipline exists because measuring an entire population (a census) is usually impossible or impractical.
2. **Sample collection method matters more than sample size** — the 1936 Literary Digest poll's 2.3 million respondents still produced a confidently wrong prediction, because the sample wasn't randomly drawn from the true population.
3. **Bad sampling is unrecoverable by analysis** — no statistical technique fixes data that wasn't collected properly in the first place.
4. **Four factors gate whether any statistical claim should be trusted** — context, source, sampling method, and conclusions; Table 1-1's Rutgers "Freshman 15" study is used as a single worked example threading through all four.
5. **Context doesn't just add meaning, it determines validity** — the same numbers can support a real statistical procedure (paired student weights) or none at all (arbitrary jersey numbers), depending purely on what they represent.
6. **Statistical significance answers "is this real?", not "does this matter?"** — the Atkins-diet trial's 2.1 lb average loss was statistically significant yet practically useless; the MicroSort examples (13/14 vs. 8/14 girls) show the same distinction from the opposite angle.

## Quotes / Important Passages

> "Si los datos muestrales no se reúnen de forma adecuada, resultarán tan inútiles que ningún grado de tortura estadística podrá salvarlos."
> — Ch. 1, on the necessity of proper sample collection

> "La correlación no implica causalidad."
> — Ch. 1, on the limits of what a statistical conclusion can justify

## My Thoughts

This book is the natural next input for [[probability-fundamentals|T3 (Probability and Statistics)]] in the study roadmap — the vault already has the distributions chapter mostly covered ([[bernoulli-distribution]], [[binomial-distribution]], [[normal-distribution]], [[poisson-distribution]], [[exponential-distribution]], [[beta-distribution]], [[dirichlet-distribution]]) but is missing the inferential half entirely: hypothesis testing, confidence intervals, regression, and ANOVA are all flagged as roadmap gaps and are exactly what Triola's Ch. 7-12 cover. This book is likely to become the primary source for that missing half of T3.

---

## Permanent Notes Created

- [[population-and-sample]] — from Ch. 1: data/statistics/population/census/sample definitions, the Literary Digest 1936 case, why collection method beats sample size
- [[principles-of-statistical-thinking]] — from Ch. 1: the four-factor checklist (context, source, sampling method, conclusions), fully worked through Table 1-1's Rutgers "Freshman 15" study, including the Kiwi Brands and Nightline bias examples
- [[statistical-significance]] — from Ch. 1, §1-2: statistical vs. practical significance (Atkins diet trial), the MicroSort 13/14 vs. 8/14 contrast, and the binomial-probability code reproducing both figures
- [[parameter-vs-statistic]] — from Ch. 1, §1-3: parameter (population) vs. statistic (sample), the μ/x̄, σ/s, p/p̂ convention, and the senators-vs-Literary Digest worked examples
- [[data-types-and-levels-of-measurement]] — from Ch. 1, §1-3: categorical/quantitative, discrete/continuous, and the nominal→ordinal→interval→ratio ladder with the "twice" test
- [[common-misuses-of-statistics]] — from Ch. 1, §1-4: the taxonomy of misuses (voluntary-response, correlation≠causation, loaded questions, misleading percentages, small samples, nonresponse, sponsored studies) plus the four percentage-conversion rules
- [[sampling-methods]] — from Ch. 1, §1-5: the random/SRS/probability-sample distinctions (senators example), the five practical methods (systematic, convenience, stratified, cluster), stratified-vs-cluster mnemonic, and multistage sampling
- [[observational-study-vs-experiment]] — from Ch. 1, §1-5: the two data sources, why only randomized experiments support causation (hormone-therapy case), and the placebo/Hawthorne/experimenter confounding effects
- [[random-sample-vs-simple-random-sample]] — from Ch. 1, §1-5: the individual-chance vs. group-chance distinction, worked through the 4-person A/B/C/D example (Design 1 = SRS, Design 2 = random but not SRS), plus the "simple ≠ replacement" clarification
- [[types-of-observational-studies]] — from Ch. 1, §1-5 Part 2: cross-sectional / retrospective (case-control) / prospective (cohort), split by *when* data is observed, and the backward-from-effect vs. forward-from-cause sampling difference
- [[experimental-design-principles]] — from Ch. 1, §1-5 Part 2: the three pillars — randomization, replication, control (blinding & double-blinding) — worked through the 1954 Salk polio trial
- [[experimental-designs-for-controlling-variables]] — from Ch. 1, §1-5 Part 2: the four designs (completely randomized, randomized block, rigorously controlled, matched pairs) for isolating a treatment from confounding
- [[sampling-error-vs-nonsampling-error]] — from Ch. 1, §1-5 Part 2: unavoidable random sampling error (shrinks with n) vs. fixable nonsampling error (bias/defective instrument/bad recording; n doesn't help)
- [[frequency-polygon]] — from Ch. 2, §2-4: histogram-as-line over class midpoints; relative-frequency variant for overlaying two datasets (Figs. 2-5, 2-6)
- [[ogive]] — from Ch. 2, §2-4: cumulative-frequency line over class boundaries; empirical CDF, "how many below X?" (Fig. 2-7)
- [[dot-plot]] — from Ch. 2, §2-4: stacked dots on a number line; lossless, reconstructs raw data
- [[stem-and-leaf-plot]] — from Ch. 2, §2-4: stem/leaf split; histogram shape plus full data retention and sorting
- [[bar-graph]] — from Ch. 2, §2-4: categorical-data bars; multiple bar graph for comparison (income-by-gender example)
- [[pareto-chart]] — from Ch. 2, §2-4: frequency-sorted bar graph spotlighting the vital few (job-search example)
- [[pie-chart]] — from Ch. 2, §2-4: relative-frequency slices; angle = rel.freq × 360°; the weak-graph caveat
- [[scatterplot]] — from Ch. 2, §2-4: paired (x,y) data and relationships; the penny two-cluster/Simpson's-paradox warning
- [[time-series-graph]] — from Ch. 2, §2-4: values over time reveal trends; the "T" in CVDVT (DJIA example)
- [[principles-of-effective-graphs]] — from Ch. 2, §2-4: Tufte's data-ink/anti-chartjunk rules and the describe/explore/compare conclusion
- [[measures-of-center]] — from Ch. 3, §3-2: mean/median/mode/midrange, the round-off rule, and *resistance* to outliers; the L2-mean vs. L1-median link to MSE/MAE loss
- [[skewness]] — from Ch. 3, §3-2: distribution shape and the mean/median/mode relationship (Fig. 3-2), plus Triola's counterexample showing mean-vs-median can't reliably identify shape
- [[weighted-mean]] — from Ch. 3, §3-2 Part 2: Σ(w·x)/Σw, the GPA example, the mean-from-frequency-distribution special case, and the per-capita-income weighting trap
- [[measures-of-variation]] — from Ch. 3, §3-3: range, variance, standard deviation (Formulas 3-4/3-5, s vs. σ, the n−1 degrees-of-freedom argument, why squaring beats the MAD's absolute value); the range rule of thumb and Empirical Rule for interpreting s; links to z-score standardization and PCA in ML
- [[chebyshevs-theorem]] — from Ch. 3, §3-3: the distribution-free "at least 1−1/K²" bound (≥75% within 2 SD, ≥89% within 3); the universal but weaker cousin of the Empirical Rule
- [[coefficient-of-variation]] — from Ch. 3, §3-3: CV = s/x̄ (unitless %), for comparing variation across different scales/units (heights vs. weights example)
- [[z-score]] — from Ch. 3, §3-4 (Ejemplo 1): standardized value as SDs-from-mean, the height-vs-weight comparison, the $|z|>2$ unusual rule, and the direct line to `StandardScaler` and the standard normal
- [[percentiles]] — from Ch. 3, §3-4 (Ejemplos 2–5): rank-based position, both value↔percentile procedures via the locator $L$, the software-convention caveat, and the 85th-percentile speed-limit rule
- [[quartiles-and-iqr]] — from Ch. 3, §3-4 (Ejemplo 6): $Q_1{=}P_{25}$ etc., IQR as resistant spread, the semi-IQR/midquartile/10–90 family, and RobustScaler in ML
- [[five-number-summary-and-boxplots]] — from Ch. 3, §3-4 (Ejemplos 7–11): the five landmarks, skeletal vs. modified boxplots, the $1.5\times\text{IQR}$ fence, and boxplots-on-shared-scale for group comparison
- [[sample-space-and-events]] — from Ch. 4, §4-2 (Ejemplo 1): procedure/outcome/event/simple-event/sample-space definitions and the granularity trap; sample space as the support of a distribution
- [[three-methods-of-assigning-probability]] — from Ch. 4, §4-2 (Ejemplos 2–9): relative-frequency / classical / subjective, the equal-likelihood warning, simulation, and the Monte-Carlo & Bayesian-prior connections
- [[law-of-large-numbers]] — from Ch. 4, §4-2: relative frequency → true probability, the $1/\sqrt n$ error shrink, the gambler's fallacy, and why Monte Carlo / SGD mini-batches work
- [[complementary-events]] — from Ch. 4, §4-2 (Ejemplo 10): $P(A)+P(\bar A)=1$, the "at least one" shortcut, and the binary-classification / cross-entropy link
- [[addition-rule]] — from Ch. 4, §4-3 (Ejemplos 1–3): $P(A\cup B)=P(A)+P(B)-P(A\cap B)$, disjoint/mutually-exclusive events, the polygraph double-counting example, and the softmax (disjoint classes) & union-bound / Bonferroni links
- [[odds]] — from Ch. 4, §4-2 Part 2 (Ejemplo 13): actual vs. payoff odds, the house edge (roulette), and the logit / logistic-regression connection

## Gaps — Notes Still to Create

- [[hypothesis-testing-and-p-values]] — already flagged in the study roadmap as T3's next priority after MLE; [[statistical-significance]] is its intuitive seed (the "how likely under no effect?" reasoning), still needs the formal null/alternative hypothesis and p-value machinery
- [[confidence-intervals]] — estimation theory, sample size determination
- [[correlation-and-regression]] — bridges directly to supervised ML's linear regression (T4)
- [[analysis-of-variance]] — ANOVA, comparing more than two group means
- [[chi-squared-and-contingency-tables]] — categorical-data inference
