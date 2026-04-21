# controllers/Alerts_controller.py
import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.Alerts_model import Alerts
from fastapi.encoders import jsonable_encoder


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

            return {"resultado": "Alert creada correctamente", "id_alert": new_id}

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail=str(err))


    # =========================
    # ✅ OBTENER EMAIL DEL ESTUDIANTE
    # =========================
    def get_student_email(self, id_student: int):
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT mail FROM students WHERE id_student = %s
            """, (id_student,))

            result = cursor.fetchone()
            print("MAIL ENCONTRADO:", result)
            return result[0] if result else None

        except Exception as e:
            print("Error obtenido mail:", e)
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