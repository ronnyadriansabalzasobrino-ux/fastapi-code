from pydantic import BaseModel

class Teacher_subject(BaseModel):
    id_Teacher_subject: int
    id_Teaching: int
    id_Subject: int
    periodo_academico: str
    id_period: str
    
    