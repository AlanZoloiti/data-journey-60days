# Day 11 — SQL: JOIN

## 🎯 Goal
Learn how to combine data from multiple tables and calculate metrics.

---

## 🧠 What I Learned

- JOIN → combine tables by key  
- INNER JOIN → only matching rows  
- LEFT JOIN → keep all rows from left table  
- ON → join condition  
- COALESCE → handle NULL values  
- JOIN + GROUP BY → calculate metrics  
- JOIN + HAVING → filter aggregated data  

---

## 🔍 Examples

SELECT users.user, orders.revenue  
FROM users  
JOIN orders  
  ON users.user_id = orders.user_id;

---

SELECT users.user, SUM(orders.revenue) AS total_revenue  
FROM users  
JOIN orders  
  ON users.user_id = orders.user_id  
GROUP BY users.user;

---

SELECT users.user, COALESCE(SUM(orders.revenue), 0) AS total_revenue  
FROM users  
LEFT JOIN orders  
  ON users.user_id = orders.user_id  
GROUP BY users.user;

---

SELECT users.user  
FROM users  
LEFT JOIN orders  
  ON users.user_id = orders.user_id  
WHERE orders.user_id IS NULL;

---

## 🔥 Key Insights

- JOIN combines data from multiple tables  
- INNER JOIN removes non-matching rows  
- LEFT JOIN keeps all users  
- NULL appears when no match exists  
- COALESCE replaces NULL with default values  
- GROUP BY + JOIN = real analytics  

---

## ⚠️ Common Mistakes

- wrong join key ❌  
- forgetting LEFT JOIN for missing data ❌  
- using COUNT(*) instead of COUNT(column) ❌  
- ignoring NULL values ❌  

---

## 🎯 Real-World Usage

- user revenue calculation  
- product analytics  
- customer segmentation  
- business reporting  

---