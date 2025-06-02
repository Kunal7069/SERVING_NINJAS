from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.models.slot import Slot
from app.models.appointment import DoctorAppointment

def create_doctor_with_slots(db: Session, doctor_data: dict):
    # Extract slot info and remove from doctor_data
    slot_list = doctor_data.pop("slots", [])
    
    # Create doctor object
    doctor = Doctor(**doctor_data)
    
    # Create slot objects and link to doctor
    for slot in slot_list:
        doctor.slots.append(Slot(**slot))
    
    # Save to DB
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

def get_all_doctors_with_slots(db: Session):
    return db.query(Doctor).all()

def get_free_slots_by_doctor(db: Session, doctor_id: int):
    # Get all slots for this doctor
    all_slots = db.query(Slot).filter(Slot.doctor_id == doctor_id).all()
    
    # Get slot_ids already booked
    booked_slot_ids = db.query(DoctorAppointment.slot_id).filter(DoctorAppointment.doctor_id == doctor_id).all()
    booked_slot_ids = [slot_id for (slot_id,) in booked_slot_ids]
    
    # Filter slots which are not booked
    free_slots = [slot for slot in all_slots if slot.id not in booked_slot_ids]
    
    return free_slots