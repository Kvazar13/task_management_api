from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.task import TaskCreate, Task
from app.crud.task import create_task, get_tasks

router = APIRouter()

@router.post("/", response_model=Task)
async def create_task_endpoint(task: TaskCreate, user_id: int):
    task_obj = await create_task(task, user_id)
    return task_obj

@router.get("/", response_model=List[Task])
async def get_tasks_endpoint(user_id: int):
    tasks = await get_tasks(user_id)
    return tasks