# Week 2 Practical: From Problem to Pipeline

**The mission:** Build a simple fraud baseline, watch it drift, catch that drift with one small function, and then automate a basic pipeline in Mage AI. Small, guided steps — no heavy stats, no external accounts needed.


## Setup: 

1. **Resume your existing Codespace** — `MLIP` repo → **Code → Codespaces** → click your existing codespace. **Do not create a new one.**
2. ```bash
   source .venv/bin/activate
   mkdir -p week-02 && cd week-02
   touch week2_practical.ipynb
   pip install scikit-learn pyarrow mage-ai
   pip freeze > ../requirements.txt
   ```
3. Open `week2_practical.ipynb` and work every block below inside it.

---

##  Simple Baseline 

```python
import numpy as np, pandas as pd
rng = np.random.default_rng(42)
n = 2000
df = pd.DataFrame({
    "amount": rng.exponential(scale=50, size=n).round(2),
    "is_new_recipient": rng.integers(0, 2, size=n),
})
df["is_fraud"] = ((df["amount"] > 150) & (df["is_new_recipient"] == 1)).astype(int)
print(df["is_fraud"].value_counts(normalize=True))
```
You're **FinPay**, flagging fraudulent P2P payments — the brief from the lecture.

### Predict, then run
Guess out loud first: **will a one-line rule get higher precision or higher recall?**
```python
df["rule_pred"] = ((df["amount"] > 150) & (df["is_new_recipient"] == 1)).astype(int)

from sklearn.metrics import precision_score, recall_score
print("Precision:", precision_score(df["is_fraud"], df["rule_pred"]))
print("Recall:   ", recall_score(df["is_fraud"], df["rule_pred"]))
```
*(Yes — the rule matches the label exactly here, on purpose, so the metrics are simple to read. In 1.2, you'll see a real model behave differently.)*


### 1.2 — One real model, one line of comparison
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df[["amount", "is_new_recipient"]], df["is_fraud"], test_size=0.3, random_state=1
)
model = LogisticRegression().fit(X_train, y_train)
preds = model.predict(X_test)
print("Model precision:", precision_score(y_test, preds, zero_division=0))
print("Model recall:   ", recall_score(y_test, preds, zero_division=0))
```
**One-line verdict, said out loud:** ship the rule, or ship the model — and why?

---

## Drift Catch 

In production, incoming data can quietly change shape. Simulate that:
```python
drifted = df[["amount", "is_new_recipient"]].copy()
drifted["amount"] = drifted["amount"] * 1.5   # a few months later, average spend has crept up
print("Original average amount:", df["amount"].mean())
print("Drifted average amount: ", drifted["amount"].mean())
```

Now write the simplest possible monitor for this — no statistics needed, just a percentage check:
```python
def check_feature_drift(new_avg, baseline_avg, pct_threshold=0.2):
    # TODO: return True if new_avg is more than pct_threshold (e.g. 20%)
    # bigger than baseline_avg
    pass

fires = check_feature_drift(drifted["amount"].mean(), df["amount"].mean())
print("Drift alert fired:", fires)
```


**30-second discussion:** if this ran every morning on yesterday's transactions, what's one real-world reason `amount` might drift that *isn't* fraud going up?

---

## Quick Format Check 

**Guess first:** which file will be smaller, CSV or Parquet?
```python
import os
df.to_csv("data.csv", index=False)
df.to_parquet("data.parquet")

print("CSV size (KB):    ", os.path.getsize("data.csv") / 1024)
print("Parquet size (KB):", os.path.getsize("data.parquet") / 1024)
```


**30-second discussion:** CSV is plain text and human-readable; Parquet is compressed and binary. Which would you pick to hand to a colleague to eyeball in a text editor? Which would you pick to store years of transaction history?

---

## Mage AI Sprint: Automate a Basic Pipeline 

Everything above — load data, check it, save it — is exactly what an **orchestrated pipeline** can run automatically instead of you re-running notebook cells. Let's build a small one, using the file you already created in Block 3 (no external accounts needed).

```bash
mage start data_pipeline_demo
```
Click the forwarded `http://localhost:6789` URL. Log in: `admin@admin.com` / `admin`.


1. **New pipeline** → Standard batch → name it `MLIP_WK2`
2. **Data Loader** (Extract): load `data.csv` (the file you already created in Block 3) into a DataFrame.
3. **Transformer** (Transform): keep only the columns `amount` and `is_new_recipient`, and add a new column flagging any row where `amount > 150`.
4. **Data Exporter** (Load): write the result to a new file, e.g. `flagged_transactions.csv`, inside `data_pipeline_demo/`.
5. Run the pipeline. All blocks green = done.

**60-second pair discussion:** which block matches which line of code you already wrote earlier today? What would you need to add to this pipeline to make it check for drift automatically (hint: Block 2)?

> ⚠️ **Shut down your Codespace the moment you're done with Mage** — its server keeps running in the background and burns your free hours fast.

---

## 🏁 Final 5 Min — Commit, Score, Exit

```bash
cd ..
git add .
git commit -m "Week 02: baseline model, drift check, format comparison, Mage AI pipeline"
git push
```

---

## If You Finish Everything Early
- Try a stricter fraud rule (e.g. `amount > 100`) — how do precision and recall move?
- Add a second Transformer block in Mage that also flags `is_new_recipient == 1` rows separately
- Swap `LogisticRegression` for a `RandomForestClassifier` — does the verdict from 1.2 change?

---

