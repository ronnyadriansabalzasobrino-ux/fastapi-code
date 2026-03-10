from pydantic import BaseModel
import datetime
class Assists(BaseModel):
    id_Assists: int
    id_Student_subject: int
    Date: str
    State: str

    
    