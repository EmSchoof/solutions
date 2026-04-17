# filepath src/output/dashboard.py

# import modules and global params
import streamlit as st
import requests
import os
API_URL = os.getenv("API_URL")

# creat temporary dashboard
try:
    data = requests.get(API_URL).json()
    st.write(data)
except Exception as e:
    st.error("API not running. Please start FastAPI server.")