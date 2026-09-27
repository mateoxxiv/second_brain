---
tags:
  - status/seed
  - literature
type: course
domain: data-engineering
sources:
  - "https://www.udemy.com/course/microsoft-fabric-la-formacion-completa/"
author: "Mikail Altundas (Data Engineer / Scientist)"
date_read: "2026-09-25 (in progress)"
---

## Summary

*Microsoft Fabric — La formación completa* (Udemy, Mikail Altundas) is a beginner-to-job-ready, project-driven course on **Microsoft Fabric**, Microsoft's unified SaaS analytics platform. It walks through Fabric's core workloads — Data Factory (ingestion), Data Engineering (Lakehouse + Spark), Data Warehouse, and Power BI — and the storage options (Lakehouse, Warehouse, KQL databases), transformation tools (Spark Notebooks in PySpark/Spark SQL, Dataflows Gen2), and best practices like the **Medallion Architecture**. It targets the **DP-600** and **DP-700** certifications and assumes no prerequisites.

> **Role in the vault — read this before deriving notes.** This is a **technical/practical complement, NOT a source of conceptual mastery.** It teaches the *how* (which Fabric item to create, in what order, which button to click) and is tied to one vendor's platform. So it does **not** "cover" the underlying concepts — data-lake/warehouse theory, dimensional modeling, Spark internals, the medallion pattern's rationale. Those permanent notes must be **theory-derived** (Kimball, Delta Lake / Spark docs, *Designing Data-Intensive Applications*). This course contributes the **runnable implementation layer**: the concrete Fabric workflow that makes the theory tangible and preps the DP-600/DP-700 exams. When a class maps to a note below, treat it as the **implementation companion**, never the origin.

---

## Chapter / Class Map

> **Provisional** — built from the course description (Udemy blocks scraping), organized by Fabric's components. To be corrected section-by-section as watched. Vault notes are empty because this is a new domain for the vault — the Gaps section lists the notes to create.

| Module | Topic | Vault notes |
|---|---|---|
| 1 | Intro to Fabric + free access (personal/pro account) | [[microsoft-fabric]] |
| 2 | Core concepts: workspaces, OneLake, capacities, item types | |
| 3 | Data Factory: pipelines & Dataflows Gen2 (ingestion/ETL) | |
| 4 | Data Engineering: Lakehouse + Spark Notebooks (PySpark, Spark SQL) | |
| 5 | Data Warehouse: T-SQL warehouse & SQL analytics endpoint | |
| 6 | Storage methods compared: Lakehouse vs Warehouse vs KQL DB | |
| 7 | Medallion Architecture (bronze/silver/gold) & best practices | |
| 8 | Power BI: semantic models, DirectLake, reports | |
| 9 | Certification prep: DP-600 & DP-700 | |

---

## All Topics at a Glance

**Module 1 — Intro**
- [[microsoft-fabric]] — one SaaS platform where every workload shares one copy of the data (OneLake, Delta/Parquet)

---

## Key Takeaways

1. **Fabric is a unified SaaS platform, not a set of separate tools** — Data Factory, Data Engineering, Warehouse, and Power BI all sit on one storage layer (OneLake), so data isn't copied between services.
2. **OneLake is the "OneDrive for data"** — a single, tenant-wide lake built on Delta/Parquet; every workload reads and writes the same open-format files.
3. **Lakehouse vs. Warehouse is the central storage decision** — Lakehouse (files + Spark, schema-on-read) vs. Warehouse (T-SQL, schema-on-write); the course's storage module is the practical version of this classic trade-off.
4. **Medallion Architecture (bronze → silver → gold) is the recommended pipeline pattern** — raw → cleaned → business-ready layers, a vendor-neutral best practice Fabric implements.
5. **Two transformation paths** — code-first Spark Notebooks (PySpark / Spark SQL) vs. low-code Dataflows Gen2 (Power Query); choosing between them is a recurring practical decision.

## Quotes / Important Passages

> "No se requiere ningún requisito previo para seguir este curso: abordaremos juntos todos los conceptos, de la A a la Z."
> — Course description (prerequisites)

## My Thoughts

This sits in a different lane from the current probability/stats track, but it's squarely on the **AI architect / data-engineering** path — the "supporting foundations … to production systems" goal in the vault charter. The most transferable, vendor-neutral ideas are the **Medallion Architecture** and the **Lakehouse-vs-Warehouse** trade-off; those deserve theory-first permanent notes that Fabric merely illustrates. The DP-600/DP-700 prep is a concrete external milestone worth tracking in the study roadmap. Next: as I watch, capture the vendor-neutral concepts as permanent notes and keep the Fabric-specific clicks in this literature note.

---

## Permanent Notes Created

- [[microsoft-fabric]] — what Fabric is: unified SaaS platform on OneLake, its three layers, and collaboration by role (Module 1–2 companion)

## Gaps — Notes Still to Create

- [[medallion-architecture]] — bronze/silver/gold data-layering pattern; **theory-first** (vendor-neutral), Fabric as one implementation
- [[lakehouse-vs-data-warehouse]] — the storage-model trade-off (schema-on-read + files vs. schema-on-write + T-SQL); links to [[databases]] foundations
- [[data-lake-and-onelake]] — the data-lake concept and OneLake as Fabric's unified, open-format (Delta/Parquet) store
- [[etl-vs-elt]] — ingestion/transformation ordering, the frame behind Data Factory / Dataflows Gen2
- [[spark-and-pyspark-basics]] — distributed dataframes and lazy evaluation; the engine under Fabric's Notebooks
