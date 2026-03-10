from pydantic import BaseModel

class Semesters(BaseModel):
    id_Semester:int = None
    Number_Semesters: str
    Description: str
    
    