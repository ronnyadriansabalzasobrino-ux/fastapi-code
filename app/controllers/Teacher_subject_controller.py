import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Teacher_subject_model import Teacher_subject
from fastapi.encoders import jsonable_encoder

class DocenteMateriaController:
    def create_Teacher_subject(self, Teacher_subject: Teacher_subject):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Teacher_subject (id_Teaching, id_Subject, Academic_period, State, id_period)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                Teacher_subject.id_Teaching,
                Teacher_subject.id_Subject,
                Teacher_subject.Academic_period,
                Teacher_subject.State,
                Teacher_subject.id_period
            ))
            conn.commit()
            return {"resultado": "Asignación creada"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear asignación")
        finally:
            conn.close()

    def get_Teacher_subject(self, id_Teacher_subject: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Teacher_subject WHERE id_Teacher_subject = %s", (id_Teacher_subject,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Asignación no encontrada")
            content = {
                "id_Teacher_subject": result[0],
                "id_Teaching": result[1],
                "id_Subject": result[2],
                "Academic_period": result[3],
                "State": result[4],
                "id_period": result[5]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def get_Teacher_subjects(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Teacher_subject")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No hay asignaciones")
            payload = []
            for row in result:
                payload.append({
                    "id_Teacher_subject": row[0],
                    "id_Teaching": row[1],
                    "id_Subject": row[2],
                    "Academic_period": row[3],
                    "State": row[4],
                    "id_period": row[5]
                })
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def update_Teacher_subject(self, id_Teacher_subject: int, Teacher_subject: Teacher_subject):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Teacher_subject
                SET id_Teaching = %s, id_Subject = %s, Academic_period = %s, State = %s, id_period = %s
                WHERE id_Teacher_subject = %s
            """, (
                Teacher_subject.id_Teaching,
                Teacher_subject.id_Subject,
                Teacher_subject.Academic_period,
                Teacher_subject.State,
                Teacher_subject.id_period,
                id_Teacher_subject
            ))
            conn.commit()
            return {"resultado": "Asignación actualizada"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar asignación")
        finally:
            conn.close()

    def delete_Teacher_subject(self, id_Teacher_subject: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Teacher_subject WHERE id_Teacher_subject = %s", (id_Teacher_subject,))
            conn.commit()
            return {"resultado": "Asignación eliminada"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar asignación")
        finally:
            conn.close()