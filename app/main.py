from fastapi import FastAPI
from datetime import datetime
from typing import List

app = FastAPI()

items = [
    {"id": 1, "name": "Widget", "created_at": datetime(2022, 9, 1, 12, 0, 0)},
    {"id": 2, "name": "Gadget", "created_at": datetime(2022, 9, 2, 14, 30, 15)},
    {"id": 3, "name": "Thingamajig", "created_at": datetime(2022, 9, 3, 9, 15, 45)},
]

@app.get("/v1/items")
def get_items():
    return items
