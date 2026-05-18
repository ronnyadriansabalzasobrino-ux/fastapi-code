import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL = "ronnyadriansabalzasobrino@gmail.com"
PASSWORD = "lwjk jylo rhsw jzqo"

ADMIN_EMAIL = "ronnyadriansabalzasobrino@gmail.com"


async def send_email(destinatario: str, asunto: str, contenido: str):

    try:

        mensaje = MIMEMultipart()

        mensaje["From"] = EMAIL
        mensaje["To"] = destinatario
        mensaje["Subject"] = asunto

        mensaje.attach(
            MIMEText(contenido, "html")
        )

        servidor = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        )

        servidor.starttls()

        servidor.login(
            EMAIL,
            PASSWORD
        )

        servidor.sendmail(
            EMAIL,
            destinatario,
            mensaje.as_string()
        )

        servidor.quit()

        print("Correo enviado correctamente")

    except Exception as e:

        print("ERROR CORREO:", e)