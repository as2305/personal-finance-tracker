from fastapi import FastAPI
import database


app = FastAPI()

database.init_db()


@app.get("/balance")
def get_balance():
    return database.balance

@app.get("/history")
def get_history():
    return database.history