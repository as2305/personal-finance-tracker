from fastapi import FastAPI
import database


app = FastAPI()

database.init_db()


@app.post("/record")
def record(mode:str, amount:int):
    output = database.add_transaction(mode, amount)
    if output:
        return {"message": "success"}
    else:
        return {"message": "failed"}
    

@app.get("/balance")
def get_balance():
    return database.balance

@app.get("/history")
def get_history():
    return database.transaction_history