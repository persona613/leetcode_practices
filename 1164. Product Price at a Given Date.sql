/*
793 ms runtime beats 80.58%
*/
# Write your MySQL query statement below
with cte as (
    SELECT product_id, new_price 
    FROM (
        SELECT *,
        RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) as rk
        FROM Products
        WHERE change_date <= '2019-08-16'
    ) as d
    WHERE rk=1
)
SELECT DISTINCT p.product_id,
    IFNULL(cte.new_price, 10) as price
    FROM Products as p
    LEFT JOIN cte
    ON p.product_id=cte.product_id
