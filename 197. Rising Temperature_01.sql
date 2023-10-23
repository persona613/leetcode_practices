/*
Wrong Answer
7 / 14 testcases passed
Editorial
Input
Weather =
| id | recordDate | temperature |
| -- | ---------- | ----------- |
| 1  | 2000-12-16 | 3           |
| 2  | 2000-12-15 | -1          |

Use Testcase
Output
| id |
| -- |
Expected
| id |
| -- |
| 1  |
*/
# Write your MySQL query statement below
SELECT cur.id FROM Weather cur
    JOIN Weather pre
    ON cur.id=pre.id+1
    WHERE cur.temperature>pre.temperature