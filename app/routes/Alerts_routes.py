# Alerts_routes.py

from fastapi import APIRouter
from app.controllers.Alerts_controller import AlertsController
from app.models.Alerts_model import Alerts
from app.services.email_service import send_email
from app.config.db_config import get_db_connection
from app.services.email_template import build_email
router = APIRouter()
nueva_Alerts = AlertsController()


@router.post("/create_Alerts")
async def create_Alerts(alert: Alerts):

    result = nueva_Alerts.create_Alerts(alert)

    student_mail = nueva_Alerts.get_student_email(alert.id_student)

    if student_mail:

        try:
            html = build_email(
                "Nueva alerta académica",
                "Se ha generado una nueva alerta académica para ti.",
                f"""
                <b>tipo_alert:</b> {alert.tipo_alert}<br>
                <b>Descripción:</b> {alert.description}<br>
                <b>Riesgo:</b> {alert.risk_level}<br>
                <b>Estado:</b> {alert.state}<br>
                """

            )
            send_email(
                destinatario=student_mail,
                asunto="⚠️ Nueva alerta académica",
                contenido=html
            )

        except Exception as e:
            print("Error enviando correo:", e)

    return result


@router.get("/get_Alerts/")
async def get_Alerts():
    return nueva_Alerts.get_Alerts()


@router.get("/get_Alerts/{id_Alerts}")
async def get_Alert(id_Alerts: int):
    return nueva_Alerts.get_Alert(id_Alerts)


@router.put("/update_Alerts/{id_Alerts}")
async def update_Alerts(id_Alerts: int, alert: Alerts):

    result = nueva_Alerts.update_Alerts(id_Alerts, alert)

    student_mail = nueva_Alerts.get_student_email(alert.id_student)

    if student_mail:

        try:
            html = build_email(
                "Alerta actualizada",
                "Se ha actualizado la información de una alerta académica.",
                f"""
                <b>tipo_alert:</b> {alert.tipo_alert}<br>
                <b>Descripción:</b> {alert.description}<br>
                <b>Riesgo:</b> {alert.risk_level}<br>
                <b>Estado:</b> {alert.state}<br>
                """
            )
            send_email(
                destinatario=student_mail,
                asunto="✏️ Alerta actualizada",
                contenido=html
            )

        except Exception as e:
            print("Error enviando correo:", e)

    return result



@router.delete("/delete_Alerts/{id_Alerts}")
async def delete_Alerts(id_Alerts: int):

    alert = nueva_Alerts.get_Alert(id_Alerts)

    result = nueva_Alerts.delete_Alerts(id_Alerts)

    try:
        html = build_email(
            "Alerta eliminada",
            "Se ha eliminado una alerta académica del sistema.",
            f"""
            <b>ID:</b> {id_Alerts}<br>
            """
        )
        await send_email(
            destinatario="ronnyadriansabalzasobrino@gmail.com",
            asunto="🗑️ Alerta eliminada",
            contenido=html
        )

    except Exception as e:
        print("Error enviando correo:", e)

    except Exception as e:
        print("Error enviando correo:", e)

    return result


@router.get("/alerts_public")
async def alerts_public():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            a.id_alert,
            s.name,
            s.last_name,
            s.mail,
            a.tipo_alert,
            a.description,
            a.risk_level,
            a.state,
            a.generation_date
        FROM alerts a
        JOIN students s ON a.id_student = s.id_student
    """)

    rows = cursor.fetchall()

    result = []

    for row in rows:
        result.append({
            "id_alert": row[0],
            "student": f"{row[1]} {row[2]}",
            "email": row[3],
            "tipo_alert": row[4],
            "description": row[5],
            "risk_level": row[6],
            "state": row[7],
            "date": str(row[8])
        })

    cursor.close()
    conn.close()

    return result       
