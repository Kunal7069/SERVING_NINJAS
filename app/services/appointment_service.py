
from sqlalchemy.orm import Session
from app.models.appointment import DoctorAppointment
from sqlalchemy.orm import joinedload


def create_appointment(db: Session, appointment_data: dict):
    appointment = DoctorAppointment(**appointment_data)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment



def get_appointments_by_patient_name(db: Session, patient_name: str):
    return (
        db.query(DoctorAppointment)
        .options(joinedload(DoctorAppointment.doctor), joinedload(DoctorAppointment.slot))
        .filter(DoctorAppointment.patient_name == patient_name)
        .all()
    )
    
def get_appointments_by_doctor_id(db: Session, doctor_id: int):
    return (
        db.query(DoctorAppointment)
        .options(joinedload(DoctorAppointment.doctor), joinedload(DoctorAppointment.slot))
        .filter(DoctorAppointment.doctor_id == doctor_id)
        .all()
    )