# Day 9 — SQL: SELECT, WHERE, AND, OR

## 🎯 Goal
Learn how to filter data using SQL and combine conditions correctly.

---

## 🧠 What I Learned

- SELECT → choose columns  
- WHERE → filter rows  
- AND → all conditions must be True  
- OR → at least one condition must be True  
- BETWEEN → range (inclusive)  
- NOT IN → exclude values  
- importance of condition order and parentheses  

---

## 🔍 Examples

SELECT user, revenue  
FROM users  
WHERE revenue > 30;

---

SELECT user, revenue  
FROM users  
WHERE revenue > 20 AND revenue < 50;

---

SELECT user, revenue  
FROM users  
WHERE revenue < 20 OR revenue > 50;

---

SELECT user, revenue  
FROM users  
WHERE revenue BETWEEN 20 AND 60  
  AND revenue NOT IN (35, 60);

---

## 🔥 Key Insights

- SQL works row by row  
- AND → narrows results  
- OR → combines results  
- parentheses control logic  
- BETWEEN includes boundaries  
- NOT IN excludes specific values  

---

## ⚠️ Common Mistakes

- forgetting parentheses ❌  
- mixing AND and OR incorrectly ❌  
- assuming OR picks only one condition ❌  
- writing conditions without logical operators ❌  

---

## 🎯 Real-World Usage

- filtering users  
- building datasets  
- preparing data for analysis  

---