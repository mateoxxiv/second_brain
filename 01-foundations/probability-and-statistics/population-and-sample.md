---
tags:
  - status/seed
  - probability
related:
  - "[[probability-fundamentals]]"
  - "[[probability-distributions]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1."
---

> **TL;DR** — Statistics draws conclusions about a population by studying a sample — but the conclusion is only as trustworthy as *how* that sample was collected; no amount of analysis rescues a badly-collected one.

---

## Intuition

You almost never get to measure everyone you care about — a full census is expensive or outright impossible, so you measure a subset (a **sample**) and try to say something true about the whole (the **population**). The entire discipline of statistics exists to make that leap rigorous.

But the leap only works if the sample was collected properly — ideally through some form of random selection. A huge sample gathered the wrong way can be *worse* than a small one gathered the right way, because size fixes noise, not bias.

## Mechanics

**Core vocabulary (Triola, Ch. 1):**

| Term | Definition |
|---|---|
| Data | The raw collected information — measurements, categories, survey responses |
| Statistics | The science of planning studies, collecting data, and organizing / summarizing / analyzing / interpreting it to draw conclusions |
| Population | The complete set of every element under study |
| Census | Data collected from *every single* member of the population |
| Sample | A subset of members actually selected and measured |

**Worked example — the 1936 Literary Digest poll.** Population: all U.S. voting-age adults. Sample: 2.3 million respondents — enormous by any standard. Yet the poll predicted the wrong winner, because respondents were drawn from car registrations, phone directories, and club memberships — in 1936, a systematically wealthier, non-representative slice of the population. A much smaller but properly randomized Gallup poll got it right instead.

**The lesson, stated precisely**: sample *size* buys protection against random noise; sample *collection method* is what determines whether you're even measuring the right thing. A huge biased sample still converges — confidently — to the wrong answer.

```python
import numpy as np
rng = np.random.default_rng(42)

# true population support for a candidate: 45%
population = rng.random(1_000_000) < 0.45

# biased sample: drawn from a subgroup with different (60%) support, despite large n
biased_sample = rng.random(200_000) < 0.60
print("biased sample estimate (n=200,000):", biased_sample.mean())   # ~0.60 -- confidently wrong

# small but properly random sample
random_sample = rng.choice(population, size=1_000, replace=False)
print("random sample estimate (n=1,000):", random_sample.mean())    # ~0.45 -- close to truth
```

## In ML

**Train/test splits are population/sample thinking** — your training data is a sample from the true data-generating population you actually care about. If collection is biased (non-random scraping, survivorship bias, convenience sampling), the model learns and validates on a skewed slice, and no amount of tuning fixes that — the Literary Digest failure, wearing modern clothes.

**Dataset bias is this problem at scale** — web-scraped image or text datasets inherit whatever demographic, geographic, or platform skew their sources have. A model trained on that data generalizes to the *sample's* population, not the one you intended.

**The i.i.d. assumption depends on proper sampling** — [[probability-fundamentals]]'s independent-and-identically-distributed assumption only holds if data collection actually approximates random sampling from the target population. Violate that, and every downstream guarantee — confidence intervals, generalization bounds — is built on sand.

## Exercises

**Basic** — A university with 30,000 students wants to know average student debt. It surveys the 500 students in the campus library on a Tuesday afternoon. Identify the population, the sample, and one concrete reason this sample might not be representative.

**Intermediate** — Using the Literary Digest example, explain why a sample of 2.3 million produced a worse estimate than Gallup's much smaller one. What single factor determines sample quality more than sample size?

**Advanced** — A company trains a resume-screening model only on resumes from applicants who were eventually hired. Frame this as a population/sample mismatch: what population does the company actually want to generalize to, what is the model's real training sample, and what specific bias does the mismatch introduce?
