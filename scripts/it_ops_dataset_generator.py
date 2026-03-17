import random
import math
from datetime import datetime, timedelta
from collections import defaultdict
import csv
import os

random.seed(42)

OUTPUT_DIR = os.path.join(os.getcwd(), "it_ops_dataset_output")
YEAR = 2025
NUM_AGENTS = 12
TARGET_TICKETS = 73000

PRIORITIES = [
    {"priority_id": 1, "priority_name": "Critical", "assign_sla_min": 5, "action_sla_min": 15, "weight": 0.03},
    {"priority_id": 2, "priority_name": "High", "assign_sla_min": 10, "action_sla_min": 45, "weight": 0.12},
    {"priority_id": 3, "priority_name": "Medium", "assign_sla_min": 20, "action_sla_min": 120, "weight": 0.25},
    {"priority_id": 4, "priority_name": "Normal", "assign_sla_min": 30, "action_sla_min": 30, "weight": 0.45},
    {"priority_id": 5, "priority_name": "Low", "assign_sla_min": 60, "action_sla_min": 240, "weight": 0.15},
]

CHANNELS = [
    {"channel_id": 1, "channel_name": "Phone", "weight": 0.42},
    {"channel_id": 2, "channel_name": "Portal", "weight": 0.28},
    {"channel_id": 3, "channel_name": "Email", "weight": 0.18},
    {"channel_id": 4, "channel_name": "Chat", "weight": 0.09},
    {"channel_id": 5, "channel_name": "Walk-up", "weight": 0.03},
]

SHIFTS = [
    {"shift_id": 1, "shift_name": "Morning", "start_hour": 7, "end_hour": 15, "weight": 0.35},
    {"shift_id": 2, "shift_name": "Standard", "start_hour": 8, "end_hour": 16, "weight": 0.40},
    {"shift_id": 3, "shift_name": "Late", "start_hour": 10, "end_hour": 18, "weight": 0.25},
]

SUPPORT_GROUPS = [
    {"group_id": 1, "group_name": "N1 Service Desk", "group_type": "L1"},
    {"group_id": 2, "group_name": "Workplace Support", "group_type": "L2"},
    {"group_id": 3, "group_name": "Identity & Access", "group_type": "L2"},
    {"group_id": 4, "group_name": "Network Operations", "group_type": "L2"},
    {"group_id": 5, "group_name": "Business Apps", "group_type": "L2"},
    {"group_id": 6, "group_name": "Infrastructure", "group_type": "L2"},
    {"group_id": 7, "group_name": "Field Support", "group_type": "L2"},
    {"group_id": 8, "group_name": "Security Operations", "group_type": "L2"},
]

CATEGORIES = [
    (1, "Access Management", "Password Reset", 0.14, 0.00, 3),
    (2, "Access Management", "MFA / SSO", 0.08, 0.30, 3),
    (3, "Hardware", "Laptop / Desktop", 0.10, 0.35, 2),
    (4, "Hardware", "Printer / Scanner", 0.07, 0.18, 7),
    (5, "Network", "VPN", 0.10, 0.30, 4),
    (6, "Network", "LAN / WiFi", 0.05, 0.38, 4),
    (7, "Applications", "Microsoft 365", 0.11, 0.27, 5),
    (8, "Applications", "ERP / Internal App", 0.09, 0.42, 5),
    (9, "Telephony", "Softphone / Contact Center", 0.05, 0.22, 5),
    (10, "Security", "Antivirus / Alert", 0.03, 0.55, 8),
    (11, "Accounts", "User Creation / Update", 0.08, 0.16, 3),
    (12, "Monitoring", "Server / Infra Alert", 0.02, 0.68, 6),
    (13, "Remote Access", "VDI / Citrix", 0.04, 0.34, 2),
    (14, "Other", "General Request", 0.04, 0.10, 2),
]

RETURN_REASONS = [
    "Wrong support group",
    "Missing diagnostic evidence",
    "Missing user impact / urgency",
    "Already solved in N1",
    "Insufficient reproduction steps",
    "Wrong categorization",
]

STATUSES_CLOSED = ["Resolved", "Closed"]
FINAL_STATUSES = ["Resolved", "Closed", "Cancelled"]

FIRST_NAMES = ["Daniel", "Laura", "Pablo", "Marta", "Javier", "Sara", "Nerea", "Sergio", "Iván", "Lucía", "Raúl", "Claudia"]
LAST_NAMES = ["García", "Martín", "López", "Santos", "Romero", "Pérez", "Ruiz", "Navarro", "Díaz", "Torres", "Moreno", "Vega"]


