from pydantic import BaseModel
from datetime import date
from app.schemas.educator_slot_schema import EducatorSlotResponse
from app.schemas.educator_schema import EducatorResponse

class EducatorAppointmentCreate(BaseModel):
    educator_id: int
    slot_id: int
    date: date
    student_name: str
    gender: str
    age: int
    address: str
    phone: str

class EducatorAppointmentResponse(EducatorAppointmentCreate):
    id: int
    slot: EducatorSlotResponse
    educator: EducatorResponse

    class Config:
        orm_mode = True
