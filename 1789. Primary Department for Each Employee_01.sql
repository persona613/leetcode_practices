/*
Wrong Answer
22 / 23 testcases passed
*/
# Write your MySQL query statement below
with cte as (
    SELECT employee_id,
    department_id
    FROM Employee as e
    WHERE primary_flag='Y'
    GROUP BY employee_id
)
SELECT e.employee_id,
    IFNULL(cte.department_id, e.department_id) as department_id
    FROM Employee as e
    LEFT JOIN cte
    ON e.employee_id=cte.employee_id
    GROUP BY e.employee_id


# wrong
# SELECT employee_id,
#     CASE
#         WHEN COUNT(employee_id)=1 THEN department_id
#         WHEN COUNT(employee_id)>1 AND primary_flag='Y' THEN department_id
#         ELSE NULL
#         END AS department_id
#     FROM Employee as e
#     GROUP BY employee_id