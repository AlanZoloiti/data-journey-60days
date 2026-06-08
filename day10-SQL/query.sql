# 1
SELECT user, COUNT(*)
FROM users
GROUP BY user
HAVING COUNT(*) > 1;

# 2

SELECT user, SUM(revenue)
FROM users
GROUP BY user
HAVING SUM(revenue) > 30;

# 3

SELECT COUNT(DISTINCT user)
FROM users
WHERE revenue > 30;

# 4

SELECT 
  user,
  COUNT(*) AS record_number,
  MAX(revenue) AS max_revenue
FROM users
GROUP BY user;