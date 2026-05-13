from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True)
    action = Column(String(50))
    lead_id = Column(Integer)
    user_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)