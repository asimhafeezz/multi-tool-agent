import requests
from langchain.agents import Tool
from config import OPENWEATHER_API_KEY

def get_weather(city: str) -> str:
    """Get current weather for a city.
    
    Args:
        city (str): The name of the city to get weather for
        
    Returns:
        str: Weather information or error message
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        res = requests.get(url).json()
        if res.get("cod") != 200:
            return f"Could not find weather for '{city}'."
        weather = res["weather"][0]["description"]
        temp = res["main"]["temp"]
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    except Exception as e:
        return f"Weather API error: {e}"

# weather tool
weather_tool = Tool(
    name="Weather",
    func=get_weather,
    description="Use to get current weather in a city. Input should be a city name."
)