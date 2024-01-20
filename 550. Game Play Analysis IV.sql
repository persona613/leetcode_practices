/*
1447 ms runtime beats 12.93%
*/
# Write your MySQL query statement below
with cte as(
    SELECT player_id,
    ADDDATE(MIN(event_date), 1) as ad
    FROM Activity
    GROUP BY player_id
)
SELECT ROUND(AVG(a.event_date is not NULL),2) as fraction
    FROM cte c
    LEFT JOIN Activity a
    ON c.player_id=a.player_id AND c.ad=a.event_date
