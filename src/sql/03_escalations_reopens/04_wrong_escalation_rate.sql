-- File: 04_wrong_escalation_rate.sql
-- Objective: Calculate wrong escalation rate

SELECT
    SUM(escalated_flag) AS escalated_tickets,
    SUM(wrong_escalation_flag) AS wrong_escalations,
    SUM(escalated_flag) - SUM(wrong_escalation_flag) AS correct_escalations,
    ROUND(100.0 * SUM(wrong_escalation_flag) / SUM(escalated_flag), 2) AS wrong_escalation_rate_pct
FROM tickets_final
WHERE escalated_flag IS NOT NULL
  AND wrong_escalation_flag IS NOT NULL;