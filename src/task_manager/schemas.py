from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import enum

class Priority(str, enum.Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = ''
    priority: Optional[Priority] = Priority.medium
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[Priority] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None

class TaskOut(TaskBase):
    id: int
    status: str
    created_at: datetime
    completed: bool

    class Config:
        orm_mode = True
