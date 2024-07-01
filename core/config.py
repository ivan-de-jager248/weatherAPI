from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    weather_api_key:str
    redis_host:str
    redis_port:int
    
    suggestions: dict = {
        1000: ["Wear sunglasses", "Apply sunscreen", "Go for a walk or hike"],
        1003: ["Carry a light jacket", "Sunglasses may be needed", "Have a picnic"],
        1006: ["Dress in layers", "Carry an umbrella", "Visit a museum or indoor event"],
        1009: ["Wear warm clothes", "Carry an umbrella", "Read a book indoors"],
        1030: ["Drive carefully", "Use fog lights", "Avoid outdoor activities"],
        1063: ["Carry an umbrella", "Wear waterproof clothing", "Visit an indoor cafe"],
        1066: ["Wear warm clothes", "Drive carefully", "Build a snowman"],
        1069: ["Wear warm clothes", "Drive carefully", "Stay indoors and watch a movie"],
        1072: ["Wear warm clothes", "Drive carefully", "Avoid traveling if possible"],
        1087: ["Stay indoors", "Avoid tall objects", "Check for weather updates"],
        1114: ["Wear warm clothes", "Drive carefully", "Expect possible delays"],
        1117: ["Stay indoors", "Wear warm clothes", "Avoid travel if possible"],
        1135: ["Drive carefully", "Use fog lights", "Avoid outdoor activities"],
        1147: ["Stay indoors", "Drive carefully", "Avoid travel if possible"],
        1150: ["Carry an umbrella", "Wear waterproof clothing", "Drive carefully"],
        1153: ["Carry an umbrella", "Wear waterproof clothing", "Drive carefully"],
        1168: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1171: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1180: ["Carry an umbrella", "Wear waterproof clothing", "Check for weather updates"],
        1183: ["Carry an umbrella", "Wear waterproof clothing", "Check for weather updates"],
        1186: ["Carry an umbrella", "Wear waterproof clothing", "Check for weather updates"],
        1189: ["Carry an umbrella", "Wear waterproof clothing", "Check for weather updates"],
        1192: ["Carry an umbrella", "Wear waterproof clothing", "Check for weather updates"],
        1195: ["Stay indoors", "Wear waterproof clothing", "Check for weather updates"],
        1198: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1201: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1204: ["Carry an umbrella", "Wear warm clothes", "Drive carefully"],
        1207: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1210: ["Wear warm clothes", "Drive carefully", "Expect possible delays"],
        1213: ["Wear warm clothes", "Drive carefully", "Expect possible delays"],
        1216: ["Wear warm clothes", "Drive carefully", "Expect possible delays"],
        1219: ["Wear warm clothes", "Drive carefully", "Expect possible delays"],
        1222: ["Wear warm clothes", "Drive carefully", "Expect possible delays"],
        1225: ["Stay indoors", "Wear warm clothes", "Avoid travel if possible"],
        1237: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1240: ["Carry an umbrella", "Wear waterproof clothing", "Check for weather updates"],
        1243: ["Carry an umbrella", "Wear waterproof clothing", "Check for weather updates"],
        1246: ["Stay indoors", "Wear waterproof clothing", "Check for weather updates"],
        1249: ["Carry an umbrella", "Wear warm clothes", "Drive carefully"],
        1252: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1255: ["Wear warm clothes", "Drive carefully", "Expect possible delays"],
        1258: ["Stay indoors", "Wear warm clothes", "Avoid travel if possible"],
        1261: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1264: ["Stay indoors", "Wear warm clothes", "Drive carefully"],
        1273: ["Stay indoors", "Avoid tall objects", "Check for weather updates"],
        1276: ["Stay indoors", "Avoid tall objects", "Check for weather updates"],
        1279: ["Stay indoors", "Wear warm clothes", "Avoid travel if possible"],
        1282: ["Stay indoors", "Wear warm clothes", "Avoid travel if possible"]
    }

settings = Settings()