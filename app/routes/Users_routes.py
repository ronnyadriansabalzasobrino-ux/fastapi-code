from fastapi import APIRouter, Depends
from app.controllers.Users_controller import UserController
from app.models.Users_model import Users
from app.auth.bearer_auth import JWTBearer
from pydantic import BaseModel
from app.services.email_service import send_email  

router = APIRouter()
user_controller = UserController()

class LoginData(BaseModel):
    mail: str
    password: str


# =========================
# CRUD Users
# =========================

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


# 🔥 DELETE + CORREO
@router.delete("/users/{id_user}", dependencies=[Depends(JWTBearer())])
async def delete_user(id_user: int):

    # 1. eliminar usuario
    result = user_controller.delete_user(id_user)

    # 2. enviar correo al admin
    try:
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",  
            asunto="🗑️ Usuario eliminado",
            contenido=f"""
            <h2>Usuario eliminado</h2>

            <p>Se eliminó un usuario del sistema</p>

            <p><b>ID:</b> {id_user}</p>

            <hr>
            <p>Sistema de alertas</p>
            """
        )
    except Exception as e:
        print("Error enviando correo:", e)

    return result


# =========================
# LOGIN
# =========================
@router.post("/login")
async def login(data: LoginData):
    return user_controller.login(data.mail, data.password)