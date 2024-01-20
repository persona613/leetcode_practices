/*
1430 ms runtime beats 96.75%
*/
# Write your MySQL query statement below

-- Dense_Rank() OVER
with r as (
SELECT
    *,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rk
FROM Employee
)

SELECT
    d.name as Department,
    r.name as Employee,
    r.salary as Salary
FROM r
JOIN Department d
ON r.departmentId = d.id
WHERE r.rk <= 3
