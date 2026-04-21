from fastapi import APIRouter, Query
from app.controllers.Reports_controller import ReportsController    

router = APIRouter()
reports_controller = ReportsController()


@router.get("/reports/pdf")
def generate_report(
    risk_level: str = Query(None),
    state: str = Query(None),
    id_program: int = Query(None)
):
    return reports_controller.generate_pdf_report(
        risk_level, state, id_program
    )