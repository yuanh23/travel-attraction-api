from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from .. import models
from ..database import SessionLocal

router = APIRouter(prefix="/analytics", tags=["Analytics"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/trip/{trip_id}/total-spent")
def get_total_spent(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(models.Trip).filter(models.Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    total = db.query(func.sum(models.Expense.amount)).filter(
        models.Expense.trip_id == trip_id
    ).scalar()

    return {
        "trip_id": trip_id,
        "total_spent": total or 0
    }


@router.get("/trip/{trip_id}/remaining-budget")
def get_remaining_budget(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(models.Trip).filter(models.Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    total = db.query(func.sum(models.Expense.amount)).filter(
        models.Expense.trip_id == trip_id
    ).scalar()

    total_spent = total or 0
    remaining_budget = trip.budget - total_spent

    return {
        "trip_id": trip_id,
        "budget": trip.budget,
        "total_spent": total_spent,
        "remaining_budget": remaining_budget
    }