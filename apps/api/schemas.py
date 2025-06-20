from datetime import datetime
from pydantic import BaseModel

class PostCreate(BaseModel):
    text: str

class PostRead(BaseModel):
    id: int
    text: str
    created_at: datetime

    class Config:
        orm_mode = True
