from fastapi import APIRouter
from app.controllers.Alerts_controller import AlertsController
from app.models.Alerts_model import Alerts
from app.services.email_service import send_email
from app.config.db_config import get_db_connection

router = APIRouter()
nueva_Alerts = AlertsController()


@router.post("/create_Alerts")
async def create_Alerts(alert: Alerts):

    # 1. CREAR ALERTA
    result = nueva_Alerts.create_Alerts(alert)

    # 2. OBTENER EMAIL
    student_mail = nueva_Alerts.get_student_email(alert.id_student)

    # 3. ENVIAR CORREO
    if student_mail:
        await send_email(
            destinatario=student_mail,
            asunto="⚠️ Nueva alerta académica",
            contenido=f"""
            Hola 👋

            Se ha generado una nueva alerta en tu cuenta:

            📌 Tipo: {alert.tipo_alert}
            📌 Descripción: {alert.description}
            📌 Nivel de riesgo: {alert.risk_level}

            Por favor revisa el sistema.
            """
        )

    return result


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
