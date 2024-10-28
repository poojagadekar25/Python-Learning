from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons=Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons= Depends(common_parameters)):
    return commons

def get_db():
    db = {"name": "pooja"}  # Simulating a database connection
    return db

# Using dependency injection
@app.get("/item/")
def read_items(db=Depends(get_db)):
    return {"db_name": db}

def add(a:int,b:int):
    return a+b

@app.get("/sum/")
def avg(sum=Depends(add)):
    return sum/2