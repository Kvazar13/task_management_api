from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

async def create_task(task: TaskCreate, user_id: int):
    task_obj = await Task.create(
        title=task.title,
        description=task.description,
        completed=False,
        due_date=None,
        owner_id=user_id
    )
    return task_obj

async def get_tasks(user_id: int):
    return await Task.filter(owner_id=user_id).all()

async def update_task(task_id: int, task: TaskUpdate, user_id: int):
    task_obj = await Task.filter(id=task_id, owner_id=user_id).first()
    if task_obj:
        task_data = task.dict(exclude_unset=True)
        task_obj.update_from_dict(task_data)
        await task_obj.save()
        return task_obj
    return None