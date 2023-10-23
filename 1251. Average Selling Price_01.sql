/*
Wrong Answer
15 / 16 testcases passed
*/
# Write your MySQL query statement below
SELECT p.product_id, 
    ROUND(SUM(p.price*u.units)/SUM(u.units), 2) 'average_price'
    FROM Prices p
    JOIN UnitsSold u
    ON p.product_id=u.product_id
    AND p.start_date<=u.purchase_date
    AND u.purchase_date<=p.end_date
    GROUP BY p.product_id