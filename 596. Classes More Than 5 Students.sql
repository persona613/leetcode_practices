/*
572 ms runtime beats 56.03%
*/
# Write your MySQL query statement below
SELECT class
    FROM Courses
    GROUP BY class
    HAVING COUNT(*) >= 5