from app.models.task import Task
from app.schemas.task import TaskCreate

async def create_task(task: TaskCreate, user_id: int):
    task_obj = await Task.create(
        **task.dict(),
        owner_id=user_id
    )
    return task_obj

async def get_tasks(user_id: int):
    return await Task.filter(owner_id=user_id).all()