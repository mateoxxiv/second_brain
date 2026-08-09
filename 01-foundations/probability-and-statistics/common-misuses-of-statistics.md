---
tags:
  - status/seed
  - probability
related:
  - "[[principles-of-statistical-thinking]]"
  - "[[population-and-sample]]"
  - "[[statistical-significance]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-4."
---

> **TL;DR** — A statistic can be arithmetically perfect and still lie: most real-world abuse comes from a fixed catalog of failure modes — bad samples, loaded questions, confused percentages, and correlation dressed up as causation — and knowing the list is how you spot them.

---

## Intuition

"There are three kinds of lies: lies, damned lies, and statistics" (Disraeli). The point of §1-4 isn't to distrust statistics — it's that the *misuses* cluster into a small number of recurring shapes. Once you can name them, you catch them on sight, whether they come from a dishonest actor or an innocent mistake. This is the concrete companion to the four-factor checklist in [[principles-of-statistical-thinking]]: that note gives the *framework* (context, source, sampling, conclusions); this one is the *field guide* to the specific traps.

The quickest reflex: a *precise* number ("103,215,027 households") feels *accurate*, but precision is not accuracy — it's often just an estimate wearing a suit.

## Mechanics

**The catalog of misuses (Triola §1-4):**

| Misuse                          | What goes wrong                                                                             | Example                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Voluntary response sample       | Subjects self-select; people with extreme views over-participate → biased, unrepresentative | Newsweek's online Napster poll; the 1936 *Literary Digest* mail-in              |
| Correlation ≠ causation         | An association is reported (or implied) as one variable *causing* another                   | Smoking vs. pulse rate correlate — neither is shown to cause the other          |
| Self-interest / sponsored study | Funder profits from the result → conflict of interest                                       | Kiwi Brands (shoe polish) "scuffed shoes lose interviews"; pharma-funded trials |
| Reported vs. measured results   | People report the flattering answer, not the true one                                       | 70% *say* they voted; records show only 61% did — measure weight, don't ask it  |
| Small samples                   | Conclusion rests on too few cases (even inside a big survey, once you slice subgroups)      | "67% suspended ≥3 times" — based on **3** students                              |
| Misleading percentages          | % > 100% abused; base unclear                                                               | Continental's "improved lost-baggage 100%" would mean *zero* bags lost          |
| Loaded / order-biased questions | Wording or question order steers the answer                                                 | 97% vs. 57% "yes" for the same veto question, reworded                          |
| Nonresponse & missing data      | Refusers differ systematically from responders; missing not at random                       | Census undercounts low-income/homeless; phone-only surveys miss the poor        |
| Precise ≠ accurate              | A very exact-looking figure is really an estimate                                           | "103,215,027 households" is really ~103 million                                 |
| Deliberate distortion           | Outright fabrication or hidden methodology                                                  | *Corporate Travel*'s Avis survey; faked coin-flip data (Benford's law flags it) |

**Percentage arithmetic (the recurring source of confusion):** "percent" literally means *divided by 100*.

```python
# the four conversions Triola drills, since most percentage abuse is a base/units slip
pct_of   = lambda p, amount: (p / 100) * amount   # 6% of 1200  -> 72.0
frac2pct = lambda num, den: (num / den) * 100      # 3/4         -> 75.0
dec2pct  = lambda d: d * 100                        # 0.250       -> 25.0
pct2dec  = lambda p: p / 100                        # 85%         -> 0.85
print(pct_of(6, 1200), frac2pct(3, 4), dec2pct(0.250), pct2dec(85))
```

**Worked examples (Triola §1-4):**

- **Voluntary response** — *Newsweek*'s online poll asked readers "Would you keep using Napster if it charged a fee?"; of 1,873 self-selected responses, 19% said yes. People with strong opinions self-select, so the figure describes only *who bothered to click*, not the population.
- **Voluntary response, the classic** — *Literary Digest* (1936) mailed 10 million ballots, got 2.3 million back, and predicted Landon would win. Gallup, with only ~50,000 *properly sampled* people, correctly called Roosevelt. Size didn't save a self-selected, wealthier-skewed sample.
- **Reported vs. measured** — 70% of 1,002 people *said* they voted in a recent election; official records showed only 61% actually did. Ask for weight and people give their *desired* weight — put them on a scale instead.
- **Small sample** — the Children's Defense Fund reported "67% of suspended students were suspended ≥3 times" — a figure computed from just **3** students; the media never mentioned the sample size.
- **Small sample by slicing** — even "2,000 randomly chosen adults" becomes tiny once you drill to "21-year-old Republican men in Pocatello."
- **Misleading percentage** — Continental Airlines advertised it had "improved lost baggage by 100% in six months." A 100% improvement would mean *zero* bags lost — which they hadn't achieved.
- **Loaded wording** — "Should the president use the veto to *eliminate waste*?" got 97% yes; "Should the president use the veto, *or not*?" got 57% yes. Same power, different wording. Likewise "welfare" (19% agree) vs. "assistance to the poor" (63% agree).
- **Question order** — a German survey: naming traffic first, 45% blamed traffic for air pollution; naming industry first, 57% blamed industry. Order alone flipped the result.
- **Self-interest** — Kiwi Brands (shoe polish) funded a survey concluding scuffed shoes were the top reason applicants failed interviews. Always ask whether the sponsor profits from the answer.
- **Precise ≠ accurate** — "There are 103,215,027 households in the U.S." looks exact but is really an estimate; "about 103 million" is the honest phrasing.
- **Deliberate distortion** — *Corporate Travel* ran a survey naming Avis the car-rental winner; when Hertz asked for the raw data, the responses had "disappeared" and the survey coordinator resigned. (Fabricated data often fails randomness checks — real 500-flip coin runs contain streaks of six, and first digits obey **Benford's law**.)

## In ML

**Voluntary-response bias = selection bias in training data** — opt-in feedback, product reviews, and user-generated content are self-selected samples; a model trained on them learns the opinions of whoever bothered to participate, exactly the [[population-and-sample|Literary Digest]] failure at scale.

**Correlation ≠ causation is the cardinal sin of model interpretation** — a model finding feature A predicts label B never licenses "A *causes* B." Feature-importance and SHAP values describe association, not intervention; acting on them as causal is how deployed models produce harmful policy.

**Nonresponse ↔ missing-not-at-random data** — when missingness correlates with the target (low earners hiding income), naive imputation bakes the bias in. Recognizing the *mechanism* of missingness (MCAR / MAR / MNAR) is the ML translation of Triola's "missing data" warning.

## Exercises

**Basic** — A radio host asks listeners to call in: "Do you support the new tax?" 8,000 call, 80% say no. Name the specific misuse and explain why the 80% can't be generalized to the city.

**Intermediate** — A gym advertises "members improved their fitness by 200%." Explain, using the percentage rules, why this claim is either meaningless or needs a clearly defined base to interpret.

**Advanced** — A study funded by a sugar-industry group finds a correlation between "artificial sweetener use" and weight gain, and the press release implies sweeteners *cause* weight gain. Identify *three* separate misuses from the catalog at work here and explain each.
