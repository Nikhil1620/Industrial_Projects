from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.schemas.lead import LeadCreate
from app.services.lead_service import create_lead, get_leads

router = APIRouter(prefix="/leads")

@router.post("/")
def create(lead: LeadCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_lead(db, lead)


@router.get("/")
def list_leads(search: str = None, stage: str = None, page: int = 1, limit: int = 10,
               db: Session = Depends(get_db), user=Depends(get_current_user)):

    skip = (page - 1) * limit
    return get_leads(db, search, stage, skip, limit)