import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_productivity_endpoint():
    response = client.get("/productivity")
    assert response.status_code == 200
    assert "productivity_score" in response.json()
    assert 0 <= response.json()["productivity_score"] <= 100

def test_productivity_endpoint_failure():
    # Mock the get_weather function to return None
    async def mock_get_weather():
        return None

    app.dependency_overrides[get_weather] = mock_get_weather

    response = client.get("/productivity")
    assert response.status_code == 503
    assert response.json() == {"detail": "Unable to fetch weather data"}

    # Reset the dependency override
    del app.dependency_overrides[get_weather]
