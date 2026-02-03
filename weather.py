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
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
