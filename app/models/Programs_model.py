from pydantic import BaseModel

class Programs(BaseModel):
    id_Program: int
    NAME_Program: str
    Faculty: str
    Level: str

    
    