from app.models.user import User

async def get_user(username: str):
    return await User.get(username=username)