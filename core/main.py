import redis
import json
from datetime import datetime
from typing import Annotated, Literal
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from .helpers import celsius_to_fahrenheit, fetch_weather, get_suggestions
from .config import settings
from .models import Recommendation, MessageResponse, get_recommendation_responses, create_recommendation_responses
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to Redis 
    app.state.db = redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0)

    # Delete the existing suggestions key 
    app.state.db.delete("suggestions")

    # Store the suggestions database
    for key, value in settings.suggestions.items():
        app.state.db.hset("suggestions", key, json.dumps(value))

    print("Suggestions dictionary stored in Redis database")

    yield

    # Close the connection to Redis
    app.state.db.close()


async def get_db_client() -> redis.Redis:
    try:
        return app.state.db
    except AttributeError:
        raise HTTPException(status_code=500, detail="Database client not found")


app = FastAPI(
    title="My Awesome Weather API",
    description="This is my Weather API which gives realtime weather updates and recommendations based on the weather.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/", response_model=MessageResponse)
async def read_root():
    return {"message": "Welcome to the weather app!"}


@app.post(
    "/recommendation",
    response_model=MessageResponse,
    responses=create_recommendation_responses,
)
async def create_recommendation(
    db: Annotated[redis.Redis, Depends(get_db_client)],
    location: str,
    temp_symbol: Literal["C", "F"] = "C",
):

    data = None
    try:
        data = fetch_weather(db, location)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

    suggestions = get_suggestions(db, data["current"]["condition"]["code"])

    # Create recommendation object
    recommendation_data: Recommendation = {
        "location": data["location"],
        "temp": (
            data["current"]["temp_c"]
            if temp_symbol == "C"
            else celsius_to_fahrenheit(data["current"]["temp_c"])
        ),
        "temp_unit": "Celcius" if temp_symbol == "C" else "Fahrenheit",
        "condition": data["current"]["condition"]["text"],
        "suggestions": suggestions,
        "timestamp": datetime.now().isoformat(),
    }

    # Store the recommendation data in Redis
    db.hset("recommendations", location.lower(), json.dumps(recommendation_data))

    return {"message": "Data and recommendation stored successfully"}


@app.get(
    "/recommendation",
    response_model=Recommendation,
    responses=get_recommendation_responses,
)
async def get_recommendation(
    location: str, db: Annotated[redis.Redis, Depends(get_db_client)]
):
    # Get recommendation from database
    recommendation = db.hget("recommendations", location.lower())

    if recommendation:
        return json.loads(recommendation)
    else:
        raise HTTPException(status_code=404, detail="No recommendation found for the given location.")
