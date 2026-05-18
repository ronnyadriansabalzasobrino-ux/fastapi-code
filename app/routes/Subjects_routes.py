# Subjects_routes.py

from fastapi import APIRouter
from app.controllers.Subjects_controller import *
from app.models.Subjects_model import Subjects
from app.services.email_service import send_email

router = APIRouter()
new_subject = SubjectsController()


@router.post("/subjects")
async def create_subject(subject: Subjects):

    result = new_subject.create_subject(subject)

    try:
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="📘 Nueva materia creada",
            contenido=f"""
            <h2>Nueva materia registrada</h2>

            <p><b>Materia:</b> {subject.name_subject}</p>
            <p><b>Créditos:</b> {subject.credits}</p>
            <p><b>ID Programa:</b> {subject.id_program}</p>

            <hr>
            <p>Sistema académico</p>
            """
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.get("/subjects/{id_subject}")
async def get_subject(id_subject: int):
    return new_subject.get_subject(id_subject)


@router.get("/subjects")
async def get_subjects():
    return new_subject.get_subjects()


@router.put("/subjects/{id_subject}")
async def update_subject(id_subject: int, subject: Subjects):

    result = new_subject.update_subject(id_subject, subject)

    try:
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="✏️ Materia actualizada",
            contenido=f"""
            <h2>Materia actualizada</h2>

            <p><b>Materia:</b> {subject.name_subject}</p>
            <p><b>Créditos:</b> {subject.credits}</p>

            <hr>
            <p>Sistema académico</p>
            """
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.delete("/subjects/{id_subject}")
async def delete_subject(id_subject: int):

    subject = new_subject.get_subject(id_subject)

    result = new_subject.delete_subject(id_subject)

    try:
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="🗑️ Materia eliminada",
            contenido=f"""
            <h2>Materia eliminada</h2>

            <p><b>Materia:</b> {subject.get("name_subject")}</p>

            <hr>
            <p>Sistema académico</p>
            """
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


# 🔥 POWER BI
@router.get("/subjects_public")
async def subjects_public():
    return new_subject.get_subjects()