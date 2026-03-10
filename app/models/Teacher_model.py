from pydantic import BaseModel

class Teacher (BaseModel):
    id_Teaching: int
    Name: str
    Last_name: str
    Number_id: str
    Mail: str
    Phone: str
    speciality: str

    
    