from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    due_date: Optional[datetime]
    owner_id: int

    class Config:
        from_attributes = True