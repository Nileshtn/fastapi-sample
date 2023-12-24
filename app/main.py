from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from utils.math import add

app = FastAPI()


class item(BaseModel):
    name: str
    price: float
    is_offer : Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add")
def get_add():
    c = add(1,4)
    return c


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}