/*
1083 ms runtime beats 56.74%
*/
# Write your MySQL query statement below
select name as Customers
from Customers
where id not in (
    select customerId
    from Orders
)