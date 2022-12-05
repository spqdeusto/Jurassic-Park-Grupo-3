from pydantic import BaseModel
"""
class Especie(BaseModel):
  name:str
  class Config:
    orm_mode=True
"""
class Dinosaur(BaseModel):
  id: int
  name: str
  species: str
  age: int
  weigh: int
  gender: bool
  dangerousness: bool
  recinto: int
  class Config:
    orm_mode=True

class TodoTerreno(BaseModel):
  id:int
  ruta: bool
  numvisitantes: int
  sistemaseguridad: bool
  class Config:
    orm_mode=True

class Recinto(BaseModel):
  id: int
  name: str
  state: bool
  dinosaurs: list[Dinosaur]
  class Config:
    orm_mode=True

class GetRequest(BaseModel):
  id:int
  
class DeleteRequest(BaseModel):
  id: int
  
class UpdateDinosaur(BaseModel):
  id: int
  update: Dinosaur

class UpdateRecinto(BaseModel):
  id: int
  update: Recinto

class UpdateTodoTerreno(BaseModel):
  id: int
  update: TodoTerreno
