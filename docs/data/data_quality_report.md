# Data Quality Report

## 1. Data Loading Issues

### Problem
CSV files were not loaded correctly due to incorrect delimiter and encoding.

### Impact
- All data was initially loaded as a single column.
- Data could not be analyzed.

### Solution
- Updated data loading using:
  - sep=";"
  - encoding="utf-8-sig"

---

## 2. Data Type Issues

### Problem
Several columns are stored as `object` instead of proper types:
- Date columns (created_at, assigned_at, etc.)
- Some numeric fields

### Impact
- Cannot perform time calculations
- Risk of incorrect analysis

---

## 3. Missing Values

### Tickets Table

- assigned_at → 285 missing
- resolved_at → 1350 missing
- closed_at → 162 missing

### Interpretation
- Tickets not yet assigned, resolved or closed

---

## 4. Escalation Data

### Problem
- escalated_group_id → many missing values
- correct_target_group_id → many missing values

### Interpretation
- Not all tickets are escalated (expected behavior)

---

## 5. Status History

### Problem
- changed_by_agent_id has many null values

### Interpretation
- Likely system-generated status changes

---

## 6. Agents Table

### Problem
- active_to is null for all agents

### Interpretation
- Agents are currently active

---

## Conclusion

The dataset is structurally consistent but requires:
- Data type corrections
- Date parsing
- Business logic validation for null values