/*
Wrong Answer
17 / 21 testcases passed
*/
# Write your MySQL query statement below
SELECT 
    g1.num as ConsecutiveNums
FROM Logs as g1
JOIN Logs as g2
ON g1.id=g2.id-1
JOIN Logs as g3
ON g1.id = g3.id-2
WHERE g1.num=g2.num and g2.num=g3.num
