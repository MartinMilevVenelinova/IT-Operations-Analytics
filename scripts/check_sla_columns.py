import duckdb

query = """
SELECT *
FROM read_csv('data/final/tickets_final.csv')
LIMIT 1;
"""

result = duckdb.execute(query).fetchdf()

print("Columns in tickets_final.csv:\n")
for column in result.columns:
    print(column)