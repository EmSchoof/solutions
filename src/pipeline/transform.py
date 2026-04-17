# filepath src/pipeline/transform.py

# create transformation procedure
def transform(df):
    df["is_purchase"] = df["event"] == "purchase"
    return df