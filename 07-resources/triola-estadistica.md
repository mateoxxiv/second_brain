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
date_read: "2026-08-02 (in progress; Ch. 7 added 2026-10-17; Ch. 8 §8-2 added 2026-10-28)"
---

## Summary

*Elementary Statistics* (Spanish edition: *Estadística*) is one of the most widely used introductory statistics textbooks, known for building every technique from real, worked datasets rather than abstract formulas alone. It moves from descriptive statistics and probability through the standard inferential toolkit — estimation, hypothesis testing, regression, and ANOVA — with a strong emphasis on interpreting results, not just computing them. Chapters 1–7 (through §7-3) are captured so far in the chapter-by-chapter map below; Chapters 8–12 will fill in as pages are shared.

---

## Chapter / Class Map

> Provisional — based on this book's well-known standard structure for the 11th edition (technology update). To be confirmed/corrected chapter-by-chapter as we actually read through it.

| Ch  | Topic                                                    | Vault notes                                                                                                                                                                                                                                                                                                                                                                                           |
| --- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Introduction to Statistics                               | [[population-and-sample]], [[parameter-vs-statistic]], [[data-types-and-levels-of-measurement]], [[principles-of-statistical-thinking]], [[statistical-significance]], [[common-misuses-of-statistics]]                                                                                                                                                                                               |
| 2   | Summarizing and Graphing Data                            | [[frequency-distribution]], [[relative-frequency-distribution]], [[histogram]], [[characteristics-of-data]], [[frequency-polygon]], [[ogive]], [[dot-plot]], [[stem-and-leaf-plot]], [[bar-graph]], [[pareto-chart]], [[pie-chart]], [[scatterplot]], [[time-series-graph]], [[principles-of-effective-graphs]]                                                                                       |
| 3   | Statistics for Describing, Exploring, and Comparing Data | [[measures-of-center]], [[skewness]], [[weighted-mean]], [[measures-of-variation]], [[chebyshevs-theorem]], [[coefficient-of-variation]], [[z-score]], [[percentiles]], [[quartiles-and-iqr]], [[five-number-summary-and-boxplots]]                                                                                                                                                                   |
| 4   | Probability                                              | [[probability-fundamentals]], [[sample-space-and-events]], [[three-methods-of-assigning-probability]], [[law-of-large-numbers]], [[complementary-events]], [[addition-rule]], [[multiplication-rule]], [[conditional-probability]], [[monte-carlo-simulation]], [[counting-and-combinatorics]], [[bayes-theorem]], [[odds]]                                                                           |
| 5   | Discrete Probability Distributions                       | [[random-variable]], [[discrete-probability-distribution]], [[mean-and-variance-of-a-probability-distribution]], [[expected-value]], [[identifying-unusual-results]], [[bernoulli-distribution]], [[binomial-distribution-requirements]], [[binomial-distribution]], [[binomial-mean-and-variance]], [[hypergeometric-distribution]], [[poisson-distribution]], [[poisson-approximation-to-binomial]] |
| 6   | Normal Probability Distributions                         | [[normal-distribution]], [[probability-density-function]], [[uniform-distribution]], [[standard-normal-distribution]], [[critical-values-and-z-alpha]], [[cdf-and-quantiles]], [[normal-probabilities-via-standardization]], [[finding-values-from-normal-areas]], [[sampling-distribution]], [[unbiased-and-biased-estimators]], [[bias-correction]], [[central-limit-theorem]], [[standard-error-of-the-mean]], [[probabilities-for-sample-means]], [[normal-approximation-to-binomial]], [[continuity-correction]]                                                                                                                                                                                                                |
| 7   | Estimates and Sample Sizes                               | [[point-estimate]], [[confidence-interval]], [[confidence-interval-for-proportion]], [[margin-of-error]], [[interpreting-confidence-intervals]], [[sample-size-for-proportion]], [[adjusted-wald-and-wilson-intervals]], [[estimating-from-published-interval]], [[confidence-interval-for-mean]], [[sample-size-for-mean]], [[estimating-sigma-for-sample-size]], [[chi-squared-distribution]], [[confidence-interval-for-variance]]                                                                                                                                                                                     |
| 8   | Hypothesis Testing | [[null-and-alternative-hypotheses]], [[test-statistic]], [[critical-region-and-significance-level]], [[p-value]], [[one-tailed-vs-two-tailed-tests]], [[type-i-and-type-ii-errors]], [[statistical-power]], [[hypothesis-test-decision-methods]], [[concluding-hypothesis-tests-in-plain-language]], [[multiple-testing-problem]] |
| 9   | Inferences from Two Samples                              |                                                                                                                                                                                                                                                                                                                                                                                                       |
| 10  | Correlation and Regression                               |                                                                                                                                                                                                                                                                                                                                                                                                       |
| 11  | Multinomial Experiments and Contingency Tables           |                                                                                                                                                                                                                                                                                                                                                                                                       |
| 12  | Analysis of Variance (ANOVA)                             |                                                                                                                                                                                                                                                                                                                                                                                                       |

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
- [[multiplication-rule]] — §4-4: $P(A\text{ and }B)=P(A)\cdot P(B\mid A)$, independent vs. dependent events, with/without replacement, the 5% guideline, and the i.i.d.-likelihood / chain-rule (autoregressive) connections
- [[conditional-probability]] — §4-5: $P(B\mid A)=P(A\cap B)/P(A)$, the reduced-sample-space method, confusion of the inverse ($P(B\mid A)\ne P(A\mid B)$), and the base-rate-fallacy / precision-vs-recall connections; also §4-5's "at least one" = $1-P(\text{none})$ (covered in [[complementary-events]])
- [[monte-carlo-simulation]] — §4-6: estimating probability by imitating a procedure with random numbers and counting (birthday problem, 6-streak in coin flips); the intractable-math escape hatch, with the MC-integration / bootstrap / MCMC connections
- [[counting-and-combinatorics]] — §4-7: the five counting rules (fundamental, factorial, permutations, permutations-with-repeats, combinations) picked by *order?* and *repeats?*; $_nP_r$ vs. $_nC_r$, and the binomial-coefficient / combinatorial-explosion connections
- [[bayes-theorem]] — §4-8: **independently sourced** — Triola's §4-8 defers Bayes to its companion website, so this note was written from external references (medical-test / base-rate framing); flips $P(B\mid A)\to P(A\mid B)$ via the prior, resolving §4-5's confusion of the inverse
- [[odds]] — §4-2 Part 2: actual odds against/in-favor vs. payoff odds, the house edge (roulette 37:1 vs. 35:1), and the logit link to logistic regression

