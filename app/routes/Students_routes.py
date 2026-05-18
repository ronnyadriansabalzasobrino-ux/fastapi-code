# Students_routes.py

from fastapi import APIRouter
from app.controllers.Students_controller import StudentsController
from app.models.Students_model import students
from app.services.email_service import send_email

router = APIRouter()
students_controller = StudentsController()


@router.post("/students")
async def create_student(student: students):

    result = students_controller.create_student(student)

    try:
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="👨‍🎓 Nuevo estudiante creado",
            contenido=f"""
            <h2>Nuevo estudiante registrado</h2>

            <p><b>Nombre:</b> {student.name} {student.last_name}</p>
            <p><b>Email:</b> {student.mail}</p>
            <p><b>ID:</b> {student.number_id}</p>

            <hr>
            <p>Sistema académico</p>
            """
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
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="✏️ Estudiante actualizado",
            contenido=f"""
            <h2>Estudiante actualizado</h2>

            <p><b>Nombre:</b> {student.name} {student.last_name}</p>
            <p><b>Email:</b> {student.mail}</p>
            <p><b>ID:</b> {student.number_id}</p>

            <hr>
            <p>Sistema académico</p>
            """
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
            await send_email(
                destinatario="ronnyadriansabalzasobrino@gmail.com",
                asunto="🗑️ Estudiante eliminado",
                contenido=f"""
                <h2>Estudiante eliminado</h2>

                <p><b>Nombre:</b> {student.get("name")} {student.get("last_name")}</p>
                <p><b>Email:</b> {student.get("mail")}</p>
                <p><b>ID:</b> {id_student}</p>

                <hr>
                <p>Sistema académico</p>
                """
            )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.get("/students_public")
async def students_public():
    return students_controller.get_students()