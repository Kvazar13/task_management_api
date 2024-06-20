from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    due_date: Optional[datetime]
    owner_id: int

    class Config:
        from_attributes = True