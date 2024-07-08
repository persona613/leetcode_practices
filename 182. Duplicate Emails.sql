/*
636 ms runtime beats 83.64%
*/
# Write your MySQL query statement below
SELECT
    email as Email
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(email) > 1


-- SELECT
--     email as Email
-- FROM (
--     SELECT email, COUNT(*) as cnt
--     FROM Person
--     GROUP BY email
-- ) temp
-- WHERE
--     cnt > 1