# filename: src/analytics/queries.py

# Impport modules
import duckdb

# Create Data Query Grab from DB
def run_queries(df):
    con = duckdb.connect()

    result = con.execute("""
        SELECT user_id, SUM(amount) as total_spent
        FROM df
        GROUP BY user_id
    """).df()

    return result