-- File: 02_ticket_volume_per_agent.sql
-- Objective: Calculate completed ticket volume per agent

WITH agent_base AS (
    SELECT
        t.ticket_id AS ticket_id,
        t.assigned_agent_id AS assigned_agent_id
    FROM tickets_final t
    WHERE t.assigned_agent_id IS NOT NULL
      AND t.status IN ('Resolved', 'Closed')
)

SELECT
    assigned_agent_id,
    COUNT(ticket_id) AS completed_ticket_count
FROM agent_base
GROUP BY assigned_agent_id
ORDER BY completed_ticket_count DESC, assigned_agent_id;