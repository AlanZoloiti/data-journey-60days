# Day 7 — NumPy: Arrays & np.where

## 🎯 Goal
Learn how to work with NumPy arrays and use np.where to apply conditional logic efficiently without loops.

---

## 🧠 What I Learned

- NumPy arrays vs Python lists  
- vectorized operations  
- boolean masks (True / False arrays)  
- np.where as a vectorized if/else  
- replacing apply() with faster operations  

---

## 🔍 Problem

Classify users based on revenue using a fast, scalable approach.

---

## ⚙️ Approach — np.where()

import numpy as np

df['revenue_flag'] = np.where(df['revenue'] > 30, 'high', 'low')

---

## 🧠 How It Works

Step 1 — create condition:

df['revenue'] > 30  

Result:

[False, False, True, True, False]

---

Step 2 — apply np.where:

np.where(condition, 'high', 'low')

Final result:

['low', 'low', 'high', 'high', 'low']

---

## 🔥 Key Insights

- np.where works on entire columns (vectorization)  
- no loops → faster performance  
- uses boolean masks internally  
- ideal replacement for simple apply logic  

---

## ⚠️ Common Mistakes

- using strings instead of numeric arrays ❌  
- misunderstanding boolean masks ❌  
- incorrect conditions (>, >=, etc.) ❌  

---

## 🎯 Real-World Usage

- feature engineering  
- user segmentation  
- flag creation (high/low activity, risk, etc.)  

---

## 🧠 Mental Model

condition → boolean mask  
np.where → apply logic to entire column  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  