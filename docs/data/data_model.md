# IT Operations Analytics & SLA Monitoring Platform

## 1. Overview

This project simulates a real-world IT Service Desk operation with high
ticket volume and SLA management.

The goal is to build a realistic dataset based on my experience in IT
support, in order to analyze:

-   SLA compliance
-   Agent performance
-   Escalation quality
-   Operational efficiency
-   User experience (reopens, claims)

The dataset represents around one year of activity in a corporate
environment.

## 2. Data Model Design

I designed a relational model inspired by real ticketing systems.

### Core Table

-   tickets → represents each incident or request.

### Dimensions

-   agents → support agents with different performance levels
-   categories → classification of tickets
-   channels → entry channel (phone, portal, email...)
-   support_groups → IT teams (N1, N2, N3)
-   shifts → working shifts
-   sla_targets → SLA definitions by priority

### Event Tables

-   status_history → ticket lifecycle
-   ticket_reopens → reopen events
-   user_claims → user complaints
-   escalation_returns → returned escalations

## 3. Business Logic

### SLA Assignment

Time between ticket creation and assignment.

### SLA Action

Time between creation and first action (resolve or escalate).

A breach happens when real time exceeds SLA target.

## 4. Realism

The dataset includes:

-   SLA breaches
-   Outliers
-   Wrong escalations
-   Missing data
-   Reopens
-   Claims

## 5. Volume

-   \~70k tickets/year
-   \~200 per day
-   12 agents

## 6. Use Cases

-   SLA analysis
-   Agent performance
-   Escalation quality
-   Ticket lifecycle
-   Channel comparison

## 7. AI Usage

AI was used to help generate data at scale and simulate scenarios.

However, all design decisions, business logic and validation were done
by me.
