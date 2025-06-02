from pydantic import BaseModel
from typing import List

class SlotCreate(BaseModel):
    start_time: str
    end_time: str

class DoctorCreate(BaseModel):
    center_name: str
    doctor_name: str
    address: str
    phone: str
    city: str
    speciality: str
    slots: List[SlotCreate]
    
    

class SlotResponse(BaseModel):
    id: int
    start_time: str
    end_time: str

    class Config:
        orm_mode = True

class DoctorResponse(BaseModel):
    id: int
    center_name: str
    doctor_name: str
    address: str
    phone: str
    city: str
    speciality: str
    slots: List[SlotResponse] = []

    class Config:
        orm_mode = True