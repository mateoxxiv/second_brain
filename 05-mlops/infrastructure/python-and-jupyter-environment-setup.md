---
tags:
  - status/seed
  - mlops
related:
  - "[[types-of-machine-learning]]"
  - "[[ml-pipeline]]"
  - "[[platzi-fundamentos-machine-learning]]"
domain: mlops
sources:
  - "Platzi — Curso de Fundamentos de Machine Learning, Clase 4 (setup del entorno)."
  - "https://docs.python.org/3/library/venv.html"
  - "https://docs.astral.sh/uv/"
---

> **TL;DR** — Never install project packages into the system Python; create an **isolated virtual environment** per project, install Jupyter inside it, and you get a reproducible, disposable workspace where code, notes, and plots live together in a notebook.

---

## Intuition

Think of the system Python as a shared kitchen: if every project dumps its own ingredients into it, they collide (project A needs pandas 1.5, project B needs 2.2) and eventually nothing runs. A **virtual environment** gives each project its own private pantry — an isolated copy of Python + its own packages — that you can throw away and rebuild from a recipe. That "recipe" (a `requirements.txt`) is what makes the work *reproducible*: anyone can recreate your exact setup.

**Jupyter Notebook** is the workbench on top of that: a document that interleaves runnable code cells, prose, math, and plots, so exploration and explanation live in one file (`.ipynb`) instead of scattered scripts.

## Mechanics

**"Raw" Python + venv (stdlib, no extra installer) — the path the question asks for:**

```bash
# 1. install Python 3.10+ from python.org (check "Add to PATH" on Windows)
python --version                      # verify it's on PATH

# 2. create an isolated environment in the project folder
python -m venv .venv

# 3. activate it
.venv\Scripts\Activate.ps1            # Windows PowerShell
# source .venv/bin/activate           # macOS / Linux

# 4. install Jupyter INSIDE the active env
pip install jupyter pandas numpy scikit-learn

# 5. launch and create a notebook (e.g. "cebollitas-dia-uno.ipynb")
jupyter notebook                      # opens in the browser

# 6. freeze the recipe so others can rebuild it
pip freeze > requirements.txt         # rebuild later: pip install -r requirements.txt
```

First smoke test — one cell to confirm the kernel runs:

```python
print("Bienvenidos al Cebollitas FC")
```

**Which environment manager?**

| Tool | What it is | Use when |
|---|---|---|
| **venv** + pip | Stdlib, ships with Python ("raw") | Default; simple, no extra install |
| **uv** | Rust-based, ~10–100× faster resolver/installer | Modern projects wanting speed + lockfiles |
| **conda / Anaconda** | Bundles Python + sci packages + non-Python binaries | Heavy data-science stacks, no compiler on Windows |

> The golden rule: **one environment per project**, and it must be **activated** before `pip install` — otherwise packages leak into the global Python (the exact mess venv prevents). Add `.venv/` to `.gitignore`; commit `requirements.txt`, never the environment itself.

## In ML

**Reproducibility is the first MLOps habit** — a model result is worthless if no one can rerun it. The `requirements.txt` (or `uv.lock`) pins the exact library versions, so a training run today reproduces months later. This is the seed of the same reproducibility that [[docker]] later hardens by pinning the OS too, and that a full [[ml-pipeline]] depends on.

**Jupyter is where EDA and prototyping live** — the entire early ML workflow ([[types-of-machine-learning|choosing a paradigm]], cleaning, scaling, first models) happens in notebook cells because the tight code→plot→explain loop is ideal for exploration. Production code later graduates *out* of notebooks into tested `.py` modules — but discovery starts here.

## Exercises

**Basic** — Create a fresh venv, activate it, install `pandas`, and confirm inside Python that `import pandas` works. What breaks if you skip the activation step?

**Intermediate** — You have two projects needing different NumPy versions. Show the sequence of commands that lets both run on the same machine without conflict, and explain why `pip freeze` matters for a teammate cloning your repo.

**Advanced** — A notebook runs on your machine but fails on a colleague's with `ModuleNotFoundError`, even though both cloned the same repo. List three distinct causes (hint: kernel selection, missing `requirements.txt`, Python version) and how to diagnose each.
