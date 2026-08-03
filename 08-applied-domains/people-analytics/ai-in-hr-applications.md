---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[exit-interview-nlp-analysis]]"
  - "[[hr-data-ethics]]"
  - "[[people-analytics]]"
  - "[[people-analytics-strategy-pillars]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — AI is reshaping HR on three concrete fronts — candidate matching (ATS), large-scale text analysis, and organizational network analysis (ONA) — but every one of them must clear an internal ethics/policy review before deployment, not after.

---

## Intuition

"AI in HR" isn't one generic capability — it shows up doing three specific jobs. Two are extensions of familiar ideas: matching candidates to a role, and reading qualitative text at scale. The genuinely new idea is ONA: making visible a layer of organizational reality the org chart hides entirely — who people actually talk to, not who they formally report to.

## Mechanics

**Three fronts where AI is already active in HR:**

| Front | What it does | Connects to |
|---|---|---|
| ATS (Applicant Tracking Systems) | Matches and ranks candidates against a role description, speeding up selection | Text-similarity / ranking models |
| Large-scale text analysis | Finds trends across qualitative sources (surveys, open comments) too costly to read manually | [[exit-interview-nlp-analysis]] |
| Organizational Network Analysis (ONA) | Maps who actually interacts with whom, surfacing influence that doesn't map to job title | Graph theory / centrality measures |

**ONA, in more depth** — built from interaction data (email/calendar/chat metadata, or self-reported relationships in a survey), represented as a graph: people are nodes, interactions are edges. Centrality measures then answer "who matters structurally":

- **Degree centrality** — who has the most direct connections.
- **Betweenness centrality** — who sits on the shortest path between otherwise-disconnected people, i.e. who bridges silos.

A person with modest formal seniority can score highest on either measure — that's the whole point: ONA reveals influence the hierarchy doesn't show.

**The policy gate comes first, not last** — before deploying any AI-based tool (ATS, text analysis, or ONA), review the organization's internal policy on AI use. The technical potential is real, but skipping the ethical/regulatory review is what turns adoption into a reputational risk — see [[hr-data-ethics]].

```python
import networkx as nx

# edges = observed interactions (e.g. from meeting/email metadata)
edges = [("alice", "bob"), ("alice", "carla"), ("bob", "carla"),
         ("carla", "dan"), ("dan", "erin"), ("carla", "erin")]

G = nx.Graph()
G.add_edges_from(edges)

degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)

# "carla" may not hold the most senior title, but she can still be
# the network's most structurally important connector.
print(sorted(degree.items(), key=lambda x: -x[1]))
print(sorted(betweenness.items(), key=lambda x: -x[1]))
```

## In ML

**ONA is applied graph theory** — degree centrality, betweenness centrality, and community detection are standard graph-ML tools; HR just supplies the edge list (interactions) instead of a social-network export.

**ATS is a text-similarity / ranking problem** — under the hood, an ATS embeds the job description and each resume, scores similarity, and ranks candidates — the same embedding machinery referenced in [[exit-interview-nlp-analysis]] and [[people-analytics]]'s qualitative-analysis-with-LLMs section, applied to matching instead of clustering.

**Policy review is a deployment gate, not paperwork** — an ATS or ONA model that's accurate but violates an internal or legal use policy is not a deployable model, regardless of its performance. This is the same gate [[hr-data-ethics]] sets for any HR data use.

## Exercises

**Basic** — For each question, name which of the three fronts (ATS, text analysis, ONA) answers it: (a) who should we shortlist for this open role, (b) what themes recur in this quarter's engagement survey comments, (c) which mid-level employee is quietly critical to cross-team coordination.

**Intermediate** — Using the code above, explain why "carla" could show high betweenness centrality without having the highest degree, and what that specifically signals about her role in the network (bridging silos vs. simply being well-connected).

**Advanced** — Design an ONA study for a 200-person org using calendar-meeting metadata as the interaction signal. Name two privacy/ethical risks specific to this data source, connecting each to [[hr-data-ethics]], and specify a mitigation for each before running the study.
