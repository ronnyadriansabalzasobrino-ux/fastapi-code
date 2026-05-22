# Teacher_routes.py

from fastapi import APIRouter
from app.controllers.Teacher_controller import *
from app.models.Teacher_model import Teacher
from app.services.email_service import send_email
from app.services.email_template import build_email
router = APIRouter()
nuevo_Teacher = TeacherController()


@router.post("/create_Teacher")
async def create_teacher(teacher: Teacher):

    result = nuevo_Teacher.create_Teacher(teacher)

    try:
        html = build_email(
            "Nuevo docente registrado",
            "Se ha registrado un nuevo docente en el sistema.",
            f"""
            <b>Nombre:</b> {teacher.name} {teacher.last_name}<br>
            <b>Email:</b> {teacher.mail}<br>
            <b>Especialidad:</b> {teacher.specialty}<br>
            """
        )
        send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="👨‍🏫 Nuevo docente creado",
            contenido=html
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
        html = build_email(
            "Docente actualizado",  
            "Se ha actualizado la información de un docente en el sistema.",
            f"""
            <b>Nombre:</b> {Teacher.name} {Teacher.last_name}<br>
            <b>Email:</b> {Teacher.mail}<br>
            <b>Especialidad:</b> {Teacher.specialty}<br>
            """
        )
        send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="✏️ Docente actualizado",
            contenido=html
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


        
       

   


@router.delete("/delete_Teacher/{id_Teaching}")
async def delete_Teacher(id_Teaching: int):

    teacher = nuevo_Teacher.get_Teacher(id_Teaching)

    result = nuevo_Teacher.delete_Teacher(id_Teaching)

    try:
        html = build_email(
            "Docente eliminado",
            "Se ha eliminado un docente del sistema.",
            f"""
            <b>Nombre:</b> {teacher.get("name")} {teacher.get("last_name")}<br>
            <b>Email:</b> {teacher.get("mail")}<br>
            """
        )
        send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="🗑️ Docente eliminado",
            contenido=html
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.get("/teachers_public")
async def teachers_public():
    return nuevo_Teacher.get_Teachers()