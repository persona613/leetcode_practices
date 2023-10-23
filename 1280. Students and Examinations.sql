/*
1669 ms runtime beats 69.44%
*/
# Write your MySQL query statement below
with tb as (
    SELECT student_id, student_name, subject_name 
        FROM Students
        JOIN Subjects
        ORDER BY student_id, subject_name
)
SELECT tb.student_id, tb.student_name, tb.subject_name, 
    COUNT(ex.subject_name) as 'attended_exams' 
    From tb
    LEFT JOIN Examinations ex
    ON tb.student_id=ex.student_id AND tb.subject_name=ex.subject_name
    GROUP BY tb.student_id, tb.subject_name
    ORDER BY student_id, subject_name;
 
