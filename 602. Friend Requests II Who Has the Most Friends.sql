/*
482 ms runtime beats 84.35%
*/
# Write your MySQL query statement below

-- RID
with rid as (
SELECT
    requester_id as id,
    COUNT(*) as rc
FROM RequestAccepted 
GROUP BY requester_id
),

-- AID
aid as (
SELECT
    accepter_id as id,
    COUNT(*) as ac
FROM RequestAccepted 
GROUP BY accepter_id
)

SELECT
    r.id,
    r.rc + IFNULL(a.ac, 0) as num
FROM rid r
LEFT JOIN aid a
ON r.id=a.id

UNION

SELECT
    a.id,
    a.ac + IFNULL(r.rc, 0) as num
FROM rid r
RIGHT JOIN aid a
ON r.id=a.id

ORDER BY num DESC
LIMIT 1