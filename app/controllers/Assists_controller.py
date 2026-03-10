import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Assists_model import Assists
from fastapi.encoders import jsonable_encoder

class AssistsController:
    def create_Assists(self, Assists: Assists):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Assists (id_Student_subject, Date, State)
                VALUES (%s, %s, %s)
            """, (
                Assists.id_Student_subject,
                Assists.Date,
                Assists.State
            ))
            conn.commit()
            return {"resultado": "Assists registrada"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al registrar Assists")
        finally:
            conn.close()

    def get_Assists(self, id_Assists: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Assists WHERE id_Assists = %s", (id_Assists,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Assists no encontrada")
            content = {
                "id_Assists": result[0],
                "id_Student_subject": result[1],
                "Date": result[2],
                "State": result[3]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def get_Assists(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Assists")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No hay Assists")
            payload = []
            for row in result:
                payload.append({
                    "id_Assists": row[0],
                    "id_Student_subject": row[1],
                    "Date": row[2],
                    "State": row[3]
                })
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def update_Assists(self, id_Assists: int, Assists: Assists):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Assists
                SET id_Student_subject = %s, Date = %s, State = %s
                WHERE id_Assists = %s
            """, (
                Assists.id_Student_subject,
                Assists.Date,
                Assists.State,
                id_Assists
            ))
            conn.commit()
            return {"resultado": "Assists actualizada"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar Assists")
        finally:
            conn.close()

    def delete_Assists(self, id_Assists: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Assists WHERE id_Assists = %s", (id_Assists,))
            conn.commit()
            return {"resultado": "Assists eliminada"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar Assists")
        finally:
            conn.close()