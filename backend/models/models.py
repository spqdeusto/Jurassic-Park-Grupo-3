from pydantic import BaseModel

class DinosaurRequest(BaseModel):
  name: str
  species: str
  age: int
  weigh: int
  gender: str
  dangerousness: str

class GetRequest(BaseModel):
  id:int
  
class DeleteRequest(BaseModel):
  id: int
  
class UpdateRequest(BaseModel):
  id: int
  update: DinosaurRequest