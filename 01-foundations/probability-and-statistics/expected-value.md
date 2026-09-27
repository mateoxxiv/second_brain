---
tags:
  - status/seed
  - probability
related:
  - "[[mean-and-variance-of-a-probability-distribution]]"
  - "[[discrete-probability-distribution]]"
  - "[[odds]]"
  - "[[law-of-large-numbers]]"
  - "[[weighted-mean]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-2 (Valor esperado)"
---

> **TL;DR** — The expected value $E = \sum[x\cdot P(x)]$ is the average outcome you'd get if you could repeat a procedure forever — and it's literally equal to the distribution's mean $\mu$.

---

## Intuition

If you played a game infinitely many times, what would your *average* result be? That long-run average is the **expected value**. It's not the outcome you expect on any single try (a game can have $E = -\$0.26$ even though you never lose exactly 26 cents on one bet) — it's the center of gravity of all outcomes, each pulled by its probability.

The name is almost misleading: the "expected" value need not be a value the variable can even take, and need not be an integer even when every outcome is. Think of it as the fair price of a gamble — over the [[law-of-large-numbers|long run]] your realized average converges to it.

## Mechanics

$$E = \sum [\,x \cdot P(x)\,] = \mu$$

Expected value **is** the [[mean-and-variance-of-a-probability-distribution|mean of the distribution]] (Formula 5-1) — same computation, different name emphasizing the "long-run average outcome" reading. It underpins **decision theory**: to compare two choices, compute each one's $E$ and pick the better.

**Worked example — betting \$5 (Triola).** Model each bet as a random variable = net gain, then take $E$:

| Bet | Outcomes & probabilities | $E = \sum x\,P(x)$ |
|-----|--------------------------|--------------------|
| Roulette, #7 | $-\$5$ w.p. $37/38$; $+\$175$ w.p. $1/38$ | $\approx -26$ ¢ |
| Craps, pass line | $-\$5$ w.p. $251/495$; $+\$5$ w.p. $244/495$ | $-35/495 \approx -7$ ¢ |

Both are negative (the house always wins long-run — see [[odds]]), but craps loses *less* per bet, so it's the better decision. Higher $E$ wins, even when the flashier bet offers a bigger jackpot.

```python
# Roulette: net gain and its probabilities
x = [-5, 175]; P = [37/38, 1/38]
E = sum(xi*pi for xi,pi in zip(x,P))     # ≈ -0.263  → about -26 cents
```

## In ML

**Every training objective is an expected value.** "Minimize the loss" formally means minimize $\mathbb{E}[\,\ell(\theta)\,]$ over the data distribution. Because we can't integrate over the true distribution, we approximate $E$ with a sample average — the empirical risk — which the [[law-of-large-numbers|law of large numbers]] promises converges to the true expectation.

**Reinforcement learning maximizes expected return.** A policy's value is the *expected* cumulative reward, $\mathbb{E}[\sum_t \gamma^t r_t]$. Just like the casino example, the agent compares actions by their expected value and greedily chooses the higher one — decision theory at scale.

## Exercises

**Basic** — A lottery ticket costs \$2. It pays \$500 with probability $1/1000$, else nothing. What is the expected net value of a ticket?

**Intermediate** — An insurance policy charges a \$300 premium. It pays out \$50,000 with probability $0.002$ this year. Compute $E$ from the *insurer's* side. Why must it be positive for them?

**Advanced** — Show that expected value is linear: $E[aX + b] = aE[X] + b$ for constants $a, b$. Use only the definition $E[X]=\sum x P(x)$ and $\sum P(x)=1$.
