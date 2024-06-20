from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.task import TaskCreate, Task, TaskUpdate
from app.crud.task import create_task, get_tasks, update_task
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

@router.put("/{task_id}", response_model=Task)
async def update_task_endpoint(task_id: int, task: TaskUpdate, user: User = Depends(get_current_user)):
    task_obj = await update_task(task_id, task, user.id)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_obj