/*
2901 ms runtime beats 26.29%
*/
# Write your MySQL query statement below
with cte as (
    SELECT category,
        COUNT(*) as accounts_count
        FROM (
            SELECT *,
            CASE
                WHEN income<20000 THEN 'Low Salary'
                WHEN income>50000 THEN 'High Salary'
                ELSE 'Average Salary'
                END AS category
            FROM Accounts
        ) as t
        GROUP BY category
    UNION
    SELECT
        'High Salary' as category,
        0 as accounts_count
    UNION
    SELECT
        'Average Salary' as category,
        0 as accounts_count
    UNION
    SELECT
        'Low Salary' as category,
        0 as accounts_count
)
SELECT category,
    SUM(accounts_count) as accounts_count
    FROM cte
    GROUP BY category
