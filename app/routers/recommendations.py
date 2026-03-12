from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/budget/{max_cost}", response_model=List[schemas.DestinationResponse])
def recommend_by_budget(max_cost: float, db: Session = Depends(get_db)):
    return db.query(models.Destination).filter(
        models.Destination.avg_cost_per_day <= max_cost
    ).order_by(models.Destination.avg_rating.desc()).limit(10).all()


@router.get("/season/{season}", response_model=List[schemas.DestinationResponse])
def recommend_by_season(season: str, db: Session = Depends(get_db)):
    return db.query(models.Destination).filter(
        models.Destination.best_season.ilike("%" + season + "%")
    ).order_by(models.Destination.avg_rating.desc()).limit(10).all()


@router.get("/trending", response_model=List[schemas.DestinationResponse])
def trending_destinations(db: Session = Depends(get_db)):
    return db.query(models.Destination).order_by(
        models.Destination.annual_visitors_millions.desc()
    ).limit(10).all()