from typing import Union

from fastapi import FastAPI
from util import item_value

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, name: Union[str] = None):
    # raise Exception("some error")
    response =  item_value(item_id, name)
    return response

# Query parameter example http://localhost:8001/items1/123?q="jegan"
@app.get("/items1/{item_id}")
def read_item(item_id: int, q: Union[str,None] = None):
    # raise Exception("some error")
    response =  item_value(item_id, q)
    return response