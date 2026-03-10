import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Followups_model import Followups
from fastapi.encoders import jsonable_encoder


class FollowupsController:

    def create_Followups(self, Followup: Followups):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Followups
                (id_Alerts, id_teaching, observation, followup_date, action_taken)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                Followup.id_Alerts,
                Followup.id_teaching,
                Followup.observation,
                Followup.followup_date,
                Followup.action_taken
            ))

            conn.commit()
            return {"resultado": "Followup registrado correctamente"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al registrar followup")

        finally:
            conn.close()


    def get_Followup(self, id_Followups: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM Followups WHERE id_Followups = %s",
                (id_Followups,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Followup no encontrado")

            content = {
                "id_Followups": result[0],
                "id_Alerts": result[1],
                "id_teaching": result[2],
                "observation": result[3],
                "followup_date": result[4],
                "action_taken": result[5]
            }

            return jsonable_encoder(content)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def get_followups(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Followups")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay followups registrados")

            payload = []

            for row in result:
                payload.append({
                    "id_Followups": row[0],
                    "id_Alerts": row[1],
                    "id_teaching": row[2],
                    "observation": row[3],
                    "followup_date": row[4],
                    "action_taken": row[5]
                })

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            conn.close()


    def update_followup(self, id_followup: int, Followup: Followups):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Followups
                SET id_Alerts = %s,
                    id_teaching = %s,
                    observation = %s,
                    followup_date = %s,
                    action_taken = %s
                WHERE id_Followups = %s
            """, (
                Followup.id_Alerts,
                Followup.id_teaching,
                Followup.observation,
                Followup.followup_date,
                Followup.action_taken,
                id_followup
            ))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Followup no encontrado")

            return {"resultado": "Followup actualizado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al actualizar followup")

        finally:
            conn.close()


    def delete_followup(self, id_followup: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM Followups WHERE id_Followups = %s",
                (id_followup,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Followup no encontrado")

            return {"resultado": "Followup eliminado"}

        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error al eliminar followup")

        finally:
            conn.close()