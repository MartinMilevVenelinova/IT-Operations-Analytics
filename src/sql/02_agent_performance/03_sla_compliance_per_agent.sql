-- File: 03_sla_compliance_per_agent.sql
-- Objective: Calculate SLA compliance rate per agent

WITH agent_base AS (
    SELECT
        t.ticket_id AS ticket_id,
        t.assigned_agent_id AS assigned_agent_id,
        CASE
            WHEN t.assignment_sla_breached = 0
             AND t.action_sla_breached = 0 THEN 1
            ELSE 0
        END AS sla_compliant_flag
    FROM tickets_final t
    WHERE t.assigned_agent_id IS NOT NULL
      AND t.status IN ('Resolved', 'Closed')
      AND t.assignment_sla_breached IS NOT NULL
      AND t.action_sla_breached IS NOT NULL
)

SELECT
    assigned_agent_id,
    COUNT(ticket_id) AS total_completed_tickets,
    SUM(sla_compliant_flag) AS sla_compliant_tickets,
    COUNT(ticket_id) - SUM(sla_compliant_flag) AS sla_non_compliant_tickets,
    ROUND(100.0 * SUM(sla_compliant_flag) / COUNT(ticket_id), 2) AS sla_compliance_rate_pct
FROM agent_base
GROUP BY assigned_agent_id
ORDER BY sla_compliance_rate_pct DESC, assigned_agent_id;