from pydantic import BaseModel

class Users (BaseModel):
    id_User: int
    Name: str
    Last_name: str
    Post: str
    Mail: str
    Phone: str
    rol: str
    