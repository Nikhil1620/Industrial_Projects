from pydantic import BaseModel, EmailStr
from typing import Optional

class LeadCreate(BaseModel):
    full_name: str
    phone: str
    email: EmailStr
    class_name: str
    school_name: str
    parent_name: str
    source: str
    pipeline_stage: str
    notes: Optional[str]