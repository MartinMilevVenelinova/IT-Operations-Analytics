# Escalations and Reopens Definition

## Objective
Define the KPI logic for escalation and reopen analysis.

## Analysis Scope
The escalation and reopen analysis will include all tickets in the final dataset.

This includes:
- escalated tickets
- non-escalated tickets
- reopened tickets
- non-reopened tickets

This scope allows full comparison between different ticket behaviors.

## Main KPI
The first KPI is escalation rate.

### Definition
Escalation rate is the percentage of tickets that were escalated.

A ticket is considered escalated if:
- escalated_flag = 1

### Formula
Escalation Rate (%) = (number of escalated tickets / total number of tickets) * 100

## Second KPI
The second KPI is reopen rate.

### Definition
Reopen rate is the percentage of tickets that were reopened after being resolved.

A ticket is considered reopened if:
- reopened_flag = 1

### Formula
Reopen Rate (%) = (number of reopened tickets / total number of tickets) * 100

## Third KPI
The third KPI is wrong escalation rate.

### Definition
Wrong escalation rate is the percentage of escalated tickets that were sent to the wrong support group.

A ticket is considered a wrong escalation if:
- wrong_escalation_flag = 1

### Formula
Wrong Escalation Rate (%) = (number of wrong escalations / number of escalated tickets) * 100

## Fourth KPI
The fourth KPI is escalation return rate.

### Definition
Escalation return rate is the percentage of escalated tickets that were returned to the previous support group.

A ticket is considered returned if:
- escalation_returned_flag = 1

### Formula
Escalation Return Rate (%) = (number of returned escalations / number of escalated tickets) * 100