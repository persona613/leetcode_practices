/*
Wrong Answer
8 / 9 testcases passed
*/
# Write your MySQL query statement below
SELECT l.name FROM Employee l, Employee r
    WHERE l.id=r.managerId
    GROUP BY l.name
    HAVING COUNT(*)>=5