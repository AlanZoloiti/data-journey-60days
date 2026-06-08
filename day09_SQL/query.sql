# 1
SELECT user, revenue
FROM users
WHERE (revenue > 20 AND revenue < 50) OR revenue < 15;

# 2
SELECT user, revenue
FROM users
WHERE revenue > 20 AND (revenue < 30 OR revenue > 40);

 # OR

 SELECT user, revenue
 FROM users
 WHERE revenue > 20 
   AND revenue NOT BETWEEN 30 AND 40;

# 3
 SELECT user, revenue
 FROM users
 WHERE (revenue < 15 OR revenue > 50) AND revenue != 10;