# IT Operations Analytics & SLA Monitoring Platform

## 1. Visión general

Este proyecto simula una operación real de soporte IT con alto volumen
de incidencias y gestión de SLA.

El objetivo es construir un dataset realista basado en mi experiencia en
soporte técnico para analizar:

-   Cumplimiento de SLA
-   Rendimiento de agentes
-   Calidad de escalados
-   Eficiencia operativa
-   Experiencia de usuario

## 2. Modelo de datos

He diseñado un modelo relacional inspirado en sistemas reales.

### Tabla principal

-   tickets → incidencias

### Dimensiones

-   agents
-   categories
-   channels
-   support_groups
-   shifts
-   sla_targets

### Eventos

-   status_history
-   ticket_reopens
-   user_claims
-   escalation_returns

## 3. Lógica de negocio

SLA de asignación → desde creación hasta asignación\
SLA de acción → desde creación hasta resolución o escalado

## 4. Realismo

Incluye: - Incumplimientos - Outliers - Escalados incorrectos -
Reaperturas - Reclamaciones

## 5. Volumen

-   \~70k tickets/año
-   12 agentes

## 6. Uso de IA

Se ha usado IA para generar datos y simular escenarios, pero el diseño y
validación han sido realizados por mí.
