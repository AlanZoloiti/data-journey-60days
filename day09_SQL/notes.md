# Day 9 — Notes (SQL Basics)

## 🧠 SELECT

SELECT → choose columns

SELECT user, revenue  
FROM users  

---

## 🧠 WHERE

WHERE → filter rows

WHERE revenue > 30  

---

## ⚡ AND vs OR

AND → all conditions must be True  
OR → at least one condition must be True  

---

## 🔥 BETWEEN

BETWEEN → range (inclusive)

revenue BETWEEN 20 AND 60  
= revenue >= 20 AND revenue <= 60  

---

## 🔥 NOT IN

exclude values

revenue NOT IN (35, 60)  

---

## ❗ Order of Logic

use parentheses ()

(revenue > 20 AND revenue < 50) OR revenue < 15  

---

## 🧠 Key Idea

SQL works row by row  

each row → True or False  

---

## ⚡ Mental Model

AND → narrow  
OR → combine  

---

## ⚠️ Common Mistakes

- forgetting parentheses ❌  
- mixing AND/OR logic ❌  
- thinking OR selects only one condition ❌  
- wrong column names ❌  

---

## 🎯 Example

SELECT user, revenue  
FROM users  
WHERE revenue BETWEEN 20 AND 60  
  AND revenue NOT IN (35, 60);  

---