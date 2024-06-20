from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.task import TaskCreate, Task
from app.crud.task import create_task, get_tasks
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Task)
async def create_task_endpoint(task: TaskCreate, user: User = Depends(get_current_user)):
    task_obj = await create_task(task, user.id)
    return task_obj

@router.get("/", response_model=List[Task])
async def get_tasks_endpoint(user: User = Depends(get_current_user)):
    tasks = await get_tasks(user.id)
    return tasks