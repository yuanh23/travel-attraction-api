from sqlalchemy import Column, Date, Float, Integer, String
from .database import Base
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    budget = Column(Float, nullable=False)

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    note = Column(String, nullable=True)

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    destination_name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    continent = Column(String, nullable=True)
    destination_type = Column(String, nullable=True)
    avg_cost_per_day = Column(Float, nullable=True)
    best_season = Column(String, nullable=True)
    avg_rating = Column(Float, nullable=True)
    annual_visitors_millions = Column(Float, nullable=True)
    unesco_site = Column(String, nullable=True)

