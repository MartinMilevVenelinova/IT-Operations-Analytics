import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

def load_data():
    datasets = {}
    for file in os.listdir(RAW_PATH):
        if file.endswith(".csv"):
            name = file.replace(".csv", "")
            datasets[name] = pd.read_csv(
                os.path.join(RAW_PATH, file),
                sep=";",
                encoding="utf-8-sig"
            )
    return datasets

def clean_tickets(df):
    # Convert dates
    date_cols = [
        "created_at", "assigned_at", "first_response_at",
        "resolved_at", "closed_at"
    ]

    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df

def save_data(datasets):
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    for name, df in datasets.items():
        df.to_csv(os.path.join(PROCESSED_PATH, f"{name}.csv"), index=False)

def main():
    datasets = load_data()

    # Clean tickets table
    datasets["tickets"] = clean_tickets(datasets["tickets"])

    save_data(datasets)

if __name__ == "__main__":
    main()