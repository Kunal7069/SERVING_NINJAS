from pydantic import BaseModel, EmailStr
from typing import Literal

class UserCreate(BaseModel):
    name : str
    email: EmailStr
    password: str
    role: Literal["user", "doctor", "educator"]

class UserResponse(BaseModel):
    id: int
    name : str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

