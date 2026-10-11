---
tags:
  - status/seed
  - probability
related:
  - "[[law-of-large-numbers]]"
  - "[[three-methods-of-assigning-probability]]"
  - "[[complementary-events]]"
  - "[[binomial-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-6 (Ejemplos 1–3)."
---

> **TL;DR** — A **simulation (Monte Carlo)** estimates a probability by *imitating* the procedure many times with random numbers and counting how often the event happens — the escape hatch when the exact math is intractable.

---

## Intuition

Sometimes the formula is a nightmare. What's the probability that 200 coin flips contain a run of 6+ heads or 6+ tails? Deriving it exactly is brutal. But you can *just flip the coin* — or, faster, have a computer generate 200 random 0/1s and scan for a streak. Repeat a few thousand times, count the fraction with a streak, and you have your answer without a single formula.

That's the whole idea: **replace analysis with imitation.** Build a process that *behaves like* the real one (a "simulation"), run it a lot, and read the probability off the [[three-methods-of-assigning-probability|relative frequency]] of the event. It trades a hard derivation for cheap computation — and it works because of the [[law-of-large-numbers|law of large numbers]].

## Mechanics

**Definition (Triola):** a *simulation* of a procedure is a process that behaves the same way as the procedure, so it produces similar results.

**The recipe:**
1. **Model** each outcome with random numbers (fair coin → 0/1; a birthday → an integer 1–365).
2. **Generate** one trial's worth of random values.
3. **Check** whether the event of interest occurred.
4. **Repeat** N times; estimate $P(\text{event}) \approx \dfrac{\#\text{ trials with the event}}{N}$.

By the [[law-of-large-numbers|LLN]] this estimate converges to the true probability; its error shrinks like $1/\sqrt{N}$ — so 100× more trials gives ~10× more accuracy (diminishing returns).

**Worked — the birthday problem** (P that ≥2 of 25 people share a birthday). Exact math is fiddly; simulation is trivial:

```python
import numpy as np
rng = np.random.default_rng(0)

def trial(n=25):
    days = rng.integers(1, 366, size=n)          # 25 random birthdays
    return len(np.unique(days)) < n              # True if any collision

est = np.mean([trial() for _ in range(10_000)])
print(round(est, 3))                             # 0.558  (exact ≈ 0.5687)
```

## In ML

**Monte Carlo estimates intractable expectations.** Approximating $\mathbb{E}[f(X)]$ by the sample mean $\frac1N\sum f(x_i)$ over simulated draws is *the* workhorse when the integral has no closed form — the basis of MC integration, policy rollouts in reinforcement learning, and MCMC posterior sampling in Bayesian inference.

**The bootstrap is simulation for uncertainty.** Resampling your data with replacement many times and recomputing a statistic estimates its sampling distribution — a simulation-based alternative to analytic standard-error formulas.

**Simulation reveals what intuition misses.** Just as Triola's students under-produce 6-streaks when faking coin flips (real randomness is streakier than people expect), simulation surfaces counterintuitive behavior — MC dropout for uncertainty, randomized ablations, and stress-testing pipelines all lean on "just run it many times."

## Exercises

**Basic** — Describe a simulation to estimate the probability of getting exactly 2 heads in 3 coin tosses. What do you represent with random numbers, and what do you count?

**Intermediate** — Using the [[complementary-events|complement]], the "at least one 6 in four rolls" probability is $1-(5/6)^4\approx0.518$. Sketch a simulation that estimates it, and explain how you'd know your N is large enough.

**Advanced** — Explain why a simulation's error falls like $1/\sqrt{N}$ rather than $1/N$, and what that implies for how many trials you need to add one more decimal digit of accuracy. Connect this to the [[law-of-large-numbers|LLN]].
