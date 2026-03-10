import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Teacher_model import Teacher
from fastapi.encoders import jsonable_encoder

class TeacherController:
    def create_Teacher(self, Teacher: Teacher):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Teacher (Name, Last_name, Number_id, Mail, Phone, speciality)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                Teacher.Name,
                Teacher.Last_name,
                Teacher.Number_id,
                Teacher.Mail,
                Teacher.Phone,
                Teacher.speciality
            ))
            conn.commit()
            return {"resultado": "Teacher creado"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear Teacher")
        finally:
            conn.close()

    def get_Teacher(self, id_Teaching: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Teacher WHERE id_Teaching = %s", (id_Teaching,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Teacher no encontrado")
            content = {
                "id_Teaching": result[0],
                "Name": result[1],
                "Last_name": result[2],
                "Number_id": result[3],
                "Mail": result[4],
                "Phone": result[5],
                "speciality": result[6]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def get_Teachers(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Teacher")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No hay Teacher")
            payload = []
            for row in result:
                payload.append({
                    "id_Teaching": row[0],
                    "Name": row[1],
                    "Last_name": row[2],
                    "Number_id": row[3],
                    "Mail": row[4],
                    "Phone": row[5],
                    "speciality": row[6]
                })
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    def update_Teacher(self, id_Teaching: int, Teacher: Teacher):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Teacher
                SET Name = %s, Last_name = %s, Number_id = %s, Mail = %s, Phone = %s, speciality = %s
                WHERE id_Teaching = %s
            """, (
                Teacher.Name,
                Teacher.Last_name,
                Teacher.Number_id,
                Teacher.Mail,
                Teacher.Phone,
                Teacher.speciality,
                id_Teaching
            ))
            conn.commit()
            return {"resultado": "Teacher actualizado"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar Teacher")
        finally:
            conn.close()

    def delete_Teacher(self, id_Teaching: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Teacher WHERE id_Teaching = %s", (id_Teaching,))
            conn.commit()
            return {"resultado": "Teacher eliminado"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar Teacher")
        finally:
            conn.close()