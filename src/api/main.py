# filename src/api/main.py

# Import Modules
from fastapi import FastAPI
from src.ingestion.load_data import load_data
from src.pipeline.transform import transform
from src.analytics.queries import run_queries

# Create API Layer
app = FastAPI()

@app.get("/analytics")
def get_analytics():
    df = load_data()
    df = transform(df)
    result = run_queries(df)
    return result.to_dict(orient="records")