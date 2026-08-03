---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[data-cleaning-for-people-analytics]]"
  - "[[people-analytics-employee-lifecycle]]"
  - "[[people-analytics]]"
  - "[[bias-in-people-analytics]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — Likert-scale scores only measure what you thought to ask; a 4-phase pipeline (clean → quantitative exploration → NLP on open comments → sentiment scoring) surfaces what employees actually said, which can overturn the story the numbers alone tell.

---

## Intuition

A closed question ("rate your manager 1–5") is easy to average but limited to the dimension you predefined. An open comment can say anything — richer, but unreadable at scale by a human across thousands of exit interviews. NLP is what makes free text tractable, the same way a pivot table makes a numeric column tractable: it turns "too much to read" into a pattern you can act on.

## Mechanics

**Likert scale** — a rating scale (e.g. 1–5) that converts a subjective perception into a number that can be averaged and compared across people, departments, or time.

**Natural Language Processing (NLP)** — the branch of AI that lets a machine understand, classify, and extract meaning from human-written text; here, used to analyze open comments without reading every one individually.

**The 4-phase pipeline:**

| Phase | Input | Output | Typical tooling |
|---|---|---|---|
| 1. Clean & standardize | Raw exports, different format per area/geography | One homologated dataset, comparable across segments | Excel — see [[data-cleaning-for-people-analytics]] |
| 2. Quantitative exploration | Likert-scale variables | Best- and worst-performing variables | Excel, for moderate volumes |
| 3. NLP on open comments | Free-text responses | Frequent terms and themes closed questions never asked about | R / Python NLP libraries |
| 4. Sentiment analysis | Free-text responses + a reference word list | A numeric emotional-tone score per comment, area, or geography | R / Python NLP libraries |

**How sentiment scoring works** — each word in a comment is compared against a lexicon that assigns it a positive or negative weight (e.g. "terrible" scores far more negative than "bad"). Summing a comment's word scores gives one value per comment; aggregating by area or geography gives one value per segment. Plot the distribution as a histogram, cross-referenced by segment, to see where perception skews positive, negative, or neutral.

**Why phase 3–4 matter even when phase 2 looks clean** — in one project, the phase-2 quantitative exploration alone gave one picture, but phase 3's frequent-term analysis surfaced *different* improvement areas the Likert questions never captured. The initial hypothesis — that people leaving the company write mostly negative comments — was then tested with phase 4 and refuted: sentiment scores came back more favorable than expected, changing the internal read on the exit climate entirely.

```python
lexicon = {"terrible": -3, "bad": -1, "great": 2, "good": 1}

def sentiment_score(comment: str) -> int:
    words = comment.lower().split()
    return sum(lexicon.get(w, 0) for w in words)

print(sentiment_score("the manager was terrible but the team was great"))  # -3 + 2 = -1
```

**Choosing how deep to go** — not every project needs phases 3–4. The right depth depends on three factors: (1) the maturity of your HR processes, (2) available tooling — Excel vs. a statistical language like R, (3) the team's analytical skillset. Excel-only phase 1–2 is a legitimate stopping point if that's genuinely all the situation calls for.

## In ML

**Lexicon-based sentiment is the classical baseline** — summing per-word scores from a fixed list is fast and interpretable, but blind to negation, sarcasm, and context ("not bad" scores as negative). Modern pipelines replace the fixed lexicon with a fine-tuned classifier or an LLM prompt, trading interpretability for nuance.

**Frequent-term discovery is topic modeling in disguise** — phase 3's "which words appear most" result is an informal version of keyword extraction / topic modeling; embedding + clustering (see [[people-analytics-employee-lifecycle]]'s offboarding stage) formalizes the same idea into machine-discovered themes instead of manually eyeballed word frequencies.

**Likert score + sentiment score as two features, not one metric** — treating the 1–5 rating as a numeric feature and the sentiment score as a second, independent feature lets both feed the same downstream model (e.g. an attrition-risk classifier) instead of forcing one proxy to represent the whole employee experience.

## Exercises

**Basic** — Using the lexicon `{"terrible": -3, "bad": -1, "great": 2, "good": 1}`, compute the sentiment score for "the process was bad but my manager was good." What single limitation of lexicon-based scoring does this example expose (hint: word order and negation)?

**Intermediate** — The initial hypothesis ("leavers write mostly negative comments") was refuted by phase 4. Which phase alone — 1, 2, or 3 — could never have caught this, and why does averaging Likert scores hide the emotional tone entirely?

**Advanced** — A company runs 3,000 exit interviews a year across 5 languages. What breaks in the lexicon-based sentiment approach at that scale, and what would you replace phases 3–4 with? Justify the choice against the three depth-decision factors in this note.
