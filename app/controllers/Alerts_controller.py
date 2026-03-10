import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Alerts_model import Alerts
from fastapi.encoders import jsonable_encoder

class AlertsController:
    def create_Alerts(self, Alerts: Alerts):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Alerts (id_Student, tipo_alerta, Description, generation_date, Risk_level, State, id_period)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                Alerts.id_Student,
                Alerts.tipo_alerta,
                Alerts.Description,
                Alerts.generation_date,
                Alerts.Risk_level,
                Alerts.State,
                Alerts.id_period
            ))
            conn.commit()
            return {"resultado": "Alerts creada correctamente"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear Alerts")
        finally:
            conn.close()

    def get_Alerts(self, id_alerta: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Alerts WHERE id_alert = %s", (id_alerta,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Alerts no encontrada")
            content = {
                "id_alert": result[0],
                "id_Student": result[1],
                "tipo_alerta": result[2],
                "Description": result[3],
                "generation_date": result[4],
                "Risk_level": result[5],
                "State": result[6],
                "id_period": result[7]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def get_Alerts(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Alerts")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No hay Alerts registradas")
            payload = []
            for row in result:
                payload.append({
                    "id_alert": row[0],
                    "id_Student": row[1],
                    "tipo_alerta": row[2],
                    "Description": row[3],
                    "generation_date": row[4],
                    "Risk_level": row[5],
                    "State": row[6],
                    "id_period": row[7]
                })
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def update_Alerts(self, id_alerta: int, Alerts: Alerts):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Alerts
                SET id_Student = %s, tipo_alerta = %s, Description = %s, generation_date = %s, Risk_level = %s, State = %s, id_period = %s
                WHERE id_alert = %s
            """, (
                Alerts.id_Student,
                Alerts.tipo_alerta,
                Alerts.Description,
                Alerts.generation_date,
                Alerts.Risk_level,
                Alerts.State,
                Alerts.id_period,
                id_alerta
            ))
            conn.commit()
            return {"resultado": "Alerts actualizada correctamente"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar Alerts")
        finally:
            conn.close()

    def delete_Alerts(self, id_alerta: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Alerts WHERE id_alert = %s", (id_alerta,))
            conn.commit()
            return {"resultado": "Alerts eliminada correctamente"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar Alerts")
        finally:
            conn.close()