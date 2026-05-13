from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)

    full_name = Column(String(100), index=True)
    phone = Column(String(20), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)

    class_name = Column(String(50))
    school_name = Column(String(100))
    parent_name = Column(String(100))
    source = Column(String(50))

    pipeline_stage = Column(String(50), index=True)
    notes = Column(Text)

    is_deleted = Column(Integer, default=0)  # soft delete