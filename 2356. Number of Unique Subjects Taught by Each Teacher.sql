/*
853 ms runtime beats 82.71%
*/
# Write your MySQL query statement below
SELECT teacher_id,
    COUNT(DISTINCT subject_id) as cnt
    FROM Teacher
    GROUP BY teacher_id