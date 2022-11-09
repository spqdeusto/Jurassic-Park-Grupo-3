from fastapi import FastAPI
import schema
from database import SessionLocal, engine
import model

model.Base.metadata.create_all(bind=engine)

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}