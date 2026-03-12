from fastapi import FastAPI

from . import models
from .database import engine
from .routers import trips

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Attraction API")

app.include_router(trips.router)


@app.get("/")
def root():
    return {"message": "Travel Attraction API is running"}