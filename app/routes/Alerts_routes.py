from fastapi import APIRouter
from controllers.Alerts_controller import *
from models.Alerts_model import Alerts

router = APIRouter()
nueva_Alerts = AlertsController()

@router.post("/create_Alerts")
async def create_Alerts(Alerts: Alerts):
    return nueva_Alerts.create_Alerts(Alerts)

@router.get("/get_Alerts/{id_Alerts}", response_model=Alerts)
async def get_Alerts(id_Alerts: int):
    return nueva_Alerts.get_Alerts(id_Alerts)

@router.get("/get_Alerts/")
async def get_Alerts():
    return nueva_Alerts.get_Alerts()

@router.put("/update_Alerts/{id_Alerts}")
async def update_Alerts(id_Alerts: int, Alerts: Alerts):
    return nueva_Alerts.update_Alerts(id_Alerts, Alerts)

@router.delete("/delete_Alerts/{id_Alerts}")
async def delete_Alerts(id_Alerts: int):
    return nueva_Alerts.delete_Alerts(id_Alerts)