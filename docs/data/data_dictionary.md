# Data Dictionary

## Overview

This project contains several tables related to IT operations and ticket management.

---

## 1. Tickets

Main table containing all ticket information.

| Column | Description | Type |
|--------|------------|------|
| ticket_id | Unique ticket identifier | int |
| ticket_code | Ticket code | string |
| created_at | Ticket creation timestamp | datetime |
| assigned_at | Assignment timestamp | datetime |
| first_response_at | First response timestamp | datetime |
| resolved_at | Resolution timestamp | datetime |
| closed_at | Closing timestamp | datetime |
| status | Current status of the ticket | string |
| priority_id | Priority level | int |
| category_id | Ticket category | int |
| channel_id | Channel used | int |
| assigned_agent_id | Assigned agent | int |
| opened_group_id | Initial support group | int |
| escalated_flag | Indicates if ticket was escalated | int |
| escalated_group_id | Escalated group | int |
| correct_target_group_id | Correct group for escalation | int |
| wrong_escalation_flag | Incorrect escalation flag | int |
| escalation_returned_flag | Escalation returned flag | int |
| missing_minimum_data_flag | Missing data flag | int |
| reopened_flag | Indicates if ticket was reopened | int |
| reopen_count | Number of reopens | int |
| user_claim_count | Number of user complaints | int |
| assignment_sla_target_min | SLA for assignment | int |
| action_sla_target_min | SLA for action | int |
| assignment_minutes | Time to assign | float |
| first_response_minutes | Time to first response | float |
| action_minutes | Time to action | float |
| total_duration_minutes | Total duration | float |
| assignment_sla_breached | SLA breach flag | int |
| action_sla_breached | SLA breach flag | int |

---

## 2. Agents

Information about support agents.

| Column | Description | Type |
|--------|------------|------|
| agent_id | Unique agent ID | int |
| agent_code | Agent code | string |
| agent_name | Agent name | string |
| email | Agent email | string |
| shift_id | Shift assigned | int |
| primary_group_id | Main support group | int |
| experience_level | Experience level | string |
| productivity_factor | Productivity factor | float |
| speed_factor | Speed factor | float |
| quality_risk_factor | Quality risk | float |
| active_from | Start date | datetime |
| active_to | End date (null if active) | datetime |
| is_active | Active flag | int |

---

## 3. Categories

Ticket categories and subcategories.

---

## 4. Channels

Communication channels.

---

## 5. SLA Targets

SLA definitions based on priority.

---

## 6. Status History

Track of status changes for each ticket.

---

## 7. Escalation Returns

Information about incorrect escalations.

---

## 8. Ticket Reopens

Reopened tickets tracking.

---

## 9. User Claims

User complaints or repeated contacts.