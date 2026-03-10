from fastapi import APIRouter
from controllers.Subjects_controller import *
from models.Subjects_model import Subjects

router = APIRouter()
new_subject = SubjectsController()


@router.post("/subjects")
async def create_subject(subject: Subjects):
    return new_subject.create_subject(subject)


@router.get("/subjects/{id_subject}", response_model=Subjects)
async def get_subject(id_subject: int):
    return new_subject.get_subject(id_subject)


@router.get("/subjects")
async def get_subjects():
    return new_subject.get_subjects()


@router.put("/subjects/{id_subject}")
async def update_subject(id_subject: int, subject: Subjects):
    return new_subject.update_subject(id_subject, subject)


@router.delete("/subjects/{id_subject}")
async def delete_subject(id_subject: int):
    return new_subject.delete_subject(id_subject)