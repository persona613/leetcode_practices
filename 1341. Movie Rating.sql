/*
3280 ms runtime beats 12.84%
*/
# Write your MySQL query statement below

-- user name
with cte1 as (
SELECT 
    r.user_id,
    u.name,
    Count(r.user_id) as cnt
FROM MovieRating r
JOIN Users u
ON r.user_id=u.user_id
GROUP BY user_id
ORDER BY cnt DESC, u.name
LIMIT 1
),

-- movie name
cte2 as (
SELECT
    r.movie_id,
    r.rating,
    r.created_at,
    AVG(r.rating) art,
    m.title
FROM MovieRating r
JOIN Movies m
ON r.movie_id=m.movie_id
WHERE
    DATE_FORMAT(r.created_at, '%Y-%m') = '2020-02'
GROUP BY r.movie_id
ORDER BY art DESC, m.title
LIMIT 1
)

SELECT name as results
FROM cte1
UNION ALL
SELECT title as results
FROM cte2