# Day 10 — Notes (SQL Aggregation)

## 🧠 GROUP BY

GROUP BY → split data into groups  

---

## ⚡ Aggregation

aggregation → many rows → one value  

---

## 🔥 Functions

COUNT(*) → number of rows  
SUM(revenue) → total  
AVG(revenue) → average  
MAX(revenue) → max value  

---

## ❗ Rule

SELECT must contain:
✔ group columns  
✔ aggregate functions  

---

## ⚠️ Example (wrong)

SELECT user, revenue  
FROM users  
GROUP BY user;  

---

## ✅ Example (correct)

SELECT user, SUM(revenue)  
FROM users  
GROUP BY user;  

---

## 🔥 HAVING

HAVING → filter after aggregation  

---

## ⚡ Example

SELECT user, SUM(revenue)  
FROM users  
GROUP BY user  
HAVING SUM(revenue) > 30;  

---

## 🧠 Key Idea

GROUP BY → split  
AGGREGATE → compress  
SELECT → show result  

---

## ⚡ Mental Model

GROUP BY → boxes  
COUNT → how many inside  

---

## 🔥 Advanced

COUNT(CASE WHEN revenue > 30 THEN 1 END)  
SUM(CASE WHEN revenue > 30 THEN 1 ELSE 0 END)  

---
