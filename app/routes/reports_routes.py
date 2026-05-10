from fastapi import APIRouter
from app.controllers.Reports_controller import ReportsController

router = APIRouter()

reports_controller = ReportsController()

@router.get("/reports/data")
def get_reports_data():
    return reports_controller.get_reports_data()