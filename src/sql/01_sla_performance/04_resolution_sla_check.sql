-- File: 04_prepare_sla_base.sql
-- Objective: Prepare base dataset to analyze SLA compliance

SELECT
    t.ticket_id AS Ticket_ID,
    t.priority_id AS Priority_ID,
    t.status AS Status,
    t.time_to_resolution_min AS Resolution_Time_Min,
    s.resolution_sla_target_min AS SLA_Target_Min,

    -- SLA flag
    CASE 
        WHEN t.time_to_resolution_min <= s.resolution_sla_target_min THEN 'Met'
        ELSE 'Breached'
    END AS SLA_Status

FROM tickets_final t
LEFT JOIN sla_targets s
    ON t.priority_id = s.priority_id

WHERE
    t.time_to_resolution_min IS NOT NULL
    AND t.priority_id IS NOT NULL
    AND t.status IN ('Resolved', 'Closed');