import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.student_subject_model import Student_subject
from fastapi.encoders import jsonable_encoder

class StudentSubjectController:
    def create_student_subject(self, student_subject: Student_subject):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO student_subject (id_student, id_subject, academic_period, state, id_period)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                student_subject.id_student,
                student_subject.id_subject,
                student_subject.academic_period,
                student_subject.state,
                student_subject.id_period
            ))
            conn.commit()
            return {"result": "Student subject created"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error creating student subject")
        finally:
            conn.close()

    def get_student_subject(self, id_student_subject: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student_subject WHERE id_student_subject = %s", (id_student_subject,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Student subject not found")
            content = {
                "id_student_subject": result[0],
                "id_student": result[1],
                "id_subject": result[2],
                "academic_period": result[3],
                "state": result[4],
                "id_period": result[5]
            }
            return jsonable_encoder(content)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Database error")
        finally:
            conn.close()

    def get_student_subjects(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student_subject")
            result = cursor.fetchall()
            if not result:
                raise HTTPException(status_code=404, detail="No student subjects found")
            payload = []
            for row in result:
                payload.append({
                    "id_student_subject": row[0],
                    "id_student": row[1],
                    "id_subject": row[2],
                    "academic_period": row[3],
                    "state": row[4],
                    "id_period": row[5]
                })
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Database error")
        finally:
            conn.close()

    def update_student_subject(self, id_student_subject: int, data: Student_subject):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE student_subject
                SET id_student = %s, id_subject = %s, academic_period = %s, state = %s, id_period = %s
                WHERE id_student_subject = %s
            """, (
                data.id_student,
                data.id_subject,
                data.academic_period,
                data.state,
                data.id_period,
                id_student_subject
            ))
            conn.commit()
            return {"result": "Student subject updated"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error updating student subject")
        finally:
            conn.close()

    def delete_student_subject(self, id_student_subject: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM student_subject WHERE id_student_subject = %s", (id_student_subject,))
            conn.commit()
            return {"result": "Student subject deleted"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error deleting student subject")
        finally:
            conn.close()