/*
786 ms runtime beats 83.70%
*/
# Write your MySQL query statement below
SELECT activity_date as day,
    COUNT(DISTINCT user_id) as active_users
    FROM Activity
    GROUP BY day
    HAVING activity_date > ADDDATE('2019-07-27',-30)
    AND activity_date <= '2019-07-27'