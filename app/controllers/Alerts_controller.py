# controllers/Alerts_controller.py
import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.Alerts_model import Alerts
from fastapi.encoders import jsonable_encoder
from app.services.email_service import send_email


class AlertsController:
    
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
            cursor.close()
            conn.close()

            # 🔥 PASO 7: ENVIAR CORREO AUTOMÁTICO
            try:
                subject = "🚨 Nueva alerta registrada en el sistema"

                # 🔥 AGREGADO: obtener email del estudiante
                student_email = self.get_student_email(alert.id_student)

                message = f"""
                Se ha creado una nueva alerta:

                🧑 Estudiante ID: {alert.id_student}
                ⚠️ Tipo: {alert.tipo_alert}
                📄 Descripción: {alert.description}
                📊 Riesgo: {alert.risk_level}
                📌 Estado: {alert.state}

                🔗 ID alerta: {new_id}
                """

                send_email(
                    to_email=student_email,
                    subject=subject,
                    message=message
                )

            except Exception as email_error:
                print("Error enviando correo:", email_error)

            return {"resultado": "Alert creada correctamente", "id_alert": new_id}

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))


    # =========================
    # 🔥 AGREGADO: obtener email estudiante
    # =========================
    # =========================
    # GET STUDENT EMAIL
    # =========================
    def get_student_email(self, id_student: int):
        try:
            conn = None
            cursor = None

            # 🔥 Intento 1: tabla students
            try:
                cursor.execute("""
                    SELECT email FROM users WHERE id_users = %s
                """, (id_student,))
                result = cursor.fetchone()
                conn.commit() 

            except Exception as e:
                print("Error obtenido email:", e)
                if conn:
                    conn.rollback()

                return None
        finally:
            cursor.close()
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
            cursor.execute("SELECT * FROM alerts WHERE id_alert=%s", (id_alert,))
            row = cursor.fetchone()

            if not row:
                raise HTTPException(status_code=404, detail="Alert no encontrada")

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
    # UPDATE
    # =========================
    def update_Alerts(self, id_alert: int, alert: Alerts):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE alerts
                SET id_student=%s, tipo_alert=%s, description=%s,
                    generation_date=%s, risk_level=%s, state=%s, id_period=%s
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
            cursor.close()
            conn.close()

            return {"resultado": "Alert actualizada correctamente"}

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))


    # =========================
    # DELETE
    # =========================
    def delete_Alerts(self, id_alert: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM alerts WHERE id_alert=%s", (id_alert,))

            conn.commit()
            cursor.close()
            conn.close()

            return {"resultado": "Alert eliminada correctamente"}

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))