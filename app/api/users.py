from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, User
from app.crud.user import create_user
from app.utils import get_user
from app.core.security import create_access_token, verify_password
from tortoise.exceptions import IntegrityError

router = APIRouter()

@router.post("/", response_model=User)
async def register_user(user: UserCreate):
    try:
        user_obj = await create_user(user)
        return user_obj
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User with this email or username already exists")

@router.post("/token")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}