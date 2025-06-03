from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.config import Base

class Educator(Base):
    __tablename__ = "educators"

    id = Column(Integer, primary_key=True, index=True)
    center_name = Column(String, nullable=False)
    educator_name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)

    slots = relationship("EducatorSlot", back_populates="educator", cascade="all, delete")
    
    # 🔧 Add this line to define the reverse relationship
    appointments = relationship("EducatorAppointment", back_populates="educator", cascade="all, delete")