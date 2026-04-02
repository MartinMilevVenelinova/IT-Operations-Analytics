# Agent Performance Results

## Objective
Summarize the main SQL results for agent performance analysis.

## KPI 1 - Ticket Volume per Agent

| Agent ID | Completed Tickets |
|---------:|------------------:|
| 1 | 7484 |
| 2 | 6795 |
| 3 | 6013 |
| 6 | 5975 |
| 4 | 5963 |
| 5 | 5939 |
| 7 | 5699 |
| 11 | 5398 |
| 8 | 5346 |
| 12 | 5199 |
| 9 | 5047 |
| 10 | 4779 |

## KPI 2 - SLA Compliance per Agent

| Agent ID | Total Completed Tickets | SLA Compliant Tickets | SLA Non-Compliant Tickets | SLA Compliance Rate (%) |
|---------:|------------------------:|----------------------:|--------------------------:|------------------------:|
| 1 | 7484 | 6713 | 771 | 89.70 |
| 2 | 6795 | 5902 | 893 | 86.86 |
| 4 | 5963 | 4865 | 1098 | 81.59 |
| 3 | 6013 | 4895 | 1118 | 81.41 |
| 5 | 5939 | 4806 | 1133 | 80.92 |
| 6 | 5975 | 4716 | 1259 | 78.93 |
| 7 | 5699 | 4484 | 1215 | 78.68 |
| 8 | 5346 | 4132 | 1214 | 77.29 |
| 11 | 5398 | 4043 | 1355 | 74.90 |
| 9 | 5047 | 3674 | 1373 | 72.80 |
| 12 | 5199 | 3643 | 1556 | 70.07 |
| 10 | 4779 | 3252 | 1527 | 68.05 |

## KPI 3 - Average Resolution Time per Agent

| Agent ID | Total Completed Tickets Used | Avg Resolution Time (min) |
|---------:|-----------------------------:|--------------------------:|
| 2 | 6795 | 837.92 |
| 1 | 7484 | 841.31 |
| 6 | 5975 | 846.36 |
| 5 | 5939 | 848.61 |
| 9 | 5047 | 851.08 |
| 3 | 6013 | 861.29 |
| 4 | 5963 | 869.97 |
| 8 | 5345 | 872.37 |
| 7 | 5699 | 899.91 |
| 11 | 5398 | 912.05 |
| 10 | 4779 | 933.66 |
| 12 | 5198 | 937.90 |

## Main Findings
- Agent 1 has the highest completed ticket volume.
- Agent 10 has the lowest completed ticket volume.
- Agent 1 has the best SLA compliance rate at 89.70%.
- Agent 10 has the lowest SLA compliance rate at 68.05%.
- Agent 2 has the fastest average resolution time.
- Agent 12 has the slowest average resolution time.

## Data Notes
- The average resolution time KPI uses only tickets with non-null `time_to_resolution_min`.
- Because of this, agent 8 and agent 12 have one less ticket in the speed KPI than in the volume KPI.