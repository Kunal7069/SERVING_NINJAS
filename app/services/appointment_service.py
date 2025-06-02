from sqlalchemy.orm import Session
from app.models.appointment import DoctorAppointment

def create_appointment(db: Session, appointment_data: dict):
    appointment = DoctorAppointment(**appointment_data)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment
