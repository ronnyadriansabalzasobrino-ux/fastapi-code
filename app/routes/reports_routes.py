from fastapi import APIRouter
from app.controllers.Reports_controller import ReportsController
from pydantic import BaseModel
from app.services.email_service import send_email
import base64

router = APIRouter()

class PDFReport(BaseModel):
    pdf:str

@router.post("/reports/send")
async def send_report(report: PDFReport):

    try:
        pdf_bytes = base64.b64decode(
            report.pdf
        )

        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="📊 Reporte académico",
            contenido="""
            <h2>
            se ha creado un nuevio reporte académico
            </h2>
            
            <p>
            se adjunta el reporte académico en formato PDF.
            </p>
            """,
            archivo=pdf_bytes
        )
        return {"message": "Reporte enviado por correo exitosamente."}
    
    except Exception as e:
        return{
            "error": str(e)
        }

    except Exception as e:
        print("ERROR ENVIANDO CORREO:", e)

reports_controller = ReportsController()

@router.get("/reports/data")
def get_reports_data():
    return reports_controller.get_reports_data()


@router.get("/reports/student/{mail}")
def get_student_reports(mail: str):
    return reports_controller.get_student_reports(mail)