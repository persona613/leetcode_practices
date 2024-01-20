/*
1623 ms runtime beats 8.39%
*/
# Write your MySQL query statement below
SELECT 
    employee_id,
    department_id
FROM Employee as e
WHERE primary_flag='Y'

UNION

SELECT 
    employee_id,
    department_id
FROM Employee as e
GROUP BY employee_id
HAVING  Count(*)=1
