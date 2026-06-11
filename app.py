import streamlit as st
import requests


def get_balance():
    a = requests.get("http://127.0.0.1:8000/balance").json()
    return a["balance"]

balance = get_balance()

st.header("💰 Personal Finance Tracker")
display = st.empty()
display.markdown((f"## {balance}"))

if st.button("Update Balance"):
    display.markdown(f"## {get_balance()}")