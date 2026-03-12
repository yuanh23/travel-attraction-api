# Travel Budget and Destination Recommendation API

## Overview
This project is a data-driven web API built with FastAPI and SQLite. It allows users to manage trips and expenses, analyse travel budgets, and explore destination recommendations using a public tourism dataset.

## Features
- CRUD operations for trips
- CRUD operations for expenses
- Budget analytics for trips
- Destination dataset integration
- Recommendation endpoints based on budget, season, trending popularity, and trip budget

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pandas
- Uvicorn

## Project Structure

```
app/
  main.py
  database.py
  models.py
  schemas.py
  import_destinations.py
  routers/
    trips.py
    expenses.py
    analytics.py
    destinations.py
    recommendations.py
data/
  tourist_destinations.csv
requirements.txt
README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yuanh23/travel-attraction-api.git
cd travel-attraction-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Import the destination dataset

Before running the API, import the tourism dataset into the database.

```bash
python -m app.import_destinations
```

### 4. Run the API server

```bash
uvicorn app.main:app --reload
```

### 5. Open API documentation

Open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows interactive testing of all API endpoints.

## Dataset

This project uses a public tourism dataset from Kaggle (https://www.kaggle.com/datasets/umeradnaan/tourism-dataset?utm_source=chatgpt.com) containing information about global travel destinations.

Dataset fields include:

- Destination Name
- Country
- Continent
- Type
- Avg Cost (USD/day)
- Best Season
- Avg Rating
- Annual Visitors (M)
- UNESCO Site

The dataset is imported into the database using the script:

```bash
python -m app.import_destinations
```

## API Endpoints

### Trips

| Method | Endpoint | Description |
|------|------|------|
POST | `/trips/` | Create a new trip |
GET | `/trips/` | Retrieve all trips |
GET | `/trips/{trip_id}` | Retrieve a specific trip |
PUT | `/trips/{trip_id}` | Update trip |
DELETE | `/trips/{trip_id}` | Delete trip |

### Expenses

| Method | Endpoint | Description |
|------|------|------|
POST | `/expenses/` | Add expense |
GET | `/expenses/` | Retrieve all expenses |
GET | `/expenses/{expense_id}` | Retrieve specific expense |
PUT | `/expenses/{expense_id}` | Update expense |
DELETE | `/expenses/{expense_id}` | Delete expense |

### Budget Analytics

| Method | Endpoint | Description |
|------|------|------|
GET | `/analytics/trip/{trip_id}/total-spent` | Calculate total trip spending |
GET | `/analytics/trip/{trip_id}/remaining-budget` | Calculate remaining trip budget |

### Destinations

| Method | Endpoint | Description |
|------|------|------|
GET | `/destinations/` | Retrieve destinations |
GET | `/destinations/country/{country}` | Filter destinations by country |
GET | `/destinations/top-rated` | Retrieve top rated destinations |
GET | `/destinations/budget-friendly` | Retrieve cheapest destinations |

### Recommendations

| Method | Endpoint | Description |
|------|------|------|
GET | `/recommendations/budget/{max_cost}` | Recommend destinations within a budget |
GET | `/recommendations/season/{season}` | Recommend destinations by travel season |
GET | `/recommendations/trending` | Show trending destinations |
GET | `/recommendations/trip/{trip_id}` | Recommend destinations based on trip budget |

## Example Workflow

1. A user creates a trip using `/trips/`.
2. The user records expenses using `/expenses/`.
3. The API calculates total spending and remaining budget.
4. The user queries `/recommendations/trip/{trip_id}` to receive destination suggestions based on the trip budget.

## Future Improvements

Possible improvements include:

- User authentication
- Saving destinations to trips
- Filtering by continent and destination type
- Deploying the API to a public server

## GenAI Usage

Generative AI tools were used during the development of this project to assist with:

- project planning
- debugging code
- designing database models
- structuring API endpoints
- improving documentation

All AI usage will be declared in the accompanying technical report as required by the coursework guidelines.

## Author

Student: Yuan H  
Module: COMP3011 – Web Services and Web Data  
University of Leeds