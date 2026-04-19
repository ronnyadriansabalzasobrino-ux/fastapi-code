from fastapi import APIRouter, HTTPException
from app.controllers.Alerts_controller import AlertsController
from app.models.Alerts_model import Alerts

router = APIRouter()
nueva_Alerts = AlertsController()

@router.post("/create_Alerts")
async def create_Alerts(alert: Alerts):
    return nueva_Alerts.create_Alerts(alert)

@router.get("/get_Alerts/")
async def get_Alerts():
    return nueva_Alerts.get_Alerts()

@router.get("/get_Alerts/{id_Alerts}")
async def get_Alert(id_Alerts: int):
    return nueva_Alerts.get_Alert(id_Alerts)

@router.put("/update_Alerts/{id_Alerts}")
async def update_Alerts(id_Alerts: int, alert: Alerts):
    return nueva_Alerts.update_Alerts(id_Alerts, alert)

@router.delete("/delete_Alerts/{id_Alerts}")
async def delete_Alerts(id_Alerts: int):
    return nueva_Alerts.delete_Alerts(id_Alerts)

# 🔥 NUEVO (POWER BI)
@router.get("/alerts_public")
async def alerts_public():
    return nueva_Alerts.get_Alerts()
