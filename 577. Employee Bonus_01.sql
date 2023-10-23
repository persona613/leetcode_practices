/*
Wrong Answer
19 / 20 testcases passed
*/
# Write your MySQL query statement below
SELECT  name, bonus FROM Employee em
    LEFT JOIN Bonus bo
    USING (empId)
    WHERE bonus>1000 IS NOT TRUE