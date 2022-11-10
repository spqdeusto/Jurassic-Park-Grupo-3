from typing import Optional
from pydantic import BaseModel

class Dinosaur(BaseModel):
	id: Optional[int]
	name: str
	species: str
	age: int
	dangerousness: int
