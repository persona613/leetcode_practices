/*
1402 ms runtime beats 10.19%
*/
# Write your MySQL query statement below
select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1