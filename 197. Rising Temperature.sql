/*
597 ms runtime beats 98.69%
*/
# Write your MySQL query statement below
SELECT cur.id FROM Weather cur
    JOIN Weather pre
    ON cur.recordDate = pre.recordDate + INTERVAL 1 DAY
    WHERE cur.temperature>pre.temperature