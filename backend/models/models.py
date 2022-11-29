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
  state: bool

class TodoTerrenoRequest(BaseModel):
  ruta: bool
  numvisitantes: int
  sistemaseguridad: bool

class GetRequest(BaseModel):
  id:int
  
class DeleteRequest(BaseModel):
  id: int
  
class UpdateRequest(BaseModel):
  id: int
  update: DinosaurRequest