from fastapi import APIRouter
from controllers.Assists_controller import *
from models.Assists_model import Assists

router = APIRouter()
nueva_Assists = AssistsController()

@router.post("/create_Assists")
async def create_Assists(Assists: Assists):
    return nueva_Assists.create_Assists(Assists)

@router.get("/get_Assists/{id_Assists}", response_model=Assists)
async def get_Assists(id_Assists: int):
    return nueva_Assists.get_Assists(id_Assists)

@router.get("/get_Assists/")
async def get_Assists():
    return nueva_Assists.get_Assists()

@router.put("/update_Assists/{id_Assists}")
async def update_Assists(id_Assists: int, Assists: Assists):
    return nueva_Assists.update_Assists(id_Assists, Assists)

@router.delete("/delete_Assists/{id_Assists}")
async def delete_Assists(id_Assists: int):
    return nueva_Assists.delete_Assists(id_Assists)