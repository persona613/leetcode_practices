/*
495 ms runtime beats 66.28%
0 MB memory beats 100%
*/
# Write your MySQL query statement below
SELECT name, population, area FROM World
    WHERE area>=3000000 or population>=25000000