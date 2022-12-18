from sqlalchemy import Column, Integer, String, Sequence, Boolean, CheckConstraint,ForeignKey
from backend.mysql.base import Base
from sqlalchemy.orm import relationship
"""
class Especie(Base):
  __tablename__ = "especies"
  id = Column(Integer, primary_key=True)
  name = Column(String(25), nullable=False)
  dinosaurs = relationship("Dinosaur", cascade="all, delete")

  def __repr__(self) -> str:
    return "<Especie(id= '%d', name='%s')>" % (
      self.id,
      self.name,
    )
"""
class Dinosaur(Base):
  """
    Esta clase representa a un dinosaurio en la base de datos.
    
    @param id (int): el ID único del dinosaurio en la base de datos.
    @param name (str): el nombre del dinosaurio.
    @param species (str): la especie a la que pertenece el dinosaurio.
    @param age (int): la edad del dinosaurio.
    @param weigh (int): el peso del dinosaurio.
    @param gender (bool): un valor booleano que indica si el dinosaurio es macho (True) o hembra (False).
    @param dangerousness (bool): un valor booleano que indica si el dinosaurio es agresivo (True) o pacífico (False).
    @param recinto (int): el ID del recinto al que pertenece el dinosaurio.
    
    @return: un objeto que representa al dinosaurio.
    """
  __tablename__ = "dinosaurs"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  name = Column(String(100))
  species = Column(String(100))
  age = Column(Integer)
  weigh = Column(Integer)
  #true es macho y false hembra
  gender = Column(Boolean(create_constraint=True), nullable=False)
  #true es agresivo, false pacifico
  dangerousness = Column(Boolean(create_constraint=True), nullable=False)
  recinto = Column(Integer, ForeignKey("recinto.id"), nullable=False)

  def __repr__(self) -> str:
    """
        Devuelve una representación en cadena del dinosaurio.
        
        @return: una cadena que representa al dinosaurio.
        """
    return "<Dinosaur(id= '%d', name='%s', species='%s', age='%d', weigh='%d', gender='%b', dangerousness='%b',recinto='%d')>" % (
      self.id,
      self.name,
      self.species,
      self.age,
      self.weigh,
      self.gender,
      self.dangerousness,
      self.recinto,
    )

class Recinto(Base):
  """
    Esta clase representa un recinto en la base de datos.
    
    @param id (int): el ID único del recinto en la base de datos.
    @param name (str): el nombre del recinto.
    @param state (bool): un valor booleano que indica si el recinto está abierto (True) o cerrado (False).
    @param dinosaurs (list): una lista de objetos Dinosaur que pertenecen al recinto.
    
    @return: un objeto que representa al recinto.
    """
  __tablename__ = "recinto"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  name = Column(String(100))
  state = Column(Boolean(create_constraint=True), nullable=False)
  dinosaurs = relationship("Dinosaur", cascade="all, delete")
  
  def __repr__(self) -> str:
    """
        Devuelve una representación en cadena del recinto.
        
        @return: una cadena que representa al recinto.
        """
    return "<Recinto(id= '%d', name='%s', state='%b')>" % (
      self.id,
      self.name,
      self.state,
    )

class TodoTerreno(Base):
  """
  Clase que representa un todo terreno.
  
  @param id (int): Identificador único del todo terreno.
  @param ruta (bool): Indica si el todo terreno es apto para recorrer rutas.
  @param  numvisitantes (int): Número de visitantes que puede llevar el todo terreno.
  @param  sistemaseguridad (bool): Indica si el todo terreno cuenta con sistema de seguridad.
  """
  __tablename__ = "todoterreno"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  ruta=Column(Boolean(create_constraint=True), nullable=False, default=False)
  numvisitantes=Column(Integer, CheckConstraint("numvisitantes > 1 AND numvisitantes < 6"))
  sistemaseguridad=Column(Boolean(create_constraint=True), nullable=False, default=False)

  def __repr__(self) -> str:
    """
    Devuelve una representación en forma de cadena del todo terreno.
    
    @return Representación en forma de cadena del todoterreno.
    """
    return "<TodoTerreno(id= '%d', ruta='%b', numvisitantes='%d', sistemaseguridad='%b')>" % (
      self.id,
      self.ruta,
      self.numvisitantes,
      self.sistemaseguridad,
    )
