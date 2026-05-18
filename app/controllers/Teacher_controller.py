import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.Teacher_model import Teacher
from fastapi.encoders import jsonable_encoder
from app.services.email_service import send_email

class TeacherController:
    async def create_Teacher(self, Teacher: Teacher):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Teacher (name, last_name, number_id, mail, phone, specialty)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                Teacher.name,
                Teacher.last_name,
                Teacher.number_id,
                Teacher.mail,
                Teacher.phone,
                Teacher.specialty
            ))
            conn.commit()
            
            await send_email(
                Teacher.mail,
                "docente registrado",
                f"""
                <h2>registro exitoso</h2>
                <p> Hola {Teacher.name}, tu cuenta docente fue creada correctamente. </p>
                """
            )
            return {"resultado": "Teacher creado"}
        
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()

    def get_Teacher(self, id_teaching: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Teacher WHERE id_teaching = %s", (id_teaching,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Teacher no encontrado")
            content = {
                "id_teaching": result[0],
                "name": result[1],
                "last_name": result[2],
                "number_id": result[3],
                "mail": result[4],
                "phone": result[5],
                "specialty": result[6]
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
                    "id_teaching": row[0],
                    "name": row[1],
                    "last_name": row[2],
                    "number_id": row[3],
                    "mail": row[4],
                    "phone": row[5],
                    "specialty": row[6]
                })
            return jsonable_encoder(payload)
        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            conn.close()

    async def update_Teacher(self, id_teaching: int, Teacher: Teacher):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Teacher
                SET name = %s, last_name = %s, number_id = %s, mail = %s, phone = %s, specialty = %s
                WHERE id_teaching = %s
            """, (
                Teacher.name,
                Teacher.last_name,
                Teacher.number_id,
                Teacher.mail,
                Teacher.phone,
                Teacher.specialty,
                id_teaching
            ))
            conn.commit()
            
            await send_email(
                Teacher.mail,
                "Docente actualizado",
                f"""
                <h2>Datos actualizados</h2>
                <p> Hola {Teacher.name}, tus datos fueron actualizados exitosamente. </p>
                """
            )


            return {"resultado": "Teacher actualizado"}
        

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar Teacher")
        finally:
            conn.close()

    async def delete_Teacher(self, id_teaching: int):
        try:
            conn = get_db_connection()
            cursor.execute(
                "SELECT mail, name FROM Teacher WHERE id_teaching = %s",
                (id_teaching,)
            )
            teacher_data = cursor.fetchone()
            teacher_mail = teacher_data[0]
            teacher_name = teacher_data[1]

            cursor = conn.cursor()
            cursor.execute("DELETE FROM Teacher WHERE id_teaching = %s", (id_teaching,))
            
            conn.commit()
            
            await send_email(
                teacher_mail,
                "Docente eliminado",
                f"""
                <h2>Docente eliminado</h2>
                <p> Hola {teacher_name}, lamentamos informarte que tu cuenta ha sido eliminada. Si tienes alguna pregunta, no dudes en contactarnos. </p>
                """
            )
            return {"resultado": "Teacher eliminado"}
        
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar Teacher")
        finally:
            conn.close()