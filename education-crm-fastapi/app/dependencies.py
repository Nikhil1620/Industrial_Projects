from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.auth.token import verify_token


security = HTTPBearer()


# DATABASE DEPENDENCY
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# CURRENT USER DEPENDENCY
def get_current_user(token=Depends(security)):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid token"
    )

    payload = verify_token(token.credentials)

    if payload is None:
        raise credentials_exception

    return payload