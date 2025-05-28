from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from math_tasks.sqrt import sqrt_number
from math_tasks.triangeel import calculate_triangle_angles
app = FastAPI()

class Triangle(BaseModel):
    a: float
    b: float
    c: float

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/sqrt/{number}")
def sqrt(number: float):
    sqrted_number = sqrt_number(number)
    return {"number": number, "sqrted_number": sqrted_number}

@app.get("/triangle/calculate_angles")
def calculate_angles(triangle: Triangle):
    angles = calculate_triangle_angles(triangle.a, triangle.b, triangle.c)
    return {"alfa": angles[0], "beta": angles[1], "gamma": angles[2]}
