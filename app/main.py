import os
from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.config import TORTOISE_ORM

# Load environment variables
load_dotenv()

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Task Management API!"}