from fastapi import FastAPI

app = FastAPI(title="Travel Attraction API")


@app.get("/")
def root():
    return {"message": "Travel Attraction API is running"}