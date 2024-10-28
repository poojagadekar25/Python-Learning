from fastapi import FastAPI, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sqlmodel import SQLModel, Field, Session, create_engine, select
from pydantic import BaseModel
    
# Initialize FastAPI app
app = FastAPI()

# Configure database connection (using SQLite for demonstration)
DATABASE_URL = "mysql+pymysql://root:sai%40123@localhost/frontend"
engine = create_engine(DATABASE_URL)

# Setup Jinja2 templates
templates = Jinja2Templates(directory="Template")

# Database model using SQLModel
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

# Create the database table
SQLModel.metadata.create_all(engine)

# Database dependency for session
def get_session():
    with Session(engine) as session:
        yield session

# Display the login form
@app.get("/", response_class=HTMLResponse)
async def read_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Handle form submission
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...), session: Session = Depends(get_session)):
    # Query user from the database
    query = select(User).where(User.username == username, User.password == password)
    user = session.exec(query).first()
    
    if user:
        return {"message": "Login successful!"}
    else:
        return {"message": "Invalid username or password"}

# Endpoint to add a user for testing (optional)
@app.post("/register")
async def register(username: str, password: str, session: Session = Depends(get_session)):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": f"User {new_user.username} registered successfully"}
