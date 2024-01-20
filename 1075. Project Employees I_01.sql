/*
Wrong Answer
3 / 8 testcases passed
*/
# Write your MySQL query statement below
SELECT p.project_id, AVG(experience_years) 'average_years'
    FROM Project p
    JOIN Employee e
    ON p.employee_id=e.employee_id
    GROUP BY p.project_id