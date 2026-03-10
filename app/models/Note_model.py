from pydantic import BaseModel
import datetime
class Note(BaseModel):
    id_Note: int
    id_Student_subject: int
    Evaluation_type: str
    Percentage: float
    Qualification: float
    Registration_date: str

    
    