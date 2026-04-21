import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.Students_model import students
from fastapi.encoders import jsonable_encoder


class StudentsController:

    def create_student(self, student: students):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO "students"
                (name, last_name, number_id, mail, phone, id_program, id_semester)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """,(
                student.name,
                student.last_name,
                student.number_id,
                student.mail,
                student.phone,
                student.id_program,
                student.id_semester
            ))

            conn.commit()

            return {"resultado": "Student creado"}

        except psycopg2.Error as err:
            conn.rollback()
            print("ERROR REAL:", err)
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            conn.close()


    def get_students(self):

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM "students"')
            result = cursor.fetchall()

            payload = []

            for row in result:
                payload.append({
                    "id_student": row[0],
                    "name": row[1],
                    "last_name": row[2],
                    "number_id": row[3],
                    "mail": row[4],
                    "phone": row[5],
                    "id_program": row[6],
                    "id_semester": row[7],
                    "registration_date": row[8],
                    "state": row[9]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    # 🔥 ESTE TE FALTABA BIEN DEFINIDO
    def get_student(self, id_student: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                'SELECT * FROM "students" WHERE id_student=%s',
                (id_student,)
            )

            row = cursor.fetchone()

            if not row:
                return None

            return {
                "id_student": row[0],
                "name": row[1],
                "last_name": row[2],
                "number_id": row[3],
                "mail": row[4],
                "phone": row[5],
                "id_program": row[6],
                "id_semester": row[7],
                "registration_date": row[8],
                "state": row[9]
            }

        except Exception as e:
            print(e)
            return None

        finally:
            conn.close()


    def update_student(self, id_student: int, student: students):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE "students"
                SET name=%s,
                    last_name=%s,
                    number_id=%s,
                    mail=%s,
                    phone=%s,
                    id_program=%s,
                    id_semester=%s
                WHERE id_student=%s
            """,(
                student.name,
                student.last_name,
                student.number_id,
                student.mail,
                student.phone,
                student.id_program,
                student.id_semester,
                id_student
            ))

            conn.commit()

            return {"resultado":"student actualizado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar")

        finally:
            conn.close()


    def delete_student(self,id_student:int):

        try:
            conn=get_db_connection()
            cursor=conn.cursor()

            cursor.execute(
                'DELETE FROM "students" WHERE id_student=%s',
                (id_student,)
            )

            conn.commit()

            return {"resultado":"student eliminado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500,detail="Error al eliminar")

        finally:
            conn.close()