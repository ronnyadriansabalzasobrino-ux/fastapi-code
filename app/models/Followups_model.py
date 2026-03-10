from pydantic import BaseModel
import datetime
class Followups (BaseModel):
    id_followup: int
    id_Alerts: int
    id_teaching: int
    descripcion: str
    observation: str
    followup_date: str
    action_taken: str

    
    