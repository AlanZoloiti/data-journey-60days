
---

# 🧠 NOTES (Day 12)

```markdown
# Day 12 — Notes (EDA)

## 📊 EDA

EDA = understand data before analysis  

---

## 🔥 describe()

count → number of values  
mean → average  
std → spread  
min / max → range  

---

## ⚡ Mean vs Median

mean ≠ median → skewed data  

---

## 📦 Boxplot

- shows median  
- shows distribution  
- shows outliers  

---

## 🔥 Outliers

outlier = value far from others  

---

## 📏 IQR

IQR = Q3 - Q1  

lower = Q1 - 1.5 * IQR  
upper = Q3 + 1.5 * IQR  

---

## ⚠️ Detection

value < lower OR value > upper → outlier  

---

## 🧹 Cleaning

remove:
df[(col >= lower) & (col <= upper)]

clip:
df[col].clip(lower, upper)

---

## 📊 Histplot

shows distribution  

---

## 🔥 Skew

right skew → tail right  
left skew → tail left  

---

## 🎯 Insight

data is rarely normal  

---

## 💡 Rule

EDA = visualize → understand → clean  

---