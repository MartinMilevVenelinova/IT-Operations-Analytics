-- File: 01_prepare_agent_base.sql
-- Objective: Prepare the base dataset for agent performance analysis

SELECT
    t.ticket_id AS ticket_id,
    t.assigned_agent_id AS assigned_agent_id,
    t.status AS status,
    t.time_to_resolution_min AS time_to_resolution_min,
    t.assignment_sla_breached AS assignment_sla_breached,
    t.action_sla_breached AS action_sla_breached,
    CASE
        WHEN t.assignment_sla_breached = 0
         AND t.action_sla_breached = 0 THEN 1
        ELSE 0
    END AS sla_compliant_flag
FROM tickets_final t
WHERE t.assigned_agent_id IS NOT NULL
  AND t.status IN ('Resolved', 'Closed')
  AND t.time_to_resolution_min IS NOT NULL
  AND t.assignment_sla_breached IS NOT NULL
  AND t.action_sla_breached IS NOT NULL;