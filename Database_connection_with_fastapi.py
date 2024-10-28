from fastapi import FastAPI, Depends,HTTPException
from sqlmodel import SQLModel, Session, create_engine, select, Field
from pydantic import BaseModel

app = FastAPI()

# Database connection (MySQL)
DATABASE_URL = "mysql+pymysql://root:sai%40123@localhost/application"
engine = create_engine(DATABASE_URL)

# Define database table
class Users(SQLModel, table=True):
    id: int = Field( primary_key=True)  
    name: str
    email: str
    password: str

# Pydantic model for input/output (response validation)
class UserCreate(BaseModel):
    id:int
    name: str
    email: str
    password: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str

class UserUpdate(BaseModel): 
    name: str 
    email: str 
    password: str 

# Create the database tables
SQLModel.metadata.create_all(engine)

# Dependency to get a database session
def get_db():
    with Session(engine) as session:
        yield session

# Route to get all users
@app.get("/users", response_model=list[UserRead])  # Use UserRead model for response
def get_users(db: Session = Depends(get_db)):
    return db.exec(select(Users)).all()

# Route to create a new user
@app.post("/users", response_model=UserRead)  # Use UserRead model for response
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = Users(id=user.id,name=user.name, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh to get the generated id
    return new_user



# Route to update an existing user (PUT endpoint)
@app.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    # Find the user by ID
    user = db.get(Users, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update the user's information
        user.name = user_update.name
        user.email = user_update.email
        user.password = user_update.password

    # Commit the changes to the database
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user


# Route to delete a user (DELETE endpoint)
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(Users, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    
    return {"message": "User deleted successfully"}