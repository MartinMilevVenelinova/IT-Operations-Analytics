import duckdb

query = """
SELECT *
FROM read_csv('data/final/tickets_final.csv')
LIMIT 5;
"""

result = duckdb.execute(query).fetchdf()
print(result)