-- File: 03_sla_compliance_by_priority.sql
-- Objective: Calculate SLA compliance rate by priority

WITH sla_base AS (
    SELECT
        t.ticket_id AS ticket_id,
        t.priority_id AS priority_id,
        t.assignment_sla_breached AS assignment_sla_breached,
        t.action_sla_breached AS action_sla_breached,
        CASE
            WHEN t.assignment_sla_breached = 0
             AND t.action_sla_breached = 0 THEN 1
            ELSE 0
        END AS sla_compliant_flag
    FROM tickets_final t
    WHERE t.assignment_sla_breached IS NOT NULL
      AND t.action_sla_breached IS NOT NULL
)

SELECT
    priority_id,
    COUNT(*) AS total_tickets,
    SUM(sla_compliant_flag) AS sla_compliant_tickets,
    COUNT(*) - SUM(sla_compliant_flag) AS sla_non_compliant_tickets,
    ROUND(100.0 * SUM(sla_compliant_flag) / COUNT(*), 2) AS sla_compliance_rate_pct
FROM sla_base
GROUP BY priority_id
ORDER BY priority_id;