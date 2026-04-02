from pathlib import Path
import duckdb

con = duckdb.connect()

con.execute("""
    CREATE OR REPLACE VIEW tickets_final AS
    SELECT *
    FROM read_csv('data/final/tickets_final.csv');
""")

sql_file = Path("src/sql/03_escalations_reopens/04_wrong_escalation_rate.sql")
sql_query = sql_file.read_text(encoding="utf-8")

result = con.execute(sql_query).fetchdf()
print(result.to_string(index=False))

con.close()