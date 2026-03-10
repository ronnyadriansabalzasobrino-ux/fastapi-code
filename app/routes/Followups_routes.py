from fastapi import APIRouter
from controllers.Followups_controller import *
from models.Followups_model import Followups

router = APIRouter()
new_followup = FollowupsController()


@router.post("/followups")
async def create_followup(data: Followups):
    return new_followup.create_Followups(data)


@router.get("/followups/{id_followup}", response_model=Followups)
async def get_followup(id_followup: int):
    return new_followup.get_Followup(id_followup)


@router.get("/followups")
async def get_followups():
    return new_followup.get_followups()



@router.put("/followups/{id_followup}")
async def update_followup(id_followup: int, data: Followups):
    return new_followup.update_followup(id_followup, data)


@router.delete("/followups/{id_followup}")
async def delete_followup(id_followup: int):
    return new_followup.delete_followup(id_followup)