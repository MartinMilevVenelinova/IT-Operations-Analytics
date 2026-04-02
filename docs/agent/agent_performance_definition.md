# Agent Performance Definition

## Objective
Define the KPI logic for agent performance analysis.

## Analysis Scope
The agent performance analysis will include tickets that:

- have an assigned agent
- have a final status such as Resolved or Closed

This scope helps measure agent performance on completed work only.

## Main KPI
The first KPI is ticket volume per agent.

### Definition
Ticket volume per agent means the number of completed tickets assigned to each agent.

This KPI helps identify workload distribution across the team.

## Second KPI
The second KPI is SLA compliance per agent.

### Definition
SLA compliance per agent means the percentage of completed tickets assigned to an agent that meet SLA.

A ticket is SLA compliant only if:
- assignment_sla_breached = 0
- action_sla_breached = 0

This KPI helps compare service quality across agents.

## Third KPI
The third KPI is average resolution time per agent.

### Definition
Average resolution time per agent means the average value of `time_to_resolution_min` for completed tickets assigned to each agent.

This KPI helps compare speed across agents.

## Notes
- Agent performance should be reviewed with more than one KPI.
- High ticket volume does not always mean better performance.
- SLA compliance and resolution time must be analyzed together.
- Tickets without assigned agents should be excluded from this analysis.
- Only completed tickets should be included in the main agent performance KPIs.