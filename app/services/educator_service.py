from sqlalchemy.orm import Session
from app.models.educator import Educator
from app.models.educator_slot import EducatorSlot
from app.models.educator_appointment import EducatorAppointment
from datetime import date

def create_educator_with_slots(db: Session, educator_data: dict):
    # Extract slot info and remove from educator_data
    slot_list = educator_data.pop("slots", [])
    
    # Create educator object
    educator = Educator(**educator_data)
    
    # Create slot objects and link to educator
    for slot in slot_list:
        educator.slots.append(EducatorSlot(**slot))
    
    # Save to DB
    db.add(educator)
    db.commit()
    db.refresh(educator)
    return educator

def get_all_educators_with_slots(db: Session):
    return db.query(Educator).all()

def get_free_slots_by_educator(db: Session, educator_id: int, selected_date: date):
    # Get all slots for this educator
    all_slots = db.query(EducatorSlot).filter(EducatorSlot.educator_id == educator_id).all()

    # Get slot_ids already booked for the given date
    booked_slot_ids = db.query(EducatorAppointment.slot_id).filter(
        EducatorAppointment.educator_id == educator_id,
        EducatorAppointment.date == selected_date
    ).all()
    booked_slot_ids = [slot_id for (slot_id,) in booked_slot_ids]

    # Filter slots which are not booked
    free_slots = [slot for slot in all_slots if slot.id not in booked_slot_ids]

    return free_slots
