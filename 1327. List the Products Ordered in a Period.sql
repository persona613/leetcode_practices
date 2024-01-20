/*
1690 ms runtime beats 18.82%
*/
# Write your MySQL query statement below

-- 2020-02
with c as (
SELECT 
    product_id,
    SUM(unit) as tu
FROM Orders
WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
GROUP BY product_id
)

SELECT
    p.product_name,
    c.tu as unit
FROM c
JOIN Products as p
ON c.product_id=p.product_id
WHERE c.tu >= 100