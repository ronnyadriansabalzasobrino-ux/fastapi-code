from fastapi import APIRouter, Depends
from app.controllers.Users_controller import UserController
from app.models.Users_model import Users
from app.auth.bearer_auth import JWTBearer
from pydantic import BaseModel

router = APIRouter()
user_controller = UserController()

class LoginData(BaseModel):
    mail: str
    password: str

# CRUD Users
@router.post("/users")
async def create_user(user: Users):
    return user_controller.create_User(user)

@router.get("/users", dependencies=[Depends(JWTBearer())])
async def get_users():
    return user_controller.get_User()

@router.get("/users/{id_user}", dependencies=[Depends(JWTBearer())])
async def get_user(id_user: int):
    return user_controller.get_user(id_user)

@router.put("/users/{id_user}", dependencies=[Depends(JWTBearer())])
async def update_user(id_user: int, user: Users):
    return user_controller.update_user(id_user, user)

@router.delete("/users/{id_user}", dependencies=[Depends(JWTBearer())])
async def delete_user(id_user: int):
    return user_controller.delete_user(id_user)

# Login
@router.post("/login")
async def login(data: LoginData):
    return user_controller.login(data.mail, data.password)