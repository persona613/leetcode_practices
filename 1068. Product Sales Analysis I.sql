/*
1656 ms runtime beats 96.41%
*/
# Write your MySQL query statement below
SELECT product_name, year, price FROM Sales
    JOIN Product
    USING (product_id)