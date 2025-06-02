from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.config import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    center_name = Column(String, nullable=False)
    doctor_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    city = Column(String, nullable=False)
    speciality = Column(String, nullable=False)

    slots = relationship("Slot", back_populates="doctor", cascade="all, delete")
    
    appointments = relationship("DoctorAppointment", back_populates="doctor")
