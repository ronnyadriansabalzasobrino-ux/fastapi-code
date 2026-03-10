from pydantic import BaseModel
import datetime
class periods(BaseModel):
    id_period: int
    period_code: str
    start_date: str
    end_date: str
   

    
    