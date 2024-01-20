/*
1342 ms runtime beats 90.37%
*/
# Write your MySQL query statement below
with c as (
    SELECT person_name,
    SUM(weight) OVER (ORDER BY turn) as cw
    FROM Queue
    ORDER BY turn
)
SELECT person_name
    FROM c
    WHERE cw <= 1000
    ORDER BY cw DESC
    LIMIT 1
