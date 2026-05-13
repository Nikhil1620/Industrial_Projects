from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.auth.hashing import hash_password, verify_password
from app.auth.jwt import create_token
    
router = APIRouter()

fake_users = {}

@router.post("/register")
def register(user: dict, db: Session = Depends(get_db)):
    user["password"] = hash_password(user["password"])
    fake_users[user["email"]] = user
    return {"message": "User registered"}

@router.post("/login")
def login(email: str, password: str):
    user = fake_users.get(email)
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(400, "Invalid credentials")

    token = create_token({"sub": email, "role": user["role"]})
    return {"access_token": token}