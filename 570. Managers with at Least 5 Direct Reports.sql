"""
489 ms runtime beats 86.97%
"""
# Write your MySQL query statement below
SELECT l.name
FROM Employee l, Employee r
WHERE l.id=r.managerId
GROUP BY l.id
HAVING COUNT(*)>=5