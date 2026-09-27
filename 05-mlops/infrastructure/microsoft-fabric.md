---
tags:
  - status/seed
  - data-engineering
  - microsoft-fabric
related:
  - "[[udemy-microsoft-fabric]]"
  - "[[data-lake-and-onelake]]"
  - "[[lakehouse-vs-data-warehouse]]"
  - "[[medallion-architecture]]"
  - "[[etl-vs-elt]]"
  - "[[spark-and-pyspark-basics]]"
domain: data-engineering
sources:
  - "https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview"
  - "https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview"
  - "https://www.udemy.com/course/microsoft-fabric-la-formacion-completa/"
---

> **TL;DR** — Microsoft Fabric is a single SaaS analytics platform where ingestion, engineering, warehousing, real-time analytics, and BI all read and write **one shared copy of the data** (OneLake, in open Delta/Parquet), so you stop stitching separate tools together.

---

## Intuition

A typical data stack used to be a relay race between separate products: one tool to ingest (Data Factory), one to store (a data lake), one to transform (Spark/Databricks), one to serve SQL (a warehouse), one to visualize (Power BI). Each handoff means copying data, managing credentials, paying for separate compute, and debugging integrations.

Fabric's promise: **one building instead of five buildings connected by bridges.** Each team gets its own room (workload), but everyone shares the same floor (storage), the same security, and the same electricity bill (capacity).

Key nuance: Fabric did not invent new engines. It **repackages existing Microsoft products** (Synapse, Data Factory, Power BI) as workloads on one storage layer. The novelty is the unification, not the tools.

## Mechanics

Fabric has three layers:

1. **Storage — OneLake.** One logical lake per tenant ("the OneDrive for data"). Tables are stored as **Delta Lake** (Parquet files plus a transaction log), an open format any engine can read. **Shortcuts** and **mirroring** expose external data (ADLS, S3, databases) without physically copying it.
2. **Workloads (compute experiences).** One per role, all reading and writing OneLake (see the table below), plus Real-Time Intelligence (KQL) for streaming data.
3. **Governance and billing.** One tenant, one workspace model, one security and lineage layer (Purview), and one pooled **capacity** (F-SKUs measured in Capacity Units) shared by every workload.

**Collaboration by role.** Teams work together inside shared **workspaces**, which have Git integration and deployment pipelines. Each role gets its own workload, but they all work on the same tables, so one team's output is the next team's input with no handoff:

| Role | Main workload | What they do |
|---|---|---|
| Data engineer | Data Factory, Data Engineering (Lakehouse + Spark) | Design ingestion and transformation pipelines |
| Data scientist | Data Science (notebooks, MLflow) | Build and track ML/AI models |
| Data analyst | Data Warehouse (T-SQL), Power BI | Query, analyze, and build reports |
| ML/AI engineer | Data Science (model registry, batch scoring), deployment pipelines | Deploy, monitor, and maintain models in production |

| Property | What it means | Why it matters |
|---|---|---|
| SaaS | No clusters or servers to provision | Setup in minutes; less infrastructure work |
| One copy of data | Every engine reads the same Delta tables | No export/import steps, no drift between copies |
| Open format | Delta/Parquet, not a proprietary format | Less lock-in; external tools can read it |
| Shared capacity | One compute budget for all workloads | Simpler billing, but heavy jobs can starve others |
| Direct Lake | Power BI reads Delta files directly | BI without import refreshes or slow DirectQuery |

```python
# Inside a Fabric notebook attached to a Lakehouse
df = spark.read.table("sales")               # Delta table living in OneLake
by_region = df.groupBy("region").sum("amount")
by_region.write.mode("overwrite").saveAsTable("sales_by_region")
# No export step: the SQL analytics endpoint and Power BI (Direct Lake)
# can query "sales_by_region" immediately, because it is the same files.
```

## In ML

**Feature pipelines** — The [[medallion-architecture]] (bronze → silver → gold) in a Lakehouse produces clean, versioned Delta tables. Gold tables become the training set, and Delta's time travel lets you reproduce the exact data a model was trained on.

**Training and tracking** — The Data Science workload runs Spark or pandas notebooks with built-in MLflow experiment tracking and a model registry, so training happens next to the data instead of after an export.

**Serving insight to users** — Batch predictions written back to OneLake are immediately visible in Power BI. That closes the loop from raw data to model output to business report inside one platform.

## Exercises

**Basic** — Name the three layers of Fabric and give one component of each. Why does storing everything as Delta/Parquet matter more than the number of workloads?

**Intermediate** — A company uses Azure Data Factory → ADLS → Databricks → Synapse → Power BI. List every point where data is copied or credentials are managed. Which of those does Fabric remove, and which remain (hint: external sources still need ingestion, or a shortcut/mirror)?

**Advanced** — "Unify everything in one platform" has costs. Argue the case *against* Fabric for a given team: think about shared-capacity contention (noisy neighbours), vendor lock-in beyond the storage format, and maturity compared to specialized tools. When is a best-of-breed stack the better architecture?
