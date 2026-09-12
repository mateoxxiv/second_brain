---
tags:
  - status/seed
  - probability
related:
  - "[[sample-space-and-events]]"
  - "[[law-of-large-numbers]]"
  - "[[probability-fundamentals]]"
  - "[[statistical-significance]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-2 (Ejemplos 2–9)."
---

> **TL;DR** — There are **three** ways to assign a probability: **relative frequency** (count what actually happened), **classical** (count equally-likely outcomes, $s/n$), and **subjective** (informed estimate). The classical method *requires* equally-likely outcomes — never assume it.

---

## Intuition

"What's the probability?" has no single recipe — it depends on what you can access. If you can *run the experiment*, count outcomes (relative frequency). If the setup is symmetric and every outcome is equally likely, just count the favorable fraction (classical). If neither holds — a one-off event with no symmetry and no repeatable trials — the best you can do is an informed guess (subjective). The whole skill is diagnosing *which situation you're in*.

The cardinal sin is reaching for the clean classical formula when outcomes aren't equally likely. "Pass or fail — so P = 1/2" is wrong: two outcomes doesn't mean two *equally likely* outcomes. When you know nothing about the outcomes, that's a reason to *not* assume equal likelihood — not a license to.

## Mechanics

| Method | Formula | Requires |
|--------|---------|----------|
| **Relative frequency** | $P(A) = \dfrac{\#\text{ times }A\text{ occurred}}{\#\text{ trials}}$ | Observed/repeatable data (gives an *approximation*) |
| **Classical** | $P(A) = \dfrac{s}{n}$ | All $n$ simple events **equally likely** |
| **Subjective** | informed estimate | Knowledge of the circumstances |

- **Relative frequency** — car accidents: $6{,}511{,}100 / 135{,}670{,}000 = 0.0480$. (Can't use classical: accident vs. no-accident aren't equally likely.) It's an *estimate* that sharpens with more data — see [[law-of-large-numbers]].
- **Classical** — genotypes {AA, Aa, aA, aa}, all equally likely; "two different components" = {Aa, aA} → $2/4 = 0.5$. "Exactly 2 boys in 3 births" → $3/8 = 0.375$ (needs the correct 8-event [[sample-space-and-events|sample space]]).
- **Subjective** — probability a NASA astronaut survives a mission ≈ 0.99; probability of getting stuck in an elevator ≈ 0.0001. No data, no symmetry — expert judgment.

**⚠ Always verify equal likelihood before using $s/n$.** And **simulation** is a practical stand-in for the classical method: when exact counting is intractable (e.g. probability of winning solitaire), imitate the procedure many times and read off the relative frequency instead.

## In ML

**Relative frequency = empirical estimation / Monte Carlo.** Estimating $P$ by counting occurrences in data is exactly maximum-likelihood estimation for a categorical variable, and Monte Carlo methods approximate intractable probabilities and integrals by simulating and averaging — the classical method's escape hatch, formalized.

**Classical = uniform prior; subjective = informative prior.** The classical "equally likely" assumption is a uniform distribution over the sample space. Subjective probability is the philosophical root of **Bayesian priors** — encoding belief before data, then updating via [[probability-fundamentals|Bayes]].

## Exercises

**Basic** — A bag has 4 red and 6 blue marbles, drawn at random. Which method applies, and what is P(red)?

**Intermediate** — You flip a real thumbtack 200 times; it lands point-up 120 times. Estimate P(point-up). Why is the classical method *invalid* here even though there are only two outcomes?

**Advanced** — You want P(a shuffled deck is dealt into a winning solitaire game). All deals are equally likely, so classical *applies in principle* — explain why it's still useless in practice, and describe how a simulation gives you the answer instead.
