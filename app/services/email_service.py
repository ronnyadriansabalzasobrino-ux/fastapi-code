from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="ronnyadriansabalzasobrino@gmail.com",
    MAIL_PASSWORD="lwjk jylo rhsw jzqo",
    MAIL_FROM="ronnyadriansabalzasobrino@gmail.com",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

ADMIN_EMAIL = "ronnyadriansabalzasobrino@gmail.com"


async def send_email(destinatario: str, asunto: str, contenido: str):

    message = MessageSchema(
        subject=asunto,
        recipients=[destinatario],
        body=contenido,
        subtype="html"
    )

    fm = FastMail(conf)

    await fm.send_message(message)