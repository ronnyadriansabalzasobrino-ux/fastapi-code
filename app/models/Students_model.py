from pydantic import BaseModel
from typing import Optional
from datetime import date

class students(BaseModel):

    id_student: Optional[int] = None
    name: str
    last_name: str
    number_id: str
    mail: str
    phone: str
    id_program: int
    id_semester: int
    registration_date: Optional[date] = None
    state: Optional[str] = "asset"