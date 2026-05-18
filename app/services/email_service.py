import resend

resend.api_key = "re_LuYPymGq_3FeAPrDybj5d7rXbX2rZPAaf"

ADMIN_EMAIL = "ronnyadriansabalzasobrino@gmail.com"


async def send_email(destinatario: str, asunto: str, contenido: str):

    try:

        params = {
            "from": "onboarding@resend.dev",
            "to": [destinatario],
            "subject": asunto,
            "html": contenido,
        }

        email = resend.Emails.send(params)

        print("CORREO ENVIADO")
        print(email)

    except Exception as e:

        print("ERROR CORREO:", e)