/*
1123 ms runtime beats 45.93%
*/
# Write your MySQL query statement below
SELECT date_format(trans_date, '%Y-%m') as month,
    country,
    Count(*) as trans_count,
    SUM(state='approved') as approved_count,
    SUM(amount) as trans_total_amount,
    SUM(if(state='approved',amount,0)) as approved_total_amount
    FROM Transactions t
    GROUP BY month, country
