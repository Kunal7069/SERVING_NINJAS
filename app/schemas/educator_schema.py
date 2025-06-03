from pydantic import BaseModel
from typing import List
from app.schemas.educator_slot_schema import EducatorSlotCreate, EducatorSlotResponse

class EducatorCreate(BaseModel):
    center_name: str
    educator_name: str
    address: str
    phone: str
    city: str
    subject: str
    slots: List[EducatorSlotCreate]

class EducatorResponse(BaseModel):
    id: int
    center_name: str
    educator_name: str
    address: str
    phone: str
    city: str
    subject: str
    slots: List[EducatorSlotResponse]

    class Config:
        orm_mode = True
