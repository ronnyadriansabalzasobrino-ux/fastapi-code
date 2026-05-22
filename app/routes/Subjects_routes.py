# Subjects_routes.py

from fastapi import APIRouter
from app.controllers.Subjects_controller import *
from app.models.Subjects_model import Subjects
from app.services.email_service import send_email
from app.services.email_template import build_email
router = APIRouter()
new_subject = SubjectsController()


@router.post("/subjects")
async def create_subject(subject: Subjects):

    result = new_subject.create_subject(subject)

    try:
        html = build_email(
            "Nueva materia registrada",
            "Se ha registrado una nueva materia en el sistema.",
            f"""
            <b>Materia:</b> {subject.name_subject}<br>
            <b>Créditos:</b> {subject.credits}<br>
            <b>ID Programa:</b> {subject.id_program}<br>
            """
        )
        send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="📘 Nueva materia creada",
            contenido=html
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
        html = build_email(
            "Materia actualizada",
            "Se ha actualizado la información de una materia en el sistema.",
            f"""
            <b>Materia:</b> {subject.name_subject}<br>
            <b>Créditos:</b> {subject.credits}<br>
            <b>ID Programa:</b> {subject.id_program}<br>
            """
        )
        send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="✏️ Materia actualizada",
            contenido=html
        )

    except Exception as e:
        print("Error enviando correo:", e)
        return result


@router.delete("/subjects/{id_subject}")
async def delete_subject(id_subject: int):

    subject = new_subject.get_subject(id_subject)

    result = new_subject.delete_subject(id_subject)

    try:
        html = build_email(
            "Materia eliminada",
            "Se ha eliminado una materia del sistema.",
            f"""
            <b>Materia:</b> {subject.get("name_subject")}<br>
            """
        )
        send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="🗑️ Materia eliminada",
            contenido=html
        )

    except Exception as e:
        print("Error enviando correo:", e)

    return result


# 🔥 POWER BI
@router.get("/subjects_public")
async def subjects_public():
    return new_subject.get_subjects()