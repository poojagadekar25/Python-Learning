from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Nested model for individual items in an order
class Item(BaseModel):
    name: str
    price: float
    quantity: int

# Nested model for user information
class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None

# Main model for an order, which includes the user and a list of items
class Order(BaseModel):
    order_id: int
    user: User  # User model nested here
    items: List[Item]  # List of Item models
    total_price: float

@app.post("/orders/")
async def create_orders(order: Order):
    return {"message": "Order received", "order": order}
