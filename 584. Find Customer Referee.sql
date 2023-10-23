/*
935 ms runtime beats 72.44%
*/
# Write your MySQL query statement below
SELECT name FROM Customer
    WHERE referee_id != 2 OR referee_id is NULL