# EDA Visualizations

This document presents the main visual insights from the exploratory data analysis.

---

## Ticket volume by priority

![Ticket Volume](../../reports/visuals/ticket_volume_by_priority.png)

- Most tickets are concentrated in medium priority levels.
- Priority 4 represents the largest workload segment.
- High priority tickets are less frequent.

---

## Resolution time by priority

![Resolution by Priority](../../reports/visuals/resolution_time_by_priority.png)

- Resolution time varies across all priority levels.
- No strong difference between priorities in terms of median.
- High variability suggests other influencing factors.

---

## Ticket status distribution

![Status Distribution](../../reports/visuals/ticket_status_distribution.png)

- Most tickets are completed (Closed or Resolved).
- Cancelled tickets are minimal.
- The support process appears stable.

---

## Resolution time distribution (filtered)

![Resolution Distribution](../../reports/visuals/resolution_time_distribution_filtered.png)

- Most tickets are resolved within a consistent time range.
- Distribution is right-skewed.
- Extreme values distort the full distribution.

---

## Resolution time outliers

![Outliers Full](../../reports/visuals/resolution_time_outliers_full.png)

- A significant number of extreme values exist.
- These outliers impact SLA metrics.

---

## Resolution time core distribution

![Core Distribution](../../reports/visuals/resolution_time_core_distribution.png)

- Filtering reveals the true operational behavior.
- Most tickets follow a consistent resolution pattern.