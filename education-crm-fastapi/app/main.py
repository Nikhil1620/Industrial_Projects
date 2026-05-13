from fastapi import FastAPI
from app.routers import auth, lead
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Education CRM API (MySQL)")

app.include_router(auth.router)
app.include_router(lead.router)