from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.config import Base

class EducatorSlot(Base):
    __tablename__ = "educator_slots"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)

    educator_id = Column(Integer, ForeignKey("educators.id"))
    educator = relationship("Educator", back_populates="slots")

    # 🔧 Add this line to complete the relationship with appointments
    appointments = relationship("EducatorAppointment", back_populates="slot", cascade="all, delete")
