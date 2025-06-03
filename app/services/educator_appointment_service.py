from sqlalchemy.orm import Session, joinedload
from app.models.educator_appointment import EducatorAppointment

def create_educator_appointment(db: Session, appointment_data: dict):
    appointment = EducatorAppointment(**appointment_data)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def get_appointments_by_student_name(db: Session, student_name: str):
    return (
        db.query(EducatorAppointment)
        .options(joinedload(EducatorAppointment.educator), joinedload(EducatorAppointment.slot))
        .filter(EducatorAppointment.student_name == student_name)
        .all()
    )

def get_appointments_by_educator_id(db: Session, educator_id: int):
    return (
        db.query(EducatorAppointment)
        .options(joinedload(EducatorAppointment.educator), joinedload(EducatorAppointment.slot))
        .filter(EducatorAppointment.educator_id == educator_id)
        .all()
    )
