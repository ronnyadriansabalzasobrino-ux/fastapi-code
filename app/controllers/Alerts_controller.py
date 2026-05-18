# controllers/Alerts_controller.py

import psycopg2
import asyncio

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.config.db_config import get_db_connection
from app.models.Alerts_model import Alerts
from app.services.email_service import send_email


class AlertsController:

    # =========================
    # CREATE ALERT
    # =========================
    def create_Alerts(self, alert: Alerts):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO alerts
                (id_student, tipo_alert, description, generation_date, risk_level, state, id_period)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                RETURNING id_alert
            """,(
                alert.id_student,
                alert.tipo_alert,
                alert.description,
                alert.generation_date,
                alert.risk_level,
                alert.state,
                alert.id_period
            ))

            new_id = cursor.fetchone()[0]

            conn.commit()

            # =========================
            # ENVIAR CORREO
            # =========================

            student_mail = self.get_student_email(alert.id_student)

            if student_mail:

                asyncio.run(send_email(
                    student_mail,
                    "Nueva alerta académica",
                    f"""
                    <h2>⚠️ Nueva alerta académica</h2>

                    <p>Se ha generado una nueva alerta en el sistema.</p>

                    <ul>
                        <li><b>Tipo:</b> {alert.tipo_alert}</li>
                        <li><b>Descripción:</b> {alert.description}</li>
                        <li><b>Riesgo:</b> {alert.risk_level}</li>
                        <li><b>Estado:</b> {alert.state}</li>
                    </ul>
                    """
                ))

            cursor.close()
            conn.close()

            return {
                "resultado": "Alert creada correctamente",
                "id_alert": new_id
            }

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))


    # =========================
    # OBTENER MAIL ESTUDIANTE
    # =========================
    def get_student_email(self, id_student: int):

        conn = None
        cursor = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT mail FROM students
                WHERE id_student = %s
            """, (id_student,))

            result = cursor.fetchone()

            return result[0] if result else None

        except Exception as e:
            print("Error obteniendo mail:", e)
            return None

        finally:

            if cursor:
                cursor.close()

            if conn:
                conn.close()


    # =========================
    # GET ALL
    # =========================
    def get_Alerts(self):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM alerts")

            result = cursor.fetchall()

            payload = []

            for row in result:

                payload.append({
                    "id_alert": row[0],
                    "id_student": row[1],
                    "tipo_alert": row[2],
                    "description": row[3],
                    "generation_date": row[4],
                    "risk_level": row[5],
                    "state": row[6],
                    "id_period": row[7]
                })

            cursor.close()
            conn.close()

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))


    # =========================
    # GET ONE
    # =========================
    def get_Alert(self, id_alert: int):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM alerts WHERE id_alert=%s",
                (id_alert,)
            )

            row = cursor.fetchone()

            if not row:
                raise HTTPException(
                    status_code=404,
                    detail="Alert no encontrada"
                )

            content = {
                "id_alert": row[0],
                "id_student": row[1],
                "tipo_alert": row[2],
                "description": row[3],
                "generation_date": row[4],
                "risk_level": row[5],
                "state": row[6],
                "id_period": row[7]
            }

            cursor.close()
            conn.close()

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))


    # =========================
    # UPDATE ALERT
    # =========================
    def update_Alerts(self, id_alert: int, alert: Alerts):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE alerts
                SET id_student=%s,
                    tipo_alert=%s,
                    description=%s,
                    generation_date=%s,
                    risk_level=%s,
                    state=%s,
                    id_period=%s
                WHERE id_alert=%s
            """,(
                alert.id_student,
                alert.tipo_alert,
                alert.description,
                alert.generation_date,
                alert.risk_level,
                alert.state,
                alert.id_period,
                id_alert
            ))

            conn.commit()

            # =========================
            # CORREO UPDATE
            # =========================

            student_mail = self.get_student_email(alert.id_student)

            if student_mail:

                asyncio.run(send_email(
                    student_mail,
                    "Alerta actualizada",
                    f"""
                    <h2>⚠️ Alerta actualizada</h2>

                    <p>Tu alerta académica fue actualizada.</p>

                    <ul>
                        <li><b>Tipo:</b> {alert.tipo_alert}</li>
                        <li><b>Riesgo:</b> {alert.risk_level}</li>
                        <li><b>Estado:</b> {alert.state}</li>
                    </ul>
                    """
                ))

            cursor.close()
            conn.close()

            return {"resultado": "Alert actualizada correctamente"}

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))


    # =========================
    # DELETE ALERT
    # =========================
    def delete_Alerts(self, id_alert: int):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            # =========================
            # OBTENER ID STUDENT
            # =========================

            cursor.execute("""
                SELECT id_student
                FROM alerts
                WHERE id_alert=%s
            """, (id_alert,))

            result = cursor.fetchone()

            student_mail = None

            if result:
                student_mail = self.get_student_email(result[0])

            # =========================
            # DELETE
            # =========================

            cursor.execute("""
                DELETE FROM alerts
                WHERE id_alert=%s
            """, (id_alert,))

            conn.commit()

            # =========================
            # CORREO DELETE
            # =========================

            if student_mail:

                asyncio.run(send_email(
                    student_mail,
                    "Alerta eliminada",
                    """
                    <h2>Alerta eliminada</h2>

                    <p>La alerta académica fue eliminada correctamente.</p>
                    """
                ))

            cursor.close()
            conn.close()

            return {"resultado": "Alert eliminada correctamente"}

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))
