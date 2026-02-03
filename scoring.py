def calculate_productivity_score(weather_data):
    temperature = weather_data["current_weather"]["temperature"]
    wind_speed = weather_data["current_weather"]["windspeed"]

    # Best productivity is 72°F with low wind (0 mph ideal)
    temp_score = max(0, min(100, (temperature - 32) * 3.33))  # Scale from 32°F to 104°F
    wind_score = max(0, 100 - min(100, wind_speed * 5))  # Scale wind speed from 0 mph to 20 mph

    return (temp_score + wind_score) / 2
