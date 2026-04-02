-- File: 01_prepare_sla_base.sql
-- Objective: Prepare the base dataset for SLA compliance analysis

SELECT
    t.ticket_id AS ticket_id,
    t.priority_id AS priority_id,
    t.status AS status,
    t.assignment_sla_breached AS assignment_sla_breached,
    t.action_sla_breached AS action_sla_breached,
    CASE
        WHEN t.assignment_sla_breached = 0
         AND t.action_sla_breached = 0 THEN 1
        ELSE 0
    END AS sla_compliant_flag
FROM tickets_final t
WHERE t.assignment_sla_breached IS NOT NULL
  AND t.action_sla_breached IS NOT NULL;