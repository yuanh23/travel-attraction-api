from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/destinations", tags=["Destinations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.DestinationResponse])
def get_destinations(db: Session = Depends(get_db)):
    return db.query(models.Destination).limit(100).all()


@router.get("/country/{country}", response_model=List[schemas.DestinationResponse])
def get_by_country(country: str, db: Session = Depends(get_db)):
    return db.query(models.Destination).filter(
        models.Destination.country == country
    ).all()


@router.get("/top-rated", response_model=List[schemas.DestinationResponse])
def top_rated(db: Session = Depends(get_db)):
    return db.query(models.Destination).order_by(
        models.Destination.avg_rating.desc()
    ).limit(10).all()


@router.get("/budget-friendly", response_model=List[schemas.DestinationResponse])
def budget_friendly(db: Session = Depends(get_db)):
    return db.query(models.Destination).order_by(
        models.Destination.avg_cost_per_day.asc()
    ).limit(10).all()