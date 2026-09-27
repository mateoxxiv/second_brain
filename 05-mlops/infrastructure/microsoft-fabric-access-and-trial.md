---
tags:
  - status/seed
  - data-engineering
  - microsoft-fabric
related:
  - "[[microsoft-fabric]]"
  - "[[udemy-microsoft-fabric]]"
domain: data-engineering
sources:
  - "https://learn.microsoft.com/en-us/fabric/fundamentals/fabric-trial"
  - "https://learn.microsoft.com/en-us/fabric/fundamentals/free-trial-account-personal-email"
  - "https://www.udemy.com/course/microsoft-fabric-la-formacion-completa/"
---

> **TL;DR** — To use Fabric you need two things: an **organizational identity** (a work/school account in a Microsoft Entra ID tenant) and a **capacity** to run on (a free 60-day trial or a paid F-SKU). A personal Gmail/Outlook account can't sign in directly, so you create an Azure tenant and make an organizational user inside it.

---

## Intuition

Think of Fabric as a gym inside an office building. The **badge** (identity) proves you belong to an organization, and the **membership** (capacity) pays for the machines. A corporate email already comes with a badge; you only need a membership. A personal email has no badge, so you first "create your own company" (an Azure tenant) and issue yourself one.

## Mechanics

**Access model.** Three pieces must line up:

| Piece | Options | Notes |
|---|---|---|
| Identity | Organizational account in an Entra ID tenant | Personal Microsoft accounts (MSA) are not supported |
| Per-user license | Fabric (Free), Power BI Pro, Premium Per User | The free license is enough to join a trial |
| Capacity | Trial (F4 or F64, 60 days), paid F-SKU (F2 and up), Power BI Premium P | Non-Power BI items (notebooks, lakehouses, pipelines) only run on a capacity |

**Path A — Corporate email**
1. Go to `https://app.fabric.microsoft.com` and sign in with the corporate account.
2. Open the profile icon (Account manager), select **Start trial**, and fill in the form (choose the region carefully; moving it later means deleting items).
3. If there is no trial button, the tenant admin must enable **Users can create Fabric items** and **Users can try Microsoft Fabric paid features** in *Admin portal → Tenant settings*.

**Path B — Personal email (via Azure)**
1. Create a free Azure account with your personal email (phone and card are used for verification only).
2. In the Azure portal: **Microsoft Entra ID → Users → New user → Create new user**. This creates an organizational user like `name@yourtenant.onmicrosoft.com`.
3. Save the user principal name (UPN) and password somewhere safe.
4. *(Optional, recommended)* **Assign roles → Fabric Administrator**. The trial doesn't require it, but it gives you the Admin portal so you can change tenant settings yourself.
5. Sign in to Fabric with the **UPN**, not your personal email, then **Profile → Free trial → Activate**.

**Trial facts.** 60 days, up to 1 TB in OneLake, no Copilot/AI functions, no autoscale. After it ends, Fabric items become inactive and are deleted after 7 days unless the workspace moves to a paid capacity. Tenants have a limit on the number of trials, and a second trial isn't guaranteed.

**Paid tier.** Buy an F-SKU capacity in Azure (pay-as-you-go, billed per hour). You can **pause** it when idle, so a small F2 is a cheap way to practice once the trial is over.

## In ML

**Budget for experiments** — Every Spark session, notebook run, and model training job consumes the same Capacity Units. On an F4 trial, a heavy training job can slow down everyone else on the capacity. Knowing the capacity size explains "why is my notebook queued?"

**Identity is the security boundary** — Workspace roles, OneLake permissions, and service principals for automated pipelines (CI/CD, scheduled scoring) all hang off Entra ID. Production ML systems use service principals, not personal logins.

**Plan for the trial ending** — A model trained on a trial capacity disappears 7 days after the trial ends. Export the artifacts (MLflow model, notebooks via Git integration) or move to a paid capacity before then.

## Exercises

**Basic** — Why does Fabric reject `me@gmail.com` but accept `me@mytenant.onmicrosoft.com`, even though you created both?

**Intermediate** — You're on a corporate account and see no **Start trial** button. List three possible causes and who can fix each one.

**Advanced** — Your trial ends in 5 days and it holds a lakehouse, three notebooks, and a trained model. Design a plan to keep everything at minimal cost. Think about F2 + pause, Git integration, and what happens during the 7-day grace period.
