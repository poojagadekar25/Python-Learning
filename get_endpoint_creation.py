from fastapi import FastAPI
app=FastAPI()
@app.get("/items/")
def read_items():
    return {"message": "This is the first endpoint"}

# @app.get("/items/")
# def read_items_v2():
#     return {"message": "This is the second endpoint"}


# Note ==> having to get endpoints with same route is not allowed
