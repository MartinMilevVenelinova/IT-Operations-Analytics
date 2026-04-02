# SLA Compliance Results

## Objective
Summarize the main SQL results for SLA compliance analysis.

## Overall SLA Compliance
The overall SLA compliance rate is **79.18%**.

### Main values
- Total tickets: 70,985
- SLA compliant tickets: 56,204
- SLA non-compliant tickets: 14,781

## SLA Compliance by Priority

| Priority ID | Total Tickets | SLA Compliant Tickets | SLA Non-Compliant Tickets | SLA Compliance Rate (%) |
|------------|---------------:|----------------------:|--------------------------:|------------------------:|
| 1 | 3,307 | 2,594 | 713 | 78.44 |
| 2 | 8,733 | 6,996 | 1,737 | 80.11 |
| 3 | 17,013 | 13,447 | 3,566 | 79.04 |
| 4 | 31,946 | 25,363 | 6,583 | 79.39 |
| 5 | 9,986 | 7,804 | 2,182 | 78.15 |

## Main Findings
- SLA compliance is stable across all priority levels.
- The best result is in priority 2 with 80.11%.
- The lowest result is in priority 5 with 78.15%.
- The difference between the highest and lowest result is small.
- Overall, the support operation shows consistent SLA performance.

## KPI Rule Used
A ticket is SLA compliant only if:
- assignment_sla_breached = 0
- action_sla_breached = 0