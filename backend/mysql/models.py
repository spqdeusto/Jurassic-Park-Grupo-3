from sqlalchemy import Column, Integer, String, Sequence, Boolean
from backend.mysql.base import Base


class Dinosaur(Base):
  __tablename__ = "dinosaurs"
  id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
  name = Column(String(25))
  species = Column(String(25))
  age = Column(Integer)
  weigh = Column(Integer)
  sex = Column(String(25))
  dangerousness = Column(String(25))


  def __repr__(self) -> str:
    return "<Dinosaur(id= '%d', name='%s', species='%s', age='%d', weigh='%d', sex='%s', dangerousness='%s')>" % (
      self.id,
      self.name,
      self.species,
      self.age,
      self.weigh,
      self.sex,
      self.dangerousness,
    )