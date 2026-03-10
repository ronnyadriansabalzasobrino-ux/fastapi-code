from pydantic import BaseModel
import datetime
class Alerts(BaseModel):
    id_alert: int
    id_Student: int
    tipo_alert: str
    Description: str
    generation_date: str
    Risk_level: str
    State: str

    
    