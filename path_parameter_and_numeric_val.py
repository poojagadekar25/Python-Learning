from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
# Without using Annotated
@app.get("/items/{item_id}")
def read_item(item_id: int = Path(title="The id of item", ge=1, le=100)):
    return {"item_id": item_id}


# using Annotated ==> combines both type hint and metadata/validations in one place  in 
@app.get("/items/{item_id}")
def read_item(item_id: Annotated[int, Path(ge=1, le=100)]):
    return {"item_id": item_id}




app = FastAPI()

@app.get("/product/")
def read_items(price: Annotated[float, Query(ge=1.0, le=100.0)] = 10.0):
    return {"price": price}


