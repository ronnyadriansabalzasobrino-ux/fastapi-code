from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secretfastapi123"

ALGORITHM = "HS256"

def create_token(data: dict, expires_minutes=60):

    payload = data.copy()

    payload.update({
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)
    })

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def validate_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except Exception:

        return None