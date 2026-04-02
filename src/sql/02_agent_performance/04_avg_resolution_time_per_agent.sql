-- File: 04_avg_resolution_time_per_agent.sql
-- Objective: Calculate average resolution time per agent

WITH agent_base AS (
    SELECT
        t.ticket_id AS ticket_id,
        t.assigned_agent_id AS assigned_agent_id,
        t.time_to_resolution_min AS time_to_resolution_min
    FROM tickets_final t
    WHERE t.assigned_agent_id IS NOT NULL
      AND t.status IN ('Resolved', 'Closed')
      AND t.time_to_resolution_min IS NOT NULL
)

SELECT
    assigned_agent_id,
    COUNT(ticket_id) AS total_completed_tickets,
    ROUND(AVG(time_to_resolution_min), 2) AS avg_resolution_time_min
FROM agent_base
GROUP BY assigned_agent_id
ORDER BY avg_resolution_time_min ASC, assigned_agent_id;