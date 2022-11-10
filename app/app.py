from fastapi import FastAPI
from routes.dinosaur import dinosaur
from config.openapi import tags_metadata

app = FastAPI(
    title="Dinosaurs API",
    description="REST API CRUD using FastAPI and SqlAlchemy",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(dinosaur)