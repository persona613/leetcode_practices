/*
Wrong Answer
24 / 25 testcases passed
*/
# Write your MySQL query statement below

-- REGEXP '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}$';
SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z]+[A-Za-z0-9._-]*@leetcode.com$';