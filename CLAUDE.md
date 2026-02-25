# Second Brain — AI/ML Knowledge Base

## Project Overview

This is a personal Obsidian vault and learning repository. The owner (Mateo) is building a comprehensive knowledge base covering AI, ML, deep learning, LLMs, and all supporting foundations — from first principles to production systems. The goal is to become an expert AI architect and engineer: someone who can design, implement, and orchestrate intelligent systems end-to-end.

Mateo has an intermediate level in both theory (math, statistics) and computation (Python, ML libraries), but this vault intentionally covers topics from scratch for deep review and mastery.

## Communication

- **Language**: Always English — both in conversation and in all generated content (notes, code, comments, commit messages).
- **Teaching style**: Mix of direct explanation and Socratic questioning. Explain concepts clearly first, then challenge with questions to test understanding.
- **Content recommendations**: Proactively suggest learning resources — papers, blog posts, videos, documentation, courses — relevant to whatever topic we're working on.
- **Role**: Act as a study partner, not just an assistant. Push back, correct misconceptions, and suggest what to learn next.

## Vault Structure

Single Obsidian vault with the following folder hierarchy:

```
second_brain/
├── 00-inbox/                  # Fleeting notes, quick captures, unsorted ideas
├── 01-foundations/
│   ├── linear-algebra/
│   ├── calculus/
│   ├── probability-and-statistics/
│   ├── algorithms-and-data-structures/
│   └── databases/
├── 02-machine-learning/
│   ├── supervised/
│   ├── unsupervised/
│   ├── ensemble-methods/
│   ├── feature-engineering/
│   └── evaluation/
├── 03-deep-learning/
│   ├── fundamentals/
│   ├── cnns/
│   ├── rnns/
│   ├── transformers/
│   └── training-techniques/
├── 04-llms-and-agents/
│   ├── architectures/
│   ├── fine-tuning/
│   ├── rag/
│   ├── prompt-engineering/
│   ├── agent-frameworks/
│   ├── apis-and-services/       # OpenAI, Anthropic, Gemini, Mistral, Cohere, Replicate APIs
│   ├── tooling-ecosystem/       # Vector DBs, eval frameworks, observability, orchestration tools
│   └── integration-patterns/    # Multi-model routing, fallbacks, cost optimization, API design
├── 05-mlops/
│   ├── deployment/
│   ├── monitoring/
│   ├── ci-cd/
│   └── infrastructure/
├── 06-projects/               # Hands-on implementations and exercises
├── 07-resources/              # Papers, courses, bookmarks, curated content
├── templates/                 # Note templates (see Note System below)
└── code/                      # Runnable Python files linked from notes
    ├── foundations/
    ├── ml/
    ├── dl/
    ├── llms/
    └── projects/
```

## Note System (Zettelkasten-based)

### Note Types

1. **Fleeting notes** (`00-inbox/`) — Quick captures during study. Process within 24-48 hours into permanent notes or discard.
2. **Literature notes** (`07-resources/`) — Summaries of external sources (papers, videos, blogs). Always include source link and date.
3. **Permanent notes** (folders `01` through `05`) — Atomic, self-contained knowledge units. One concept per note.
4. **Project notes** (`06-projects/`) — Implementation logs, design decisions, lessons learned.

### Atomic Note Rules

- **One idea per note**. If a note covers two concepts, split it.
- **Write in your own words**. Never copy-paste without rephrasing.
- **Link aggressively**. Every note should link to at least 1-2 related notes using `[[wikilinks]]`.
- **Use tags sparingly**. Prefer links over tags for organization. Tags are for status only: `#status/seed`, `#status/growing`, `#status/evergreen`.
- **Title = clear concept name**. E.g., "Gradient Descent", "Bias-Variance Tradeoff", "Attention Mechanism".

### Note Template (Permanent Notes)

```markdown
**Related**: [[note1]], [[note2]]
**Tags**: #status/seed

## Core Idea

(One paragraph explaining the concept in your own words)

## Details

(Deeper explanation, math if applicable, diagrams)

## Code Example

(Inline snippet for illustration)

\```python
# short example
\```

> For runnable implementation, see: [[code/path/to/file.py]]

## Connections

- How does this relate to [[other concept]]?
- Why does this matter for [[broader topic]]?

## Sources

- [Source title](url)
```

## Code Practices

### In Notes (inline)
- Short illustrative snippets only (< 30 lines)
- Focus on demonstrating the concept, not production code
- Always include brief comments explaining the "why"

### In `code/` Directory (runnable files)
- Linked from notes with relative paths
- Must be self-contained and runnable
- Include docstring at top explaining what the file demonstrates
- Follow this style:
  - Type hints on function signatures
  - Snake_case for variables and functions
  - Minimal dependencies — prefer stdlib + numpy/scipy/sklearn when possible
  - Each file should be focused: one concept, one experiment, one implementation

### Python Stack

Primary: Python 3.10+
Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, requests, httpx
Deep Learning: PyTorch (preferred over TensorFlow)
LLMs: transformers (HuggingFace), langchain/langgraph, openai/anthropic SDKs

## Git Workflow

- **Auto-commit**: Commit changes automatically after creating or editing notes and code. Do not ask for confirmation.
- **Branch**: Work directly on `main`.
- **Commit messages**: Simple and descriptive. Examples:
  - `add note on gradient descent`
  - `add linear regression implementation`
  - `update transformer architecture note with attention details`
  - `reorganize foundations folder structure`
- **Never commit**: `.obsidian/workspace.json`, `.obsidian/workspace-v2.json` (these are local UI state).

## Learning Depth

This vault follows a **deep-first approach**. We don't skim — we master.

### What "deep" means
- **Derive, don't memorize**. Understand where formulas come from. If you can't derive it, you don't own it.
- **Implement from scratch**. Build algorithms with raw Python/NumPy before using libraries. This reveals what the abstractions hide.
- **Prove intuition**. Mathematical intuition must be backed by working through the math yourself. Include proofs and derivations in notes when they build understanding.
- **Progressive exercises**. Every concept needs multiple exercises at increasing difficulty:
  - **Basic**: Apply the formula / definition directly
  - **Intermediate**: Combine concepts, solve non-trivial problems
  - **Advanced**: Edge cases, proofs, "why does this break when..."
- **Connect across domains**. Every math concept should link forward to its ML/DL application. Every ML concept should link back to its mathematical foundation.

### Exercise Philosophy
- Exercises are NOT optional — they're how understanding is tested and solidified
- Code exercises should include expected outputs so correctness is verifiable
- When stuck on an exercise, Claude should guide via hints (Socratic), not give the answer immediately
- Each code file should include a `exercises()` section with progressive challenges

## Content Creation

When creating notes or content:
- Prioritize depth over breadth — a well-explained atomic note is better than a shallow overview
- Include mathematical notation using LaTeX (`$inline$` and `$$block$$`) when relevant
- Use diagrams described in text or Mermaid blocks when visual explanation helps
- After explaining a concept, always connect it back to the bigger picture (why does this matter for building AI systems?)
- Include derivations and proofs when they build intuition — don't just state results
- Always suggest additional resources: textbooks, lectures, papers, blog posts, videos

## Monitoring and News

- When asked, search for recent developments in AI/ML and summarize them as literature notes
- Track important releases: new models, frameworks, papers, tools
- Suggest relevant content based on what we're currently studying
