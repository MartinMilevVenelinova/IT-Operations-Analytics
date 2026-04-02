-- File: 03_reopen_rate.sql
-- Objective: Calculate reopen rate

SELECT
    COUNT(ticket_id) AS total_tickets,
    SUM(reopened_flag) AS reopened_tickets,
    COUNT(ticket_id) - SUM(reopened_flag) AS non_reopened_tickets,
    ROUND(100.0 * SUM(reopened_flag) / COUNT(ticket_id), 2) AS reopen_rate_pct
FROM tickets_final
WHERE reopened_flag IS NOT NULL;