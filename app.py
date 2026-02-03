from fastapi import FastAPI, HTTPException
from weather import get_weather
from scoring import calculate_productivity_score

app = FastAPI()

@app.get("/productivity")
async def productivity():
    weather_data = await get_weather()
    if not weather_data:
        raise HTTPException(status_code=503, detail="Unable to fetch weather data")
    score = calculate_productivity_score(weather_data)
    return {"productivity_score": score}
