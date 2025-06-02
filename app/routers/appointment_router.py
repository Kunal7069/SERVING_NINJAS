from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database.config import SessionLocal
from app.schemas.appointment_schema import AppointmentCreate, AppointmentResponse
from app.services.appointment_service import create_appointment,get_appointments_by_patient_name

router = APIRouter(prefix="/appointment", tags=["Appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AppointmentResponse)
def book_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db, appointment.dict())

class PatientNameRequest(BaseModel):
    patient_name: str

@router.post("/by-patient")
def get_appointments_for_patient(data: PatientNameRequest, db: Session = Depends(get_db)):
    appointments = get_appointments_by_patient_name(db, data.patient_name)
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found for this patient.")
    return appointments