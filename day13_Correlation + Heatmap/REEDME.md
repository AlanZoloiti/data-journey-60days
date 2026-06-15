# Day 13 — Correlation & Heatmap

## 🎯 Goal
Learn how to identify relationships between variables and determine which factors influence a target metric.

---

## 🧠 Key Concepts

### Correlation
Correlation measures the relationship between two variables.

- +1 → strong positive correlation  
- 0 → no correlation  
- -1 → strong negative correlation  

---

## 📊 Example

```python
import pandas as pd

df = pd.DataFrame({
    'ads': [1, 2, 3, 4, 5],
    'revenue': [10, 20, 30, 40, 50],
    'users': [5, 3, 6, 2, 7]
})

df.corr()