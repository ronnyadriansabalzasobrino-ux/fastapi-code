from fastapi import APIRouter
from controllers.Semesters_controller import SemestersController
from models.Semesters_model import Semesters

router = APIRouter()
semester_controller = SemestersController()


@router.post("/semesters")
async def create_semester(semester: Semesters):
    return semester_controller.create_semester(semester)



@router.get("/semesters/{id_semester}", response_model=Semesters)
async def get_semester(id_semester: int):
    return semester_controller.get_semester(id_semester)


@router.get("/semesters")
async def get_semesters():
    return semester_controller.get_semesters()



@router.put("/semesters/{id_semester}")
async def update_semester(id_semester: int, semester: Semesters):
    return semester_controller.update_semester(id_semester, semester)



@router.delete("/semesters/{id_semester}")
async def delete_semester(id_semester: int):
    return semester_controller.delete_semester(id_semester)