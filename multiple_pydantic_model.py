from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Item(BaseModel):
    name: str= Field(..., title="The name of the item", max_length=50)
    price: float

class Order(BaseModel):
    order_id: int
    quantity: int

@app.post("/orders/")
async def create_order(order: Order, item: Item):
    return {
        "order_id": order.order_id,
        "item_name": item.name,
        "price": item.price,
        "quantity": order.quantity
    }
