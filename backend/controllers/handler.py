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

  def get_all(self):
    """
    Gets all dinosaurs
    """
    db = DatabaseClient(gb.MYSQL_URL)
    response: list = []
    with Session(db.engine) as session:
      response = session.query(mysql_models.Dinosaur).all()
      session.close()
      
    return response

  def get_dinosaur(self, id: int):
    """
    Selects dinosaur by its UID
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      dinosaur = session.query(mysql_models.Dinosaur).get(id)
      session.close()
      
    return dinosaur
  
  def create_dinosaur(self, body: models.Dinosaur):
    """
    Creates new dinosaur in  the database
    """
    body_row = mysql_models.Dinosaur(name=body.name, species=body.species, age=body.age, weigh=body.weigh, sex=body.sex, dangerousness=body.dangerousness)
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}
  
  def delete_dinosaur(self, id: int):
    """
    Deletes dinosaur by its UID
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      dinosaurToBeDeleted = session.query(mysql_models.Dinosaur).get(id)
      session.delete(dinosaurToBeDeleted)
      session.commit()
      session.close()
      
    return {"status": "ok"}
  
  def update_dinosaur(self, body: models.UpdateRequest):
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