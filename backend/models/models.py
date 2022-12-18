from pydantic import BaseModel
"""
class Especie(BaseModel):
  name:str
  class Config:
    orm_mode=True
"""
class Dinosaur(BaseModel):

  """
    Modelo que representa un dinosaurio.
    
    @param id: El ID único del dinosaurio.
    @type id: int
    @param name: El nombre del dinosaurio.
    @type name: str
    @param species: La especie a la que pertenece el dinosaurio.
    @type species: str
    @param age: La edad del dinosaurio.
    @type age: int
    @param weigh: El peso del dinosaurio.
    @type weigh: int
    @param gender: El género del dinosaurio.
    @type gender: bool
    @param dangerousness: Si el dinosaurio es peligroso o no.
    @type dangerousness: bool
    @param recinto: El ID del recinto en el que se encuentra el dinosaurio.
    @type recinto: int
    """
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

  """
    Modelo que representa un todoterreno.
    
    @param id: El ID único del todoterreno.
    @type id: int
    @param ruta: La ruta que sigue el todoterreno.
    @type ruta: bool
    @param numvisitantes: El número de visitantes permitidos en el todoterreno.
    @type numvisitantes: int
    @param sistemaseguridad: Si el todoterreno cuenta con sistema de seguridad o no.
    @type sistemaseguridad: bool
    """
  id:int
  ruta: bool
  numvisitantes: int
  sistemaseguridad: bool
  class Config:
    orm_mode=True

class Recinto(BaseModel):
  """
    Modelo que representa un recinto.
    
    @param id: El ID único del recinto.
    @type id: int
    @param name: El nombre del recinto.
    @type name: str
    @param state: El estado del recinto (abierto o cerrado).
    @type state: bool
    @param dinosaurs: La lista de dinosaurios que se encuentran en el recinto.
    @type dinosaurs: list[Dinosaur]
    """

  id: int
  name: str
  state: bool
  dinosaurs: list[Dinosaur]
  class Config:
    orm_mode=True

class GetRequest(BaseModel):
  """
    Modelo que representa una solicitud de obtención de información.
    
    @param id: El ID del elemento que se desea obtener.
    @type id: int
    """
  id:int
  
class DeleteRequest(BaseModel):
  """
  Modelo que representa una solicitud de eliminación.
  
  @param id: El ID del elemento que se desea eliminar.
  @type id: int
  """
  id: int
  
class UpdateDinosaur(BaseModel):
  """
    Modelo que representa una solicitud de actualización de dinosaurio.
    
    @param id: El ID del dinosaurio que se desea actualizar.
    @type id: int
    @param update: Los datos actualizados para el dinosaurio.
    @type update: Dinosaur
    """
  id: int
  update: Dinosaur

class UpdateRecinto(BaseModel):
  """
    Modelo que representa una solicitud de actualización de recinto.
    
    @param id: El ID del recinto que se desea actualizar.
    @type id: int
    @param update: Los datos actualizados para el recinto.
    @type update: Recinto
    """
  id: int
  update: Recinto

class UpdateTodoTerreno(BaseModel):
  """
    Modelo que representa una solicitud de actualización de todoterreno.
    
    @param id: El ID del todoterreno que se desea actualizar.
    @type id: int
    @param update: Los datos actualizados para el todoterreno.
    @type update: TodoTerreno
    """
  id: int
  update: TodoTerreno
