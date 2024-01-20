/*
446 ms runtime beats 66.06%
*/
# Write your MySQL query statement below

-- DENSE_RANK
with c as (
SELECT
    DISTINCT salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as rk
FROM Employee
)

SELECT
    MAX(salary) as SecondHighestSalary
FROM c
WHERE rk = 2


-- DENSE_RANK
# with c as (
# SELECT
#     DISTINCT salary,
#     DENSE_RANK() OVER (ORDER BY salary DESC) as rk
# FROM Employee
# )

# SELECT (
#     SELECT
#         salary
#     FROM c
#     WHERE rk = 2
# ) as SecondHighestSalary


# SELECT 
#     MAX(salary) as SecondHighestSalary
# FROM Employee
# WHERE salary < (SELECT MAX(salary) FROM Employee)