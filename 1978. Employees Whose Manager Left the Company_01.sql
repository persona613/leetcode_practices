/*
Wrong Answer
10 / 13 testcases passed
*/
# Write your MySQL query statement below
SELECT
    employee_id
FROM
    Employees
WHERE
    salary < 30000
    AND
    manager_id not in (
        SELECT employee_id FROM Employees
    )