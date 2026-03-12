from datetime import date
from pydantic import BaseModel


class TripBase(BaseModel):
    title: str
    destination: str
    start_date: date
    end_date: date
    budget: float


class TripCreate(TripBase):
    pass


class TripUpdate(TripBase):
    pass


class TripResponse(TripBase):
    id: int

    class Config:
        orm_mode = True