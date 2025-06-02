from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.config import SessionLocal
from app.schemas.user_schema import UserCreate, UserResponse,UserLogin
from app.services.user_service import create_user,login_user

router = APIRouter(prefix="/user", tags=["User"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.dict())

@router.post("/login", response_model=UserResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user.email, user.password)
