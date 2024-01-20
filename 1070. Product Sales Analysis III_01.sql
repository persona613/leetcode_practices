/*
Wrong Answer
1 / 10 testcases passed
*/
# Write your MySQL query statement below
SELECT product_id,
    MIN(year) as first_year,
    quantity,
    price
    FROM Sales
    GROUP BY product_id