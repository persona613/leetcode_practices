/*
2978 ms runtime beats 19.94%
*/
# Write your MySQL query statement below
SELECT
    u.user_id as buyer_id,
    u.join_date,
    SUM(IF(o.order_date LIKE '2019%', 1, 0)) as orders_in_2019
FROM
    Users as u
LEFT JOIN
    Orders as o
ON
    u.user_id = o.buyer_id
GROUP BY
    u.user_id