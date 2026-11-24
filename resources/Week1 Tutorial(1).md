# MLIP Setup & Weekly Workflow Guide

Today isn't about machine learning itself — it's about the tools you'll use *every week* from here on: an editor, a package/environment manager, and version control. Most of what breaks in a data science project in practice is tooling, not modelling — so getting this right once now saves hours of friction later.

The guide has two parts: **Part A** explains each tool/concept once; **Part B** puts them to work building your actual `MLIP` repository and Codespace.

---

## Before You Start

- [ ] Free **GitHub** account: <https://github.com/join>
- [ ] (If working on your own machine, not Codespaces) **Anaconda**: <https://www.anaconda.com/download> and **VS Code**: <https://code.visualstudio.com/download>
- [ ] The **python-basics `.zip`** file
- [ ] The **Git cheat sheet PDF** (official GitHub Education one-pager): <https://education.github.com/git-cheat-sheet-education.pdf>
- [ ] This guide itself, saved as a `.md` file, so you can upload it into your repo later

Didn't get to all of this beforehand? No problem — everything below walks through it live.

---

# Part A — Toolkit & Concepts

## A1. Your Toolkit: Anaconda + VS Code
*(Optional — skip this if you're working entirely in a Codespace, since Part B gives you a fully configured environment with nothing to install. Useful to have locally too, as a fallback.)*

**Anaconda** bundles Python, the `conda` package/environment manager, Jupyter, and most common data science libraries in one installer.
1. Download for your OS: <https://www.anaconda.com/download>, run it, accept the defaults.
2. Verify in a terminal (Windows: use **Anaconda Prompt**):
   ```bash
   conda --version
   python --version
   ```

**VS Code** is the editor for writing and running both `.py` scripts and notebooks.
1. Download: <https://code.visualstudio.com/download>, install, open it.
2. In the **Extensions** panel, install **Python** and **Jupyter** (both by Microsoft).

**Checkpoint:** `conda --version` and `python --version` both print a version number, and VS Code shows both extensions installed.

## A2. Git & GitHub Basics
Git tracks changes to your code over time; GitHub hosts a copy of that history online so you can back it up, share it, and collaborate. GitHub **Codespaces** (used throughout Part B) is a full, pre-configured VS Code environment running in the cloud — no local install needed, and free for verified students via the GitHub Student Developer Pack.

| Command | What it does |
|---|---|
| `git init` | Turn the current folder into a Git repository |
| `git status` | See what's changed since your last commit |
| `git add <file>` (or `git add .`) | Stage changes to be committed |
| `git commit -m "message"` | Save a snapshot of the staged changes |
| `git log --oneline` | See your commit history |
| `git clone <url>` | Copy a remote repository to your machine |
| `git pull` | Fetch and merge the latest changes from GitHub |
| `git push` | Send your local commits to GitHub |
| `git branch` | List branches |
| `git checkout -b <name>` | Create and switch to a new branch |

Keep the full **Git cheat sheet** open in a tab: <https://education.github.com/git-cheat-sheet-education.pdf>

## A3. Why Virtual Environments
A virtual environment isolates the packages installed for one project from every other project, so upgrading a package for Project B doesn't silently break Project A. Part B has you create the real one for `MLIP` — this is just the concept and the two alternatives you won't use there:

- **`conda` alternative** (manages non-Python dependencies too, e.g. compilers):
  ```bash
  conda create -n myenv python=3.10
  conda activate myenv
  conda install pandas
  conda env export > environment.yml
  ```
- **Google Colab** — you usually *don't* need one; each session is already an isolated cloud machine. Just install what you need directly, and keep a `requirements.txt` for reproducibility:
  ```python
  %pip install -r requirements.txt
  ```

## A4. Notebooks vs. Scripts

| | Notebooks (`.ipynb`) | Scripts (`.py`) |
|---|---|---|
| Best for | Interactive exploration, inline visualisations | Production code, testing, automation |
| Version control | Harder — large JSON files, messy diffs | Easy — plain text, clean diffs |
| Output | Inline, cell by cell | None by default (you `print`/log explicitly) |

**Recommended workflow:** prototype in a notebook → move reusable code into a `.py` module → import that module back into notebooks when needed → for anything unattended in production, schedule the `.py` script (Airflow, cron, a scheduled GitHub Action), not the notebook. This is the same "prototype messy, productionise clean" pattern.

## A5. Python Basics Self-Check
*(Do this at home, at your own pace — not seminar time.)* The `python-basics.zip` you loaded into your repo contains code, tasks, and solutions covering variables, functions, and a range of other core concepts. Skim it; if it's all familiar, you're in good shape. If something trips you up, that's exactly what it's there to surface — better now than three weeks from now.

---

# Part B — Hands-On: Build Your MLIP Workspace

## Your Quest Log

- [ ] **Mission 1** — Create the `MLIP` repository on GitHub
- [ ] **Mission 2** — Launch your Codespace
- [ ] **Mission 3** — Structure your repo for the whole module
- [ ] **Mission 4** — Load in your materials
- [ ] **Mission 5** — Create your virtual environment
- [ ] **Mission 6** — Your first commit & push
- [ ] **Mission 7** — Lock in the weekly ritual
- [ ] **Boss Level** — Prove it: check your commit shows up on GitHub

By the end, your GitHub profile starts showing a growing trail of green squares — a visible, backed-up record of a full module's work. That's the same habit real ML teams run on.

### Mission 1 — Create the `MLIP` Repository
1. Go to <https://github.com/new>
2. **Repository name:** `MLIP` — exactly that.
3. **Description:** e.g. `My weekly workspace for 7DATA001W Machine Learning in Practice`
4. **Visibility:** **Public** (add a collaborator later if a facilitator needs access).
5. Check **Add a README file**.
6. **Add .gitignore** → choose the **Python** template (this auto-excludes things like `.venv/`, so Mission 5 needs no extra setup).
7. Click **Create repository**.

**Checkpoint:** you're on a page titled `your-username/MLIP` with a green **Code** button.

### Mission 2 — Launch Your Codespace
1. Green **Code** button → **Codespaces** tab → **Create codespace on main**.
2. Wait a minute or two for it to build.

You'll land in a full VS Code interface — file explorer, editor, and a **terminal at the bottom**, where almost everything below happens.

> From today onward, never create a new Codespace for this module — always **resume this one** (Mission 7 shows how). Free accounts get 60 hours/month of Codespace runtime, plenty if you reuse the same one all term.

**Checkpoint:** a terminal is open at the bottom, with a prompt that includes `MLIP`.

### Mission 3 — Structure Your Repo for the Whole Module
```bash
mkdir -p resources python-basics week-01
touch week-01/.gitkeep
```
`.gitkeep` keeps the empty `week-01/` folder visible in Git until it has real files in it.

```
MLIP/
├── README.md
├── .gitignore
├── resources/        ← cheat sheets, guides
├── python-basics/     ← your Python basics folder
└── week-01/           ← this week's work
```
Every future week, add one more folder (`week-02`, `week-03`, ...) the same way.

**Checkpoint:** `ls` shows `resources`, `python-basics`, and `week-01`.

### Mission 4 — Load In Your Materials
Upload via the file explorer: right-click a folder → **Upload...** (or drag-and-drop).

1. **Python basics `.zip`** → upload to the repo root, then:
   ```bash
   unzip python-basics.zip -d python-basics
   rm python-basics.zip
   ```
2. **Git cheat sheet PDF** and **this guide's `.md` file** → upload both directly into `resources/`.

**Checkpoint:** `ls python-basics` shows real files, and `ls resources` shows both reference documents.

### Mission 5 — Create Your Virtual Environment
Applying the concept from **A3** to your actual repo:
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r python-basics/requirements.txt   # only if that file exists — check with: ls python-basics
pip freeze > requirements.txt
```
`.venv` never needs manually gitignoring — the Python template from Mission 1 already excludes it (it's large and trivially rebuilt from `requirements.txt`, so committing it would just bloat the repo).

**Checkpoint:** your prompt shows `(.venv)`, and `pip list` reflects this environment only.

### Mission 6 — Your First Commit & Push (the Boss Fight)
```bash
git status        # see everything you've changed
git add .
git commit -m "Initial setup: repo structure, python basics, resources, and virtual environment"
git push
```
| Command | What just happened |
|---|---|
| `git add .` | Staged every new/changed file |
| `git commit -m "..."` | Took a permanent snapshot with your message attached |
| `git push` | Sent that snapshot from your Codespace to github.com |

**Checkpoint (Boss Level):** refresh `github.com/your-username/MLIP` — you should see `resources/`, `python-basics/`, `week-01/`, and `requirements.txt` (but no `.venv/`), with your message under "Latest commit." If it's on the website, it's genuinely saved.

### Mission 7 — Lock In the Weekly Ritual
Every week, from now on:
1. **Resume your Codespace** — repo → **Code** → **Codespaces** tab → click your existing `MLIP` codespace (or go straight to <https://github.com/codespaces>).
2. **Re-activate your environment:** `source .venv/bin/activate`
3. **Start the week's folder:** `mkdir week-02` (bump the number each week)
4. **Do the week's work** inside it. Installed something new? `pip freeze > requirements.txt`
5. **Commit and push:**
   ```bash
   git add .
   git commit -m "Week 02: <short description of what you did>"
   git push
   ```
6. **Stop your Codespace** — don't just close the tab. Command Palette (`Cmd/Ctrl+Shift+P`) → **Codespaces: Stop Current Codespace**, or find it at <https://github.com/codespaces> → **"..."** → **Stop codespace**. It auto-stops eventually, but stopping it yourself protects your free monthly hours. Nothing is deleted — your `.venv` and files are exactly as you left them next time.

> **Commit message habit:** "its good to include clear and short msg which tells future-you or other developer what you did".


## Quick Troubleshooting

| Problem | Fix |
|---|---|
| `git push` rejects username/password | Codespaces pre-authenticate `git push` automatically. If it still fails, check `git remote -v` starts with `https://github.com/your-username/MLIP` |
| `unzip: command not found` | Try `python3 -m zipfile -e python-basics.zip python-basics` |
| Can't find your Codespace | <https://github.com/codespaces> — it auto-stops but isn't deleted; resume from there |
| `git commit` says "Please tell me who you are" | `git config --global user.email "you@example.com"` and `git config --global user.name "Your Name"`, then retry |
| Prompt doesn't show `(.venv)` | Run `source .venv/bin/activate` from the repo root — check with `ls -a` |
| `requirements.txt` install fails with "No such file" | It may not exist in your zip — just `pip install` what you actually need |
| Not sure if a Codespace is still running (burning hours) | <https://github.com/codespaces> shows **Active**/**Stopped** for each one |

## Recap
```
open Codespace → activate .venv → work in this week's folder → git add . → git commit -m "..." → git push → stop the Codespace
```
