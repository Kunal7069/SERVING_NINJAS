from pydantic import BaseModel

class SlotResponse(BaseModel):
    id: int
    start_time: str
    end_time: str

    class Config:
        orm_mode = True