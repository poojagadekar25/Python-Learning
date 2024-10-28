from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_items():
    return {"message": "Fetching all items"}

@app.get("/users/")
def read_users():
    return {"message": "Fetching all users"}

@app.get("/products/{product_id}")
def read_product(product_id: int):
    return {"product_id": product_id}

@app.get("/orders/{order_id}")
def read_order(order_id: int):
    return {"order_id": order_id}
