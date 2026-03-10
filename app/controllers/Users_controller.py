import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Users_model import Users
from fastapi.encoders import jsonable_encoder


class UserController:

    # Crear usuario
    def create_User(self, user: Users):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Users
                (Name, Last_name, Post, Mail, Phone, rol)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                user.Name,
                user.Last_name,
                user.Post,
                user.Mail,
                user.Phone,
                user.rol
            ))

            conn.commit()
            return {"resultado": "User creado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al crear user")

        finally:
            conn.close()


    # Obtener usuario por ID
    def get_user(self, id_user: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Users WHERE id_user = %s",
                (id_user,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="User no encontrado")

            content = {
                "id_user": result[0],
                "Name": result[1],
                "Last_name": result[2],
                "Post": result[3],
                "Mail": result[4],
                "Phone": result[5],
                "rol": result[6]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    # Obtener todos los usuarios
    def get_User(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Users")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay users")

            payload = []

            for row in result:
                payload.append({
                    "id_user": row[0],
                    "Name": row[1],
                    "Last_name": row[2],
                    "Post": row[3],
                    "Mail": row[4],
                    "Phone": row[5],
                    "rol": row[6]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    # Actualizar usuario
    def update_user(self, id_user: int, user: Users):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Users
                SET Name = %s,
                    Last_name = %s,
                    Post = %s,
                    Mail = %s,
                    Phone = %s,
                    rol = %s
                WHERE id_user = %s
            """, (
                user.Name,
                user.Last_name,
                user.Post,
                user.Mail,
                user.Phone,
                user.rol,
                id_user
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="User no encontrado")

            return {"resultado": "User actualizado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar user")

        finally:
            conn.close()


    # Eliminar usuario
    def delete_user(self, id_user: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM Users WHERE id_user = %s",
                (id_user,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="User no encontrado")

            return {"resultado": "User eliminado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar user")

        finally:
            conn.close()  