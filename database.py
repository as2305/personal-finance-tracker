import json
from pathlib import Path
from datetime import date
import secrets


balance = {
    "balance": 0
    }
transaction_history = []

bal_path = Path("balance.json")
th_path = Path("transaction_history.json")


#future implementation
#def balance_calc(a):
#    total_deposit = 0
#    total_withdrawn = 0
#    for entry in a:
#        if entry["mode"] == "deposit":
#            total_deposit += entry["amount"]
#        elif entry["mode"] == "withdraw":
#            total_withdrawn += entry["amount"]
#    return total_deposit - total_withdrawn


#generate unique ID
def id_gen():
    return secrets.token_hex(3)

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
        transaction_history.append({"id": id_gen(), "mode": mode, "amount": amount, "date": str(date.today())})
        update_bal()
        update_th()
        return True
    elif mode == "withdraw":
        balance["balance"] -= amount
        transaction_history.append({"id": id_gen(), "mode": mode, "amount": amount, "date": str(date.today())})
        update_bal()
        update_th()
        return True
    else:
        return False


def del_transaction(uid):
    global balance
    global transaction_history
    length = len(transaction_history)
    #add break statement
    for i in transaction_history:
        if i["id"] == uid:
            if i["mode"] == "withdraw":
                balance["balance"] += i["amount"]
            elif i["mode"] == "deposit":
                balance["balance"] -= i["amount"]
    transaction_history = [e for e in transaction_history if e["id"] != uid]
    update_th()
    if len(transaction_history) != length:
        return True
    else:
        return False