def weighted_choice(items, weight_key="weight"):
    weights = [i[weight_key] for i in items]
    return random.choices(items, weights=weights, k=1)[0]


def random_dt_in_day(day):
    hour = random.choices(
        population=[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        weights=[3, 6, 10, 12, 12, 11, 10, 8, 7, 5, 3, 2],
        k=1,
    )[0]
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime(day.year, day.month, day.day, hour, minute, second)


def maybe_null(value, probability=0.0):
    return None if random.random() < probability else value


def minutes_between(start, end):
    if start is None or end is None:
        return None
    return round((end - start).total_seconds() / 60.0, 2)


def format_dt(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S") if dt else ""


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def build_agents():
    agents = []
    performance_profiles = [
        ("top", 1.25, 0.75, 0.85),
        ("strong", 1.15, 0.85, 0.95),
        ("solid", 1.00, 1.00, 1.00),
        ("solid", 1.00, 1.00, 1.00),
        ("solid", 1.00, 1.00, 1.00),
        ("solid", 1.00, 1.05, 1.00),
        ("support", 0.95, 1.05, 1.05),
        ("support", 0.90, 1.10, 1.10),
        ("junior", 0.85, 1.20, 1.20),
        ("junior", 0.80, 1.30, 1.20),
        ("escalation-heavy", 0.92, 1.15, 1.35),
        ("quality-risk", 0.88, 1.25, 1.40),
    ]
    shift_pool = [1,1,1,1,2,2,2,2,2,3,3,3]
    for i in range(NUM_AGENTS):
        first = FIRST_NAMES[i % len(FIRST_NAMES)]
        last = LAST_NAMES[i % len(LAST_NAMES)]
        profile, prod, speed, quality = performance_profiles[i]
        agents.append({
            "agent_id": i + 1,
            "agent_code": f"AG{str(i+1).zfill(3)}",
            "agent_name": f"{first} {last}",
            "email": f"{first.lower()}.{last.lower()}{i+1}@corp.local",
            "shift_id": shift_pool[i],
            "primary_group_id": 1,
            "experience_level": profile,
            "productivity_factor": prod,
            "speed_factor": speed,
            "quality_risk_factor": quality,
            "active_from": f"{YEAR}-01-01",
            "active_to": "",
            "is_active": 1,
        })
    return agents


def build_dimensions():
    categories = []
    for cat_id, cat, subcat, weight, esc_rate, correct_group in CATEGORIES:
        categories.append({
            "category_id": cat_id,
            "category_name": cat,
            "subcategory_name": subcat,
            "ticket_share": weight,
            "expected_escalation_rate": esc_rate,
            "default_target_group_id": correct_group,
        })
    sla_targets = []
    for p in PRIORITIES:
        sla_targets.append({
            "sla_id": p["priority_id"],
            "priority_id": p["priority_id"],
            "priority_name": p["priority_name"],
            "assignment_sla_minutes": p["assign_sla_min"],
            "action_sla_minutes": p["action_sla_min"],
            "business_hours_only": 0,
            "description": f"{p['priority_name']} priority SLA target",
        })
    return categories, sla_targets


def choose_agent(agents):
    return random.choices(agents, weights=[a["productivity_factor"] for a in agents], k=1)[0]


def get_priority_id_for_category(category_name):
    r = random.random()
    if category_name in ["Monitoring", "Security"]:
        if r < 0.30:
            return 1
        if r < 0.65:
            return 2
        if r < 0.90:
            return 3
        return 4
    if category_name in ["Network", "Hardware"]:
        if r < 0.06:
            return 1
        if r < 0.20:
            return 2
        if r < 0.45:
            return 3
        if r < 0.87:
            return 4
        return 5
    if category_name in ["Access Management", "Accounts", "Applications"]:
        if r < 0.02:
            return 1
        if r < 0.12:
            return 2
        if r < 0.35:
            return 3
        if r < 0.85:
            return 4
        return 5
    if r < 0.02:
        return 1
    if r < 0.10:
        return 2
    if r < 0.35:
        return 3
    if r < 0.82:
        return 4
    return 5


def generate_assignment_delay(priority, channel_name, agent):
    sla = priority["assign_sla_min"]
    base = random.gammavariate(2.0, max(1, sla / 5.5))
    if channel_name == "Phone":
        base *= 0.55
    elif channel_name == "Portal":
        base *= 1.05
    elif channel_name == "Email":
        base *= 1.20
    elif channel_name == "Walk-up":
        base *= 0.85
    base *= agent["speed_factor"]
    if random.random() < 0.08:
        base *= random.uniform(2.0, 5.0)
    return round(max(1, base), 2)


def generate_action_delay(priority, escalated, agent, category_row):
    sla = priority["action_sla_min"]
    base = random.gammavariate(2.3, max(2, sla / 4.8))
    if escalated:
        base *= random.uniform(0.8, 1.2)
    else:
        base *= random.uniform(0.85, 1.3)
    if category_row["category_name"] in ["Hardware", "Applications", "Monitoring"]:
        base *= 1.1
    base *= agent["speed_factor"]
    if random.random() < 0.06:
        base *= random.uniform(3.0, 8.0)
    return round(max(2, base), 2)


def generate_resolution_duration(priority, escalated, category_name, reopened_count, claim_count):
    if escalated:
        hours = random.gammavariate(2.2, 7.0)
    else:
        hours = random.gammavariate(2.0, 2.8)
    if category_name in ["Hardware", "Monitoring", "ERP / Internal App"]:
        hours *= 1.25
    if priority["priority_name"] == "Critical":
        hours *= 0.55
    if priority["priority_name"] == "Low":
        hours *= 1.25
    hours *= (1 + reopened_count * 0.18 + claim_count * 0.10)
    if random.random() < 0.025:
        hours *= random.uniform(4.0, 10.0)
    return round(hours * 60, 2)


def main():
    ensure_dir(OUTPUT_DIR)
    agents = build_agents()
    categories, sla_targets = build_dimensions()

    tickets = []
    escalation_returns = []
    ticket_reopens = []
    user_claims = []
    status_history = []

    priority_map = {p["priority_id"]: p for p in PRIORITIES}
    channel_map = {c["channel_id"]: c for c in CHANNELS}
    cat_map = {c["category_id"]: c for c in categories}
    shift_map = {s["shift_id"]: s for s in SHIFTS}

    ticket_id = 1
    status_id = 1
    return_id = 1
    reopen_id = 1
    claim_id = 1

    start_day = datetime(YEAR, 1, 1)
    for day_offset in range(365):
        day = start_day + timedelta(days=day_offset)
        weekday = day.weekday()
        day_base = random.randint(170, 230)
        if weekday == 0:
            day_base += random.randint(10, 25)
        elif weekday >= 5:
            day_base -= random.randint(20, 35)
        for _ in range(day_base):
            created_at = random_dt_in_day(day)
            category = random.choices(categories, weights=[c["ticket_share"] for c in categories], k=1)[0]
            priority = priority_map[get_priority_id_for_category(category["category_name"])]
            channel = weighted_choice(CHANNELS)
            agent = choose_agent(agents)
            shift = shift_map[agent["shift_id"]]

            assignment_delay_min = generate_assignment_delay(priority, channel["channel_name"], agent)
            assigned_at = created_at + timedelta(minutes=assignment_delay_min)
            first_response_delay = max(1, round(assignment_delay_min * random.uniform(0.35, 1.10), 2))
            first_response_at = created_at + timedelta(minutes=first_response_delay)

            escalation_prob = min(0.85, max(0.02, category["expected_escalation_rate"] * random.uniform(0.8, 1.2) * (agent["quality_risk_factor"] * 0.95)))
            escalated = 1 if random.random() < escalation_prob else 0
            action_delay_min = generate_action_delay(priority, escalated, agent, category)
            action_at = assigned_at + timedelta(minutes=action_delay_min)

            wrong_escalation = 0
            escalation_returned = 0
            return_reason = ""
            missing_minimum_data = 0
            escalated_group_id = category["default_target_group_id"] if escalated else ""
            correct_group_id = category["default_target_group_id"]

            if escalated:
                wrong_prob = min(0.35, 0.06 * agent["quality_risk_factor"] + 0.03)
                if random.random() < wrong_prob:
                    wrong_escalation = 1
                    possible_groups = [g["group_id"] for g in SUPPORT_GROUPS if g["group_id"] != correct_group_id and g["group_id"] != 1]
                    escalated_group_id = random.choice(possible_groups)
                missing_minimum_data = 1 if random.random() < min(0.28, 0.09 * agent["quality_risk_factor"] + 0.04) else 0
                if wrong_escalation or missing_minimum_data:
                    escalation_returned = 1 if random.random() < 0.82 else 0
                elif random.random() < 0.03:
                    escalation_returned = 1
                if escalation_returned:
                    return_reason = random.choice(RETURN_REASONS)
                    return_delay = random.randint(15, 360)
                    return_at = action_at + timedelta(minutes=return_delay)
                    escalation_returns.append({
                        "return_id": return_id,
                        "ticket_id": ticket_id,
                        "returned_from_group_id": escalated_group_id,
                        "returned_to_group_id": 1,
                        "return_timestamp": format_dt(return_at),
                        "return_reason": return_reason,
                        "wrong_group_flag": wrong_escalation,
                        "missing_minimum_data_flag": missing_minimum_data,
                    })
                    return_id += 1
                    if wrong_escalation:
                        escalated_group_id = correct_group_id

            claim_count = 0
            if random.random() < 0.12:
                claim_count = random.choices([1, 2, 3, 4], weights=[0.68, 0.22, 0.08, 0.02], k=1)[0]

            reopen_count = 0
            reopen_base = 0.045 + (0.05 if escalation_returned else 0) + (0.03 if wrong_escalation else 0)
            if random.random() < min(0.30, reopen_base):
                reopen_count = random.choices([1, 2, 3], weights=[0.80, 0.17, 0.03], k=1)[0]

            resolution_minutes = generate_resolution_duration(priority, escalated, category["subcategory_name"], reopen_count, claim_count)
            resolved_at = assigned_at + timedelta(minutes=resolution_minutes)
            close_delay = random.randint(10, 4320)
            closed_at = resolved_at + timedelta(minutes=close_delay)
            current_status = random.choices(FINAL_STATUSES, weights=[0.44, 0.54, 0.02], k=1)[0]
            if current_status == "Cancelled":
                resolved_at = None
                closed_at = assigned_at + timedelta(minutes=random.randint(5, 240))

            assignment_breach = 1 if assignment_delay_min > priority["assign_sla_min"] else 0
            action_breach = 1 if action_delay_min > priority["action_sla_min"] else 0
            total_duration_min = minutes_between(created_at, closed_at)

            # Claims timeline
            for c in range(claim_count):
                claim_at = created_at + timedelta(minutes=random.randint(20, max(21, int(total_duration_min or 120))))
                user_claims.append({
                    "claim_id": claim_id,
                    "ticket_id": ticket_id,
                    "claim_timestamp": format_dt(claim_at),
                    "claim_channel": random.choice(["Phone", "Email", "Portal"]),
                    "claim_reason": random.choice([
                        "No update provided",
                        "Service still unavailable",
                        "Ticket taking too long",
                        "Issue not solved",
                        "Urgency increased by user",
                    ]),
                    "claim_sequence": c + 1,
                })
                claim_id += 1

            # Reopens timeline
            last_resolved = resolved_at
            reopen_events_for_ticket = []
            for r in range(reopen_count):
                if last_resolved is None:
                    break
                reopen_at = last_resolved + timedelta(minutes=random.randint(60, 10080))
                reopen_reason = random.choice([
                    "Issue reoccurred",
                    "Incomplete resolution",
                    "User could not validate fix",
                    "Related symptom persisted",
                ])
                event = {
                    "reopen_id": reopen_id,
                    "ticket_id": ticket_id,
                    "reopen_timestamp": format_dt(reopen_at),
                    "reopen_reason": reopen_reason,
                    "reopen_sequence": r + 1,
                }
                ticket_reopens.append(event)
                reopen_events_for_ticket.append(event)
                reopen_id += 1
                if r == reopen_count - 1 and current_status != "Cancelled":
                    last_resolved = reopen_at + timedelta(minutes=random.randint(45, 480))
                    resolved_at = last_resolved
                    closed_at = resolved_at + timedelta(minutes=random.randint(30, 1440))
                    total_duration_min = minutes_between(created_at, closed_at)

            # Mild data quality noise
            first_response_at = maybe_null(first_response_at, 0.004)
            if random.random() < 0.002:
                closed_at = None
                current_status = "Resolved"
            if random.random() < 0.003 and resolved_at is not None:
                resolved_at = closed_at

            tickets.append({
                "ticket_id": ticket_id,
                "ticket_code": f"INC-{YEAR}-{str(ticket_id).zfill(6)}",
                "created_at": format_dt(created_at),
                "assigned_at": format_dt(assigned_at),
                "first_response_at": format_dt(first_response_at) if first_response_at else "",
                "resolved_at": format_dt(resolved_at) if resolved_at else "",
                "closed_at": format_dt(closed_at) if closed_at else "",
                "status": current_status,
                "priority_id": priority["priority_id"],
                "category_id": category["category_id"],
                "channel_id": channel["channel_id"],
                "assigned_agent_id": agent["agent_id"],
                "opened_group_id": 1,
                "escalated_flag": escalated,
                "escalated_group_id": escalated_group_id,
                "correct_target_group_id": correct_group_id if escalated else "",
                "wrong_escalation_flag": wrong_escalation,
                "escalation_returned_flag": escalation_returned,
                "missing_minimum_data_flag": missing_minimum_data,
                "reopened_flag": 1 if reopen_count > 0 else 0,
                "reopen_count": reopen_count,
                "user_claim_count": claim_count,
                "assignment_sla_target_min": priority["assign_sla_min"],
                "action_sla_target_min": priority["action_sla_min"],
                "assignment_minutes": assignment_delay_min,
                "first_response_minutes": minutes_between(created_at, first_response_at) if first_response_at else "",
                "action_minutes": action_delay_min,
                "total_duration_minutes": total_duration_min if total_duration_min is not None else "",
                "assignment_sla_breached": assignment_breach,
                "action_sla_breached": action_breach,
            })

            # Status history
            status_history.append({"status_event_id": status_id, "ticket_id": ticket_id, "status_timestamp": format_dt(created_at), "status_name": "Open", "changed_by_agent_id": ""}); status_id += 1
            status_history.append({"status_event_id": status_id, "ticket_id": ticket_id, "status_timestamp": format_dt(assigned_at), "status_name": "Assigned", "changed_by_agent_id": agent["agent_id"]}); status_id += 1
            if first_response_at:
                status_history.append({"status_event_id": status_id, "ticket_id": ticket_id, "status_timestamp": format_dt(first_response_at), "status_name": "In Progress", "changed_by_agent_id": agent["agent_id"]}); status_id += 1
            if escalated:
                status_history.append({"status_event_id": status_id, "ticket_id": ticket_id, "status_timestamp": format_dt(action_at), "status_name": "Escalated", "changed_by_agent_id": agent["agent_id"]}); status_id += 1
            if escalation_returned:
                ret_ts = escalation_returns[-1]["return_timestamp"]
                status_history.append({"status_event_id": status_id, "ticket_id": ticket_id, "status_timestamp": ret_ts, "status_name": "Returned", "changed_by_agent_id": ""}); status_id += 1
            if resolved_at:
                status_history.append({"status_event_id": status_id, "ticket_id": ticket_id, "status_timestamp": format_dt(resolved_at), "status_name": "Resolved", "changed_by_agent_id": agent["agent_id"]}); status_id += 1
            for ro in reopen_events_for_ticket:
                status_history.append({"status_event_id": status_id, "ticket_id": ticket_id, "status_timestamp": ro["reopen_timestamp"], "status_name": "Reopened", "changed_by_agent_id": ""}); status_id += 1
            if closed_at:
                status_history.append({"status_event_id": status_id, "ticket_id": ticket_id, "status_timestamp": format_dt(closed_at), "status_name": current_status, "changed_by_agent_id": agent["agent_id"] if current_status != "Cancelled" else ""}); status_id += 1

            ticket_id += 1

    # Trim or keep near target volume by deterministic slice
    tickets = tickets[:TARGET_TICKETS]
    valid_ticket_ids = {t["ticket_id"] for t in tickets}
    escalation_returns = [r for r in escalation_returns if r["ticket_id"] in valid_ticket_ids]
    ticket_reopens = [r for r in ticket_reopens if r["ticket_id"] in valid_ticket_ids]
    user_claims = [c for c in user_claims if c["ticket_id"] in valid_ticket_ids]
    status_history = [s for s in status_history if s["ticket_id"] in valid_ticket_ids]

    files = {
        "tickets.csv": tickets,
        "agents.csv": agents,
        "categories.csv": categories,
        "sla_targets.csv": sla_targets,
        "support_groups.csv": SUPPORT_GROUPS,
        "channels.csv": CHANNELS,
        "shifts.csv": SHIFTS,
        "escalation_returns.csv": escalation_returns,
        "ticket_reopens.csv": ticket_reopens,
        "user_claims.csv": user_claims,
        "status_history.csv": status_history,
    }

    for filename, rows in files.items():
        if not rows:
            continue
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=';')
            writer.writeheader()
            writer.writerows(rows)

    print(f"Generated {len(tickets)} tickets in {OUTPUT_DIR}")
    print("Files:")
    for k in files:
        print(f" - {k}")


if __name__ == "__main__":
    main()
