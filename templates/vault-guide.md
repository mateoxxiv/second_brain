## What Is This Vault?

A personal knowledge base for mastering AI/ML from first principles to
production systems. Built on the Zettelkasten method: atomic notes, aggressive
linking, progressive depth.

## Note Types

| Type | Location | Purpose |
|------|----------|---------|
| **Fleeting** | `00-inbox/` | Quick captures. Process within 48h or discard |
| **Permanent** | `01-05` folders | One concept per note. The core of the vault |
| **Literature** | `07-resources/` | Summaries of papers, videos, courses. Always include source |
| **Project** | `06-projects/` | Implementation logs, design decisions, lessons learned |

## Note Status

Every permanent note has a status tag that tracks its maturity:

### #status/seed

Just planted. The note exists but needs work.

- Core idea may be incomplete or rough
- Few or no connections to other notes
- Missing code examples, worked examples, or derivations
- **Action**: Expand, add depth, link to related notes

### #status/growing

Actively developing. Solid content but not yet complete.

- Core idea is clear and well-explained
- Has worked examples and/or derivations
- Connected to several related notes
- May be missing edge cases, advanced examples, or polish
- **Action**: Add missing sections, refine explanations, test with exercises

### #status/evergreen

Mature and reliable. A reference you can trust.

- Comprehensive coverage with intuition, formal definitions, and worked examples
- Well-connected (5+ links to related notes)
- Includes code examples and ML applications
- Has been tested through exercises or quizzes
- Sources listed
- **Action**: Maintain. Update only if new insights emerge

### Progression

```
seed ──→ growing ──→ evergreen
 │          │            │
 │          │            └── Trusted reference, rarely changes
 │          └── Solid content, being refined through study
 └── Just created, needs expansion
```

A note earns promotion by being **studied, exercised, and connected** — not
just by having more text. If you can explain the concept from memory and solve
problems with it, it's ready to grow.

## Note Structure

Every permanent note follows this template (see `templates/permanent-note.md`):

```
**Related**: [[note1]], [[note2]]
**Tags**: #status/seed

## Core Idea        ← One paragraph, your own words
## Details          ← Deep explanation, math, derivations
## Code Example     ← Short inline snippet + link to runnable file
## Connections      ← How this relates to other concepts
## Sources          ← Where you learned this
```

## Linking Rules

- **Link aggressively** — every note should connect to 2+ others
- **Use [[wikilinks]]** — Obsidian resolves them automatically
- **Prefer links over tags** — tags are only for status
- **Link forward** — reference concepts you haven't written yet (they'll exist eventually)

## Code Files

Runnable Python implementations live in `code/` and are linked from notes:

```
code/
├── foundations/    ← Linear algebra, calculus, probability
├── ml/            ← Supervised, unsupervised, evaluation
├── dl/            ← Neural networks, CNNs, transformers
├── llms/          ← API integrations, agents
└── projects/      ← End-to-end implementations
```

Every code file includes an `exercises()` function with progressive challenges
(basic, intermediate, advanced).

## Folder Map

```
00-inbox/              Unsorted captures
01-foundations/        Math, algorithms, databases
02-machine-learning/   Supervised, unsupervised, evaluation
03-deep-learning/      Neural networks, CNNs, transformers
04-llms-and-agents/    APIs, agents, RAG, prompt engineering
05-mlops/              Deployment, monitoring, CI/CD
06-projects/           Hands-on implementations
07-resources/          Papers, courses, roadmap
templates/             Note templates and this guide
code/                  Runnable Python files
```
