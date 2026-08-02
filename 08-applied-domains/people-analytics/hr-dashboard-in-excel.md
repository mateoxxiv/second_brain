---
tags:
  - status/seed
  - people-analytics
  - ml
related:
  - "[[kpi-design]]"
  - "[[data-cleaning-for-people-analytics]]"
  - "[[people-analytics]]"
domain: ml
sources:
  - "https://platzi.com/cursos/people-analytics-excel/"
---

> **TL;DR** — A dashboard is a clean table turned into pivot tables and charts, then wired to shared filters — so a chosen KPI set becomes something a stakeholder can read and explore in seconds, not something they have to ask you about.

---

## Intuition

A KPI is just a number until someone can see it, compare it, and slice it by department or gender without asking an analyst to rerun a query. The dashboard is that translation layer. Its entire value is speed of understanding — if a stakeholder has to squint or ask a follow-up question, the dashboard hasn't done its job yet.

## Mechanics

**Build sequence:**

1. **Prepare the data** — every field needs a header with a real definition; no blank header cells. A pivot table or chart silently breaks or misgroups when the source table has gaps.
2. **Convert to a table** — select the range, `Ctrl + T`. This locks in structure and lets pivot tables and charts auto-update as rows are added.
3. **Build pivot tables** — select the table, insert a pivot table, and break KPIs down by the dimensions that matter (department, gender, tenure band, etc.).

**Choosing a chart type:**

| Chart | Best for | Example |
|---|---|---|
| Bar chart | Comparing quantities across categories | Headcount by department |
| Stacked column chart | Comparing sub-categories at a glance | Performance rating breakdown by team |
| Pie chart | Percentage distribution | Headcount by gender |

Keep every chart minimal — drop elements that don't add information (e.g. a totals label the audience doesn't need). A chart's job is to be read in three seconds, not admired.

**Making it interactive:**

1. **Insert slicers** (Excel's "segmentación de datos") for the dimensions people will want to filter by — area, performance level, etc.
2. **Link every pivot table and chart to the same slicers**, so one click on a filter updates the entire dashboard at once, not just one chart.

## In Practice

**A dashboard that doesn't trigger action is decoration** — see [[people-analytics-employee-lifecycle]]: the point isn't the chart, it's the decision the chart makes obvious. If a stakeholder can look at it and immediately know what to do next, it worked.

**Garbage in, garbage displayed** — a beautifully linked dashboard built on unresolved duplicates or bad formats just makes the wrong numbers easier to trust. [[data-cleaning-for-people-analytics]] has to happen before step 1 here, not after.

**"Quality means doing the right thing when no one is watching" (Henry Ford)** — applied to dashboards: keep the underlying table, pivot logic, and chart choices clean and defensible even for the KPIs nobody's scrutinizing today. Someone eventually will.

## Exercises

**Basic** — You're given a spreadsheet with a blank header on column F. What breaks if you try to build a pivot table before fixing this, and why?

**Intermediate** — You need to show headcount by department (5 departments) and performance rating distribution (4 levels) on the same dashboard. Which chart type fits each, and why would swapping them (bar for the distribution, stacked column for headcount) make the dashboard harder to read?

**Advanced** — Design a one-page HR dashboard for the KPI set you built in [[kpi-design]]'s Advanced exercise (5 KPIs targeting early attrition). Specify: which pivot tables you'd build, which chart type for each KPI, and which single slicer dimension would let a stakeholder investigate all 5 at once.
