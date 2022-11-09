from datetime import date
from pydantic import BaseModel
class Dinosaur(BaseModel):
    id = int
    name = str
    species = str
    age = int
    dangerousness = int

    class Config:
        orm_mode = True