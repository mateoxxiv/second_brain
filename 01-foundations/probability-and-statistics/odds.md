---
tags:
  - status/seed
  - probability
related:
  - "[[probability-fundamentals]]"
  - "[[complementary-events]]"
  - "[[three-methods-of-assigning-probability]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-2 (Parte 2, Ejemplo 13)."
---

> **TL;DR** — **Odds** re-express a probability as a ratio. *Actual* odds against $A$ = $P(\bar A):P(A)$ (the real chances); *payoff* odds are set by the house to guarantee profit, so they never equal the actual odds.

---

## Intuition

Gamblers quote "35 to 1," not "0.027." Odds are just a probability rewritten as a ratio of two chances, and they're preferred at casinos and racetracks because they map directly onto money: "35:1" means "win \$35 for each \$1 staked." Statisticians dislike them (ratios make algebra ugly) and stick to probabilities — but the two encode the same information, and one key ML tool (logistic regression) is built *on* odds.

The critical distinction is **actual vs. payoff** odds. Actual odds describe reality (the true probability). Payoff odds are a *business decision* by the house — deliberately stingier than the actual odds. The gap between them is exactly the house's profit margin.

## Mechanics

For an event $A$ with true probability $P(A)$ (and complement $P(\bar A)$):

| Quantity | Definition |
|----------|------------|
| **Actual odds against** $A$ | $\dfrac{P(\bar A)}{P(A)}$, written $a{:}b$ (integers, no common factor) |
| **Actual odds in favor** of $A$ | reciprocal — $b{:}a$ |
| **Payoff odds against** $A$ | $(\text{net profit}):(\text{amount bet})$, set by the house |

**Worked — roulette, \$5 on number 13.** $P(13)=\frac1{38}$, $P(\text{not }13)=\frac{37}{38}$.

- **Actual odds against 13** $= \dfrac{37/38}{1/38} = \dfrac{37}{1} = 37{:}1$.
- **Casino's payoff odds** are only $35{:}1$ → net profit \$35 per \$1, so a \$5 win pays $5\times35 = \$175$ profit (plus your \$5 back).
- A *fair* game would pay the actual $37{:}1$ → \$185 profit on \$5. The house pockets the \$10 difference — that's the **house edge**.

## In ML

**Odds → log-odds → logistic regression.** The natural log of the odds, $\ln\frac{p}{1-p}$, is the **logit** — the exact quantity a logistic regression predicts as a linear function of features. The model outputs a log-odds; the sigmoid inverts it back to a probability $p$. So "odds" isn't just a gambling curiosity — it's the native output space of the most common classifier.

**Odds ratios in statistics.** In epidemiology and A/B testing, the *odds ratio* (odds under treatment ÷ odds under control) is a standard effect-size measure, and logistic-regression coefficients are literally log-odds-ratios once exponentiated.

## Exercises

**Basic** — An event has probability $P(A)=0.25$. Find the actual odds against $A$ and the actual odds in favor of $A$.

**Intermediate** — A racetrack offers payoff odds of $4{:}1$ on a horse whose true win probability is $0.25$ (actual odds against $=3{:}1$). On a \$10 bet, how much does the track keep relative to a fair payout? Is this bet favorable to the track?

**Advanced** — Show that the logit $\ln\frac{p}{1-p}$ maps $p\in(0,1)$ onto all of $(-\infty,\infty)$, and that $p=0.5$ ↔ log-odds $=0$ ↔ actual odds $1{:}1$. Explain why this makes log-odds the convenient space for a *linear* model to predict a probability.
