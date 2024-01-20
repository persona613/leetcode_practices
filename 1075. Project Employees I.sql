/*
876 ms runtime beats 84.36%
*/
# Write your MySQL query statement below
SELECT
    p.project_id,
    ROUND(AVG(experience_years), 2) 'average_years'
FROM Project p
JOIN Employee e
ON p.employee_id=e.employee_id
GROUP BY p.project_id