import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Programs_model import Programs
from fastapi.encoders import jsonable_encoder


class ProgramsController:

    def create_program(self, program: Programs):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Programs
                (Name_program, Faculty, Level)
                VALUES (%s, %s, %s)
            """, (
                program.Name_program,
                program.Faculty,
                program.Level
            ))

            conn.commit()
            return {"resultado": "Program creado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear program")

        finally:
            conn.close()


    def get_program(self, id_program: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Programs WHERE id_program = %s",
                (id_program,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Program no encontrado")

            content = {
                "id_program": result[0],
                "Name_program": result[1],
                "Faculty": result[2],
                "Level": result[3]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def get_programs(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Programs")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay programas")

            payload = []

            for row in result:
                payload.append({
                    "id_program": row[0],
                    "Name_program": row[1],
                    "Faculty": row[2],
                    "Level": row[3]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def update_program(self, id_program: int, program: Programs):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Programs
                SET Name_program = %s,
                    Faculty = %s,
                    Level = %s
                WHERE id_program = %s
            """, (
                program.Name_program,
                program.Faculty,
                program.Level,
                id_program
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Program no encontrado")

            return {"resultado": "Program actualizado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar program")

        finally:
            conn.close()


    def delete_program(self, id_program: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM Programs WHERE id_program = %s",
                (id_program,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Program no encontrado")

            return {"resultado": "Program eliminado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar program")

        finally:
            conn.close()