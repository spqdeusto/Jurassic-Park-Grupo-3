from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from backend.controllers.handler import Controllers
from backend.mysql.mysql import DatabaseClient

import backend.utils.vars as gb
import backend.models.models as models

def initialize() -> None:
  """
  Inicializa la base de datos.
  """
  dbClient = DatabaseClient(gb.MYSQL_URL)
  dbClient.init_database()
  return

app = FastAPI()
controllers = Controllers()

initialize()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def status():
  """
  Verifica el estado del servidor.
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.check_status()

@app.get('/dinos')
async def get_all_dinos():
  """
  Obtiene todos los dinosaurios.
  
  @return Union[List[models.Dino], int]: Lista de dinosaurios o código de error.
  """
  return controllers.get_dinos()

@app.post('/recinto/down')
async def shutdown(body: models.GetRequest):
  """
  Apaga la electricidad del recinto.
  
  @args body (models.GetRequest): Datos de la solicitud.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.quit_electricity(body)

@app.post('/recinto/up')
async def shutdown(body: models.GetRequest):
  """
  Enciende la electricidad del recinto.
  
  @args body (models.GetRequest): Datos de la solicitud.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.put_electricity(body)

@app.get('/recintos')
async def get_all_recintos():
  """
  Obtiene todos los recintos.
  
  @return Union[List[models.Recinto], int]: Lista de recintos o código de error.
  """
  return controllers.get_recintos()

@app.get('/recintosEncendidos')
async def get_recintos_encendidos():
  """
  Obtiene los recintos encendidos.
  
  @return Union[List[models.Recinto], int]: Lista de recintos o código de error.
  """
  return controllers.recintosEncendidos()

@app.get('/recintosApagados')
async def get_recintos_apagados():
  """
  Obtiene los recintos apagados.
  
  @return Union[List[models.Recinto], int]: Lista de recintos o código de error.
  """
  return controllers.recintosApagados()

@app.get('/jeeps')
async def get_all_jeeps():
  """
  Obtiene todos los jeeps todo terreno.
  
  @return Union[List[models.TodoTerreno], int]: Lista de jeeps o código de error.
  """
  return controllers.get_jeeps()

@app.get('/jeepsRuta')
async def get_jeeps_ruta():
  """
  Obtiene los jeeps todo terreno que están en ruta.
  
  @return Union[List[models.TodoTerreno], int]: Lista de jeeps o código de error.
  """
  return controllers.jeepsEnRuta()

@app.get('/jeepsNoRuta')
async def get_jeeps_Noruta():
  """
  Obtiene los jeeps todo terreno que no están en ruta.
  
  @return Union[List[models.TodoTerreno], int]: Lista de jeeps o código de error.
  """
  return controllers.jeepsNoEnRuta()

@app.post('/jeep/ruta/up')
async def shutdown(body: models.GetRequest):
  """
  Inicia la ruta de un jeep todo terreno.
  
  @args body (models.GetRequest): Datos de la solicitud.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.startRuta(body)

@app.post('/jeep/ruta/down')
async def shutdown(body: models.GetRequest):
  """
  Finaliza la ruta de un jeep todo terreno.
  
  @args body (models.GetRequest): Datos de la solicitud.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.quitRuta(body)

@app.post('/recinto/create')
async def create_recinto(body: models.Recinto):
  """
  Crea un nuevo recinto.
  
  @args body (models.Recinto): Datos del recinto a crear.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.create_recinto(body)

@app.post('/dinosaur/create')
async def create_dinosaur(body: models.Dinosaur):
  """
  Crea un nuevo dinosaurio.
  
  @args body (models.Dinosaur): Datos del dinosaurio a crear.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.create_dinosaur(body)

@app.post('/todoterreno/create')
async def create_todoterreno(body: models.TodoTerreno):
  """
  Crea un nuevo jeep todo terreno.
  
  @args body (models.TodoTerreno): Datos del jeep todo terreno a crear.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.create_todoterreno(body)

@app.post('/recinto/delete')
async def delete_recinto(body: models.DeleteRequest):
  """
  Elimina un recinto.
  
  @args body (models.DeleteRequest): Datos de la solicitud de eliminación.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.delete_recinto(body)

@app.post('/dinosaur/delete')
async def delete_dinosaur(body: models.DeleteRequest):
  """
  Elimina un dinosaurio.
  
  @args body (models.DeleteRequest): Datos de la solicitud de eliminación.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.delete_dinosaur(body)

@app.post('/todoterreno/delete')
async def delete_todoterreno(body: models.DeleteRequest):
  """
  Elimina un jeep todo terreno.
  
  @args body (models.DeleteRequest): Datos de la solicitud de eliminación.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.delete_todoterreno(body)

@app.post('/recinto/update')
async def update_recinto(body: models.UpdateRecinto):
  """
  Actualiza la información de un recinto.
  
  @args body (models.UpdateRecinto): Datos de la solicitud de actualización.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.update_recinto(body)

@app.post('/dinosaur/update')
async def update_dinosaur(body: models.UpdateDinosaur):
  """
  Actualiza la información de un dinosaurio.
  
  @args body (models.UpdateDinosaur): Datos de la solicitud de actualización.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.update_dinosaur(body)

@app.post('/todoterreno/update')
async def update_todoterreno(body: models.UpdateTodoTerreno):
  """
  Actualiza la información de un jeep todo terreno.
  
  @args body (models.UpdateTodoTerreno): Datos de la solicitud de actualización.
  
  @return Union[str, int]: Mensaje de éxito o código de error.
  """
  return controllers.update_todoterreno(body)