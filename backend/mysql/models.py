from sqlalchemy import Column, Integer, String, Sequence, Boolean, CheckConstraint,ForeignKey
from backend.mysql.base import Base
from sqlalchemy.orm import relationship

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

class Dinosaur(Base):
  __tablename__ = "dinosaurs"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  name = Column(String(25))
  species = Column(Integer, ForeignKey("especies.id"), nullable=False)
  age = Column(Integer)
  weigh = Column(Integer)
  #true es macho y false hembra
  gender = Column(Boolean(create_constraint=True), nullable=False)
  #true es agresivo, false pacifico
  dangerousness = Column(Boolean(create_constraint=True), nullable=False)
  recinto = Column(Integer, ForeignKey("recinto.id"), nullable=False)

  def __repr__(self) -> str:
    return "<Dinosaur(id= '%d', name='%s', species='%s', age='%d', weigh='%d', gender='%b', dangerousness='%b',recinto='%s')>" % (
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
  __tablename__ = "recinto"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  name = Column(String(25))
  species = Column(String(25))
  state = Column(Boolean(create_constraint=True), nullable=False)
  dinosaurs = relationship("Dinosaur", cascade="all, delete")
  todoterrenos = relationship("TodoTerreno", cascade="all, delete")
  
  def __repr__(self) -> str:
    return "<Recinto(id= '%d', name='%s', species='%s', state='%b')>" % (
      self.id,
      self.name,
      self.species,
      self.state,
    )

class TodoTerreno(Base):
  __tablename__ = "todoterreno"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  ruta=Column(Boolean(create_constraint=True), nullable=False)
  numvisitantes=Column(Integer, CheckConstraint("numvisitantes > 1 AND numvisitantes < 6"))
  sistemaseguridad=Column(Boolean(create_constraint=True), nullable=False)
  recinto = Column(Integer, ForeignKey("recinto.id"), nullable=False)

  def __repr__(self) -> str:
    return "<TodoTerreno(id= '%d', ruta='%b', numvisitantes='%d', sistemaseguridad='%b', recinto='%s')>" % (
      self.id,
      self.ruta,
      self.numvisitantes,
      self.sistemaseguridad,
      self.recinto,
    )
