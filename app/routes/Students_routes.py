# Students_routes.py

from fastapi import APIRouter
from app.controllers.Students_controller import StudentsController
from app.models.Students_model import students
from app.services.email_service import send_email
from app.services.email_template import build_email

router = APIRouter()
students_controller = StudentsController()


@router.post("/students")
async def create_student(student: students):

    result = students_controller.create_student(student)

    try:
        html = build_email(
            "Nuevo estudiante registrado",
            "Se ha registrado un nuevo estudiante.",
            f""" 
            <b>Nombre:</b> {student.name} {student.last_name}<br>
            <b>Email:</b> {student.mail}<br>   
            <b>ID:</b> {student.number_id}<br>
            """ 
        )
        send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="👨‍🎓 Nuevo estudiante creado",
            contenido=html
          
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.get("/students")
async def get_students():
    return students_controller.get_students()


@router.get("/students/{id_student}")
async def get_student(id_student: int):
    return students_controller.get_student(id_student)


@router.put("/students/{id_student}")
async def update_student(id_student: int, student: students):

    result = students_controller.update_student(id_student, student)

    try:
        html = build_email(
            "Estudiante actualizado",
            "Se ha actualizado la información de un estudiante.",
            f""" 
            <b>Nombre:</b> {student.name} {student.last_name}<br>
            <b>Email:</b> {student.mail}<br>   
            <b>ID:</b> {student.number_id}<br>
            """ 
        )
        send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="✏️ Estudiante actualizado",
            contenido=html
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.delete("/students/{id_student}")
async def delete_student(id_student: int):

    student = students_controller.get_student(id_student)

    result = students_controller.delete_student(id_student)

    try:
        if student:
            html= build_email(
                "Estudiante eliminado",
                "Se ha eliminado un estudiante del sistema.",
                f"""
                <b>Nombre:</b> {student.get("name")} {student.get("last_name")}<br>
                <b>Email:</b> {student.get("mail")}<br>   
                <b>ID:</b> {id_student}<br>
                """
            )
            send_email(
                destinatario="ronnyadriansabalzasobrino@gmail.com",
                asunto="🗑️ Estudiante eliminado",
                contenido=html
            )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.get("/students_public")
async def students_public():
    return students_controller.get_students()