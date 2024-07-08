/*
Wrong Answer
14 / 21 testcases passed
submitted at May 28, 2024 20:16
*/
# Write your MySQL query statement below
select name
from SalesPerson
where sales_id not in(
    select sales_id
    from Orders
    where com_id=1
    )