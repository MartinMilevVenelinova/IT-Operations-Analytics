import pandas as pd
import os

DATA_PATH = "data/processed"

def load_data():
    datasets = {}
    for file in os.listdir(DATA_PATH):
        if file.endswith(".csv"):
            name = file.replace(".csv", "")
            datasets[name] = pd.read_csv(os.path.join(DATA_PATH, file))
    return datasets

def convert_dates(df):
    date_cols = [
        "created_at", "assigned_at", "first_response_at",
        "resolved_at", "closed_at"
    ]

    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df

def validate_tickets(df):
    print("\n--- VALIDATING TICKETS ---")

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nCheck negative times:")
    time_cols = [
        "assignment_minutes",
        "first_response_minutes",
        "action_minutes",
        "total_duration_minutes"
    ]

    for col in time_cols:
        negatives = (df[col] < 0).sum()
        print(f"{col}: {negatives} negative values")

    print("\nBusiness rule checks:")

    created_after_assigned = (df["assigned_at"] < df["created_at"]).sum()
    print(f"assigned_at earlier than created_at: {created_after_assigned}")

    created_after_first_response = (df["first_response_at"] < df["created_at"]).sum()
    print(f"first_response_at earlier than created_at: {created_after_first_response}")

    created_after_resolved = (df["resolved_at"] < df["created_at"]).sum()
    print(f"resolved_at earlier than created_at: {created_after_resolved}")

    created_after_closed = (df["closed_at"] < df["created_at"]).sum()
    print(f"closed_at earlier than created_at: {created_after_closed}")

    escalated_without_group = (
        (df["escalated_flag"] == 1) & (df["escalated_group_id"].isnull())
    ).sum()
    print(f"escalated tickets without escalated_group_id: {escalated_without_group}")

    non_escalated_with_group = (
        (df["escalated_flag"] == 0) & (df["escalated_group_id"].notnull())
    ).sum()
    print(f"non-escalated tickets with escalated_group_id: {non_escalated_with_group}")

    reopened_without_count = (
        (df["reopened_flag"] == 1) & (df["reopen_count"] == 0)
    ).sum()
    print(f"reopened tickets with reopen_count = 0: {reopened_without_count}")

    claims_without_count = (df["user_claim_count"] < 0).sum()
    print(f"tickets with negative user_claim_count: {claims_without_count}")

    assignment_sla_flag_mismatch = (
        ((df["assignment_minutes"] > df["assignment_sla_target_min"]) & (df["assignment_sla_breached"] == 0)) |
        ((df["assignment_minutes"] <= df["assignment_sla_target_min"]) & (df["assignment_sla_breached"] == 1))
    ).sum()
    print(f"assignment SLA flag mismatches: {assignment_sla_flag_mismatch}")

    action_sla_flag_mismatch = (
        ((df["action_minutes"] > df["action_sla_target_min"]) & (df["action_sla_breached"] == 0)) |
        ((df["action_minutes"] <= df["action_sla_target_min"]) & (df["action_sla_breached"] == 1))
    ).sum()
    print(f"action SLA flag mismatches: {action_sla_flag_mismatch}")

def main():
    datasets = load_data()

    datasets["tickets"] = convert_dates(datasets["tickets"])

    validate_tickets(datasets["tickets"])

if __name__ == "__main__":
    main()