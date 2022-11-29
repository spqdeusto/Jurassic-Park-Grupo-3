from fastapi import FastAPI
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


@app.get('/')
async def status():
  return controllers.status()

@app.get('/dinosaurs')
async def get_all_dinosaurs():
  return controllers.get_all()

@app.post('/dinosaur')
async def get_dinosaur(body: models.GetRequest):
  return controllers.get_dinosaur(body.id)

@app.post('/dinosaur/create')
async def create_dinosaur(body: models.Dinosaur):
  return controllers.create_dinosaur(body)

@app.post('/dinosaur/delete')
async def delete_dinosaur(body: models.DeleteRequest):
  return controllers.delete_dinosaur(body.id)

@app.post('/dinosaur/update')
async def update_dinosaur(body: models.UpdateRequest):
  return controllers.update_dinosaur(body)