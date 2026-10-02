---
tags:
  - status/seed
  - llms
  - prompt-engineering
related:
  - "[[claude-context-layers]]"
  - "[[claude-academy-claude-101]]"
  - "[[ai-fluency-framework]]"
  - "[[anthropic-claude-api]]"
  - "[[constitutional-ai]]"
domain: llms
sources:
  - "https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude"
  - "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"
---

> **TL;DR** — An effective prompt briefs Claude like a new coworker in three parts — **stage** (who you are + why), **task** (verb + scope), **rules** (format, length, tone, examples) — and every part removes guesses the model would otherwise fill with the generic average.

---

## Intuition

A smart coworker on day one knows nothing about your company. Say "make me a report" and they guess the audience, the purpose, the depth, and the format. Each prompt component answers one class of those guesses. Talk to Claude *"naturally, concisely, and conversationally"* — but completely.

## Mechanics

**Why context helps (derivation).** The model samples an answer $Y$ given your prompt $X$. Adding information $C$ (role, goal, rules) can only reduce uncertainty on average, because conditioning never increases entropy:

$$H(Y \mid X, C) = H(Y \mid X) - I(Y; C \mid X) \le H(Y \mid X), \quad \text{since } I(Y;C \mid X) \ge 0$$

Fewer plausible answers → less mass on the bland "average" response. Each component targets a different source of uncertainty:

| Component | Page's question | What to include | Common mistake |
|-----------|-----------------|-----------------|----------------|
| **1. Set the stage** | Your role, objectives, context? | Role (sets level/lens), **objective** (the *why* — lets Claude make unstated choices well), background (constraints, audience) | Omitting the objective: a task with no purpose can't be prioritized |
| **2. Define the task** | Write, analyze, build…? | A precise **verb** + explicit **scope** + named deliverables | Vague verbs ("look at"), or bundling unrelated tasks in one turn |
| **3. Specify rules** | Style, tone, examples? | Format/structure, length, tone, sources, an **attached example** | Describing style with adjectives instead of showing a sample |

**Dependency chain:** stage shapes what the task emphasizes → task shapes what the rules must structure → rules make the output checkable against the stage's goal.

**Worked example (from the lesson):**

```text
[STAGE] I'm the marketing lead at an indie streaming startup, preparing a
        pitch deck for Series A investors.            # role + small player + investor lens
[TASK]  Research the current independent film streaming market and identify
        key trends, competitor positioning, and growth opportunities.
                                                      # 2 verbs, narrow scope, 3 deliverables
[RULES] Use current web research with citations; professional report, up to
        5 pages: executive summary, market analysis, competitive landscape,
        growth opportunities.                         # sources, format, length, sections
```

Note how the sections in RULES mirror the deliverables in TASK, plus an executive summary because the STAGE says the readers are investors.

**Iterate:** the first prompt is a draft. *Follow-up* appends (good for polish); *editing* a message (pencil icon) replaces everything after it (better when the answer went off-track — the bad answer leaves the context; see [[claude-context-layers]]).

## In ML

**System vs. user prompt** — In the [[anthropic-claude-api]], durable stage + rules usually live in the `system` parameter, the per-request task in `messages`. Same three parts, split by how long they last.

**Few-shot prompting** — "Attach an example" is in-context learning: demonstrations condition the output distribution without any weight update — the cheapest alternative to fine-tuning.

**Agents and evals** — Agent instructions and LLM-as-judge rubrics are prompts with very strict rules; vague rules there become unreliable tool calls or noisy scores.

## Exercises

**Basic** — Label the stage / task / rules in: *"I teach 10th-grade biology. Make a 10-question multiple-choice quiz on photosynthesis, with an answer key, at a level suitable for struggling readers."* Which part is weakest?

**Intermediate** — Rewrite *"Write something about our new product for social media"* with all three parts. Then name the single missing fact that would change the output most, and justify it with the entropy argument.

**Advanced** — The inequality only holds *on average*. Construct a case where adding context makes the answer worse (hint: contradictory rules, or a misleading example the model copies too closely). What does this say about "more context is always better"?
