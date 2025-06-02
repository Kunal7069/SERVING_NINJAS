from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database.config import SessionLocal
from app.schemas.appointment_schema import AppointmentCreate, AppointmentResponse
from app.models.doctor import Doctor
from app.services.appointment_service import create_appointment,get_appointments_by_patient_name,get_appointments_by_doctor_id
from app.services.doctor_service import get_all_doctors_with_slots
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

class DoctorIdRequest(BaseModel):
    doctor_name: str

@router.post("/by-doctor")
def get_appointments_for_doctor(data: DoctorIdRequest, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.doctor_name == data.doctor_name).first()

    appointments = get_appointments_by_doctor_id(db, doctor.id)
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found for this doctor.")
    return appointments