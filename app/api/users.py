from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, User
from app.crud.user import create_user, get_user
from app.core.security import create_access_token
from tortoise.exceptions import IntegrityError

router = APIRouter()

@router.post("/", response_model=User)
async def register_user(user: UserCreate):
    try:
        user_obj = await create_user(user)
        return user_obj
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User with this email or username already exists")