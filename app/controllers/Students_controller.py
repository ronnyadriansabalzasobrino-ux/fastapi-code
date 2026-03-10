import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Students_model import Students
from fastapi.encoders import jsonable_encoder


class StudentsController:

    def create_student(self, student: Students):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Students 
                (Name, Last_name, Number_id, Mail, Phone, id_program, id_Semester)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                student.Name,
                student.Last_name,
                student.Number_id,
                student.Mail,
                student.Phone,
                student.id_program,
                student.id_Semester
            ))

            conn.commit()
            return {"resultado": "Student creado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear Student")

        finally:
            conn.close()


    def get_student(self, id_student: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Students WHERE id_Students = %s",
                (id_student,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Student no encontrado")

            content = {
                "id_Students": result[0],
                "Name": result[1],
                "Last_name": result[2],
                "Number_id": result[3],
                "Mail": result[4],
                "Phone": result[5],
                "id_program": result[6],
                "id_Semester": result[7],
                "Registration_date": result[8],
                "State": result[9]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def get_students(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Students")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay Students")

            payload = []

            for row in result:
                payload.append({
                    "id_Students": row[0],
                    "Name": row[1],
                    "Last_name": row[2],
                    "Number_id": row[3],
                    "Mail": row[4],
                    "Phone": row[5],
                    "id_program": row[6],
                    "id_Semester": row[7],
                    "Registration_date": row[8],
                    "State": row[9]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def update_student(self, id_student: int, student: Students):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Students
                SET Name = %s,
                    Last_name = %s,
                    Number_id = %s,
                    Mail = %s,
                    Phone = %s,
                    id_program = %s,
                    id_Semester = %s
                WHERE id_Students = %s
            """, (
                student.Name,
                student.Last_name,
                student.Number_id,
                student.Mail,
                student.Phone,
                student.id_program,
                student.id_Semester,
                id_student
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Student no encontrado")

            return {"resultado": "Student actualizado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar Student")

        finally:
            conn.close()


    def delete_student(self, id_student: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM Students WHERE id_Students = %s",
                (id_student,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Student no encontrado")

            return {"resultado": "Student eliminado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar Student")

        finally:
            conn.close()