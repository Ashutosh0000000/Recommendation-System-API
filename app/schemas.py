from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    model_config = {"from_attributes": True}  # replaces orm_mode=True


class Token(BaseModel):
    access_token: str
    token_type: str

class ActivityCreate(BaseModel):
    item_id: int
    action: str

class ActivityRead(BaseModel):
    id: int
    user_id: int
    item_id: int
    action: str
    timestamp: datetime
    class Config:
        orm_mode = True

class UserStats(BaseModel):
    user_id: int
    total_activities: int
    top_items: List[int]
