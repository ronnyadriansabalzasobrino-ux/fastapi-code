import resend
import base64
resend.api_key = "re_LuYPymGq_3FeAPrDybj5d7rXbX2rZPAaf"

ADMIN_EMAIL = "ronnyadriansabalzasobrino@gmail.com"


def send_email(destinatario: str, asunto: str, contenido: str,archivo=None,Nombre_archivo="Reporte_SAPER.pdf"):


    try:

        params = {
            "from": "onboarding@resend.dev",
            "to": [destinatario],
            "subject": asunto,
            "html": contenido,
        }

        if archivo:
            pdf_base64 = base64.b64encode(archivo).decode('utf-8')
            params["attachments"] = [
                { 
                    "filename": Nombre_archivo,
                    "content": pdf_base64,
                }
            ]

        email = resend.Emails.send(params)

        print("CORREO ENVIADO")
        print(email)

    except Exception as e:

        print("ERROR CORREO:", e)