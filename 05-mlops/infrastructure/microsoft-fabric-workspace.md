---
tags:
  - status/seed
  - data-engineering
  - microsoft-fabric
related:
  - "[[microsoft-fabric]]"
  - "[[microsoft-fabric-access-and-trial]]"
  - "[[udemy-microsoft-fabric]]"
  - "[[data-lake-and-onelake]]"
  - "[[medallion-architecture]]"
domain: data-engineering
sources:
  - "https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces"
  - "https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces"
  - "https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces"
  - "https://www.udemy.com/course/microsoft-fabric-la-formacion-completa/"
---

> **TL;DR** — A workspace is Fabric's **container for items** (notebooks, lakehouses, warehouses, pipelines, reports). It's also the **unit of access control** (roles) and the **unit of billing** (the license mode ties it to a capacity).

---

## Intuition

Think of a workspace as a **shared project folder with a door and a meter**. The folder holds every item a team builds. The door is the roles: who can enter, and whether they can only look or also edit. The meter is the license mode: which capacity pays for the compute that runs the items. One team or one project gets one workspace, and in OneLake each workspace becomes a top-level folder.

## Mechanics

**Creating one** — *Workspaces → + New workspace*, then:

| Field                     | What it sets                                                                      | Why it matters                                               |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Name                      | Unique name in the tenant                                                         | Shows up in OneLake paths and URLs                           |
| Description               | What data and purpose the workspace holds                                         | Helps people find it and trust it                            |
| Domain                    | Label that groups workspaces by business area (Sales, Finance…)                   | Supports data-mesh governance; domains are created by admins |
| Image                     | Workspace icon                                                                    | Makes it easier to spot in the list                          |
| *Advanced* → Contact list | People notified about workspace issues (default: the admins)                      | Tells others who owns it                                     |
| *Advanced* → License mode | Pro, Premium per-user, Premium capacity, Embedded, **Fabric capacity**, **Trial** | Decides which item types you can create                      |
| **Apply**                 | Creates the workspace; you become its **Admin**                                   |                                                              |

**License-mode trap.** On **Pro** or **Premium per-user**, you only get Power BI items. To create a lakehouse, notebook, warehouse, or pipeline, the workspace must be on a **capacity**: Trial, a Fabric F-SKU, or Premium P. You set this when you create the workspace, and you can change it later in *Workspace settings → License info*.

**Roles.** Roles are assigned to users or Entra ID groups for the **whole workspace**: a role sets *how much* someone can do on every item in it, not *which* items. For per-item control, use item-level permissions, OneLake security, or separate workspaces. Each role includes the permissions of the roles below it:

| Role | Can do |
|---|---|
| Viewer | View and read content (runs SQL queries through endpoints) |
| Contributor | Create, edit, and delete items |
| Member | Contributor rights + share items and add Contributors/Viewers |
| Admin | Everything, including managing all roles, settings, and deleting the workspace |

## In ML

**Environment separation** — The usual pattern is one workspace per stage (`proj-dev`, `proj-test`, `proj-prod`), connected by Git integration and deployment pipelines. This is the Fabric version of dev/prod isolation in [[medallion-architecture]] pipelines and ML CI/CD.

**Least privilege for data scientists** — Scientists get Contributor on the dev workspace so they can build notebooks and experiments, but only Viewer on prod. Automated jobs run as service principals, not personal accounts.

**Capacity = shared compute budget** — Every workspace on the same capacity draws Capacity Units from one pool. A heavy Spark training job in one workspace can throttle BI reports in another. Isolate critical workloads by putting them on separate capacities.

## Exercises

**Basic** — You created a workspace on the **Pro** license and the *Lakehouse* option is missing. Why, and what's the fix?

**Intermediate** — Design the roles for a team with 2 data engineers, 3 analysts who only build reports from gold tables, and 1 manager who only reads dashboards. Would you use one workspace or more?

**Advanced** — An analyst with **Viewer** role can still read raw bronze data through the SQL analytics endpoint. Explain why a workspace role alone can't prevent this, and propose two ways to restrict it.
