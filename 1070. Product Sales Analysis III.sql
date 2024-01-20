/*
1519 ms runtime beats 96.52%
*/
# Write your MySQL query statement below
with c as (
SELECT
    product_id,
    MIN(year) as first_year
FROM Sales
GROUP BY product_id
)

SELECT 
    s.product_id,
    c.first_year as first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN c
ON s.product_id=c.product_id
    AND s.year=c.first_year