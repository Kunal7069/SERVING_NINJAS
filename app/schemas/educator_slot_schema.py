from pydantic import BaseModel

class EducatorSlotCreate(BaseModel):
    start_time: str
    end_time: str

class EducatorSlotResponse(BaseModel):
    id: int
    start_time: str
    end_time: str

    class Config:
        orm_mode = True
