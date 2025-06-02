from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session
from typing import List
from app.database.config import SessionLocal
from app.schemas.doctor_schema import DoctorCreate,DoctorResponse
from app.schemas.slot_schema import SlotResponse
from app.services.doctor_service import get_free_slots_by_doctor
from app.services.doctor_service import create_doctor_with_slots, get_all_doctors_with_slots


from pydantic import BaseModel
class DoctorIdRequest(BaseModel):
    doctor_id: int

router = APIRouter(prefix="/doctor", tags=["Doctor"])

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    saved_doctor = create_doctor_with_slots(db, doctor.dict())
    return {"message": "Doctor added successfully", "doctor_id": saved_doctor.id}


@router.get("/", response_model=List[DoctorResponse])
def get_all_doctors(db: Session = Depends(get_db)):
    return get_all_doctors_with_slots(db)


@router.post("/free-slots/", response_model=List[SlotResponse])
def free_slots(request: DoctorIdRequest, db: Session = Depends(get_db)):
    return get_free_slots_by_doctor(db, request.doctor_id)