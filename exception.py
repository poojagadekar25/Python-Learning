from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse


app=FastAPI()

users={"pooja":"user pooja"}

@app.get("/users/{user_id}")
def  get_user(user_id:str):
    if user_id not in users:
         raise HTTPException(status_code=404,detail="details not found")
    return {"user":users[user_id]}


# adding custom header


@app.get("/item/{item_id}")
def read_item(item_id:int):
    if item_id<1:
        raise HTTPException(status_code=404,details="Item id cannot be less than 1",headers={"X-Error":"There goes my error"})
    return{"item id":item_id}


#Custom exception

#1) define custom exception
class UserNotFoundException(Exception):
    def __init__(self,user_id:int):
        self.user_id=user_id



people_db={1:"pooja",2:"gayu"}
#2) raising an exception
@app.get("/people/{people_id}")
def get_people(people_id:int):
    if people_id not in people_db:
        raise UserNotFoundException(people_id=people_id)
    return {"people_id":people_id,"name":people_db[people_id]}

#3) create exception handeler
@app.exception_handler(UserNotFoundException)
def user_not_found_handeler(request:Request,exec:UserNotFoundException):
    return JSONResponse(status_code=404,content={"msg":"user not found"})

book_db={1:"storybook",2:"textbook"}

class BookNotFoundException(Exception):
    def __init__(self,book_id:int):
        self.book_id=book_id

@app.get("/Books/{book_id}")
def get_book(book_id:int):
    if book_id not in book_db:
        raise BookNotFoundException(book_id=book_id)
    return {"Book ID":book_id,"Name":book_db[book_id]}

@app.exception_handler(BookNotFoundException)
def book_not_found_handeler(request:Request,exec:UserNotFoundException):
    return JSONResponse(status_code=404,content={"msg":"usr not found"})