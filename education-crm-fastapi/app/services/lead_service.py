from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.lead import Lead


# CREATE LEAD
def create_lead(db: Session, data):
    lead = Lead(**data.dict())
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead


# GET LEADS (SEARCH + FILTER + PAGINATION)
def get_leads(db: Session, search=None, stage=None, skip=0, limit=10):

    query = db.query(Lead).filter(Lead.is_deleted == 0)

    if search:
        query = query.filter(
            or_(
                Lead.full_name.like(f"%{search}%"),
                Lead.email.like(f"%{search}%"),
                Lead.phone.like(f"%{search}%")
            )
        )

    if stage:
        query = query.filter(Lead.pipeline_stage == stage)

    return query.offset(skip).limit(limit).all()