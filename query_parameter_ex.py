from fastapi import FastAPI

app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/{item_id}")
async def read_item( item_id:int,limit: int = 10):
    return {"limit":limit, "item id":item_id}

@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"user is":user_id}

from fastapi import FastAPI

app = FastAPI()

@app.get("/books/")
def read_items(name: str = None, price: float = None):
    items = {"item1": "Book", "item2": "Pen"}
    if name:
        return {"name_filter": name}
    if price:
        return {"price_filter": price}
    return items



items = {
    1: {"name": "Item One", "price": 10.0},
    2: {"name": "Item Two", "price": 20.0},
}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id in items:
        return items[item_id]
    else:
        return {"error": "Item not found"}





# To take only string values
@app.get("/product/{product_name}")
def get_user(product_id: str):
    if product_id.isalpha():
        raise HTTPException(status_code=400, detail="user_id must not be only numeric")
    return {"Product is": product_name}

    
