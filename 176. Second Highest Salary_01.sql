/*
Wrong Answer
8 / 9 testcases passed
*/
# Write your MySQL query statement below

-- DENSE_RANK
with c as (
SELECT
    DISTINCT salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as rk
FROM Employee
),

s as (
SELECT
    CASE
        WHEN rk!= 2 THEN 0
        ELSE salary
        END AS sal
FROM c
WHERE rk <= 2
)

SELECT IF(SUM(sal)=0, NULL, SUM(sal)) as SecondHighestSalary
FROM s
