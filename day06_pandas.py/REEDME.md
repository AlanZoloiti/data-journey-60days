# Day 6 — Pandas: apply() & Vectorization

## 🎯 Goal
Understand how to apply custom logic to data using apply() and how to rewrite it using vectorized operations (production-ready approach).

---

## 🧠 What I Learned

- apply() — applying custom logic row by row  
- axis=1 — working with rows  
- vectorization — operations on entire columns  
- np.select() — vectorized alternative to if/elif  
- importance of condition order  

---

## 🔍 Problem

Classify users based on business rules using:

- revenue  
- visits  

---

## ⚙️ Approach 1 — apply()

def classify_user(row):
    if row['revenue'] > 40 and row['visits'] > 5:
        return 'vip'
    elif row['revenue'] > 20 and row['visits'] > 2:
        return 'loyal'
    else:
        return 'casual'

df['user_score'] = df.apply(classify_user, axis=1)

---

## ⚙️ Approach 2 — Vectorization (Recommended)

import numpy as np

conditions = [
    (df['revenue'] > 40) & (df['visits'] > 5),
    (df['revenue'] > 20) & (df['visits'] > 2)
]

choices = ['vip', 'loyal']

df['user_score'] = np.select(conditions, choices, default='casual')

---

## 🔥 Key Insights

- apply() works row by row → slower  
- vectorization works on full columns → faster  
- np.select() behaves like if/elif (top-down logic)  
- order of conditions matters  

---

## ⚠️ Common Mistakes

- using apply() for large datasets ❌  
- incorrect condition order ❌  
- overlapping conditions without priority ❌  

---

## 🎯 Real-World Usage

- user segmentation  
- feature engineering  
- business rule implementation  

---

## 🧠 Mental Model

row → one user  
column → all users  

apply → row logic  
vectorization → column logic  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  