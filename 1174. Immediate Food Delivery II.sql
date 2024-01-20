/*
1419 ms runtime beats 29.98%
*/
# Write your MySQL query statement below
with cte1 as (
SELECT
    customer_id,
    MIN(order_date) fod
FROM Delivery
GROUP BY customer_id
ORDER BY customer_id
),

cte2 as (
SELECT 
    cte1.fod=d.customer_pref_delivery_date imd
FROM cte1
JOIN Delivery d
WHERE cte1.customer_id=d.customer_id
    AND cte1.fod=d.order_date
)

SELECT ROUND(AVG(cte2.imd)*100,2) as immediate_percentage
    FROM cte2
