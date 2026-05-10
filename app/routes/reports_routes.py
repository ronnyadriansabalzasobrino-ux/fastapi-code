from fastapi import APIRouter, Query
from app.controllers.Reports_controller import ReportsController

router = APIRouter()
reports_controller = ReportsController()


# 📄 GENERAR PDF (opcional)
@router.get("/reports/pdf")
def generate_report(
    risk_level: str = Query(None),
    state: str = Query(None),
    id_program: int = Query(None)
):
    return reports_controller.generate_pdf_report(
        risk_level,
        state,
        id_program
    )


# 🔥 OBTENER DATOS PARA PDF BONITO
@router.get("/reports/data")
def get_report_data(
    risk_level: str = Query(None),
    state: str = Query(None),
    id_program: int = Query(None)
):
    return reports_controller.get_report_data(
        risk_level,
        state,
        id_program
    )