/*
614 ms runtime beats 23.82%
*/
# Write your MySQL query statement below
UPDATE Salary
SET sex=IF(sex='m', 'f', 'm')