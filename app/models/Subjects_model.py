from pydantic import BaseModel

class Subjects(BaseModel):
    id_Subject: int
    name_Subject : str
    Credits: int
    id_Program: int
    
    