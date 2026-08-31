# command to run: uvicorn app:app --reload --host 0.0.0.0 --port 8001

from fastapi import FastAPI
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    age: int
    phone: int

app=FastAPI()

# http://localhost:8001/
@app.get("/") # defining @app is called as decorator.
def home():
    return {"message":"hello world!"}

# http://localhost:8001/home/
@app.get("/home")
def home1():
    return {"message":"hello world1!"}

# http://localhost:8001/item/1
@app.get("/item/{item_id}")
def item(item_id: int):
    return {"message ":" Hello ${item_id}", "item_id": item_id}

# http://localhost:8001/search?q=1&name=test
@app.get("/search")
def search(q: str=None, name: str=""):
    return {"query": q, "name": name}

# http://localhost:8001/items
# payload: {"name":"test", "age": 10}
@app.post("/items")
# def create(items: dict):
def create(items: Item): #data is pulled from Item class (Pydantic model ex.)
    return {"item": items}

# check the swagger docs in below url>
# http://localhost:8001/docs