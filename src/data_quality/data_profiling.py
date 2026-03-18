import pandas as pd
import os

DATA_PATH = "data/raw"

def load_data():
    datasets = {}
    for file in os.listdir(DATA_PATH):
        if file.endswith(".csv"):
            name = file.replace(".csv", "")
            datasets[name] = pd.read_csv(
            os.path.join(DATA_PATH, file),
            sep=";",
            encoding="utf-8-sig"
        )
    return datasets

def basic_info(df, name):
    print(f"\n--- {name.upper()} ---")
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns)
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum())

def main():
    datasets = load_data()
    for name, df in datasets.items():
        basic_info(df, name)

if __name__ == "__main__":
    main()