from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.config import SessionLocal
from app.schemas.educator_schema import EducatorCreate, EducatorResponse
from app.schemas.educator_slot_schema import EducatorSlotResponse
from app.services.educator_service import (
    create_educator_with_slots,
    get_all_educators_with_slots,
    get_free_slots_by_educator
)
from datetime import date
from pydantic import BaseModel

class EducatorIdRequest(BaseModel):
    educator_id: int
    date: date

router = APIRouter(prefix="/educator", tags=["Educator"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_educator(educator: EducatorCreate, db: Session = Depends(get_db)):
    saved_educator = create_educator_with_slots(db, educator.dict())
    return {"message": "Educator added successfully", "educator_id": saved_educator.id}

@router.get("/", response_model=List[EducatorResponse])
def get_all_educators(db: Session = Depends(get_db)):
    return get_all_educators_with_slots(db)

@router.post("/free-slots/", response_model=List[EducatorSlotResponse])
def free_slots(request: EducatorIdRequest, db: Session = Depends(get_db)):
    return get_free_slots_by_educator(db, request.educator_id, request.date)
