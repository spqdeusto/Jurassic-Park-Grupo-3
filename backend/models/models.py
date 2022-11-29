from pydantic import BaseModel

class Especie(BaseModel):
  name:str
  class Config:
    orm_mode=True

class Dinosaur(BaseModel):
  name: str
  species: int
  age: int
  weigh: int
  gender: bool
  dangerousness: bool
  recinto: str
  class Config:
    orm_mode=True

class TodoTerreno(BaseModel):
  ruta: bool
  numvisitantes: int
  sistemaseguridad: bool
  recinto: str
  class Config:
    orm_mode=True

class Recinto(BaseModel):
  name: str
  species: str
  state: bool
  dinosaurs: list[Dinosaur]
  todoterrenos: list[TodoTerreno]
  class Config:
    orm_mode=True

#luego igual los borramos
class GetRequest(BaseModel):
  id:int
  
class DeleteRequest(BaseModel):
  id: int
  
class UpdateRequest(BaseModel):
  id: int
  update: Dinosaur