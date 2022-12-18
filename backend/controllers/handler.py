import backend.models.models as models
import backend.mysql.models as mysql_models
from backend.mysql.mysql import DatabaseClient

import backend.utils.vars as gb
from sqlalchemy.orm import Session

class Controllers:
  """
    Esta clase proporciona métodos para interactuar con la base de datos y realizar
  diversas operaciones relacionadas con dinosaurios y recintos.
  """
  def __init__(self) -> None:
    """
      Constructor de la clase.

      @return: None
    """
    pass
    
  def get_dinos(self):

    """
      Recupera todos los dinosaurios de la base de datos.

      @return: Una lista de objetos Dinosaur.
    """

    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      dinos = session.query(mysql_models.Dinosaur).all()
      session.close()
    return dinos

  def startRuta(self, body: models.GetRequest):

    """
      Cambia el valor del campo "ruta" a 1 para el TodoTerreno especificado
      en el cuerpo de la solicitud. Luego, llama al método check_status y
      devuelve el resultado.

      @param body: Un objeto GetRequest que contiene el ID del TodoTerreno.
      @return: El resultado del método check_status.
    """
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.query(mysql_models.TodoTerreno).filter(mysql_models.TodoTerreno.id==body.id).update({"ruta": 1})
      session.commit()
      session.close()
    
    return {"status": "ok"}
  
  def quitRuta(self, body: models.GetRequest):

    """
      Cambia el valor del campo "ruta" a 0 para el TodoTerreno especificado
      en el cuerpo de la solicitud. Luego, llama al método jeepStateDown con
      el ID del TodoTerreno especificado y finalmente devuelve el resultado
      del método check_status.

      @param body: Un objeto GetRequest que contiene el ID del TodoTerreno.
      @return: El resultado del método check_status.
    """
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.query(mysql_models.TodoTerreno).filter(mysql_models.TodoTerreno.id==body.id).update({"ruta": 0})
      session.commit()
      session.close()
    self.jeepStateDown(body.id)
    
    return {"status": "ok"}
  
  def get_recintos(self):
    """
      Recupera todos los recintos de la base de datos y para cada recinto,
      recupera la lista de dinosaurios que están asignados a ese recinto.

      @return: Una lista de objetos Recinto con una propiedad adicional "dinosaurs"
                que contiene la lista de dinosaurios asociados al recinto.
    """

    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      recintos = session.query(mysql_models.Recinto).all()
      for recinto in recintos:
        recinto.dinosaurs = list(session.query(mysql_models.Dinosaur).where(mysql_models.Dinosaur.recinto==recinto.id))
      session.close()

    return recintos
  
  def dangerousness(self):
    """
    Comprueba si hay algún dinosaurio peligroso en algún recinto apagado.

    @return: True si hay algún dinosaurio peligroso en algún recinto apagado, False en caso contrario.
    """

    recintos = self.get_recintos()

    for recinto in recintos:
      if(recinto.state==False):
        for dino in recinto.dinosaurs:
          if(dino.dangerousness==True):
            return True

    return False
  
  def get_jeeps(self):
    """
    Recupera todos los TodoTerreno de la base de datos.

    @return: Una lista de objetos TodoTerreno.
    """

    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      jeeps = session.query(mysql_models.TodoTerreno).all()
      session.close()

    return jeeps

  def jeepsEnRuta(self):
    """
    Recupera todos los TodoTerreno que están en ruta.

    @return: Una lista de objetos TodoTerreno que están en ruta.
    """
    
    enRuta = []
    jeeps = self.get_jeeps()

    for jeep in jeeps:
      if(jeep.ruta):
        enRuta.append(jeep)

    return enRuta

  def jeepsNoEnRuta(self):
    """
    Recupera todos los TodoTerreno que no están en ruta.

    @return: Una lista de objetos TodoTerreno que no están en ruta.
    """
    
    NoenRuta = []
    jeeps = self.get_jeeps()

    for jeep in jeeps:
      if(jeep.ruta==False):
        NoenRuta.append(jeep)
    
    return NoenRuta

  def recintosApagados(self):
    """
    Recupera todos los recintos apagados.

    @return: Una lista de objetos Recinto que están apagados.
    """
    
    apagados = []
    recintos = self.get_recintos()

    for recinto in recintos:
      if(recinto.system==False):
        apagados.append(recinto)
    
    return apagados

  def recintosEncendidos(self):
    """
    Recupera todos los recintos encendidos.

    @return: Una lista de objetos Recinto que están encendidos.
    """
    
    encendidos = []
    recintos = self.get_recintos()

    for recinto in recintos:
      if(recinto.system==True):
        encendidos.append(recinto)
    
    return encendidos
    
  def jeepStateUp(self):
    """
    Cambia el valor del campo "sistemaseguridad" a 1 para todos los TodoTerreno que estén en ruta.

    @return: None
    """

    enRuta = self.jeepsEnRuta()
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      for jeep in enRuta:
        session.query(mysql_models.TodoTerreno).filter(mysql_models.TodoTerreno.id==jeep.id).update({"sistemaseguridad": 1})
      session.commit()
    session.close()
    return {"status": "ok"}

  def jeepStateDownAll(self):
    """
    Apaga el sistema de seguridad de todos los Jeep que se encuentran en ruta.
    
    @param self: objeto de la clase actual
    @return: un diccionario con el estado de la operación
    """

    enRuta = self.jeepsEnRuta()
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      for jeep in enRuta:
        session.query(mysql_models.TodoTerreno).filter(mysql_models.TodoTerreno.id==jeep.id).update({"sistemaseguridad": 0})
      session.commit()
    session.close()
    return {"status": "ok"}
  
  def jeepStateDown(self, id: int):
    """
    Cambia el valor del campo "sistemaseguridad" a 0 para el TodoTerreno con el ID especificado.

    @param id: El ID del TodoTerreno a actualizar.
    @return: None
    """

    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.query(mysql_models.TodoTerreno).filter(mysql_models.TodoTerreno.id==id).update({"sistemaseguridad": 0})
      session.commit()
      session.close()
    return {"status": "ok"}
  
  def check_electricity(self):
    """
    Verifica si hay algún recinto apagado.

    @return: True si hay al menos un recinto apagado, False en caso contrario.
    """
    
    for recinto in self.get_recintos():
      if(recinto.state==False):
        return False
    return True
  
  def check_status(self):
    """
    Verifica el estado del parque y devuelve información sobre él.

    @return: Un diccionario con la información del estado del parque. La clave "alerta"
             indica el nivel de alerta actual (puede ser "normal", "baja", "media" o "maxima"),
             las claves "recintos" y "jeeps" contienen listas de objetos Recinto y TodoTerreno,
             respectivamente.
    """
    
    if(self.dangerousness() and self.jeepsEnRuta()):
        self.jeepStateUp()
        response = {"alerta": "maxima", "recintos": self.get_recintos(), "jeeps": self.get_jeeps()}

    elif(self.dangerousness()):
      response = {"alerta": "media", "recintos": self.get_recintos(), "jeeps": self.get_jeeps()}
    
    elif(not self.check_electricity()):
      self.jeepStateDownAll()
      response = {"alerta": "baja", "recintos": self.get_recintos(), "jeeps": self.get_jeeps()}

    else:
      self.jeepStateDownAll()
      response = {"alerta": "normal", "recintos": self.get_recintos(), "jeeps": self.get_jeeps()}
    
    return response
  
  def quit_electricity(self, body: models.GetRequest):
    """
    Quita la electricidad de la pared de un recinto específico.

    @param body: El objeto GetRequest que contiene el ID del recinto.
    @return: Un diccionario con la información del estado del parque después de quitar la electricidad.
             La clave "alerta" indica el nivel de alerta actual (puede ser "normal", "baja", "media" o "maxima"),
             las claves "recintos" y "jeeps" contienen listas de objetos Recinto y TodoTerreno,
             respectivamente.
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.query(mysql_models.Recinto).filter(mysql_models.Recinto.id==body.id).update({"state": 0})
      session.commit()
      session.close()
    
    return {"status": "ok"}
  
  def put_electricity(self, body: models.GetRequest):
    """
    Pone la electricidad de la pared de un recinto específico.

    @param body: El objeto GetRequest que contiene el ID del recinto.
    @return: Un diccionario con la información del estado del parque después de poner la electricidad.
             La clave "alerta" indica el nivel de alerta actual (puede ser "normal", "baja", "media" o "maxima"),
             las claves "recintos" y "jeeps" contienen listas de objetos Recinto y TodoTerreno,
             respectivamente.
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.query(mysql_models.Recinto).filter(mysql_models.Recinto.id==body.id).update({"state": 1})
      session.commit()
      session.close()
    
    return self.check_status()
  
  def create_recinto(self, body: models.Recinto):
    """
    Crea un nuevo recinto en la base de datos.

    @param body: El objeto Recinto que contiene la información del recinto a crear.
    @return: None
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
    Crea un nuevo dinosaurio en la base de datos.

    @param body: El objeto Dinosaur que contiene la información del dinosaurio a crear.
    @return: Un diccionario con una clave "status" y un valor "ok" en caso de éxito.
    """
    print(body)
    body_row = mysql_models.Dinosaur(name=body.name, species=body.species, age=body.age, weigh=body.weigh, gender=body.gender, dangerousness=body.dangerousness, recinto=body.recinto)
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}
  
  def create_todoterreno(self, body: models.TodoTerreno):
    """
    Crea un nuevo todoterreno en la base de datos.

    @param body: El objeto TodoTerreno que contiene la información del todoterreno a crear.
    @return: Un diccionario con una clave "status" y un valor "ok" en caso de éxito.
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
    Elimina un recinto por su UID.
    
    @param body: Un objeto DeleteRequest que contiene el UID del recinto a eliminar.
    @type body: models.DeleteRequest
    @return: Un diccionario que indica el estado de la operación.
    @rtype: dict
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
    Elimina un dinosaurio por su UID.
    
    @param body: Un objeto DeleteRequest que contiene el UID del dinosaurio a eliminar.
    @type body: models.DeleteRequest
    @return: Un diccionario que indica el estado de la operación.
    @rtype: dict
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
    Elimina un todoterreno por su UID.
    
    @param body: Un objeto DeleteRequest que contiene el UID del todoterreno a eliminar.
    @type body: models.DeleteRequest
    @return: Un diccionario que indica el estado de la operación.
    @rtype: dict
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
    Actualiza un recinto por su ID.
    
    @param body: Un objeto UpdateRecinto que contiene el ID y la información actualizada del recinto.
    @type body: models.UpdateRecinto
    @return: Un diccionario que indica el estado de la operación.
    @rtype: dict
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      recinto: mysql_models.Recinto = session.query(mysql_models.Recinto).get(body.id)
      recinto.name = body.update.name
      recinto.state = body.update.state
      session.dirty
      session.commit()
      session.close()
      
    return {"status": "ok"}

  def update_dinosaur(self, body: models.UpdateDinosaur):
    """
    Actualiza un dinosaurio por su ID.
    
    @param body: Un objeto UpdateDinosaur que contiene el ID y la información actualizada del dinosaurio.
    @type body: models.UpdateDinosaur
    @return: Un diccionario que indica el estado de la operación.
    @rtype: dict
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
    Actualiza un todoterreno por su ID.
    
    @param body: Un objeto UpdateTodoTerreno que contiene el ID y la información actualizada del todoterreno.
    @type body: models.UpdateTodoTerreno
    @return: Un diccionario que indica el estado de la operación.
    @rtype: dict
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      todoterreno: mysql_models.TodoTerreno = session.query(mysql_models.TodoTerreno).get(body.id)
      todoterreno.ruta = body.update.ruta
      todoterreno.numvisitantes = body.update.numvisitantes
      todoterreno.sistemaseguridad = body.update.sistemaseguridad
      session.dirty
      session.commit()
      session.close()
      
    return {"status": "ok"}