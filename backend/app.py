from fastapi import FastAPI
from routes.dinosaur import dinosaur
from config.openapi import tags_metadata
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Dinosaurs API",
    description="REST API CRUD using FastAPI and SqlAlchemy",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"

app.include_router(dinosaur)