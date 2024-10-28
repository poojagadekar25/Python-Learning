from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Literal
app = FastAPI()

class QueryItems(BaseModel):
    price: float = 0.0
    color: str = None
    status: Literal["available", "sold_out", "pending"]

@app.post("/order/{order_id}")
def add_item(order_id: int, params: QueryItems):
    return {
        "order_id": order_id,
        "price": params.price,
        "color": params.color,
        "status":params.status
    }




class Item(BaseModel):
    name: str = Field(..., title="The name of the item", max_length=50)
    price: float = Field(..., gt=0, description="The price of the item, must be greater than 0")
    quantity: int = Field(1, ge=0, description="The quantity of the item, must be 0 or greater")

@app.post("/items/")
async def create_item(item: Item):
    return item
