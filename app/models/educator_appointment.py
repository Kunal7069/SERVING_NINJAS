from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database.config import Base

class EducatorAppointment(Base):
    __tablename__ = "educator_appointments"

    id = Column(Integer, primary_key=True, index=True)
    educator_id = Column(Integer, ForeignKey("educators.id"))
    slot_id = Column(Integer, ForeignKey("educator_slots.id"))

    date = Column(Date, nullable=False)  # Appointment date

    student_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    educator = relationship("Educator", back_populates="appointments")
    slot = relationship("EducatorSlot", back_populates="appointments")