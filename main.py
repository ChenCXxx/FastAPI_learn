from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, schemas, crud, database

app = FastAPI()

# Create the database
database.create_db()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Mount the static files directory at the root
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    if db_user:
        return {"message": "User created successfully!"}
    raise HTTPException(status_code=400, detail="User already exists.")

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user is None or not db_user.hashed_password == user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials.")
    return {"message": f"Welcome, {user.username}!"}

@app.get("/users/{userid}", response_model=schemas.UserResponse)
def get_user(userid: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, userid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user

@app.get("/api")
def read_root():
    return {
        "message": "Welcome to the FastAPI application!",
        "instructions": "Use /register to create a new user and /login to authenticate."
    }

