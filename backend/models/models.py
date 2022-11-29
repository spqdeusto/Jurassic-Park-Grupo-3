from pydantic import BaseModel

class Especie(BaseModel):
  name:str
  class Config:
    orm_mode=True

class DinosaurRequest(BaseModel):
  name: str
  species: int
  age: int
  weigh: int
  gender: bool
  dangerousness: bool
  recinto: str
  class Config:
    orm_mode=True

class TodoTerrenoRequest(BaseModel):
  ruta: bool
  numvisitantes: int
  sistemaseguridad: bool
  recinto:str
  class Config:
    orm_mode=True

class RecintoRequest(BaseModel):
  name: str
  species: str
  state: bool
  dinosaurs=list[DinosaurRequest]=[]
  todoterrenos=list[TodoTerrenoRequest]=[]
  class Config:
    orm_mode=True

#luego igual los borramos
class GetRequest(BaseModel):
  id:int
  
class DeleteRequest(BaseModel):
  id: int
  
class UpdateRequest(BaseModel):
  id: int
  update: DinosaurRequest