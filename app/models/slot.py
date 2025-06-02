from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.config import Base

class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(String, nullable=False)  # e.g. "14:00"
    end_time = Column(String, nullable=False)    # e.g. "14:15"

    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    doctor = relationship("Doctor", back_populates="slots")
    
    appointments = relationship("DoctorAppointment", back_populates="slot")
