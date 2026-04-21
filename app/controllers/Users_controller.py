import psycopg2
import bcrypt
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.db_config import get_db_connection
from app.models.Users_model import Users
from app.auth.jwt_handler import create_token

class UserController:

    # CREAR USUARIO
    def create_User(self, user: Users):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            hashed_password = bcrypt.hashpw(
                user.password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            cursor.execute("""
                INSERT INTO Users
                (name, last_name, post, mail, phone, rol, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                user.name,
                user.last_name,
                user.post,
                user.mail,
                user.phone,
                user.rol,
                hashed_password
            ))

            conn.commit()
            return {"resultado": "User creado"}

        except psycopg2.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()

    # LOGIN
    def login(self, mail: str, password: str):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Users WHERE mail = %s",
                (mail,)
            )

            user = cursor.fetchone()

            if not user:
                raise HTTPException(status_code=401, detail="Usuario no encontrado")

            stored_password = user[7]

            if password != stored_password:
                raise HTTPException(status_code=401, detail="contraseña incorrecta")
 
            token = create_token({
                "id_user": user[0],
                "rol": user[6]
            })

            return {
                "message": "Login exitoso",
                "access_token": token,
                "id_user": user[0],
                "name": user[1],
                "rol": user[6]
            }

        finally:
            conn.close()

    # OBTENER UN USUARIO
    def get_user(self, id_user: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Users WHERE id_user = %s", (id_user,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="User no encontrado")

            return jsonable_encoder({
                "id_user": result[0],
                "name": result[1],
                "last_name": result[2],
                "post": result[3],
                "mail": result[4],
                "phone": result[5],
                "rol": result[6]
            })

        finally:
            conn.close()

    # LISTAR USUARIOS
    def get_User(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Users")
            result = cursor.fetchall()

            return jsonable_encoder([{
                "id_user": row[0],
                "name": row[1],
                "last_name": row[2],
                "post": row[3],
                "mail": row[4],
                "phone": row[5],
                "rol": row[6]
            } for row in result])

        finally:
            conn.close()

    # ACTUALIZAR USUARIO
    def update_user(self, id_user: int, user: Users):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            hashed_password = bcrypt.hashpw(
                user.password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            cursor.execute("""
                UPDATE Users
                SET name=%s, last_name=%s, post=%s, mail=%s, phone=%s, rol=%s, password=%s
                WHERE id_user=%s
            """, (
                user.name,
                user.last_name,
                user.post,
                user.mail,
                user.phone,
                user.rol,
                hashed_password,
                id_user
            ))

            conn.commit()
            return {"resultado": "User actualizado"}

        finally:
            conn.close()

    # ELIMINAR USUARIO
    def delete_user(self, id_user: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM Users WHERE id_user=%s", (id_user,))
            conn.commit()

            return {"resultado": "User eliminado"}

        finally:
            conn.close()