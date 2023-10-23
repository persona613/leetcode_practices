/*
1161 ms runtime beats 67.11%
*/
# Write your MySQL query statement below
SELECT  tweet_id FROM Tweets
    WHERE CHAR_LENGTH(content)>15;