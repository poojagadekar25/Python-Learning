from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

# Define the data model using BaseModel
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str

# Sample data (usually this would come from a database)
books = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", description="A story about the American dream."),
    Book(id=2, title="1984", author="George Orwell", description="A dystopian novel."),
]

# Define a GET endpoint to fetch book details by ID
@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    # Filter the book based on its ID
    book = next((book for book in books if book.id == book_id), None)
    if book:
        return book
    return {"error": "Book not found"}
