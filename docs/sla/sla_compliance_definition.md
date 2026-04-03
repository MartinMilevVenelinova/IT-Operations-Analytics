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

## Technical Logic
The SLA compliance flag can be calculated with this rule:

```sql
CASE
    WHEN assignment_sla_breached = 0
     AND action_sla_breached = 0 THEN 1
    ELSE 0
END
```

### Importante
Esto **no es todavía la query final**.  
Solo es la regla técnica que vamos a reutilizar luego.

### Comando a ejecutar
Ninguno obligatorio en este paso.  
Solo guardar el archivo en VS Code.

### Qué output debes esperar
Al terminar, tu archivo `docs/sla_compliance_definition.md` tendrá ya:

- la definición de negocio
- la lógica KPI
- las notas
- la lógica técnica base en SQL

### Qué documentar luego en la GitHub issue
Guárdate esta nota para después:

```md
Added the technical CASE logic that will be used to calculate the SLA compliance flag in SQL.
```