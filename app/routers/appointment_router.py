from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.config import SessionLocal
from app.schemas.appointment_schema import AppointmentCreate, AppointmentResponse
from app.services.appointment_service import create_appointment

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
