from pydantic import BaseModel

class DinosaurRequest(BaseModel):
  name: str
  species: str
  age: int
  weigh: int
  gender: str
  dangerousness: str

class RecintoRequest(BaseModel):
  name: str
  species: str
  estado: bool
  
class GetRequest(BaseModel):
  id:int
  
class DeleteRequest(BaseModel):
  id: int
  
class UpdateRequest(BaseModel):
  id: int
  update: DinosaurRequest