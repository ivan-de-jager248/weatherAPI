from typing import Any, Literal
from pydantic import BaseModel


# Models
class Recommendation(BaseModel):
    location: dict[str, Any]
    temp: float
    temp_unit: Literal["Celcius", "Fahrenheit"]
    condition: str
    suggestions: list[str]
    timestamp: str


class MessageResponse(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    message: str


# Example Responses for OpenAPI docs
create_recommendation_responses = {
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": {
                    "message": "Data and recommendation stored successfully",
                }
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "model": ErrorResponse,
        "content": {
            "application/json": {"example": {"message": "Internal Server Error"}}
        },
    },
}

get_recommendation_responses = {
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": {
                    "location": {
                        "name": "Benoni",
                        "region": "Gauteng",
                        "country": "South Africa",
                        "lat": -26.18,
                        "lon": 28.32,
                        "tz_id": "Africa/Johannesburg",
                        "localtime_epoch": 1719577403,
                        "localtime": "2024-06-28 14:23",
                    },
                    "temp": 22.0,
                    "temp_unit": "Celcius",
                    "condition": "Sunny",
                    "suggestions": [
                        "Wear sunglasses",
                        "Apply sunscreen",
                        "Go for a walk or hike",
                    ],
                    "timestamp": "2023-10-01T12:00:00",
                }
            }
        },
    },
    404: {
        "description": "Not Found",
        "content": {
            "application/json": {
                "example": {
                    "message": "No recommendation found for the given location."
                }
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "model": ErrorResponse,
        "content": {
            "application/json": {"example": {"message": "Internal Server Error"}}
        },
    },
}
