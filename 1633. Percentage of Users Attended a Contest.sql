/*
1681 ms runtime beats 69.53%
*/
# Write your MySQL query statement below
SELECT contest_id, 
    ROUND(COUNT(*)/(SELECT COUNT(*) FROM Users)*100,2) 'percentage' 
    FROM Register
    GROUP BY contest_id
    ORDER BY percentage DESC, contest_id;
