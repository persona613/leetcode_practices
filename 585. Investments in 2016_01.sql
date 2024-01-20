/*
Wrong Answer
1 / 19 testcases passed
*/
# Write your MySQL query statement below

-- pid for Same tiv_2015
SELECT
    # pid,
    SUM(tiv_2016) as tiv_2016
FROM Insurance
WHERE
    tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
    )
    AND
    pid NOT IN (
    SELECT l.pid
    FROM Insurance l
    JOIN Insurance r
    WHERE l.lat=r.lat AND l.lon=r.lon AND l.pid!=r.pid
    )

-- pif for distinc loc
# SELECT
#     pid
# FROM Insurance
# WHERE pid NOT IN (
#     SELECT l.pid
#     FROM Insurance l
#     JOIN Insurance r
#     WHERE l.lat=r.lat AND l.lon=r.lon AND l.pid!=r.pid
#     )
