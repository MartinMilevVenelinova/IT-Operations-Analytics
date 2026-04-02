from pathlib import Path
import duckdb

con = duckdb.connect()

con.execute("""
    CREATE OR REPLACE VIEW tickets_final AS
    SELECT *
    FROM read_csv('data/final/tickets_final.csv');
""")

sql_file = Path("src/sql/02_agent_performance/03_sla_compliance_per_agent.sql")
sql_query = sql_file.read_text(encoding="utf-8")

result = con.execute(sql_query).fetchdf()
print(result.to_string(index=False))

con.close()