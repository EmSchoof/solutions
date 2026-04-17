# filepath src/ingestion/load_data.py

# import modules
import pandas as pd

# create load data function
def load_data():
    data = {
        "user_id": [1, 2, 1, 3, 2],
        "event": ["click", "view", "purchase", "click", "purchase"],
        "amount": [0, 0, 100, 0, 200]
    }
    df = pd.DataFrame(data)
    return df