**Ch 5 — Discrete Probability Distributions**
- [[random-variable]] — §5-2: a rule assigning one number to each outcome; discrete (counted, countable) vs. continuous (measured, unbroken scale)
- [[discrete-probability-distribution]] — §5-2: the probability of each value of a random variable, the two validity requirements (ΣP(x)=1, 0≤P(x)≤1), and the area=probability histogram
- [[mean-and-variance-of-a-probability-distribution]] — §5-2 (Formulas 5-1 to 5-4): μ, σ², σ as probability-weighted sums; derived from the frequency-table formulas by swapping f/N → P(x)
- [[expected-value]] — §5-2: E = Σ[x·P(x)] = μ, the long-run average outcome, and its use in decision theory (roulette vs. craps bet)
- [[identifying-unusual-results]] — §5-2: the range rule of thumb (μ±2σ) and the rare event rule (P(x or more/fewer) ≤ 0.05); the "or more", not "exactly" subtlety
- [[hypergeometric-distribution]] — §5-4 (& §5-2 Ex. 32): counting successes in n draws *without replacement*, P(x)=C(K,x)C(N−K,n−x)/C(N,n); the without-replacement cousin of the binomial, worked on the Sky Ranch altimeters
- [[binomial-distribution-requirements]] — §5-3: the four conditions that make a procedure binomial (fixed n, independent trials, two categories, constant p), the n/x/p/q notation, and the 5% independence guideline for without-replacement sampling
- [[binomial-distribution]] — §5-3 (Formula 5-5): P(x)=C(n,x)pˣqⁿ⁻ˣ as multiplication-rule × counting; the three calculation methods (formula, technology, Table A-1), extended with E=np, Var=npq and the CLT/ML links
- [[binomial-mean-and-variance]] — §5-4 (Formulas 5-6 to 5-8): the shortcuts μ=np, σ²=npq, σ=√npq (derived as a sum of n Bernoullis), and interpreting them with the range rule np±2√npq to judge unusual counts (Mendel's 428/580 is consistent with 75%)
- [[poisson-distribution]] — §5-5: counts of rare events in an interval, P(x)=μˣe⁻ᵘ/x!, the four requirements, μ and σ=√μ (one parameter), the binomial contrast (no upper bound on x); earthquake goodness-of-fit
- [[poisson-approximation-to-binomial]] — §5-5: when n≥100 and np≤10, approximate a large-n/small-p binomial by Poisson(μ=np); Illinois Pick 3 (0.253 ≈ binomial 0.254)

**Ch 6 — Normal Probability Distributions**
- [[probability-density-function]] — §6-1/§6-2: continuous distributions as density curves; the two requirements (area = 1, f ≥ 0), area = probability, P(X = a) = 0 so ≤ and < coincide, and height ≠ probability
- [[uniform-distribution]] — §6-2 (Ejemplos 1–2): flat rectangle of height 1/(b−a), probability = width × height (voltage 123–125 V, P(>124.5) = 0.25)
- [[standard-normal-distribution]] — §6-1/§6-2 (Ejemplos 3–5): N(0,1), a normal fixed by μ and σ (Fórmula 6-1), Table A-2 left-cumulative Φ(z), and the left / right (1−Φ) / between (Φ(b)−Φ(a)) area patterns (thermometers)
- [[critical-values-and-z-alpha]] — §6-2 (Ejemplos 6–8): area → z (inverse lookup), the special cases 1.645 / 1.96 / 2.575, critical values, and z_α = area α to the right (look up 1−α)
- [[normal-probabilities-via-standardization]] — §6-3 (Fórmula 6-2, Ejemplos 1–2): x → z = (x−μ)/σ keeps the area, so Table A-2 serves every normal; door heights (80 in → 0.9999) and birth weights (2450–4390 g → 0.95)
- [[finding-values-from-normal-areas]] — §6-3 (Ejemplos 3–4, Fig. 6-16): area → z → x = μ + zσ, the four warnings, and the which-direction flowchart; 95% door (73.6 in), birth-weight cutoffs 2489 / 4573 g
- [[sampling-distribution]] — §6-4 (Ejemplos 1–5, Tablas 6-2 to 6-5): the distribution of a statistic over all samples of size n; die simulation for x̄ / s² / p̂ (centers 3.5 / 2.92 / 0.5, s² skewed right), range example {2, 3, 10}, standard error σ/√n, why sample with replacement
- [[unbiased-and-biased-estimators]] — §6-4: E[θ̂] = θ; x̄, s², p̂ unbiased vs. range, s, median biased; Example 4 checked exactly (s² 12.67 = σ², s 2.51 < 3.56, median 5 ≠ 3); "sesgado" = biased vs. "sesgada" = skewed

**Ch 7 — Estimates and Sample Sizes**
- [[point-estimate]] — §7-2: a single best guess (p̂ for p, x̄ for μ) and why a point alone gives no accuracy information
- [[confidence-interval]] — §7-2: range that captures the parameter at the stated rate across repeated samples; p̂ ± z·√(p̂q̂/n) worked on Ejemplo 3
- [[confidence-interval-for-proportion]] — §7-2: requirements (SRS, np and nq ≥ 5) and the procedure for a proportion
- [[margin-of-error]] — §7-2: E = z·√(p̂q̂/n), the half-width of the interval, and its 1/√n behavior
- [[interpreting-confidence-intervals]] — §7-2: the 95% belongs to the method, not to any one interval; the common misreadings
- [[sample-size-for-proportion]] — §7-2: n = z²p̂q̂/E² or 0.25z²/E² with no prior, round up
- [[adjusted-wald-and-wilson-intervals]] — §7-2: Wilson score interval as a better-performing alternative (Triola's x = 10, n = 20 example)
- [[estimating-from-published-interval]] — §7-2: recover p̂ and E from a published CI (midpoint and half-width)
- [[confidence-interval-for-mean]] — §7-3: x̄ ± z·σ/√n with σ known; Ejemplo 1 (men's weights, 164.49 < μ < 180.61), rounding rule, and the plausible-values reading
- [[sample-size-for-mean]] — §7-3: n = (zσ/E)², round up; Ejemplo 2 (IQ, E = 3, n = 97) and the four-times rule
- [[estimating-sigma-for-sample-size]] — §7-3: range/4, pilot sample, prior study, and the conservative-error principle
- [[chi-squared-distribution]] — §7-5: $(n-1)s^2/\sigma^2 \sim \chi^2_{n-1}$, why the distribution is skewed and non-negative, and the right-tail-only table (A-4) lookup trap
- [[confidence-interval-for-variance]] — §7-5: the asymmetric $\sigma^2$ and $\sigma$ intervals from the chi-squared critical values, with the voltage example ($0.10 < \sigma < 0.27$ V) and the normality requirement

**Ch 8 — Hypothesis Testing**
- [[null-and-alternative-hypotheses]] — §8-2: H0 with "=", H1 with ≠, <, >; the three-step procedure (Fig. 8-2) and the rule that a claim you want to support goes in H1
- [[test-statistic]] — §8-2: z, t and χ² computed as if H0 is true; the standard error uses the hypothesized value
- [[critical-region-and-significance-level]] — §8-2: rejection region, α, and critical values by tail
- [[p-value]] — §8-2: tail probability under H0, the Fig. 8-5 rules, and the "P is not p" warning
- [[one-tailed-vs-two-tailed-tests]] — §8-2: the H1 sign sets the region (Fig. 8-6)
- [[type-i-and-type-ii-errors]] — §8-2: α and β, RNV/NRNF, and the α–β–n trade-off
- [[statistical-power]] — §8-2 Part 2: 1 − β, what raises power, and the n = 153 design example
- [[hypothesis-test-decision-methods]] — §8-2: P-value, critical-region and confidence-interval routes
- [[concluding-hypothesis-tests-in-plain-language]] — §8-2: Fig. 8-7 wording and why "accept H0" is wrong
- [[multiple-testing-problem]] — §8-2: the Peto zodiac example and family-wise false positives

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
- [[multiplication-rule]] — from Ch. 4, §4-4 (Ejemplos 1–6): $P(A\cap B)=P(A)\cdot P(B\mid A)$, independent vs. dependent events, with/without replacement (pacemaker example), the 5% guideline, redundancy, and the i.i.d.-factorized-likelihood & language-model chain-rule links
- [[conditional-probability]] — from Ch. 4, §4-5 (Ejemplos 3–4): $P(B\mid A)=P(A\cap B)/P(A)$, the reduced-sample-space intuitive method (polygraph 42/51 vs. 42/57), confusion of the inverse / prosecutor's fallacy, and the base-rate-fallacy & precision-vs-recall links; the "at least one" complement half of §4-5 lives in [[complementary-events]]
- [[monte-carlo-simulation]] — from Ch. 4, §4-6 (Ejemplos 1–3): estimating probability by imitating a procedure with random numbers and counting (gender/coin, birthday-problem, 6-in-a-row streak); the LLN justification and the MC-integration / bootstrap / MCMC / RL-rollout links
- [[counting-and-combinatorics]] — from Ch. 4, §4-7 (Ejemplos 1–7): fundamental counting rule, factorial, permutations ($_nP_r$), permutations with identical items, and combinations ($_nC_r$); the *order?/repeats?* decision, exacta & lottery examples, and the binomial-coefficient (§5-3 bridge) & combinatorial-explosion / TSP links
- [[odds]] — from Ch. 4, §4-2 Part 2 (Ejemplo 13): actual vs. payoff odds, the house edge (roulette), and the logit / logistic-regression connection
- [[random-variable]] — from Ch. 5, §5-2: the outcome→number rule, discrete-countable vs. continuous-measured, and why it decides classification vs. regression / sums vs. integrals
- [[discrete-probability-distribution]] — from Ch. 5, §5-2 (Ejemplos 1–4): P(x) for each value, the two validity requirements, the probability histogram (area=probability), and the softmax/normalization link
- [[mean-and-variance-of-a-probability-distribution]] — from Ch. 5, §5-2 (Ejemplo 5, Formulas 5-1 to 5-4): μ/σ²/σ as probability-weighted sums, the f/N→P(x) derivation, the definitional-vs-shortcut variance, and the empirical-risk / bias-variance link
- [[expected-value]] — from Ch. 5, §5-2 (Ejemplo 8): E = Σ[x·P(x)] = μ as long-run average, the roulette-vs-craps decision, and the empirical-risk / RL-return connection
- [[identifying-unusual-results]] — from Ch. 5, §5-2 (Ejemplos 6–7): range rule of thumb (μ±2σ) and rare event rule (tail P ≤ 0.05), the exactly-vs-or-more subtlety (501/1000 heads), and the hypothesis-testing / anomaly-detection links
- [[hypergeometric-distribution]] — from Ch. 5, §5-4 (worked on §5-2 Ex. 32, Sky Ranch altimeters): without-replacement success count, C(K,x)C(N−K,n−x)/C(N,n), μ=nK/N and the finite population correction; the binomial cousin and the Fisher's-exact-test link
- [[binomial-distribution-requirements]] — from Ch. 5, §5-3 (Ejemplo 1): the four requirements (fixed n / independent / two categories / constant p), the n·x·p·q notation with the "x and p same success" warning, and the 5% guideline; the i.i.d.-assumption link
- [[binomial-distribution]] — enriched from Ch. 5, §5-3 (Ejemplos 1–3, Formula 5-5): P(x)=C(n,x)pˣqⁿ⁻ˣ derived as multiplication-rule × arrangement-counting (pea 0.75³·0.25²×10), the three calculation methods, plus the pre-existing E=np/Var=npq, CLT approximation, and A/B-testing / Bernoulli–Poisson links
- [[binomial-mean-and-variance]] — from Ch. 5, §5-4 (Ejemplos 1–2, Formulas 5-6 to 5-8): μ=np, σ²=npq, σ=√npq as easier shortcuts, derived cleanly as the sum of n independent Bernoullis (the derivation Triola omits), and the range-rule interpretation (Mendel 428/580 inside [414,456] → consistent with 75%); the standard-error-of-a-proportion / accuracy-CI links
- [[poisson-distribution]] — enriched from Ch. 5, §5-5 (Ejemplo 1, earthquakes): P(x)=μˣe⁻ᵘ/x!, the four requirements, one-parameter μ with σ=√μ, the binomial contrast (x unbounded), and observed-vs-expected goodness of fit; the pre-existing E=Var=λ diagnostic and Poisson-regression / NLP links
- [[poisson-approximation-to-binomial]] — from Ch. 5, §5-5 (Ejemplo 2, Illinois Pick 3): approximate a large-n/small-p binomial by Poisson(μ=np) when n≥100 and np≤10 (0.253 ≈ exact 0.254); the same limit that defines the Poisson, plus numerical-stability / rare-event-modeling links
- [[probability-density-function]] — from Ch. 6, §6-1/§6-2: density requirements, area = probability, zero probability for exact values, and the continuous-likelihood / normalizing-flow links
- [[uniform-distribution]] — from Ch. 6, §6-2 (Ejemplos 1–2): height 1/range, width × height, mean/variance, and the U(0,1)-sampling / Glorot-uniform links
- [[standard-normal-distribution]] — from Ch. 6, §6-1/§6-2 (Ejemplos 3–5): Φ(z) and Table A-2, left/right/between areas, symmetry, and the StandardScaler / GELU = xΦ(x) links
- [[critical-values-and-z-alpha]] — from Ch. 6, §6-2 (Ejemplos 6–8): area→z procedure, special z values, critical values, z_α = Φ⁻¹(1−α), and the CI / A/B-test / anomaly-threshold links
- [[normal-probabilities-via-standardization]] — from Ch. 6, §6-3 (Ejemplos 1–2): Formula 6-2, the change-of-variables proof that standardizing preserves area, and the StandardScaler / VAE reparameterization links
- [[finding-values-from-normal-areas]] — from Ch. 6, §6-3 (Ejemplos 3–4, Fig. 6-16): x = μ + zσ as the normal quantile, Triola's four warnings, rounding vs. technology, and the threshold-from-target-rate / prediction-interval links
- [[sampling-distribution]] — from Ch. 6, §6-4: definition, the three die simulations, standard error vs. population SD, enumeration of the range example, with-replacement rationale, bootstrap / test-metric / mini-batch links
- [[unbiased-and-biased-estimators]] — from Ch. 6, §6-4: bias = E[θ̂] − θ, the biased/unbiased table with reasons (linearity, n−1, Jensen), Example 4 recomputed, MSE = bias² + variance
- [[point-estimate]] — from Ch. 7, §7-2: the sample proportion/mean as the best single estimate and the unbiased/minimal-variance sense of "best"
- [[confidence-interval]] — from Ch. 7, §7-2 (Ejemplo 3): p̂ ± E, the Why-it-works derivation, and the coverage simulation
- [[confidence-interval-for-proportion]] — from Ch. 7, §7-2: the procedure and requirements for a proportion
- [[margin-of-error]] — from Ch. 7, §7-2 (Ejemplos 3–4): Formula 7-1 and the margin-as-half-width reading
- [[interpreting-confidence-intervals]] — from Ch. 7, §7-2 (Figura 7-1): correct vs. incorrect readings of a 95% CI
- [[sample-size-for-proportion]] — from Ch. 7, §7-2 (Ejemplo 4): Formulas 7-2 and 7-3 and the worst-case p = 0.5
- [[adjusted-wald-and-wilson-intervals]] — from Ch. 7, §7-2: Wilson score interval and its advantage at small n
- [[estimating-from-published-interval]] — from Ch. 7, §7-2: recovering p̂ and E from a published interval
- [[confidence-interval-for-mean]] — from Ch. 7, §7-3 (Ejemplo 1): x̄ ± z·σ/√n with σ known, the derivation from the standardized mean, requirements, and the rounding rules
- [[sample-size-for-mean]] — from Ch. 7, §7-3 (Ejemplo 2): n = (zσ/E)², the square-root trade-off, and the finite-population note
- [[estimating-sigma-for-sample-size]] — from Ch. 7, §7-3: the three ways to estimate σ before sampling and why errors must be conservative
- [[student-t-distribution]] — from Ch. 7, §7-4: the t distribution with n − 1 degrees of freedom, why replacing σ with s fattens the tails, and the t versus z critical values
- [[bias-correction]] — from Ch. 6, §6-4 (extension): measuring an estimator's habit h = E[θ̂]/θ on a simulated population with a chosen σ ("sugar bag"), dividing real estimates by h (s with n = 5: h = 0.94 = c₄), divide-vs-subtract test, bootstrap alternative

- [[chi-squared-distribution]] — from Ch. 7, §7-5: the chi-squared law of $(n-1)s^2/\sigma^2$, its mean/variance, and the table-lookup pitfall
- [[confidence-interval-for-variance]] — from Ch. 7, §7-5 (Ejemplo 2): the asymmetric variance and SD intervals, rounding, and the normality requirement

- [[normal-approximation-to-binomial]] — from Ch. 6, §6-6: conditions np ≥ 5 and nq ≥ 5 (Triola's threshold vs. 10 in some texts), μ = np, σ = √npq, the six-step procedure, and the Viking River survey (z = −1.48, 0.9306 vs. exact 0.9313)
- [[continuity-correction]] — from Ch. 6, §6-6: x ↔ [x − 0.5, x + 0.5], the at-least / more-than / at-most / fewer-than / exactly boundary table (Fig. 6-22), and the Pew Internet survey for "exactly 2060" (difference of two z-areas)

- [[null-and-alternative-hypotheses]] — from Ch. 8, §8-2: the three-step H0/H1 procedure (Fig. 8-2), the fixed-value H0, and the rule that the claim you want to support goes in H1
- [[test-statistic]] — from Ch. 8, §8-2: z, t and χ² as standardized scores under H0; why the standard error uses the hypothesized value (XSORT z = 3.21)
- [[critical-region-and-significance-level]] — from Ch. 8, §8-2 (Ejemplos 5–6): rejection region, α, and critical values by tail (±1.96, 1.645)
- [[p-value]] — from Ch. 8, §8-2 (Ejemplos 7–8, Fig. 8-5): tail rules, the XSORT P-values (0.0007 / 0.0014), and the "P is not p" warning
- [[one-tailed-vs-two-tailed-tests]] — from Ch. 8, §8-2 (Fig. 8-6): the H1 sign sets the critical region
- [[type-i-and-type-ii-errors]] — from Ch. 8, §8-2 (Tabla 8-1, Ejemplo 10): α and β, RNV/NRNF, and the α–β–n trade-off
- [[statistical-power]] — from Ch. 8, §8-2 Part 2 (Ejemplos 11–12): 1 − β, what raises power, the power table (not reproduced; flagged), and the n = 153 design example
- [[hypothesis-test-decision-methods]] — from Ch. 8, §8-2 (Figs. 8-8, 8-9; Tabla 8-2): P-value, critical-region, and confidence-interval routes
- [[concluding-hypothesis-tests-in-plain-language]] — from Ch. 8, §8-2 (Fig. 8-7, Ejemplo 9): the conclusion table and why "accept H0" is wrong
- [[multiple-testing-problem]] — from Ch. 8, §8-2 (Peto/zodiac box): family-wise false positives; the Bonferroni line is an outside addition

## Gaps — Notes Still to Create

**§6-5 — The Central Limit Theorem (planned, in order)**
- [[central-limit-theorem]] — the theorem itself: any population with μ and σ → the distribution of x̄ tends to normal as n grows; Triola's usage rule (normal population → any n; otherwise n > 30; otherwise don't use these methods); the CLT fixes the *shape* of x̄, not of the data; Fig. 6-19 uniform/skewed populations → bell-shaped x̄
- [[standard-error-of-the-mean]] — μ_x̄ = μ and σ_x̄ = σ/√n, derived from Var(Σxᵢ/n) = nσ²/n²; the √n law (halve the SE → 4× the sample); the finite population correction √((N−n)/(N−1)) when n > 5% of N
- [[probabilities-for-sample-means]] — applying the CLT: z = (x̄ − μ)/(σ/√n) vs. z = (x − μ)/σ, the "one individual or a mean?" trap (water-taxi/elevator weights), and interpreting results with the rare event rule from [[identifying-unusual-results]]; worked on the 3/4-in screws (z ≈ −1.84, one tail 0.0329, two tails 0.0658 → not unusual; bridge to two-tailed p-values in Ch. 8)

**§6-6 — Normal approximation to the binomial (written, see Permanent Notes Created)**
- ✅ [[normal-approximation-to-binomial]] — when np ≥ 5 and nq ≥ 5, μ = np and σ = √npq; why it works (a binomial is a sum of n Bernoullis, so the CLT applies); Triola's 5 threshold vs. the 10 used in some textbooks (and in [[poisson-approximation-to-binomial]]); when to use the exact formula, a calculator, or Table A-1 instead
- ✅ [[continuity-correction]] — a discrete x becomes the interval x ± 0.5; the boundary table (at least / more than / at most / fewer than / exactly → which boundary and which tail); Figure 6-22. The "exactly x" difference-of-areas method (Pew example, 0.0009 vs. exact 0.00087) was folded in here rather than split out
- Worked examples to link from the notes, not separate notes: the Viking River survey (n = 40,000, p = 0.03, at least 1150 → z = −1.48, 0.9306) and the Pew Internet survey (n = 2822, p = 0.75, exactly 2060)
- Link forward: "unusual" judgments use P(x or more) ≤ 0.05 from [[identifying-unusual-results]]; this is the same logic as the p-value in [[p-value]]

- ✅ [[bayes-theorem]] — **now written** (independently sourced, since Triola §4-8 is web-only): flips $P(B\mid A)\to P(A\mid B)$ with the prior/base rate, resolving §4-5's confusion of the inverse and the forward-links from [[conditional-probability]] / [[bernoulli-distribution]]
- ✅ [[hypothesis-test-decision-methods]] — §8-2 written as ten atomic notes (see Permanent Notes Created); the planned umbrella slug is replaced by this one
- ✅ [[confidence-interval]] / [[confidence-interval-for-mean]] / [[sample-size-for-mean]] — §7-2 and §7-3 estimation and sample size are written (proportion and known-σ mean)
- [[t-interval-for-mean]] — §7-4: confidence intervals for μ when σ is unknown (t distribution, n-1 degrees of freedom); the natural next step after §7-3
- [[correlation-and-regression]] — bridges directly to supervised ML's linear regression (T4)
- [[analysis-of-variance]] — ANOVA, comparing more than two group means
- [[sample-size-for-variance]] — §7-5: Table 7-2 for estimating σ² or σ to within a chosen percentage (Ejemplo 3: 95% confidence, 20% error for σ → n = 48); the complex-formula alternative is replaced by tables and software
- [[chi-squared-and-contingency-tables]] — categorical-data inference
