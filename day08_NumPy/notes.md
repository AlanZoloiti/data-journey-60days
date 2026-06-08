# Day 8 — Notes (np.select & NaN)

## 🧠 np.select

np.select = multiple conditions (if / elif / else)

np.select([cond1, cond2], [A, B], default=C)

- checks top-down
- first True condition wins

---

## ⚡ np.where vs np.select

np.where → 1 condition  
np.select → multiple conditions  

---

## ❗ Condition Order

order matters

wrong order → wrong result

---

## 🧠 NaN

NaN = missing value (not a number)

- cannot compare with ==
- np.nan != np.nan

---

## ⚡ Check NaN

pd.isna(x) → correct  
np.isnan(x) → only for numeric  

---

## 🔥 Key Insight

conditions → boolean masks  
np.select → applies logic  

---

## 🎯 Mental Model

np.where → simple logic  
np.select → complex logic  
NaN → missing data  

---