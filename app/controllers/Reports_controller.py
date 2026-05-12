import psycopg2

from fastapi import HTTPException

from app.config.db_config import get_db_connection

from fastapi.encoders import jsonable_encoder


class ReportsController:

    def get_reports_data(self):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""

                SELECT
                    s.name,
                    s.last_name,
                    s.number_id,
                    p.name_program,
                    a.risk_level,
                    a.state,
                    a.tipo_alert,
                    a.generation_date

                FROM alerts a

                INNER JOIN students s
                ON a.id_student = s.id_student

                LEFT JOIN programs p
                ON s.id_program = p.id_program

                ORDER BY a.id_alert DESC

            """)

            result = cursor.fetchall()

            payload = []

            for row in result:

                payload.append({

                    "student":
                    f"{row[0]} {row[1]}",

                    "document":
                    row[2],

                    "program":
                    row[3],

                    "risk_level":
                    row[4],

                    "state":
                    row[5],

                    "tipo_alert":
                    row[6],

                    "generation_date":
                    str(row[7])

                })

            cursor.close()
            conn.close()

            return jsonable_encoder(payload)

        except psycopg2.Error as err:
            print(err)

            raise HTTPException(
                status_code=500,
                detail=str(err)
            )


    # =========================
    # REPORTES DEL ESTUDIANTE
    # =========================

    def get_student_reports(self, mail: str):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""

                SELECT
                    p.name_program,
                    a.risk_level,
                    a.state,
                    a.tipo_alert,
                    a.generation_date

                FROM alerts a

                INNER JOIN students s
                ON a.id_student = s.id_student

                LEFT JOIN programs p
                ON s.id_program = p.id_program

                WHERE s.id_user = %s

                ORDER BY a.id_alert DESC

            """, (mail,))

            result = cursor.fetchall()

            payload = []

            for row in result:

                payload.append({

                    "program":
                    row[0],

                    "risk_level":
                    row[1],

                    "state":
                    row[2],

                    "tipo_alert":
                    row[3],

                    "generation_date":
                    str(row[4])

                })

            cursor.close()
            conn.close()

            return jsonable_encoder(payload)

        except psycopg2.Error as err:

            print(err)

            raise HTTPException(
                status_code=500,
                detail=str(err)
            )