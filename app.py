import streamlit as st
import requests


def get_balance():
    try:
        a = requests.get("http://127.0.0.1:8000/balance").json()
        return a["balance"]
    except:
        return "Server Down."

def add_transaction(wh, amount):
    try:
        requests.post(f"http://127.0.0.1:8000/record?mode={wh}&amount={amount}")
    except:
        return "Error"

def get_history():
    try:
        a = requests.get("http://127.0.0.1:8000/history").json()
        return a
    except:
        return "Server Down."

def delete_transaction(uid):
    try:
        requests.post(f"http://127.0.0.1:8000/delete?uid={uid}")
    except:
        return "Error"

balance = get_balance()

st.header("💰 Personal Finance Tracker")
display = st.empty()
display.markdown((f"## $ {balance}"))

if st.button("Update Balance"):
    display.markdown(f"## $ {get_balance()}")

st.markdown("## Transaction History")

yes = get_history()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### ID")
    for i in yes:
        st.markdown(i["id"])
with col2:
    st.markdown("### Type")
    for i in yes:
        st.markdown(i["mode"])
with col3:
    st.markdown("### Amount")
    for i in yes:
        st.markdown(i["amount"])
with col4:
    st.markdown("### Date")
    for i in yes:
        st.markdown(i["date"])

with st.sidebar:
    st.title("Add Transaction")
    amount = st.text_input("Enter Amount")
    col1, col2 = st.columns(2)
    
    
    with col1:
        if st.button("Deposit", use_container_width=True):
            add_transaction("deposit", amount)
            display.markdown(f"## $ {get_balance()}")
            st.rerun()
        

    with col2:
        if st.button("Withdraw", use_container_width=True):
            add_transaction("withdraw", amount)
            display.markdown(f"## $ {get_balance()}")
            st.rerun()

    
    st.divider()

    st.title("Delete Transaction")
    box = st.text_input("Enter ID")
    if st.button("Delete"):
        delete_transaction(box)
        st.rerun()
    st.caption("Finance Tracker")