/*
Wrong Answer
17 / 18 testcases passed
submitted at May 28, 2024 21:12
*/
# Write your MySQL query statement below
select
    name,
    ifnull(sum(r.distance), 0) as travelled_distance
from Users as u
left join Rides as r
on u.id = r.user_id
group by u.name
order by travelled_distance desc, name asc