/*
511 ms runtime beats 34.07%
*/
# Write your MySQL query statement below
with ptime as (  
    SELECT st.machine_id, st.process_id, 
        nd.timestamp-st.timestamp as 'per_time' 
        FROM Activity st
        JOIN Activity nd
        ON st.machine_id=nd.machine_id 
        AND st.process_id=nd.process_id 
        AND st.activity_type='start' AND nd.activity_type='end'
)
SELECT machine_id, 
    ROUND(SUM(per_time)/COUNT(machine_id), 3) as 'processing_time' 
    FROM ptime
    GROUP BY machine_id
