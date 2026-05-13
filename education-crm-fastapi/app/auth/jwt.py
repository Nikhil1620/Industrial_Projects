from jose import jwt
from datetime import datetime, timedelta
from app.config import settings

def create_token(data: dict):
    payload = data.copy()
    payload.update({
        "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    })
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)