from sqlalchemy import Column, Integer, String, Sequence, Boolean, CheckConstraint
from backend.mysql.base import Base


class Dinosaur(Base):
  __tablename__ = "dinosaurs"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  name = Column(String(25))
  species = Column(String(25))
  age = Column(Integer)
  weigh = Column(Integer)
  gender = Column(String(25))
  dangerousness = Column(String(25))


  def __repr__(self) -> str:
    return "<Dinosaur(id= '%d', name='%s', species='%s', age='%d', weigh='%d', gender='%s', dangerousness='%s')>" % (
      self.id,
      self.name,
      self.species,
      self.age,
      self.weigh,
      self.gender,
      self.dangerousness,
    )
class TodoTerrenoRequest(BaseModel):
  ruta:bool
  numvisitantes:int
  sistemaseguridad:bool

class TodoTerreno(Base):
  __tablename__ = "todoterreno"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  ruta=Column(Boolean(create_constraint=True), nullable=False)
  numvisitantes=Column(Integer, CheckConstraint("numvisitantes > 1 AND numvisitantes < 6"))
  sistemaseguridad=Column(Boolean(create_constraint=True), nullable=False)
  #recinto = Column(String(100), ForeignKey("recinto.nme", ondelete="CASCADE"), nullable=False)


  def __repr__(self) -> str:
    return "<TodoTerreno(id= '%d', ruta='%b', numvisitantes='%d', sistemaseguridad='%b')>" % (
      self.id,
      self.ruta,
      self.numvisitantes,
      self.sistemaseguridad,
    )
