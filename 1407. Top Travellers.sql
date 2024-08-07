/*
2203 ms runtime beats 13.89%
*/
# Write your MySQL query statement below
select
    name,
    ifnull(sum(r.distance), 0) as travelled_distance
from Users as u
left join Rides as r
on u.id = r.user_id
group by r.user_id
order by travelled_distance desc, name asc