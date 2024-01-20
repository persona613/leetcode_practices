/*
Wrong Answer
1 / 22 testcases passed
*/
# Write your MySQL query statement below
with cte as (
    SELECT customer_id,
    MIN(order_date) fod,
    customer_pref_delivery_date=MIN(order_date) imd
    FROM Delivery
    GROUP BY customer_id
)
SELECT ROUND(AVG(imd)*100,2) as immediate_percentage
    FROM cte
