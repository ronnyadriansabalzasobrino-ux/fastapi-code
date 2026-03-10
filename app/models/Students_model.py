from pydantic import BaseModel
from typing import Optional
from datetime import date
class Students(BaseModel):
    id_student: int = None
    Name: str
    Last_name: str
    Number_id: str
    Mail: str
    phone: str
    id_program: int
    id_Semester: int
    Registration_date: Optional[date] = None
    State: str