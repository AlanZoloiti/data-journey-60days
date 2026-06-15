# Day 12 — EDA (Exploratory Data Analysis)

## 🎯 Goal
Understand data distribution, detect outliers, and clean data.

---

## 🧠 What I Learned

- EDA → exploratory data analysis  
- describe() → summary statistics  
- mean vs median → detect skew  
- boxplot → detect outliers  
- IQR → statistical method for outliers  
- histplot → understand distribution  
- data cleaning → remove or cap outliers  

---

## 🔍 Key Concepts

### Distribution
- Normal → symmetric  
- Right-skewed → tail on the right  
- Left-skewed → tail on the left  

---

### IQR (Interquartile Range)
- IQR = Q3 - Q1  
- Lower bound = Q1 - 1.5 * IQR  
- Upper bound = Q3 + 1.5 * IQR  

---

## 📊 Example

```python
import pandas as pd

df = pd.DataFrame({
    'revenue': [5, 10, 15, 20, 1000]
})