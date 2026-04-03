# KPI Framework

## 1. Purpose

The purpose of this document is to define the key performance indicators (KPIs) used to measure the performance of an IT support operation.

This framework is designed to:
- Provide a clear business understanding of performance
- Support dashboard design (Power BI)
- Ensure consistency across metrics
- Avoid misleading or vanity metrics
- Align KPIs with real IT service management practices

---

## 2. KPI Design Principles

All KPIs in this project follow these principles:

- Business relevance: KPIs must reflect real operational performance
- Clarity: Definitions must be simple and easy to understand
- Consistency: Same logic must be applied across all KPIs
- Actionability: KPIs must help decision making
- Data alignment: KPIs must match the available data model
- Comparability: KPIs should allow comparison across agents, priorities, and time

---

## 3. KPI Areas

KPIs are grouped into four main business areas:

### 3.1 Service Level KPIs
Measure SLA performance and response/resolution efficiency.

### 3.2 Agent Performance KPIs
Measure productivity and performance of support agents.

### 3.3 Ticket Flow and Quality KPIs
Measure process quality, escalations, and rework.

### 3.4 Workload and Demand Metrics (Context Metrics)
These metrics are not performance KPIs.

They provide context to understand workload, demand, and distribution of tickets.

They should always be analyzed together with performance KPIs.

---

## 4. KPI Definition Template

Each KPI follows this structure:

- Business area  
- Definition  
- Business meaning  
- Formula  
- Source tables / fields  
- Recommended dimensions  
- Interpretation  
- Important notes / limitations  

---

## 5. KPI Catalog

---

### 5.1 Service Level KPIs

#### KPI 1 — SLA Compliance Rate

**Business area:** Service Level  

**Definition:**  
Percentage of tickets that meet both assignment SLA and action SLA.

**Business meaning:**  
Measures overall SLA performance of the support operation.

**Formula:**  
SLA Compliance Rate = SLA Compliant Tickets / Total Tickets

**Source tables / fields:**  
- tickets_final.csv  
- assignment_sla_breached  
- action_sla_breached  

**Recommended dimensions:**  
- priority_id  
- support_group  
- date  
- agent_id  

**Interpretation:**  
Higher is better.

**Important notes / limitations:**  
Does not explain root causes of SLA breaches.

---

#### KPI 2 — Assignment SLA Breach Rate

**Business area:** Service Level  

**Definition:**  
Percentage of tickets where assignment SLA was breached.

**Business meaning:**  
Measures how quickly tickets are picked up.

**Formula:**  
Breached Assignments / Total Tickets

**Interpretation:**  
Lower is better.

---

#### KPI 3 — Action SLA Breach Rate

**Business area:** Service Level  

**Definition:**  
Percentage of tickets where action SLA was breached.

**Business meaning:**  
Measures delays in resolution or escalation.

**Formula:**  
Breached Actions / Total Tickets

**Interpretation:**  
Lower is better.

---

#### KPI 4 — Average Time to First Response

Use with caution (sensitive to outliers)

**Formula:**  
AVG(time_to_first_response_min)

---

#### KPI 5 — Average Time to Resolution

Use with caution (sensitive to outliers)

**Formula:**  
AVG(time_to_resolution_min)

---

#### KPI 6 — Median Time to Resolution

Recommended main KPI

**Business meaning:**  
More reliable measure of resolution performance.

**Formula:**  
MEDIAN(time_to_resolution_min)

---

#### KPI 7 — SLA Breach Distribution

**Business area:** Service Level  

**Definition:**  
Distribution of SLA breaches by priority.

**Business meaning:**  
Helps identify where SLA issues are concentrated.

---

---

### 5.2 Agent Performance KPIs

#### KPI 8 — Completed Tickets per Agent

**Business meaning:**  
Measures workload and productivity.

---

#### KPI 9 — SLA Compliance per Agent

**Business meaning:**  
Measures quality of work per agent.

---

#### KPI 10 — Median Resolution Time per Agent

**Business meaning:**  
More robust than average for agent comparison.

---

#### KPI 11 — Workload vs Performance Index

HIGH VALUE KPI

**Definition:**  
Compares workload and SLA performance per agent.

**Business meaning:**  
Detects overperforming and underperforming agents.

**Interpretation:**  
- High volume + high SLA → top performer  
- High volume + low SLA → overloaded  
- Low volume + low SLA → low efficiency  

---

---

### 5.3 Ticket Flow and Quality KPIs

#### KPI 12 — Escalation Rate

**Formula:**  
Escalated Tickets / Total Tickets  

---

#### KPI 13 — Wrong Escalation Rate

**Formula:**  
Wrong Escalations / Total Escalations  

---

#### KPI 14 — Escalation Return Rate

**Formula:**  
Returned Escalations / Total Escalations  

---

#### KPI 15 — Reopen Rate

**Formula:**  
Reopened Tickets / Total Tickets  

---

#### KPI 16 — Rework Rate (NEW)

VERY IMPORTANT KPI

**Definition:**  
Measures total rework in the system.

**Formula:**  
(Reopened Tickets + Returned Escalations) / Total Tickets  

**Business meaning:**  
Shows inefficiencies and repeated work.

---

---

### 5.4 Workload and Demand Metrics (Context Metrics)

These are not performance KPIs.

They provide context and must be analyzed together with KPIs.

#### Metric — Ticket Volume

#### Metric — Ticket Volume by Priority

#### Metric — Ticket Volume by Channel

#### Metric — Ticket Volume by Category

---

## 6. KPI Dimensions and Filters

- Date (day, week, month)
- Priority
- Agent
- Support group
- Channel
- Category
- Status

---

## 7. KPI Usage Notes for Power BI

- Use slicers for time and priority
- Combine KPIs with volume metrics
- Prefer median over average when needed
- Separate operational vs strategic views

---

## 8. Business Interpretation Guidelines

- Do not analyze KPIs in isolation
- Combine workload and performance
- Compare similar agents
- Investigate outliers
- Use trends over time

---

## 9. KPI Limitations

- Does not include ticket complexity
- SLA does not equal user satisfaction
- Outliers affect averages
- Simulated dataset (realistic but synthetic)