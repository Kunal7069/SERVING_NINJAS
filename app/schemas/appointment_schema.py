
from pydantic import BaseModel
from typing import Literal
from datetime import date

class AppointmentCreate(BaseModel):
    doctor_id: int
    slot_id: int
    date: date  # <-- added appointment date
    patient_name: str
    gender: Literal["male", "female", "other"]
    age: int
    address: str
    phone: str

class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    slot_id: int
    date: date  # <-- added appointment date
    patient_name: str
    gender: str
    age: int
    address: str
    phone: str

    class Config:
        orm_mode = True