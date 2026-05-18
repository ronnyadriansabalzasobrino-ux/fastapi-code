import psycopg2

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.config.db_config import get_db_connection
from app.models.Subjects_model import Subjects



class SubjectsController:


    # =========================
    # CREATE SUBJECT
    # =========================
    def create_subject(self, subject: Subjects):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Subject
                (name_subject, credits, id_program)
                VALUES (%s, %s, %s)
            """, (
                subject.name_subject,
                subject.credits,
                subject.id_program
            ))

            conn.commit()
            return {"resultado": "Subject creada"}

        except psycopg2.Error as err:

            conn.rollback()
            print(err)

            raise HTTPException(
                status_code=500,
                detail=str(err)
            )

        finally:
            conn.close()


    # =========================
    # GET SUBJECT
    # =========================
    def get_subject(self, id_subject: int):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Subject WHERE id_subject = %s",
                (id_subject,)
            )

            result = cursor.fetchone()

            if not result:

                raise HTTPException(
                    status_code=404,
                    detail="Subject no encontrada"
                )

            content = {
                "id_subject": result[0],
                "name_subject": result[1],
                "credits": result[2],
                "id_program": result[3]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:

            print(err)

            raise HTTPException(
                status_code=500,
                detail="Error en base de datos"
            )

        finally:
            conn.close()


    # =========================
    # GET ALL
    # =========================
    def get_subjects(self):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT 
                    s.id_subject,
                    s.name_subject,
                    s.credits,
                    s.id_program,
                    p.name_program
                FROM Subject s
                INNER JOIN programs p
                ON s.id_program = p.id_program
            """)

            result = cursor.fetchall()

            payload = []

            for row in result:

                payload.append({
                    "id_subject": row[0],
                    "name_subject": row[1],
                    "credits": row[2],
                    "id_program": row[3],
                    "program": row[4]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:

            print(err)

            raise HTTPException(
                status_code=500,
                detail="Error en base de datos"
            )

        finally:
            conn.close()


    # =========================
    # UPDATE SUBJECT
    # =========================
    def update_subject(self, id_subject: int, subject: Subjects):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Subject
                SET name_subject = %s,
                    credits = %s,
                    id_program = %s
                WHERE id_subject = %s
            """, (
                subject.name_subject,
                subject.credits,
                subject.id_program,
                id_subject
            ))

            conn.commit()
            return {"resultado": "Subject actualizada"}

        except psycopg2.Error as err:

            conn.rollback()
            print(err)

            raise HTTPException(
                status_code=500,
                detail="Error al actualizar Subject"
            )

        finally:
            conn.close()


    # =========================
    # DELETE SUBJECT
    # =========================
    def delete_subject(self, id_subject: int):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            # =========================
            # OBTENER NOMBRE
            # =========================

            cursor.execute("""
                SELECT name_subject
                FROM Subject
                WHERE id_subject=%s
            """, (id_subject,))

            result = cursor.fetchone()

            subject_name = result[0] if result else "Materia"

            # =========================
            # DELETE
            # =========================

            cursor.execute("""
                DELETE FROM Subject
                WHERE id_subject = %s
            """, (id_subject,))

            conn.commit()

            return {"resultado": "Subject eliminada"}

        except psycopg2.Error as err:

            conn.rollback()
            print(err)

            raise HTTPException(
                status_code=500,
                detail="Error al eliminar Subject"
            )

        finally:
            conn.close()
