import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Subjects_model import Subjects
from fastapi.encoders import jsonable_encoder


class SubjectsController:

    def create_subject(self, subject: Subjects):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Subject
                (name_Subject, Credits, id_Program)
                VALUES (%s, %s, %s)
            """, (
                subject.name_Subject,
                subject.Credits,
                subject.id_Program
            ))

            conn.commit()
            return {"resultado": "Subject creada"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear Subject")

        finally:
            conn.close()


    def get_subject(self, id_subject: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Subject WHERE id_Subject = %s",
                (id_subject,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Subject no encontrada")

            content = {
                "id_Subject": result[0],
                "name_Subject": result[1],
                "Credits": result[2],
                "id_Program": result[3]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def get_subjects(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Subject")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay Subjects")

            payload = []

            for row in result:
                payload.append({
                    "id_Subject": row[0],
                    "name_Subject": row[1],
                    "Credits": row[2],
                    "id_Program": row[3]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def update_subject(self, id_subject: int, subject: Subjects):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Subject
                SET name_Subject = %s,
                    Credits = %s,
                    id_Program = %s
                WHERE id_Subject = %s
            """, (
                subject.name_Subject,
                subject.Credits,
                subject.id_Program,
                id_subject
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Subject no encontrada")

            return {"resultado": "Subject actualizada"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar Subject")

        finally:
            conn.close()


    def delete_subject(self, id_subject: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM Subject WHERE id_Subject = %s",
                (id_subject,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Subject no encontrada")

            return {"resultado": "Subject eliminada"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar Subject")

        finally:
            conn.close()