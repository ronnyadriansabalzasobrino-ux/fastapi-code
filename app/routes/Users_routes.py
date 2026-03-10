from fastapi import APIRouter
from controllers.Users_controller import UserController
from models.Users_model import Users

router = APIRouter()
user_controller = UserController()



@router.post("/users")
async def create_user(user: Users):
    return user_controller.create_User(user)



@router.get("/users/{id_user}", response_model=Users)
async def get_user(id_user: int):
    return user_controller.get_user(id_user)



@router.get("/users")
async def get_users():
    return user_controller.get_User()



@router.put("/users/{id_user}")
async def update_user(id_user: int, user: Users):
    return user_controller.update_user(id_user, user)



@router.delete("/users/{id_user}")
async def delete_user(id_user: int):
    return user_controller.delete_user(id_user)