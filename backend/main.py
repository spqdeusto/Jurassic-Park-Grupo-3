from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from backend.controllers.handler import Controllers
from backend.mysql.mysql import DatabaseClient

import backend.utils.vars as gb
import backend.models.models as models


def initialize() -> None:
  # initialize database
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

@app.get('/hello')
async def status():
  return controllers.hello()

@app.get('/')
async def status():
  return controllers.status()

@app.post('/recinto/down')
async def shutdown(body: models.GetRequest):
  return controllers.quit_electricity(body)

@app.post('/recinto/up')
async def shutdown(body: models.GetRequest):
  return controllers.put_electricity(body)

@app.get('/recintos')
async def get_all_recintos():
  return controllers.get_recintos()

@app.post('/jeep/ruta/up')
async def shutdown(body: models.GetRequest):
  return controllers.startRuta(body)

@app.post('/jeep/ruta/down')
async def shutdown(body: models.GetRequest):
  return controllers.quitRuta(body)



@app.post('/recinto/create')
async def create_recinto(body: models.Recinto):
  return controllers.create_recinto(body)

@app.post('/dinosaur/create')
async def create_dinosaur(body: models.Dinosaur):
  return controllers.create_dinosaur(body)

@app.post('/todoterreno/create')
async def create_todoterreno(body: models.TodoTerreno):
  return controllers.create_todoterreno(body)



@app.post('/recinto/delete')
async def delete_recinto(body: models.DeleteRequest):
  return controllers.delete_recinto(body.id)

@app.post('/dinosaur/delete')
async def delete_dinosaur(body: models.DeleteRequest):
  return controllers.delete_dinosaur(body.id)

@app.post('/todoterreno/delete')
async def delete_todoterreno(body: models.DeleteRequest):
  return controllers.delete_todoterreno(body.id)



@app.post('/recinto/update')
async def update_recinto(body: models.UpdateRecinto):
  return controllers.update_recinto(body)

@app.post('/dinosaur/update')
async def update_dinosaur(body: models.UpdateDinosaur):
  return controllers.update_dinosaur(body)

@app.post('/todoterreno/update')
async def update_todoterreno(body: models.UpdateTodoTerreno):
  return controllers.update_todoterreno(body)