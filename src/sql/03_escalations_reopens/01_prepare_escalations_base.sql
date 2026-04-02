-- File: 01_prepare_escalations_base.sql
-- Objective: Prepare the base dataset for escalation and reopen analysis

SELECT
    t.ticket_id AS ticket_id,
    t.escalated_flag AS escalated_flag,
    t.reopened_flag AS reopened_flag,
    t.wrong_escalation_flag AS wrong_escalation_flag,
    t.escalation_returned_flag AS escalation_returned_flag
FROM tickets_final t
WHERE t.escalated_flag IS NOT NULL
  AND t.reopened_flag IS NOT NULL;