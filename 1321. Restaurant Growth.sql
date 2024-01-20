/*
664 ms runtime beats 73.68%
*/
# Write your MySQL query statement below

-- 1 DAY AMOUNT
with cte as (
SELECT
    visited_on,
    SUM(amount) as ds,
    SUM(SUM(amount)) OVER (ORDER BY visited_on) as asum
FROM Customer
GROUP BY visited_on
ORDER BY visited_on
)

SELECT
    l.visited_on,
    CASE
        WHEN r.visited_on IS NULL THEN l.asum
        ELSE l.asum - r.asum
    END AS amount,
    CASE
        WHEN r.visited_on IS NULL THEN ROUND(l.asum/7, 2)
        ELSE ROUND((l.asum - r.asum)/7, 2)
    END AS average_amount
FROM cte l
LEFT JOIN cte r
ON l.visited_on = r.visited_on + INTERVAL 7 DAY
ORDER BY l.visited_on
LIMIT 18446744073709551615 OFFSET 6