import pandas as pd

from app.database import SessionLocal, engine
from app import models

models.Base.metadata.create_all(bind=engine)


def import_destinations():
    df = pd.read_csv("data/tourist_destinations.csv")

    db = SessionLocal()

    for _, row in df.iterrows():
        destination = models.Destination(
            destination_name=row["Destination Name"],
            country=row["Country"],
            continent=row["Continent"],
            destination_type=row["Type"],
            avg_cost_per_day=row["Avg Cost (USD/day)"],
            best_season=row["Best Season"],
            avg_rating=row["Avg Rating"],
            annual_visitors_millions=row["Annual Visitors (M)"],
            unesco_site=row["UNESCO Site"],
        )
        db.add(destination)

    db.commit()
    db.close()


if __name__ == "__main__":
    import_destinations()