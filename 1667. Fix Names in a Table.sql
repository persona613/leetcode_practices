/*
1067 ms runtime beats 82.17%
*/
# Write your MySQL query statement below

-- substring(start, length), concat(str1, str2, ...)
SELECT
    user_id,
    CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) as name
FROM Users
ORDER BY user_id