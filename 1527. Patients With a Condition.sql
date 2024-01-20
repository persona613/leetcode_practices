/*
736 ms runtime beats 32.00%
*/
# Write your MySQL query statement below

SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%' or
      conditions LIKE '% DIAB1%'