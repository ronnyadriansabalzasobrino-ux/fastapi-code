from fastapi import APIRouter
from controllers.Programs_controller import *
from models.Programs_model import Programs

router = APIRouter()
new_program = ProgramsController()


@router.post("/programs")
async def create_program(program: Programs):
    return new_program.create_program(program)


@router.get("/programs/{id_program}", response_model=Programs)
async def get_program(id_program: int):
    return new_program.get_program(id_program)


@router.get("/programs")
async def get_programs():
    return new_program.get_programs()


@router.put("/programs/{id_program}")
async def update_program(id_program: int, program: Programs):
    return new_program.update_program(id_program, program)


@router.delete("/programs/{id_program}")
async def delete_program(id_program: int):
    return new_program.delete_program(id_program)