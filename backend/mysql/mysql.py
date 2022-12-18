import sqlalchemy as db
from backend.mysql.base import Base
from sqlalchemy.orm import sessionmaker


class DatabaseClient():
  """
  Clase que representa un cliente de base de datos
  """
  
  def __init__(self, url: str) -> None:
    """
      Inicializa una nueva instancia de la clase DatabaseClient.
      
      @param url (str): URL de la base de datos a la que se desea conectarse.
      @param engine (Engine): Objeto de motor de base de datos que se utiliza para conectarse a la base de datos.
    """
    engine = db.create_engine(url)
    self.engine = engine
    pass

  def init_database(self):
    """
    Inicializa la base de datos.
    """
    Base.metadata.create_all(self.engine)
    return
    
