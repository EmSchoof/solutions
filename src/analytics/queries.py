# filepath src/analytics/queries.py

# import modules
import duckdb

# create data query grab from DB
def run_queries(df):
    con = duckdb.connect()

    result = con.execute("""
        SELECT user_id, SUM(amount) as total_spent
        FROM df
        GROUP BY user_id
    """).df()

    return result