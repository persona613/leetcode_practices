/*
715 ms runtime beats 82.85%
*/
# Write your MySQL query statement below

-- GROUP_CONCAT(DISTINCT col ORDER BY col DESC SEPARATOR ',')
SELECT
    sell_date,
    COUNT(DISTINCT product) as num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') as products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date
