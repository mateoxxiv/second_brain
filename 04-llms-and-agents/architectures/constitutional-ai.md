---
tags:
  - status/seed
  - llms
related:
  - "[[types-of-machine-learning]]"
  - "[[anthropic-claude-api]]"
  - "[[claude-academy-claude-101]]"
domain: llms
sources:
  - "Bai et al., 2022. Constitutional AI: Harmlessness from AI Feedback (arXiv:2212.08073)."
  - "Askell et al., 2021. A General Language Assistant as a Laboratory for Alignment (the HHH framing)."
  - "Claude Academy — Claude 101, Lesson 1 (product touchpoint)."
---

> **TL;DR** — Constitutional AI (CAI) aligns a model to be **helpful, harmless, and honest** by having it *critique and revise its own outputs against a written set of principles* — a "constitution" — so most human harm-labels are replaced by **AI feedback (RLAIF)**.

---

## Intuition

Standard [[types-of-machine-learning|RLHF]] teaches harmlessness by paying humans to label mountains of harmful outputs. That's slow, expensive, exposes labelers to toxic content, and — worst for trust — bakes in values that are *never written down*. Constitutional AI fixes both problems at once: **write the values down explicitly** (a short list of natural-language principles), then let the model *police itself* against them. Instead of a human saying "this answer is harmful," the model reads a principle, judges its own draft, and rewrites it. Values become transparent and auditable, and the expensive human-labeling step is largely removed — the "compañero de pensamiento" you talk to is one trained to reason about its own behavior, not just to pattern-match a reward.

## Mechanics

The **HHH objective** (Askell 2021): be **Helpful** (do what the user wants), **Harmless** (refuse/avoid harm), and **Honest** (don't fabricate or deceive). Helpfulness and harmlessness are in tension — CAI's job is to raise harmlessness *without* collapsing into a useless "I can't help with that."

Training runs in two stages:

| Stage | What happens | Feedback source |
|-------|--------------|-----------------|
| **1. Supervised (self-critique)** | Model answers a red-team prompt → is asked to *critique* the answer against a sampled constitutional principle → *revises* it → the model is fine-tuned on the revised answers | the model, guided by the constitution |
| **2. RL from AI Feedback (RLAIF)** | Model generates response *pairs* → an AI judge picks the more harmless one per the constitution → those preferences train a **preference model** → the policy is optimized against it (RL) | AI preferences (not human harm-labels) |

Stage 1 moves the model into the right region cheaply; Stage 2 sharpens it with reinforcement learning, exactly like RLHF but with the human harm-comparisons swapped for AI ones. Helpfulness data can still come from humans; only the *harm* signal is automated.

```text
draft = model(prompt)
critique = model(f"Critique this reply per principle: {sample(constitution)}\n{draft}")
revised  = model(f"Rewrite the reply to fix the critique:\n{draft}\n{critique}")
# fine-tune on (prompt → revised); then RLAIF on AI-judged pairs
```

## In ML

**It's RLHF with the labeler replaced by a rule-following model.** The RL machinery (preference model + policy optimization) is identical; the innovation is *where the preference signal comes from* — a scalable, documented constitution instead of ad-hoc human harm judgments. This is why it scales past what human labeling could reach.

**It's what makes a model steerable and safer at once.** Because harmlessness is learned as *reasoning about principles* rather than blanket refusal, the model can be pointed at a tone/persona and still stay in-bounds — the "dirigible y colaborativo" property Claude 101 advertises: fewer harmful outputs *and* easier to direct.

**Honesty is the hardest leg.** Harmlessness has a clear training signal (avoid X); honesty/calibration does not — a fluent fabrication looks fine to an AI judge. This is the open frontier that connects CAI to hallucination and calibration research.

## Exercises

**Basic** — State the three HHH goals in your own words and give one prompt where *helpful* and *harmless* pull in opposite directions.

**Intermediate** — Explain why replacing human harm-labels with AI feedback (RLAIF) scales better than RLHF, and name one risk this introduces that human labeling didn't.

**Advanced** — A "constitution" is just text the model conditions on. Argue how the *choice and wording* of principles could bias outcomes, and propose one way to test whether a model actually follows its constitution rather than merely reciting it.
