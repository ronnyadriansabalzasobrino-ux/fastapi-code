import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Note_model import Note
from fastapi.encoders import jsonable_encoder


class NoteController:

    def create_note(self, note: Note):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Note
                (id_Student_subject, Evaluation_type, Percentage, Qualification)
                VALUES (%s, %s, %s, %s)
            """, (
                note.id_Student_subject,
                note.Evaluation_type,
                note.Percentage,
                note.Qualification
            ))

            conn.commit()
            return {"resultado": "Note registrada"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al registrar Note")

        finally:
            conn.close()


    def get_note(self, id_note: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Note WHERE id_Note = %s",
                (id_note,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Note no encontrada")

            content = {
                "id_Note": result[0],
                "id_Student_subject": result[1],
                "Evaluation_type": result[2],
                "Percentage": float(result[3]),
                "Qualification": float(result[4]),
                "Registration_date": result[5]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def get_notes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Note")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay Notes")

            payload = []

            for row in result:
                payload.append({
                    "id_Note": row[0],
                    "id_Student_subject": row[1],
                    "Evaluation_type": row[2],
                    "Percentage": float(row[3]),
                    "Qualification": float(row[4]),
                    "Registration_date": row[5]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def update_note(self, id_note: int, note: Note):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Note
                SET id_Student_subject = %s,
                    Evaluation_type = %s,
                    Percentage = %s,
                    Qualification = %s
                WHERE id_Note = %s
            """, (
                note.id_Student_subject,
                note.Evaluation_type,
                note.Percentage,
                note.Qualification,
                id_note
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Note no encontrada")

            return {"resultado": "Note actualizada"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar Note")

        finally:
            conn.close()


    def delete_note(self, id_note: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM Note WHERE id_Note = %s",
                (id_note,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Note no encontrada")

            return {"resultado": "Note eliminada"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar Note")

        finally:
            conn.close()