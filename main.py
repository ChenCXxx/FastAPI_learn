from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from schemas import UserCreate, UserLogin
app = FastAPI()

# Mount the static files directory at the root
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/api")
def read_root():
    return {
        "message": "Welcome to the FastAPI application!",
        "instructions": "Use /register to create a new user and /login to authenticate."
    }

@app.post("/login")
def login(user: UserLogin):
    return {"username": user.username, "password": user.password}

@app.post("/register")
def register(user: UserCreate):
    return {"username": user.username, "password": user.password, "email": user.email}