import psycopg2
from app.config.db_config import get_db_connection
from fastapi import HTTPException


class ReportsController:

    # 🔥 DATOS PARA EL FRONTEND
    def get_report_data(self, risk_level, state, id_program):

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
                SELECT
                    s.id_student,
                    s.name,
                    s.last_name,
                    s.id_program,
                    a.tipo_alert,
                    a.risk_level,
                    a.state

                FROM alerts a

                JOIN students s
                ON a.id_student = s.id_student

                WHERE 1=1
            """

            params = []

            if risk_level:
                query += " AND a.risk_level = %s"
                params.append(risk_level)

            if state:
                query += " AND a.state = %s"
                params.append(state)

            if id_program:
                query += " AND s.id_program = %s"
                params.append(id_program)

            cursor.execute(query, tuple(params))

            result = cursor.fetchall()

            payload = []

            for row in result:

                payload.append({

                    "id_student": row[0],
                    "name": row[1],
                    "last_name": row[2],
                    "id_program": row[3],
                    "tipo_alert": row[4],
                    "risk_level": row[5],
                    "state": row[6]

                })

            return payload

        except Exception as e:

            print(e)
            raise HTTPException(status_code=500, detail=str(e))

        finally:

            conn.close()