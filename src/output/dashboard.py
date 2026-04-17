# filepath src/output/dashboard.py

# import modules
import streamlit as st
import requests

# creat temporary dashboard
data = requests.get("http://127.0.0.1:8000/analytics").json()
st.write(data)