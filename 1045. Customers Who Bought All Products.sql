/*
936 ms runtime beats 70.38%
*/
# Write your MySQL query statement below
with cte as (
    SELECT customer_id,
    COUNT(DISTINCT product_key) as cnt
    FROM Customer
    GROUP BY customer_id)
SELECT customer_id
    FROM cte
    WHERE cnt=(SELECT COUNT(*) FROM Product)