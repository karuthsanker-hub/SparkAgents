from fastapi import FastAPI
from weather import get_weather
from scoring import calculate_productivity_score

app = FastAPI()

@app.get("/productivity")
async def productivity():
    weather_data = await get_weather()
    score = calculate_productivity_score(weather_data)
    return {"productivity_score": score}
