/*
2122 ms runtime beats 85.81%
*/
# Write your MySQL query statement below
SELECT unique_id, name FROM Employees
    LEFT OUTER JOIN EmployeeUNI uni
    ON Employees.id=uni.id