/*
1590 ms runtime beats 16.54%
*/
# Write your MySQL query statement below
SELECT e.employee_id, e.name,
    COUNT(*) as reports_count,
    ROUND(AVG(r.age)) as average_age
    FROM Employees e
    JOIN Employees r
    ON e.employee_id=r.reports_to
    GROUP BY e.employee_id
    ORDER BY e.employee_id