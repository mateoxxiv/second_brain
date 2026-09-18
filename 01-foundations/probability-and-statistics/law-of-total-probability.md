---
tags:
  - status/seed
  - probability
related:
  - "[[conditional-probability]]"
  - "[[bayes-theorem]]"
  - "[[multiplication-rule]]"
  - "[[addition-rule]]"
  - "[[complementary-events]]"
  - "[[probability-fundamentals]]"
domain: probability
sources:
  - "Blitzstein & Hwang, Introduction to Probability, 2nd ed., §2.3 (Law of Total Probability)."
---

> **TL;DR** — The **law of total probability** reassembles the overall probability of an event from its [[conditional-probability|conditional]] pieces across a set of cases: $P(B)=\sum_i P(B\mid A_i)\,P(A_i)$.

---

## Intuition

Split the world into non-overlapping groups (men/women, disease/no-disease). To find the *overall* chance of an event, find its chance **inside each group**, scale each by how big that group is, and **add them up**. You're reassembling the whole from its conditional parts — that's why it's called "total."

Analogy: to get a company's average salary, you don't need one giant list — take each department's average, weight it by the department's headcount, and sum. Same move: local (conditional) facts, weighted by size, combined into a global one. The trick is that the groups must **partition** the population — cover everything, overlap nowhere — so nobody is missed or double-counted.

## Mechanics

**Where it comes from** (derive it, don't memorize). Let $A_1,\dots,A_n$ **partition** the sample space (disjoint, and together everything). The event $B$ is then chopped into disjoint slices $B\cap A_i$:

$$B = (B\cap A_1)\cup(B\cap A_2)\cup\dots\cup(B\cap A_n)$$

Because the slices are disjoint, the [[addition-rule|addition rule]] adds them with no overlap term:

$$P(B)=\sum_i P(B\cap A_i)$$

Now rewrite each joint with the [[multiplication-rule|multiplication rule]], $P(B\cap A_i)=P(B\mid A_i)P(A_i)$:

$$\boxed{P(B)=\sum_i P(B\mid A_i)\,P(A_i)}$$

**Two-case form** (an event and its [[complementary-events|complement]]):
$$P(B)=P(B\mid A)P(A)+P(B\mid \bar A)P(\bar A)$$

**Worked — the Bayes denominator.** Disease prevalence 1%, $P(+\mid D)=0.99$, $P(+\mid \bar D)=0.05$. Total chance of a positive test:
$$P(+)=0.99\cdot 0.01 + 0.05\cdot 0.99 = 0.0594$$

```python
groups = [("D", 0.01, 0.99), ("not_D", 0.99, 0.05)]   # (name, P(group), P(+|group))
p_positive = sum(p_group * p_pos for _, p_group, p_pos in groups)
print(round(p_positive, 4))   # 0.0594
```

## In ML

**It's the denominator of [[bayes-theorem|Bayes]].** The "evidence" term $P(B)$ that normalizes a posterior is *always* a total-probability sum over hypotheses — which is why it's often the hardest part of Bayes to compute (and why methods like MCMC exist to dodge it).

**Marginalization is this law.** Getting a marginal $P(x)=\sum_z P(x\mid z)P(z)$ by summing a latent/hidden variable $z$ out of the joint is exactly total probability — the engine behind **mixture models** ($P(x)=\sum_k \pi_k\,P(x\mid \text{component }k)$), the EM algorithm, and hidden Markov models.

**Conditioning to simplify.** When a direct probability is hard, split on a helpful variable, solve each easy conditional case, and recombine — a routine problem-solving move (the discrete cousin is the law of total *expectation*, $\mathbb{E}[X]=\sum_i \mathbb{E}[X\mid A_i]P(A_i)$).

## Exercises

**Basic** — A factory: machine A makes 60% of parts (2% defective), machine B makes 40% (5% defective). What fraction of *all* parts are defective?

**Intermediate** — Two urns: Urn 1 (70% chance of being picked) has 3 red/7 blue; Urn 2 has 6 red/4 blue. Use total probability to find P(red). Then check it against Bayes by finding P(Urn 1 | red).

**Advanced** — Show that the two-case form is a special case of the general formula with the partition $\{A,\bar A\}$. Then explain why the $A_i$ *must* partition the space — what breaks if they overlap, and what breaks if they don't cover everything?
