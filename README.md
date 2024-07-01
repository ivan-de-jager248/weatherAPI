# My Awesome Weather API

This project is a FastAPI-based application that provides real-time weather updates and recommendations based on the weather. It uses Redis for caching weather data and storing recommendation data.

## Features

- Up to date weather updates
- Weather-based recommendations
- Caching with Redis

## Requirements

- Docker (for running with Docker Compose)
- Python 3.11+ (for running locally)
- Redis (must be running on localhost if running locally)

## Running the Project

### Using Docker Compose

1. **Clone the repository:**
    ```sh
    git clone https://github.com/ivan-de-jager248/weatherAPI
    cd weatherAPI
    ```

2. **Create a `.env` file in the root directory and add your Weather API key:**
    ```env
    WEATHER_API_KEY=<API KEY>
    ```

3. **Run Docker Compose:**
    ```sh
    docker-compose up --build
    ```

   This will start the FastAPI application and a Redis instance.

4. **Access the API:**
   Open your browser and go to `http://localhost:8000/docs` to see the API documentation.

### Running Locally

1. **Clone the repository:**
    ```sh
    git clone https://github.com/ivan-de-jager248/weatherAPI
    cd weatherAPI
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add your Weather API key:**
    ```env
    WEATHER_API_KEY=<API KEY>
    REDIS_HOST=localhost
    REDIS_PORT=6379
    ```

5. **Ensure Redis is running on localhost:**
    ```sh
    redis-server
    ```

6. **Run the FastAPI application using uvicorn:**
    ```sh
    uvicorn core.main:app --reload
    ```

7. **Access the API:**
   Open your browser and go to `http://localhost:8000/docs` to see the API documentation.

## API Endpoints

- **GET /recommendation**: Get weather recommendations for a specific location.
    - **Parameters**:
        - `location (query parameter, required)`: The location for which you want to get weather recommendations. This can be a city name, coordinates, or any other valid location identifier.

    - **Workflow**:
        1. Get the recommendation from Redis using the provided location. If it does not exist, return a 404 error with a message stating the recommendation for that location does not exist.
        2. Return the recommendation for the specified location.

- **POST /recommendation**: Create a new weather recommendation.
    - **Request Body**:
        - `location (string, required)`: The location for which the recommendation is being created.
        - `temp_symbol ("C" or "F", default "C")`: The temperature symbol to use for the recommendation. Defaults to Celsius if not specified.

    - **Workflow**:
        1. Get the current weather for the specified location using the Weather API.
            1. Check if there is cached weather data for this location in Redis.
            2. If there is no cached weather data, fetch new data from the API endpoint and cache it in Redis.
    	4. Use the weather data to generate a recommendation for this location using suggestions pre-defined in Redis against the **condition code** returned from the API.
        5. Store the recommendation in Redis against the location.
    	6. Return the a message indicating the recommendation is saved.

        > **Note:** Ideally with more time and budget I would have used an LLM like ChatGPT or Llama 3 to generate the suggestions on the fly, this would remove the manual writing of suggestions and eventually more context given to the LLM would have made the suggestions even more personalised.
    

## Project Structure

- `core/main.py`: Main application file where FastAPI app is defined.
- `core/config.py`: Configuration settings for the application.
- `core/helpers.py`: Helper functions for fetching weather data and other utilities.
- `core/models.py`: Data models for the application.◊