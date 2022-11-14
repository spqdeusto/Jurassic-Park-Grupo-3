from sqlalchemy.schema import Table, Column
from sqlalchemy.types import String, Integer
from config.database import meta, engine

dinosaurs = Table("dinosaurs", meta, Column(
    "id", Integer, primary_key=True, index=True),
    Column("name", String(20)),
    Column("species", String(20)),
    Column("age", Integer),
    Column("dangerousness", Integer))

meta.create_all(bind=engine)