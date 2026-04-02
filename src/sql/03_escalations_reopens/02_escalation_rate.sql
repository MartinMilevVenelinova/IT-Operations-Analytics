-- File: 02_escalation_rate.sql
-- Objective: Calculate escalation rate

SELECT
    COUNT(ticket_id) AS total_tickets,
    SUM(escalated_flag) AS escalated_tickets,
    COUNT(ticket_id) - SUM(escalated_flag) AS non_escalated_tickets,
    ROUND(100.0 * SUM(escalated_flag) / COUNT(ticket_id), 2) AS escalation_rate_pct
FROM tickets_final
WHERE escalated_flag IS NOT NULL;