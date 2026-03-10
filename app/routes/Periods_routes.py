from fastapi import APIRouter
from controllers.Periods_controller import *
from models.periods_model import periods

router = APIRouter()
nuevo_periods = PeriodController()

@router.post("/create_period")
async def create_period(period: periods):
    return nuevo_periods.create_period(period)

@router.get("/get_period/{id_period}", response_model=periods)
async def get_period(id_period: int):
    return nuevo_periods.get_period(id_period)

@router.get("/get_periods/")
async def get_periods():
    return nuevo_periods.get_periods()

@router.put("/update_period/{id_period}")
async def update_period(id_period: int, period: periods):
    return nuevo_periods.update_period(id_period, period)

@router.delete("/delete_period/{id_period}")
async def delete_period(id_period: int):
    return nuevo_periods.delete_period(id_period)