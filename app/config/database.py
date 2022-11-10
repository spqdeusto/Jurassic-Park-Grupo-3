from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+mysqlconnector://jurassic@localhost:3306/jurassic")
meta = MetaData()
conn = engine.connect()