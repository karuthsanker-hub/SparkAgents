import httpx
import asyncio

async def get_weather():
    url = "https://api.open-meteo.com/v1/current_weather"
    params = {
        "latitude": 42.44,
        "longitude": -71.22,
        "temperature_unit": "fahrenheit",
        "windspeed_unit": "mph"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()
