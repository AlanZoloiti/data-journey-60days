# Day 7 — Notes (NumPy & np.where)

## 🧠 NumPy Array

NumPy array = fast structure for numerical operations

list → slow, Python loops  
array → fast, vectorized operations  

Example:

np.array([1, 2, 3])

---

## 🔥 Vectorization

Vectorization = operations on entire column at once

df['revenue'] > 30  

No loops, no apply  

---

## 🧠 Boolean Mask

Result of condition:

df['revenue'] > 30  

→ [False, False, True, True, False]

This is called a boolean mask

---

## ⚡ np.where()

Syntax:

np.where(condition, value_if_true, value_if_false)

---

## 🧠 How it works

1. Create condition → boolean mask  
2. Apply logic using np.where  

---

## 📊 Example

np.where(df['revenue'] > 30, 'high', 'low')

---

## 🔥 What happens inside

Condition:

[False, False, True, True, False]

Result:

['low', 'low', 'high', 'high', 'low']

---

## ❗ Key Rule

np.where uses True / False, NOT actual values

---

## 🧠 Mental Model

condition → mask  
mask → controls output  

---

## ⚡ apply vs np.where

apply:
- row by row
- slower

np.where:
- column-wise
- faster
- production-ready

---

## ⚠️ Common Mistakes

- using strings instead of numeric data ❌  
- wrong condition (>, >=) ❌  
- misunderstanding boolean mask ❌  

---

## 🎯 Key Insight

apply = loop  
np.where = vectorized logic  

---

## 🧠 Final Thinking

df['revenue'] → data  
df['revenue'] > 30 → condition  
np.where(...) → result  

---