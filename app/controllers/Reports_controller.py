import psycopg2
from app.config.db_config import get_db_connection
from fastapi import HTTPException
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import io
from fastapi.responses import StreamingResponse


class ReportsController:

    def generate_pdf_report(self, risk_level, state, id_program):

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
                SELECT s.name, s.last_name, a.tipo_alert, a.risk_level, a.state
                FROM alerts a
                JOIN students s ON a.id_student = s.id_student
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
            data = cursor.fetchall()

            buffer = io.BytesIO()
            pdf = SimpleDocTemplate(buffer)

            elements = []

            styles = getSampleStyleSheet()
            title = Paragraph("REPORTE DE ALERTAS", styles["Title"])
            elements.append(title)
            elements.append(Spacer(1, 12))

            table_data = [["Nombre", "Apellido", "Tipo", "Riesgo", "Estado"]]

            for row in data:
                table_data.append(list(row))

            table = Table(table_data)

            table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.grey),
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("GRID", (0,0), (-1,-1), 0.5, colors.black),
                ("BACKGROUND", (0,1), (-1,-1), colors.beige),
            ]))

            elements.append(table)

            pdf.build(elements)

            buffer.seek(0)

            return StreamingResponse(buffer, media_type="application/pdf")

        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))