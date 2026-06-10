# 1

SELECT users.user, orders.revenue
FROM users
JOIN orders
ON users.user_id = orders.user_id;

# 2

SELECT user, SUM(orders.revenue)
FROM users
JOIN orders
ON users.user_id = orders.user_id
GROUP BY user;

# 3

SELECT 
  users.user, 
  COALESCE(SUM(orders.revenue), 0) AS Rev_from_user
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id
GROUP BY users.user;

# 4
SELECT 
  users.user, 
  SUM(orders.revenue) AS total_revenue
FROM users
JOIN orders
  ON users.user_id = orders.user_id
GROUP BY users.user_id, users.user
HAVING SUM(orders.revenue) > 100;


