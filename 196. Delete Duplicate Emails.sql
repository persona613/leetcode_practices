/*
1194 ms runtime beats 89.66%
*/
# Write your MySQL query statement below
with c as (
SELECT MIN(id) as id
FROM Person
GROUP BY email
)

DELETE
FROM Person
WHERE id NOT IN (SELECT id FROM c)