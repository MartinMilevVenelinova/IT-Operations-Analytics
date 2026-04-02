-- File: 05_escalation_return_rate.sql
-- Objective: Calculate escalation return rate

SELECT
    SUM(escalated_flag) AS escalated_tickets,
    SUM(escalation_returned_flag) AS returned_escalations,
    SUM(escalated_flag) - SUM(escalation_returned_flag) AS not_returned_escalations,
    ROUND(100.0 * SUM(escalation_returned_flag) / SUM(escalated_flag), 2) AS escalation_return_rate_pct
FROM tickets_final
WHERE escalated_flag IS NOT NULL
  AND escalation_returned_flag IS NOT NULL;