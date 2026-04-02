# SLA Compliance Definition

## Objective
Define the KPI logic for SLA compliance analysis.

## Business Rule
A ticket meets SLA only when both main SLA controls are respected:

- assignment_sla_breached = 0
- action_sla_breached = 0

## KPI Logic
A ticket is SLA compliant only if:

- assignment_sla_breached = 0
- action_sla_breached = 0

If one or both values are 1, the ticket is non-compliant.

## Notes
- This KPI gives a full SLA view.
- A ticket must pass both SLA checks to be counted as compliant.
- Tickets with null SLA flags should be reviewed before calculation.
- Status filtering will be validated before the final SQL query if needed.