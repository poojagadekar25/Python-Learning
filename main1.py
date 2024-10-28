from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from user_table.database import SessionLocal, engine
from user_table.models import Users
from pydantic import BaseModel

app = FastAPI()

# Create database tables
# This avoids circular imports by ensuring Base.metadata.create_all is in main.py
from user_table.models import Users  # Import models after engine is created
Users.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for response model
class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    # class Config:
    #     orm_mode = True

# Pydantic schema for user creation
class UserCreateSchema(BaseModel):
    name: str
    email: str
    password: str

# Route to get all users
@app.get("/users", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(Users).all()

# Route to create a new user
@app.post("/users", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    u = Users(name=user.name, email=user.email, password=user.password)
    db.add(u)
    db.commit()
    db.refresh(u)  # To get the auto-generated id
    return u


@app.put("/users/{user_id}", response_model=UserSchema)
def update_user( user_id:int,user_update: UserCreateSchema, db: Session = Depends(get_db)):
    # Find the user by ID
    user = db.get(Users, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update the user's information
    if user_update.name is not None:
        user.name = user_update.name
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.password is not None:
        user.password = user_update.password

    # Commit the changes to the database
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user


