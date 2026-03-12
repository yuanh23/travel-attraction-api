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

class ExpenseBase(BaseModel):
    trip_id: int
    category: str
    amount: float
    date: date
    note: str = None


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(ExpenseBase):
    pass


class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        orm_mode = True

class DestinationBase(BaseModel):
    destination_name: str
    country: str
    continent: str = None
    destination_type: str = None
    avg_cost_per_day: float = None
    best_season: str = None
    avg_rating: float = None
    annual_visitors_millions: float = None
    unesco_site: str = None


class DestinationResponse(DestinationBase):
    id: int

    class Config:
        orm_mode = True