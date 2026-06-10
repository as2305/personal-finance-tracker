import json
from pathlib import Path
from datetime import date

balance = {
    "balance": 0
    }
transaction_history = []

bal_path = Path("balance.json")
th_path = Path("transaction_history.json")

#Initialize Database
def init_db():
    global balance
    global transaction_history
    if not bal_path.is_file():
        bal_path.write_text(json.dumps(balance, indent = 4))
    else:
        balance = json.loads(bal_path.read_text())
    if not th_path.is_file():
        th_path.write_text(json.dumps(transaction_history, indent = 4))
    else:
        transaction_history = json.loads(th_path.read_text())

#Update JSON
def update_bal():
    bal_path.write_text(json.dumps(balance, indent = 4))
def update_th():
    th_path.write_text(json.dumps(transaction_history, indent = 4))

#add transaction
def add_transaction(mode, amount):
    global balance
    global transaction_history
    if mode == "deposit":
        balance["balance"] += amount
        transaction_history.append({"mode": mode, "amount": amount, "date": str(date.today())})
        update_bal()
        update_th()
        return True
    elif mode == "withdraw":
        balance["balance"] -= amount
        transaction_history.append({"mode": mode, "amount": amount, "date": str(date.today())})
        update_bal()
        update_th()
        return True
    else:
        return False
