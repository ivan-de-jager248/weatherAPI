import redis
import json
import requests
from datetime import datetime, timedelta
from .config import settings


def fetch_weather(db: redis.Redis, location: str) -> dict:
    """
    Fetches weather data for a specific location from a Redis database or an external API.

    Args:
        db (redis.Redis): A Redis database connection object.
        location (str): The location for which weather data is to be fetched.

    Returns:
        dict: A dictionary containing the weather data for the specified location.

    Raises:
        Exception: If the request to the external API fails with a non-200 status code.

    The function first checks the Redis database for cached weather data for the given location. If the data is found and not older than 1 day, it is returned directly. Otherwise, a request is made to the WeatherAPI to fetch the current weather data for the location. The retrieved data is then stored in the Redis database for future use and returned to the caller.
    """

    # Check database first
    weather_data = db.hget("weather_data", location.lower())
    if weather_data:
        weather_data = json.loads(weather_data)
        stored_date = datetime.fromisoformat(weather_data["timestamp"])

        # Ensure database data is of the same day
        if datetime.now().date() == stored_date.date():
            return weather_data

    url = "https://api.weatherapi.com/v1/current.json"
    params = {"q": location, "key": settings.weather_api_key}
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        response_data = response.json()

        # Save to redis database
        db.hset(
            "weather_data",
            location.lower(),
            json.dumps({"timestamp": datetime.now().isoformat(), **response_data}),
        )

        return response_data
    else:
        raise Exception(
            f"Request failed with status code {response.status_code}.\n Message: {response.text}"
        )


def get_suggestions(db: redis.Redis, condition_code: int) -> list[str]:
    """
    Get suggestions for a specific weather condition code from a Redis database.

    Args:
        db (redis.Redis): A Redis database connection object.
        condition_code (int): The weather condition code for which suggestions are to be fetched.

    Returns:
        list[str]: A list of suggestions corresponding to the provided weather condition code. Returns an empty list if no suggestions are found.

    The function retrieves suggestions from the Redis database based on the provided weather condition code. If suggestions are found for the given code, they are returned as a list of strings. If no suggestions are found, an empty list is returned.
    """
    suggestions_json = db.hget("suggestions", str(condition_code))

    if suggestions_json:
        return json.loads(suggestions_json)
    else:
        return []


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature value from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature value in Celsius to be converted to Fahrenheit.

    Returns:
        float: The temperature value converted to Fahrenheit.

    This function takes a temperature value in Celsius and converts it to Fahrenheit using the formula (celsius * 9 / 5) + 32.
    """
    return (celsius * 9 / 5) + 32