import backend.models.models as models
import backend.mysql.models as mysql_models
from backend.mysql.mysql import DatabaseClient

import backend.utils.vars as gb
from sqlalchemy.orm import Session

class Controllers:
  def __init__(self) -> None:
    pass
  
  def status(self):
    """
    Checks server status
    """
    return {"status": "ok"}

  def get_recintos(self):

    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      recintos = session.query(mysql_models.Recinto).all()
      for recinto in recintos:
        recinto.dinosaurs = list(session.query(mysql_models.Dinosaur).where(mysql_models.Dinosaur.id==recinto.id))

    return recintos
  
  def create_recinto(self, body: models.Recinto):
    """
    Creates new recinto in the database
    """
    body_row = mysql_models.Recinto(name=body.name, state=body.state)

    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}
  
  def create_dinosaur(self, body: models.Dinosaur):
    """
    Creates new dinosaur in the database
    """
    body_row = mysql_models.Dinosaur(name=body.name, species=body.species, age=body.age, weigh=body.weigh, gender=body.gender, dangerousness=body.dangerousness, recinto=body.recinto)
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}
  
  def create_todoterreno(self, body: models.TodoTerreno):
    """
    Creates new todoterreno in the database
    """
    body_row = mysql_models.TodoTerreno(ruta=body.ruta, numvisitantes=body.numvisitantes, sistemaseguridad=body.sistemaseguridad)

    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}
  
  def delete_recinto(self, body: models.DeleteRequest):
    """
    Deletes recinto by its UID
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      recintoToBeDeleted = session.query(mysql_models.Recinto).get(body.id)
      session.delete(recintoToBeDeleted)
      session.commit()
      session.close()
      
    return {"status": "ok"}

  def delete_dinosaur(self, body: models.DeleteRequest):
    """
    Deletes dinosaur by its UID
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      dinosaurToBeDeleted = session.query(mysql_models.Dinosaur).get(body.id)
      session.delete(dinosaurToBeDeleted)
      session.commit()
      session.close()
      
    return {"status": "ok"}

  def delete_todoterreno(self, body: models.DeleteRequest):
    """
    Deletes todoterreno by its UID
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      todoterrenoToBeDeleted = session.query(mysql_models.TodoTerreno).get(body.id)
      session.delete(todoterrenoToBeDeleted)
      session.commit()
      session.close()
      
    return {"status": "ok"}
  
  def update_recinto(self, body: models.UpdateRecinto):
    """
    Updates recinto by its ID
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      recinto: mysql_models.Dinosaur = session.query(mysql_models.Dinosaur).get(body.id)
      recinto.name = body.update.name
      recinto.state = body.update.state
      session.dirty
      session.commit()
      session.close()
      
    return {"status": "ok"}

  def update_dinosaur(self, body: models.UpdateDinosaur):
    """
    Updates dinosaur by its ID
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      dinosaur: mysql_models.Dinosaur = session.query(mysql_models.Dinosaur).get(body.id)
      dinosaur.name = body.update.name
      dinosaur.species = body.update.species
      dinosaur.age = body.update.age
      dinosaur.weigh = body.update.weigh
      dinosaur.sex = body.update.sex
      dinosaur.dangerousness = body.update.dangerousness
      session.dirty
      session.commit()
      session.close()
      
    return {"status": "ok"}
  
  def update_todoterreno(self, body: models.UpdateTodoTerreno):
    """
    Updates todoterreno by its ID
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      todoterreno: mysql_models.Dinosaur = session.query(mysql_models.TodoTerreno).get(body.id)
      todoterreno.ruta = body.update.ruta
      todoterreno.numvisitantes = body.update.numvisitantes
      todoterreno.sistemaseguridad = body.update.sistemaseguridad
      session.dirty
      session.commit()
      session.close()
      
    return {"status": "ok"}