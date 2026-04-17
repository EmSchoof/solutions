# filepath src/output/dashboard.py

# import modules and global params
import streamlit as st
import requests
import threading
import uvicorn
import time
import os
API_URL = os.getenv("API_URL")
UVICORN_HOST = os.getenv("UVICORN_HOST")

# import FastAPI app
from src.api.main import app

# Function to run API
def run_api():
    uvicorn.run(app, host=UVICORN_HOST, port=8000)

# Start API only once
if "api_started" not in st.session_state:
    thread = threading.Thread(target=run_api, daemon=True)
    thread.start()
    st.session_state.api_started = True
    time.sleep(2)  # give server time to start

# creat temporary dashboard with API call
try:
    response = requests.get(API_URL)
    data = response.json()
    st.write(data)
except Exception:
    st.error("API not ready yet...")