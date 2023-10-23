/*
1120 ms runtime beats 94.99%
*/
# Write your MySQL query statement below
SELECT s.user_id, ROUND(SUM(IF(action='confirmed', 1, 0))/COUNT(*),2) confirmation_rate
    FROM Confirmations c
    RIGHT JOIN Signups s
    ON c.user_id=s.user_id
    GROUP BY user_id;
