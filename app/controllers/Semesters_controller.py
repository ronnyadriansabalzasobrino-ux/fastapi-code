import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Semesters_model import Semesters
from fastapi.encoders import jsonable_encoder


class SemestersController:

    def create_Semester(self, Semester: Semesters):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Semesters 
                (Number_Semster, Description)
                VALUES (%s, %s)
            """, (
                Semester.Number_Semester,
                Semester.Description
            ))

            conn.commit()
            return {"resultado": "Semester creado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear semester")

        finally:
            conn.close()


    def get_Semester(self, id_Semester: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Semester WHERE id_Semester = %s",
                (id_Semester,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Semester no encontrado")

            content = {
                "id_semester": result[0],
                "Number_Semester": result[1],
                "Description": result[2]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def get_Semester(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM semesters")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay semesters")

            payload = []

            for row in result:
                payload.append({
                    "id_Semester": row[0],
                    "Number_Semester": row[1],
                    "Description": row[2]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def update_Semester(self, id_Semester: int, Semester: Semesters):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Semesters
                SET Number_Semster = %s,
                    Description = %s
                WHERE id_Semester = %s
            """, (
                Semester.Number_Semester,
                Semester.Description,
                id_Semester
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Semester no encontrado")

            return {"resultado": "Semester actualizado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar semester")

        finally:
            conn.close()


    def delete_Semester(self, id_Semester: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM Semesters WHERE id_Semester = %s",
                (id_Semester,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Semester no encontrado")

            return {"resultado": "Semester eliminado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar semester")

        finally:
            conn.close()