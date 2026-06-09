# Day 10 — SQL: GROUP BY & Aggregations

## 🎯 Goal
Learn how to group data and calculate key metrics using SQL.

---

## 🧠 What I Learned

- GROUP BY → split data into groups  
- COUNT → number of records  
- SUM → total value  
- AVG → average value  
- MAX → maximum value  
- HAVING → filter aggregated results  

---

## 🔍 Examples

SELECT user, COUNT(*)  
FROM users  
GROUP BY user;

---

SELECT user, SUM(revenue)  
FROM users  
GROUP BY user;

---

SELECT user, AVG(revenue)  
FROM users  
GROUP BY user;

---

SELECT user, SUM(revenue)  
FROM users  
GROUP BY user  
HAVING SUM(revenue) > 30;

---

## 🔥 Key Insights

- GROUP BY creates groups  
- Aggregations reduce multiple rows into one value  
- COUNT counts rows  
- SUM calculates total values  
- AVG calculates mean values  
- HAVING filters after aggregation  

---

## ⚠️ Common Mistakes

- selecting columns without aggregation ❌  
- forgetting GROUP BY ❌  
- using WHERE instead of HAVING ❌  
- syntax errors (commas, aliases) ❌  

---

## 🎯 Real-World Usage

- user metrics  
- revenue analysis  
- product analytics  
- business reporting  

---