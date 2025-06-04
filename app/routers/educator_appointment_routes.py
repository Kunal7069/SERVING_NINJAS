from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database.config import SessionLocal
from app.schemas.educator_appointment_schema import EducatorAppointmentCreate, EducatorAppointmentResponse
from app.models.educator import Educator
from app.services.educator_appointment_service import (
    create_educator_appointment,
    get_appointments_by_student_name,
    get_appointments_by_educator_id
)

router = APIRouter(prefix="/educator-appointment", tags=["Educator Appointments"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EducatorAppointmentResponse)
def book_educator_appointment(appointment: EducatorAppointmentCreate, db: Session = Depends(get_db)):
    return create_educator_appointment(db, appointment.dict())


class StudentNameRequest(BaseModel):
    student_name: str

@router.post("/by-student")
def get_appointments_for_student(data: StudentNameRequest, db: Session = Depends(get_db)):
    appointments = get_appointments_by_student_name(db, data.student_name)
    result= []
    if not appointments:
        return result
    return appointments


class EducatorNameRequest(BaseModel):
    educator_name: str

@router.post("/by-educator")
def get_appointments_for_educator(data: EducatorNameRequest, db: Session = Depends(get_db)):
    educator = db.query(Educator).filter(Educator.educator_name == data.educator_name).first()
    if not educator:
        raise HTTPException(status_code=404, detail="Educator not found.")

    appointments = get_appointments_by_educator_id(db, educator.id)
    result= []
    if not appointments:
        return result
    return appointments
