import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.periods_model import periods
from fastapi.encoders import jsonable_encoder

class PeriodController:
    def create_period(self, period: periods):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO periods (period_code, start_date, end_date)
                VALUES (%s, %s, %s)
            """, (
                period.period_code,
                period.start_date,
                period.end_date
            ))
            conn.commit()
            return {"resultado": "Period creado"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear period")
        finally:
            conn.close()

    def get_period(self, id_period: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM periods WHERE id_period = %s", (id_period,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Period no encontrado")
            content = {
                "id_period": result[0],
                "period_code": result[1],
                "start_date": result[2],
                "end_date": result[3]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def get_periods(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM periods")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No hay periods")
            payload = []
            for row in result:
                payload.append({
                    "id_period": row[0],
                    "period_code": row[1],
                    "start_date": row[2],
                    "end_date": row[3]
                })
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def update_period(self, id_period: int, period: periods):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE periods
                SET period_code = %s, start_date = %s, end_date = %s
                WHERE id_period = %s
            """, (
                period.period_code,
                period.start_date,
                period.end_date,
                id_period
            ))
            conn.commit()
            return {"resultado": "Period actualizado"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar period")
        finally:
            conn.close()

    def delete_period(self, id_period: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM periods WHERE id_period = %s", (id_period,))
            conn.commit()
            return {"resultado": "Period eliminado"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar period")
        finally:
            conn.close()