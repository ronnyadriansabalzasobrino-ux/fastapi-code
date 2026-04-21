from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
conf = ConnectionConfig(
    MAIL_USERNAME="ronnyadriansabalzasobrino@gmail.com",
    MAIL_PASSWORD="lwjk jylo rhsw jzqo",
    MAIL_FROM="ronnyadriansabalzasobrino@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)
ADMIN_EMAIL="ronnyadriansabalzasobrino@gmail.com"

async def send_email(destinatario: str, asunto: str, contenido: str):

    message = MessageSchema(
        subject=asunto,
        recipients=[destinatario],
        body=contenido,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)