# Teacher_routes.py

from fastapi import APIRouter
from app.controllers.Teacher_controller import *
from app.models.Teacher_model import Teacher
from app.services.email_service import send_email

router = APIRouter()
nuevo_Teacher = TeacherController()


@router.post("/create_Teacher")
async def create_teacher(teacher: Teacher):

    result = nuevo_Teacher.create_Teacher(teacher)

    try:
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="👨‍🏫 Nuevo docente creado",
            contenido=f"""
            <h2>Nuevo docente registrado</h2>

            <p><b>Nombre:</b> {teacher.name} {teacher.last_name}</p>
            <p><b>Email:</b> {teacher.mail}</p>
            <p><b>Especialidad:</b> {teacher.specialty}</p>

            <hr>
            <p>Sistema académico</p>
            """
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.get("/get_Teacher/{id_Teaching}", response_model=Teacher)
async def get_Teacher(id_Teaching: int):
    return nuevo_Teacher.get_Teacher(id_Teaching)


@router.get("/get_Teacher/")
async def get_Teachers():
    return nuevo_Teacher.get_Teachers()


@router.put("/update_Teacher/{id_Teaching}")
async def update_Teacher(id_Teaching: int, Teacher: Teacher):

    result = nuevo_Teacher.update_Teacher(id_Teaching, Teacher)

    try:
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="✏️ Docente actualizado",
            contenido=f"""
            <h2>Docente actualizado</h2>

            <p><b>Nombre:</b> {Teacher.name} {Teacher.last_name}</p>
            <p><b>Email:</b> {Teacher.mail}</p>
            <p><b>Especialidad:</b> {Teacher.specialty}</p>

            <hr>
            <p>Sistema académico</p>
            """
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.delete("/delete_Teacher/{id_Teaching}")
async def delete_Teacher(id_Teaching: int):

    teacher = nuevo_Teacher.get_Teacher(id_Teaching)

    result = nuevo_Teacher.delete_Teacher(id_Teaching)

    try:
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="🗑️ Docente eliminado",
            contenido=f"""
            <h2>Docente eliminado</h2>

            <p><b>Nombre:</b> {teacher.get("name")} {teacher.get("last_name")}</p>
            <p><b>Email:</b> {teacher.get("mail")}</p>

            <hr>
            <p>Sistema académico</p>
            """
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.get("/teachers_public")
async def teachers_public():
    return nuevo_Teacher.get_Teachers()