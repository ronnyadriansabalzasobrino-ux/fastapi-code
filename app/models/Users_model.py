from pydantic import BaseModel
from typing import Optional
class Users(BaseModel):
    id_user: int | None = None
    name: str
    last_name: str
    post: Optional[str] = ""
    mail: str
    phone: Optional[str] = ""
    rol: str
    password: str