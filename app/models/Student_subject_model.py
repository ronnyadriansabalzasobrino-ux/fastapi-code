from pydantic import BaseModel

class Student_subject(BaseModel):
    id_Student_subject: int
    id_Student: int
    id_Subject: int
    Academic_period: str
    State: str
    
    