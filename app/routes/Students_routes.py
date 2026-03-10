from fastapi import APIRouter
from controllers.Students_controller import *
from models.Students_model import Students

router = APIRouter()
nuevo_estudiante = StudentsController()


@router.post("/students")
async def create_student(student: Students):
    return nuevo_estudiante.create_student(student)


@router.get("/students/{id_student}", response_model=Students)
async def get_student(id_student: int):
    return nuevo_estudiante.get_student(id_student)


@router.get("/students")
async def get_students():
    return nuevo_estudiante.get_students()


@router.put("/students/{id_student}")
async def update_student(id_student: int, student: Students):
    return nuevo_estudiante.update_student(id_student, student)


@router.delete("/students/{id_student}")
async def delete_student(id_student: int):
    return nuevo_estudiante.delete_student(id_student)