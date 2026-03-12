from fastapi import FastAPI

from . import models
from .database import engine
from .routers import trips, expenses, analytics, destinations, recommendations

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Attraction API")

app.include_router(trips.router)
app.include_router(expenses.router)
app.include_router(analytics.router)
app.include_router(destinations.router)
app.include_router(recommendations.router)


@app.get("/")
def root():
    return {"message": "Travel Attraction API is running"}