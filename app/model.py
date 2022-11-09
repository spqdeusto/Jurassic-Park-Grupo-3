from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base
class Dinosaur(Base):
    __tablename__ = "Dinosaur"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    species = Column(String(20))
    age = Column(Integer)
    dangerousness = Column(Integer)