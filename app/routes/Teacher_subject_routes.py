from fastapi import APIRouter
from controllers.Teacher_subject_controller import *
from models.Teacher_subject_model import Teacher_subject

router = APIRouter()
nuevo_Teacher_subject = None

@router.post("/create_Teacher_subject")
async def create_Teacher_subject(data: Teacher_subject):
    return nuevo_Teacher_subject.create_Teacher_subject(data)

@router.get("/get_Teacher_subject/{id_Teacher_subject}", response_model=Teacher_subject)
async def get_Teacher_subject(id_Teacher_subject: int):
    return nuevo_Teacher_subject.get_Teacher_subject(id_Teacher_subject)

@router.get("/get_Teacher_subject/")
async def get_Teacher_subject():
    return nuevo_Teacher_subject.get_Teacher_subjects()

@router.put("/update_Teacher_subject/{id_Teacher_subject}")
async def update_Teacher_subject(id_Teacher_subject: int, data: Teacher_subject):
    return nuevo_Teacher_subject.update_Teacher_subject(id_Teacher_subject, data)

@router.delete("/delete_Teacher_subject/{id_Teacher_subject}")
async def delete_Teacher_subject(id_Teacher_subject: int):
    return nuevo_Teacher_subject.delete_Teacher_subject(id_Teacher_subject)