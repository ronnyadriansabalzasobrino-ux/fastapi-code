from fastapi import APIRouter
from app.controllers.Students_controller import StudentsController
from app.models.Students_model import students
from app.services.email_service import send_email, ADMIN_EMAIL  # 🔥 IMPORTANTE

router = APIRouter()
students_controller = StudentsController()


@router.post("/students")
async def create_student(student: students):

    result = students_controller.create_student(student)

    # 🔥 CORREO AL CREAR
    try:
        await send_email(
            destinatario=ADMIN_EMAIL,
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
async def get_student(id_student:int):
    return students_controller.get_student(id_student)


@router.put("/students/{id_student}")
async def update_student(id_student:int,student:students):
    return students_controller.update_student(id_student,student)


@router.delete("/students/{id_student}")
async def delete_student(id_student:int):

    # 🔥 1. obtener info antes de borrar
    student = students_controller.get_student(id_student)

    # 🔥 2. eliminar
    result = students_controller.delete_student(id_student)

    # 🔥 3. enviar correo
    try:
        if student:
            await send_email(
                destinatario=ADMIN_EMAIL,
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


# 🔥 POWER BI
@router.get("/students_public")
async def students_public():
    return students_controller.get_students()