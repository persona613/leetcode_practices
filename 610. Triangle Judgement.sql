/*
450 ms runtime beats 79.49%
*/
# Write your MySQL query statement below
SELECT *,
    CASE
        WHEN x+y>z AND y+z>x
            AND z+x>y THEN 'Yes'
        ELSE 'No'
        END AS triangle
    FROM Triangle