from fastapi import APIRouter
from app.controllers.Students_controller import StudentsController
from app.models.Students_model import students

router = APIRouter()
students_controller = StudentsController()

@router.post("/students")
async def create_student(student: students):
    return students_controller.create_student(student)

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
    return students_controller.delete_student(id_student)

# 🔥 POWER BI
@router.get("/students_public")
async def students_public():
    return students_controller.get_students()