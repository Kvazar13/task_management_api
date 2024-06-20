from tortoise.exceptions import DoesNotExist
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

async def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    user_obj = await User.create(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    return user_obj

async def get_user(user_id: int):
    return await User.filter(id=user_id).first()