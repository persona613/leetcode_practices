/*
3240 ms runtime beats 19.68%
*/
# Write your MySQL query statement below
SELECT
    customer_id,
    COUNT(customer_id) as count_no_trans
FROM
    Visits as v
LEFT JOIN
    Transactions as t
ON
    v.visit_id = t.visit_id
WHERE
    t.visit_id is NULL
GROUP BY
    customer_id


-- SELECT customer_id, COUNT(customer_id) as 'count_no_trans'
--     FROM Visits
--     WHERE visit_id NOT IN (
--         SELECT visit_id 
--         FROM Transactions
--         )
--     GROUP BY customer_id;


-- SELECT visit_id 
-- FROM Transactions