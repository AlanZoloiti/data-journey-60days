# Day 11 — Notes (SQL JOIN)

## 🧠 JOIN

JOIN → combine tables  

---

## 🔥 INNER JOIN

only matching rows  

---

## 🔥 LEFT JOIN

keep all rows from left table  

missing values → NULL  

---

## ⚡ ON

ON → join condition  

users.user_id = orders.user_id  

---

## ❗ NULL

no match → NULL  

---

## 🔥 COALESCE

COALESCE(x, 0) → replace NULL with 0  

---

## ⚡ COUNT

COUNT(*) → counts all rows  
COUNT(column) → counts NOT NULL  

---

## ⚠️ Important

LEFT JOIN + COUNT(*) → wrong ❌  
LEFT JOIN + COUNT(column) → correct ✅  

---

## 🔥 Example

SELECT users.user, COUNT(orders.revenue)  
FROM users  
LEFT JOIN orders  
  ON users.user_id = orders.user_id  
GROUP BY users.user;  

---

## 🧠 Missing Data

LEFT JOIN + WHERE column IS NULL  
→ find missing rows  

---

## 🎯 Key Idea

JOIN → combine  
GROUP BY → group  
SUM / COUNT → calculate  

---

## ⚡ Mental Model

JOIN → merge tables  
LEFT JOIN → keep all  
NULL → no data  

---