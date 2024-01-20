/*
596 ms runtime beats 93.60%
*/
# Write your MySQL query statement below
SELECT query_name, 
    ROUND(AVG(rating/position), 2) quality,
    ROUND(SUM(rating<3)/COUNT(rating)*100, 2) poor_query_percentage
    FROM Queries
    GROUP BY query_name;