---
tags:
  - status/seed
  - data-engineering
related:
  - "[[microsoft-fabric]]"
  - "[[udemy-microsoft-fabric]]"
  - "[[etl-vs-elt]]"
  - "[[lakehouse-vs-data-warehouse]]"
  - "[[data-lake-and-onelake]]"
  - "[[spark-and-pyspark-basics]]"
domain: data-engineering
sources:
  - "https://www.databricks.com/glossary/medallion-architecture"
  - "https://learn.microsoft.com/en-us/fabric/onelake/onelake-medallion-lakehouse-architecture"
  - "https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf"
---

> **TL;DR** — Medallion architecture organizes a lakehouse into three layers of rising quality: **bronze** (raw, untouched), **silver** (cleaned, trusted), and **gold** (business-ready). Because the raw layer is never modified, any downstream mistake can be fixed by rebuilding from bronze.

---

## Intuition

Think of a water treatment plant. **Bronze** is the reservoir: water arrives exactly as the river delivered it. **Silver** is the filtration plant, which removes dirt, bacteria, and duplicates. **Gold** is bottled water, packaged for one specific customer. The key rule: **never drain the reservoir.** If a filter turns out to be broken, you refill the bottles from the reservoir instead of going back to the river.

The question it answers: *how do you clean data for many consumers without losing the original, and without every team cleaning it differently?*

## Mechanics

**Definition.** A multi-hop design pattern where data moves through ordered layers. Each hop is a deterministic transformation, `silver = f(bronze)` and `gold = g(silver)`, so every layer can be **recomputed** from the one before it. This makes bronze the single source of truth. It follows the **ELT** order ([[etl-vs-elt]]): load raw data first, then transform it inside the lake.

| | Bronze (raw) | Silver (cleansed) | Gold (curated) |
|---|---|---|---|
| Purpose | Faithful, replayable history | One trusted view of business entities | Answer specific business questions fast |
| Shape | Source format (JSON, CSV) or Delta | Normalized Delta tables, row-level | Denormalized, read-optimized, per use case |
| Main users | Data engineers (audit, reprocessing) | Engineers, data scientists | Analysts, dashboards |
| Designed for | **Recovery** | **Reuse** | **Consumption** |

**Scope of each layer** — what belongs in it, and what must wait for the next one:

- **Bronze — ingest only.**
  - ✅ Land data exactly as the source sent it. Append every load. Add ingestion metadata (`load_date`, `source_file`). Use shortcuts instead of copies when the source already lives in a lake.
  - ❌ No cleaning, no deduplication, no type fixes, no deletes. Any change breaks the ability to replay history.
- **Silver — clean and conform, stay row-level.**
  - ✅ Remove duplicates. Cast data types and parse dates. Trim and standardize text. Unify units and currencies. *Handle* nulls (flag them, standardize them, drop records that are truly broken). Filter out test or invalid records. Match entities across sources (one customer ID). Enforce a schema and data quality rules. Use `MERGE` for incremental loads.
  - ❌ No aggregation and no report-specific business logic. Don't **fill in** nulls with means or medians: that choice is model-specific and causes data leakage, so it belongs in each ML pipeline, fitted on training data only.
- **Gold — shape for one consumer.**
  - ✅ Aggregates and KPIs (sales per hour or month). Star schemas (`fact_sales`, `dim_customer`, `dim_product`). Business rule definitions (what counts as an "active customer"). ML feature tables and prediction tables.
  - ❌ No raw or uncleaned data, and no reading directly from bronze. Every gold table is built from silver.

**Why it works.** The table format (e.g. Delta Lake) supplies the guarantees: ACID writes, so a failed load leaves no half-written layer; **time travel**, to roll back a bad silver load; and `MERGE`, for incremental upserts.

```python
raw = spark.read.json("Files/bronze/sales/2026-09-27/")         # bronze: untouched
silver = (raw.dropDuplicates(["order_id"])                       # one row per order
             .filter("is_test = false")                          # drop test records
             .withColumn("order_date", to_date("order_date")))   # standard types
silver.write.mode("append").saveAsTable("silver_sales")
gold = silver.groupBy("order_date").sum("amount_usd")            # business view
gold.write.mode("overwrite").saveAsTable("gold_daily_sales")
```

**Fabric implementation.** Each layer is a Lakehouse in OneLake, ideally in its own workspace so access can be controlled per layer. Gold can also be a Warehouse for SQL-first teams. Data Factory pipelines or **shortcuts** feed bronze, notebooks or Dataflows Gen2 move data between layers, and Power BI reads gold through Direct Lake ([[microsoft-fabric]]).

## In ML

**Training data lives in silver, not gold** — Gold is aggregated, so it has already thrown away the row-level detail a model needs. Silver is clean *and* granular, which makes it the natural source for feature tables.

**Reproducibility** — If you record the silver table version (Delta time travel) next to each model run, you can rebuild exactly the dataset a model was trained on. That's essential for debugging drift or for audits.

**Predictions flow back as gold** — Batch scoring outputs (churn scores, forecasts) are written as gold tables, so dashboards consume model results the same way they consume any other business metric.

## Exercises

**Basic** — Classify each operation as bronze, silver, or gold: (a) converting all prices to USD, (b) storing a CRM export as-is, (c) computing monthly revenue per region, (d) removing duplicate orders.

**Intermediate** — A bug in the silver cleaning code dropped valid orders for 3 weeks. Describe the recovery using bronze. Why would the loss be permanent if the cleaning had happened *during* ingestion (ETL)?

**Advanced** — Bronze keeps everything forever, including personal data. A customer invokes the GDPR "right to be forgotten". How does that conflict with an append-only, replayable bronze layer, and with Delta time travel? Propose a design that satisfies both.
