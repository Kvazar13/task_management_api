import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from app.config import TORTOISE_ORM
from app.api import users, tasks
from app.core.security import get_current_user
from app.schemas.user import User

# Load environment variables
load_dotenv()

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # Disable auto-generation, rely on Aerich
    add_exception_handlers=True,
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Task Management API!"}

@app.get("/users/me", tags=["users"])
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user