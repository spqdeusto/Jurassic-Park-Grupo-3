from fastapi import APIRouter, Response, status
from config.database import conn
from models.dinosaur import dinosaurs
from schemas.dinosaur import Dinosaur
from starlette.status import HTTP_204_NO_CONTENT

dinosaur = APIRouter()

@dinosaur.get("/dinosaurs", tags=["dinosaurs"])
def get_dinosaurs():
	return conn.execute(dinosaurs.select()).all()

@dinosaur.post("/dinosaur", response_model=Dinosaur, tags=["dinosaurs"])
def create_dinosaur(dinosaur: Dinosaur):
	new_dinosaur = {"name": dinosaur.name, "species": dinosaur.species, "age": dinosaur.age, "dangerousness": dinosaur.dangerousness}
	result = conn.execute(dinosaurs.insert().values(new_dinosaur))
	return conn.execute(dinosaurs.select().where(dinosaurs.c.id==result.lastrowid)).first()

@dinosaur.get("/dinosaurs/{id}", response_model=Dinosaur, tags=["dinosaurs"])
def get_dinosaur(id: str):
	return conn.execute(dinosaurs.select().where(dinosaurs.c.id==id)).first()

@dinosaur.delete("/dinosaur/", status_code=status.HTTP_204_NO_CONTENT, tags=["dinosaurs"])
def delete_dinosaur(id: str):
	conn.execute(dinosaurs.delete().where(dinosaurs.c.id==id))
	return Response(status_code=HTTP_204_NO_CONTENT)

@dinosaur.put("/dinosaurs/{id}", response_model=Dinosaur, tags=["dinosaurs"])
def update_dinosaur(id: str, dinosaur: Dinosaur):
	conn.execute(dinosaurs.update().values(name=dinosaur.name,species=dinosaur.species,age=dinosaur.age,dangerousness=dinosaur.dangerousness).where(dinosaurs.c.id==id))
	return conn.execute(dinosaurs.select().where(dinosaurs.c.id==id)).first()