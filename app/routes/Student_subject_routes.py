from fastapi import APIRouter
from controllers.Student_subject_controller import *
from models.Student_subject_model import Student_subject

router = APIRouter()
nuevo_estudiante_materia = StudentSubjectController()

@router.post("/create_student_subject")
async def create_student_subject(data: Student_subject):
    return nuevo_estudiante_materia.create_student_subject(data)

@router.get("/get_student_subject/{id_student_subject}", response_model=Student_subject)
async def get_student_subject(id_student_subject: int):
    return nuevo_estudiante_materia.get_student_subject(id_student_subject)

@router.get("/get_student_subjects/")
async def get_student_subjects():
    return nuevo_estudiante_materia.get_student_subjects()

@router.put("/update_student_subject/{id_student_subject}")
async def update_student_subject(id_student_subject: int, data: Student_subject):
    return nuevo_estudiante_materia.update_student_subject(id_student_subject, data)

@router.delete("/delete_student_subject/{id_student_subject}")
async def delete_student_subject(id_student_subject: int):
    return nuevo_estudiante_materia.delete_student_subject(id_student_subject)